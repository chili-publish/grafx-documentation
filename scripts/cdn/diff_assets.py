#!/usr/bin/env python3
"""
Split a CDN upload staging dir into "already on prod" vs "PR-specific".

Used by the PR paths of the CDN-offload workflows (DT-973 follow-up) so PR
preview builds only upload assets that genuinely differ from what production
already serves at /assets/. Everything else is rewritten straight to the prod
CDN prefix by rewrite_urls.py and never leaves the runner.

Usage:
  python3 scripts/cdn/diff_assets.py <upload_dir> <prod_listing.json> <out_list>

Arguments:
  upload_dir         Staging dir produced by collect_assets.py
                     (e.g. build/cdn-upload/). MODIFIED IN PLACE: files that
                     match the prod baseline are deleted, so what remains is
                     exactly the set to upload to staging/pr-<N>/assets/.
  prod_listing.json  JSON array from `az storage blob list` with the shape
                     [{"name": "<blob path>", "md5": "<base64 MD5|null>"}].
  out_list           Output file: one rel path per line for every PR-specific
                     asset (new path, changed content, or prod blob without a
                     Content-MD5). Empty file = nothing to upload.

A file counts as "already on prod" only when the same rel path exists in the
listing AND its Content-MD5 matches the local file's MD5. A prod blob with a
missing/empty MD5 is treated as different (safe fallback: upload to staging).

Exit codes:
  0  Success
  1  Bad arguments / IO error
"""
from __future__ import annotations

import base64
import hashlib
import json
import sys
from pathlib import Path


def local_md5_b64(path: Path) -> str:
    """MD5 of file contents, base64-encoded (matches blob Content-MD5)."""
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return base64.b64encode(h.digest()).decode("ascii")


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        return 1

    upload_dir = Path(sys.argv[1]).resolve()
    listing_path = Path(sys.argv[2])
    out_list = Path(sys.argv[3])

    if not upload_dir.is_dir():
        print(f"error: upload_dir is not a directory: {upload_dir}",
              file=sys.stderr)
        return 1

    try:
        listing = json.loads(listing_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"error: cannot read prod listing {listing_path}: {e}",
              file=sys.stderr)
        return 1

    prod_md5: dict[str, str] = {
        entry["name"]: entry["md5"]
        for entry in listing
        if entry.get("name") and entry.get("md5")
    }
    print(f"Prod baseline: {len(listing)} blob(s), "
          f"{len(prod_md5)} with Content-MD5")

    matched = 0
    matched_bytes = 0
    pr_specific: list[str] = []
    pr_bytes = 0

    for path in sorted(upload_dir.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(upload_dir).as_posix()
        size = path.stat().st_size
        if prod_md5.get(rel) == local_md5_b64(path):
            path.unlink()
            matched += 1
            matched_bytes += size
        else:
            pr_specific.append(rel)
            pr_bytes += size

    # Drop now-empty directories so the upload tree only contains real files.
    for d in sorted((p for p in upload_dir.rglob("*") if p.is_dir()),
                    key=lambda p: len(p.parts), reverse=True):
        if not any(d.iterdir()):
            d.rmdir()

    out_list.parent.mkdir(parents=True, exist_ok=True)
    out_list.write_text(
        "".join(f"{rel}\n" for rel in pr_specific), encoding="utf-8")

    print(f"Matched prod baseline (skipped): {matched} file(s), "
          f"{matched_bytes / 1024 / 1024:.1f} MB")
    print(f"PR-specific (to upload):         {len(pr_specific)} file(s), "
          f"{pr_bytes / 1024 / 1024:.1f} MB")
    for rel in pr_specific[:50]:
        print(f"  {rel}")
    if len(pr_specific) > 50:
        print(f"  ... and {len(pr_specific) - 50} more")

    return 0


if __name__ == "__main__":
    sys.exit(main())
