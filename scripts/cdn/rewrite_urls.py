#!/usr/bin/env python3
"""
Rewrite asset references in a mkdocs `site/` build to point at the CDN.

Walks every .html file (and optionally .xml / .css) in the site dir, finds
every reference to a binary asset that exists in the build, and replaces it
with an absolute CDN URL. Skips already-absolute URLs (http/https/data/etc.)
and references that don't have an asset extension we care about.

After this runs, site/ still contains the binaries — strip them with
scripts/cdn/strip_assets.py (or an equivalent `find ... -delete`) before the
SWA deploy.

Usage:
  python3 scripts/cdn/rewrite_urls.py <site_dir> <cdn_base> <path_prefix> [options]

Arguments:
  site_dir      Root of the mkdocs build (e.g. site/)
  cdn_base      CDN base URL (e.g. https://docs-cdn.chiligrafx.com)
  path_prefix   Container + optional sub-prefix between cdn_base and the
                site-relative path. Leading/trailing slashes are normalised.
                Examples:
                  /assets/                            (prod)
                  /staging/pr-482/assets/             (PR preview)

Options:
  --strict          Fail with exit code 2 if any unrewritten reference still
                    points at an in-scope asset extension. Recommended in CI.
  --dry-run         Don't modify files; just report what would change.
  --include-css     Also rewrite url(...) references in .css files.
  --include-xml     Also rewrite asset URLs in .xml files (sitemap, RSS).
                    Default: enabled.
  --no-include-xml  Disable .xml processing.
  --verbose         Print every individual rewrite (lots of output).

Exit codes:
  0  Success
  1  Bad arguments / IO error
  2  --strict found unrewritten asset references
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

from _assets import ASSET_EXTS

# HTML attributes that may carry a URL we want to rewrite.
# Matches: foo="...", foo='...'
# Captures: 1=attr name, 2=quote char, 3=url-or-srcset-payload
HTML_ATTR_RE = re.compile(
    r'\b(src|href|content|poster|srcset)\s*=\s*(["\'])([^"\']*)\2'
)

# CSS url() — handles quoted and unquoted forms.
# Captures: 1=quote (maybe empty), 2=url
CSS_URL_RE = re.compile(
    r'url\(\s*(["\']?)([^"\')\s]+)\1\s*\)'
)


def is_external(url: str) -> bool:
    """URL is external / special; never rewrite."""
    return url.startswith((
        "http://", "https://", "//", "data:", "mailto:", "tel:",
        "#", "javascript:",
    ))


def split_url_suffix(url: str) -> tuple[str, str]:
    """Split URL into (path_part, suffix) where suffix is ?query and/or #fragment.

    Returns ("", "") for the empty string. Suffix is empty when there is no
    query or fragment. Keeping these intact lets the rewriter preserve
    cache-busting hints (foo.png?v=2) and SVG fragment selectors (sprite.svg#icon).
    """
    for i, ch in enumerate(url):
        if ch in ("?", "#"):
            return url[:i], url[i:]
    return url, ""


def url_ext(url: str) -> str:
    """Return lowercase extension, stripped of query/fragment."""
    path_part, _ = split_url_suffix(url)
    return Path(path_part).suffix.lower()


def resolve_site_rel(url: str, host_file: Path, site_root: Path) -> Path | None:
    """Resolve a relative URL against the file's directory, return path
    relative to site_root, or None if it falls outside."""
    clean = url.split("?", 1)[0].split("#", 1)[0]
    if clean.startswith("/"):
        # site-absolute path
        target = (site_root / clean.lstrip("/")).resolve()
    else:
        target = (host_file.parent / clean).resolve()
    try:
        return target.relative_to(site_root)
    except ValueError:
        return None


def build_cdn_url(rel: Path, cdn_base: str, path_prefix: str) -> str:
    return f"{cdn_base.rstrip('/')}{path_prefix}{rel.as_posix()}"


class Rewriter:
    def __init__(
        self,
        site_root: Path,
        cdn_base: str,
        path_prefix: str,
        strict: bool,
        dry_run: bool,
        verbose: bool,
    ):
        self.site_root = site_root
        self.cdn_base = cdn_base
        # Normalise prefix: always one leading and one trailing slash.
        self.path_prefix = "/" + path_prefix.strip("/") + "/"
        self.strict = strict
        self.dry_run = dry_run
        self.verbose = verbose
        # Stats
        self.files_modified = 0
        self.files_scanned = 0
        self.rewrites_total = 0
        self.rewrites_by_ext: dict[str, int] = defaultdict(int)
        # Strict-mode collector
        self.unresolved: list[tuple[Path, str]] = []

    def _maybe_rewrite(self, url: str, host_file: Path) -> str:
        """Return rewritten URL if we should, else the original."""
        if is_external(url):
            return url
        # Split off ?query / #fragment up-front so we can reattach to the CDN
        # URL at the end -- preserves things like sprite.svg#icon and ?v=hash.
        path_part, suffix = split_url_suffix(url)
        ext = Path(path_part).suffix.lower()
        if ext not in ASSET_EXTS:
            return url
        rel = resolve_site_rel(path_part, host_file, self.site_root)
        if rel is None:
            # Asset extension but resolves outside site/ — leave it, flag in strict.
            self.unresolved.append((host_file, url))
            return url
        new = build_cdn_url(rel, self.cdn_base, self.path_prefix) + suffix
        self.rewrites_total += 1
        self.rewrites_by_ext[ext] += 1
        if self.verbose:
            rel_host = host_file.relative_to(self.site_root)
            print(f"  {rel_host}: {url} -> {new}", file=sys.stderr)
        return new

    def _rewrite_srcset(self, payload: str, host_file: Path) -> str:
        """srcset is `url descriptor, url descriptor, ...`."""
        new_parts = []
        for part in payload.split(","):
            stripped = part.strip()
            if not stripped:
                continue
            bits = stripped.split(None, 1)
            u = bits[0]
            rest = (" " + bits[1]) if len(bits) > 1 else ""
            new_parts.append(self._maybe_rewrite(u, host_file) + rest)
        return ", ".join(new_parts)

    def _process_attrs(self, content: str, host_file: Path) -> str:
        def replace(m: re.Match) -> str:
            attr, quote, payload = m.group(1), m.group(2), m.group(3)
            if attr == "srcset":
                new_payload = self._rewrite_srcset(payload, host_file)
            else:
                new_payload = self._maybe_rewrite(payload, host_file)
            return f"{attr}={quote}{new_payload}{quote}"

        return HTML_ATTR_RE.sub(replace, content)

    def _process_css_urls(self, content: str, host_file: Path) -> str:
        def replace(m: re.Match) -> str:
            quote, url = m.group(1), m.group(2)
            new_url = self._maybe_rewrite(url, host_file)
            return f"url({quote}{new_url}{quote})"

        return CSS_URL_RE.sub(replace, content)

    def rewrite_file(self, file_path: Path, process_css_urls: bool) -> None:
        self.files_scanned += 1
        try:
            content = file_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            print(f"warning: skipping {file_path}: {e}", file=sys.stderr)
            return

        before_total = self.rewrites_total
        new_content = self._process_attrs(content, file_path)
        if process_css_urls:
            new_content = self._process_css_urls(new_content, file_path)

        if new_content != content:
            self.files_modified += 1
            if not self.dry_run:
                file_path.write_text(new_content, encoding="utf-8")

        # Strict mode: scan for remaining in-scope unresolved refs in OUTPUT.
        if self.strict:
            for m in HTML_ATTR_RE.finditer(new_content):
                attr, _, payload = m.group(1), m.group(2), m.group(3)
                urls = payload.split(",") if attr == "srcset" else [payload]
                for u in urls:
                    u = u.strip().split(None, 1)[0] if attr == "srcset" else u
                    if not is_external(u) and url_ext(u) in ASSET_EXTS:
                        self.unresolved.append((file_path, u))
            if process_css_urls:
                for m in CSS_URL_RE.finditer(new_content):
                    u = m.group(2)
                    if not is_external(u) and url_ext(u) in ASSET_EXTS:
                        self.unresolved.append((file_path, u))


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Rewrite asset references in a mkdocs site/ to CDN URLs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("site_dir", help="Root of the mkdocs build (e.g. site/)")
    p.add_argument("cdn_base", help="CDN base URL (e.g. https://docs-cdn.chiligrafx.com)")
    p.add_argument("path_prefix", help="Path prefix (e.g. /assets/ or /staging/pr-482/assets/)")
    p.add_argument("--strict", action="store_true",
                   help="Fail (exit 2) if any in-scope asset refs remain unrewritten.")
    p.add_argument("--dry-run", action="store_true",
                   help="Don't modify files; just report what would change.")
    p.add_argument("--include-css", action="store_true",
                   help="Also rewrite url(...) refs in .css files.")
    p.add_argument("--include-xml", action=argparse.BooleanOptionalAction, default=True,
                   help="Also process .xml files (default: enabled).")
    p.add_argument("--verbose", action="store_true",
                   help="Print every individual rewrite.")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    site_root = Path(args.site_dir).resolve()
    if not site_root.is_dir():
        print(f"error: site_dir is not a directory: {site_root}", file=sys.stderr)
        return 1

    rewriter = Rewriter(
        site_root=site_root,
        cdn_base=args.cdn_base,
        path_prefix=args.path_prefix,
        strict=args.strict,
        dry_run=args.dry_run,
        verbose=args.verbose,
    )

    # Build the list of files to process
    targets: list[tuple[Path, bool]] = []  # (path, process_css_urls)
    for path in site_root.rglob("*"):
        if not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix == ".html":
            # HTML: attrs + inline style url() (process_css_urls=True catches both
            # inline <style> blocks and inline style="..." values).
            targets.append((path, True))
        elif suffix == ".xml" and args.include_xml:
            targets.append((path, False))
        elif suffix == ".css" and args.include_css:
            targets.append((path, True))

    for file_path, process_css in targets:
        rewriter.rewrite_file(file_path, process_css_urls=process_css)

    # Summary
    print(
        f"Scanned {rewriter.files_scanned} file(s); "
        f"modified {rewriter.files_modified}; "
        f"rewrote {rewriter.rewrites_total} reference(s)."
        f"{' (dry run, no files written)' if args.dry_run else ''}",
        file=sys.stderr,
    )
    if rewriter.rewrites_by_ext:
        for ext, n in sorted(rewriter.rewrites_by_ext.items(), key=lambda kv: -kv[1]):
            print(f"  {ext}: {n}", file=sys.stderr)

    if args.strict and rewriter.unresolved:
        # Deduplicate
        seen: set[tuple[str, str]] = set()
        uniq = []
        for f, u in rewriter.unresolved:
            key = (str(f), u)
            if key in seen:
                continue
            seen.add(key)
            uniq.append((f, u))
        print(
            f"\nstrict: {len(uniq)} unresolved asset reference(s):",
            file=sys.stderr,
        )
        for f, u in uniq[:50]:
            rel = f.relative_to(site_root)
            print(f"  {rel}: {u}", file=sys.stderr)
        if len(uniq) > 50:
            print(f"  ... and {len(uniq) - 50} more", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
