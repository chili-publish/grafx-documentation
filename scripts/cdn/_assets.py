"""
Shared constants for the CDN offload scripts (DT-973).

Single source of truth for the asset extension set used by:
- collect_assets.py  (decides which files go into the upload staging dir)
- rewrite_urls.py    (decides which HTML refs to rewrite + scan in --strict)
- strip_assets.py    (decides which files to remove from site/ post-rewrite)

Keep this list in one place so all three scripts stay in sync as we add or
remove extensions.
"""

ASSET_EXTS = frozenset({
    ".png", ".jpg", ".jpeg", ".gif", ".svg",
    ".mp4", ".webm", ".pdf", ".webp",
})
