#!/usr/bin/env python3
"""
Copy in-scope asset files from a mkdocs `site/` build into a clean staging
directory, preserving the relative path structure.

Used by the CDN-offload workflow (DT-973) to assemble the exact set of blobs
to upload to Azure Blob Storage. Kept simple on purpose — extension match,
recursive walk, copy.

Usage:
  python3 scripts/cdn/collect_assets.py <site_dir> <staging_dir>

Example:
  python3 scripts/cdn/collect_assets.py site/ build/cdn-upload/
"""
import shutil
import sys
from pathlib import Path

from _assets import ASSET_EXTS

if len(sys.argv) != 3:
    print(__doc__)
    sys.exit(1)

src = Path(sys.argv[1]).resolve()
dst = Path(sys.argv[2]).resolve()

if not src.is_dir():
    print(f"Source is not a directory: {src}", file=sys.stderr)
    sys.exit(1)

# Wipe and recreate the staging dir so stale files from previous runs don't linger
if dst.exists():
    shutil.rmtree(dst)
dst.mkdir(parents=True)

count = 0
total_bytes = 0
counts_by_ext: dict[str, int] = {}

for path in src.rglob("*"):
    if not path.is_file():
        continue
    ext = path.suffix.lower()
    if ext not in ASSET_EXTS:
        continue
    rel = path.relative_to(src)
    target = dst / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, target)
    count += 1
    total_bytes += path.stat().st_size
    counts_by_ext[ext] = counts_by_ext.get(ext, 0) + 1

mb = total_bytes / 1024 / 1024
print(f"Copied {count} files, {mb:.1f} MB into {dst}")
for ext, n in sorted(counts_by_ext.items(), key=lambda kv: -kv[1]):
    print(f"  {ext}: {n}")
