#!/usr/bin/env python3
"""
Remove in-scope asset files from a mkdocs `site/` build.

Run after `rewrite_urls.py` so the deployed Azure Static Web Apps artifact
contains only HTML/CSS/JS/fonts — the binaries are now served from the CDN.

Mirrors the same extension list as `collect_assets.py` and `rewrite_urls.py`
so the three steps stay in sync.

Usage:
  python3 scripts/cdn/strip_assets.py <site_dir> [--dry-run]

Options:
  --dry-run   Report what would be removed, don't delete anything.

Exit codes:
  0  Success
  1  Bad arguments / not a directory
"""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

from _assets import ASSET_EXTS


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("site_dir", help="Root of the mkdocs build (e.g. site/)")
    p.add_argument("--dry-run", action="store_true",
                   help="Don't delete; just report.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    site = Path(args.site_dir).resolve()
    if not site.is_dir():
        print(f"error: site_dir is not a directory: {site}", file=sys.stderr)
        return 1

    count = 0
    total_bytes = 0
    by_ext: dict[str, int] = defaultdict(int)

    for path in site.rglob("*"):
        if not path.is_file():
            continue
        ext = path.suffix.lower()
        if ext not in ASSET_EXTS:
            continue
        total_bytes += path.stat().st_size
        if not args.dry_run:
            path.unlink()
        count += 1
        by_ext[ext] += 1

    mb = total_bytes / 1024 / 1024
    verb = "Would remove" if args.dry_run else "Removed"
    print(f"{verb} {count} file(s), {mb:.1f} MB from {site}", file=sys.stderr)
    for ext, n in sorted(by_ext.items(), key=lambda kv: -kv[1]):
        print(f"  {ext}: {n}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
