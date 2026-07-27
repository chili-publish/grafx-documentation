"""Derive canonical page URLs, stable ids, and embedding records from docs.

Pure logic (no MkDocs, no network) so URL/id derivation is unit-testable.
The record shape is the contract shared with grafx-genie's store:
    {id, page_url, section, chunk_text, embedding[], model, dim}
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass

from scripts.chunker import Chunk


def page_url_from_src(src_uri: str, site_url: str) -> str:
    """Map a docs source path to its canonical published URL.

    MkDocs (directory-URL default) serves 'X/Y/index.md' at 'X/Y/' and
    'X/Y.md' at 'X/Y/'. We normalize both to a trailing-slash URL under
    site_url. 'index.md' at the root maps to site_url itself.
    """
    base = site_url.rstrip("/")
    path = src_uri.replace("\\", "/")
    if path.endswith("/index.md"):
        path = path[: -len("index.md")]        # keep trailing slash
    elif path == "index.md":
        path = ""
    elif path.endswith(".md"):
        path = path[: -len(".md")] + "/"
    return f"{base}/{path}" if path else f"{base}/"


def chunk_id(src_uri: str, section: str, index: int) -> str:
    """Stable id for a chunk: hash of (source path, section, ordinal).

    Deterministic across builds of identical content, so re-runs overwrite
    rather than duplicate (acceptance criterion).
    """
    raw = f"{src_uri}::{section}::{index}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


@dataclass
class Record:
    id: str
    page_url: str
    section: str
    chunk_text: str
    embedding: list[float]
    model: str
    dim: int

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "page_url": self.page_url,
            "section": self.section,
            "chunk_text": self.chunk_text,
            "embedding": self.embedding,
            "model": self.model,
            "dim": self.dim,
        }


def build_records(
    src_uri: str,
    site_url: str,
    chunks: list[Chunk],
    embeddings: list[list[float]],
    *,
    model: str,
    dim: int,
) -> list[Record]:
    """Zip chunks with their embeddings into records for one page."""
    if len(chunks) != len(embeddings):
        raise ValueError(f"{len(chunks)} chunks but {len(embeddings)} embeddings for {src_uri}")
    for i, emb in enumerate(embeddings):
        if len(emb) != dim:
            raise ValueError(
                f"embedding {i} for {src_uri} has length {len(emb)}, expected dim={dim}"
            )
    page_url = page_url_from_src(src_uri, site_url)
    return [
        Record(
            id=chunk_id(src_uri, chunk.section, i),
            page_url=page_url,
            section=chunk.section,
            chunk_text=chunk.text,
            embedding=emb,
            model=model,
            dim=dim,
        )
        for i, (chunk, emb) in enumerate(zip(chunks, embeddings))
    ]
