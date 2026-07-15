"""Embed the full docs site into JSONL records for grafx-genie's store.

Run deliberately (not on every build) — a full re-embed costs real OpenAI
usage. Per ticket AIML-37 we embed ALL products including GraFx-Publisher,
which intentionally diverges from the site's search-exclusion policy in
hooks.py (Publisher is noindex'd for the public search box, but the AI
documentation store indexes it on purpose).

    OPENAI_API_KEY=... python scripts/embed_docs.py --out build/doc_records.jsonl

Reads docs/ directly (frontmatter-stripped markdown), chunks heading-aware,
batches embeddings, and emits one record per line matching the store contract.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.chunker import chunk_page
from scripts.records import build_records

SITE_URL = "https://docs.chiligrafx.com/"
MODEL = os.environ.get("DOCS_EMBEDDING_MODEL", "text-embedding-3-small")
DIM = int(os.environ.get("DOCS_EMBEDDING_DIM", "1536"))
BATCH = 96

_FRONTMATTER = re.compile(r"^---\n.*?\n---\n", re.DOTALL)


def strip_frontmatter(md: str) -> str:
    return _FRONTMATTER.sub("", md, count=1)


def iter_pages(docs_dir: Path):
    """Yield (src_uri, markdown) for every .md page under docs/."""
    for path in sorted(docs_dir.rglob("*.md")):
        src_uri = path.relative_to(docs_dir).as_posix()
        text = strip_frontmatter(path.read_text(encoding="utf-8"))
        yield src_uri, text


def embed_batch(client, texts: list[str]) -> list[list[float]]:
    resp = client.embeddings.create(model=MODEL, input=texts, dimensions=DIM)
    return [d.embedding for d in resp.data]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs", type=Path, default=Path("docs"))
    parser.add_argument("--out", type=Path, default=Path("build/doc_records.jsonl"))
    parser.add_argument("--limit", type=int, default=None, help="cap pages (smoke test)")
    parser.add_argument("--dry-run", action="store_true", help="chunk only, no embedding calls")
    args = parser.parse_args()

    if not args.dry_run:
        from openai import OpenAI
        client = OpenAI()  # reads OPENAI_API_KEY

    args.out.parent.mkdir(parents=True, exist_ok=True)
    pages = list(iter_pages(args.docs))
    if args.limit:
        pages = pages[: args.limit]

    total_chunks = 0
    total_pages = 0
    with args.out.open("w", encoding="utf-8") as f:
        for src_uri, markdown in pages:
            chunks = chunk_page(markdown)
            if not chunks:
                continue
            total_pages += 1
            if args.dry_run:
                embeddings = [[0.0] * DIM for _ in chunks]
            else:
                embeddings = []
                texts = [c.text for c in chunks]
                for i in range(0, len(texts), BATCH):
                    embeddings.extend(embed_batch(client, texts[i : i + BATCH]))
            records = build_records(src_uri, SITE_URL, chunks, embeddings, model=MODEL, dim=DIM)
            for rec in records:
                f.write(json.dumps(rec.to_dict()) + "\n")
                total_chunks += 1

    mode = "dry-run (zero vectors)" if args.dry_run else f"embedded via {MODEL}"
    print(f"{total_pages} pages -> {total_chunks} chunks [{mode}] -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
