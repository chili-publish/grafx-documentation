import gzip
import os
import re
from datetime import date

# Remove GraFx Publisher and unlisted landing pages from search. Pages stay
# published; they're just kept out of the local search box, marked noindex for
# Google, and dropped from the sitemap.
#
# "landing/" holds direct-link landing pages: not in the nav, not in search,
# not indexed. Anything dropped in docs/landing/ is covered automatically.
EXCLUDE_PREFIXES = ("GraFx-Publisher/", "landing/")

NOINDEX_META = '<meta name="robots" content="noindex, nofollow">'

# Decorative images that must never open in the lightbox (glightbox).
#
# glightbox's own `skip_classes` option only sees CSS classes, but a large part
# of the site styles icons through their alt text instead (extra.css selectors
# like `img[alt=rn_icon]`). Those images carry no class at all, so they would be
# made clickable. The markdown hook below tags them with `.off-glb` — the class
# glightbox always skips — so both conventions are covered.
SKIP_LIGHTBOX_ALTS = (
    "rn_icon",
    "svg_icon",
    "connector_icon",
    "matrix-icon",
    "applogo",
    "smallapplogo",
    "tinyapplogo",
)

# ![alt](src) optionally followed by an attr_list block, e.g. {.screenshot}
IMAGE_RE = re.compile(r"!\[(?P<alt>[^\]\n]*)\]\((?P<src>[^)\n]*)\)(?P<attrs>\{[^}\n]*\})?")


def _skip_lightbox(match):
    """Add the glightbox skip class to a decorative image, keeping any attrs."""
    if match.group("alt").strip() not in SKIP_LIGHTBOX_ALTS:
        return match.group(0)
    attrs = match.group("attrs")
    if attrs is None:
        suffix = "{.off-glb}"
    elif "off-glb" in attrs:
        suffix = attrs
    else:
        suffix = attrs[:-1].rstrip() + " .off-glb}"
    return f"![{match.group('alt')}]({match.group('src')}){suffix}"


def on_page_markdown(markdown, page, config, files, **kwargs):
    """Remove EXCLUDE_PREFIXES pages from the local search index.

    Applied by path, so new pages under those folders are covered without
    editing each file's front matter. Runs before the search index is built.

    Also tags alt-text-styled icons with `.off-glb` so glightbox leaves them
    alone — see SKIP_LIGHTBOX_ALTS above.
    """
    if page.file.src_uri.startswith(EXCLUDE_PREFIXES):
        page.meta.setdefault("search", {})["exclude"] = True
    return IMAGE_RE.sub(_skip_lightbox, markdown)


def on_post_page(output, page, config, **kwargs):
    """Add a noindex robots meta to EXCLUDE_PREFIXES pages for Google.

    Pages stay crawlable (no robots.txt block) so Googlebot can read the tag.
    """
    if page.file.src_uri.startswith(EXCLUDE_PREFIXES) and "</head>" in output:
        return output.replace("</head>", f"{NOINDEX_META}\n</head>", 1)
    return output


def on_post_build(config, **kwargs):
    """Post-build fixes for llms.txt/llms-full.txt and the sitemap.

    1. Rewrites /index.md URLs to trailing-slash URLs, since the static site
       does not serve .md files (the mkdocs-llmstxt plugin uses source paths).
    2. Injects a 'Last updated' date into llms-full.txt so AI assistants can
       assess content freshness when the file is cached or mirrored.
    3. Drops EXCLUDE_PREFIXES URLs from sitemap.xml so Google isn't pointed at
       the noindex'd pages.
    4. Removes the GraFx Publisher pointer/links from the llms.txt files.
    """
    site_dir = config["site_dir"]
    today = date.today().isoformat()

    for filename in ("llms.txt", "llms-full.txt"):
        filepath = os.path.join(site_dir, filename)
        if not os.path.exists(filepath):
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("/index.md", "/")
        if filename == "llms-full.txt":
            # Insert after the H1 title line (first line starting with "# ")
            lines = content.splitlines(keepends=True)
            for i, line in enumerate(lines):
                if line.startswith("# "):
                    lines.insert(i + 1, f"\n> Last updated: {today}\n")
                    break
            content = "".join(lines)
        content = _strip_llms(content, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    _strip_sitemap(site_dir)


def _strip_sitemap(site_dir):
    """Drop EXCLUDE_PREFIXES URLs from sitemap.xml and refresh sitemap.xml.gz."""
    path = os.path.join(site_dir, "sitemap.xml")
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        xml = f.read()
    segments = tuple(f"/{prefix}" for prefix in EXCLUDE_PREFIXES)

    def keep(match):
        block = match.group(0)
        loc = re.search(r"<loc>([^<]*)</loc>", block)
        if loc and any(seg in loc.group(1) for seg in segments):
            return ""
        return block

    xml = re.sub(r"\s*<url>.*?</url>", keep, xml, flags=re.DOTALL)
    with open(path, "w", encoding="utf-8") as f:
        f.write(xml)
    with open(path, "rb") as f_in, gzip.open(path + ".gz", "wb") as f_out:
        f_out.writelines(f_in)


def _strip_llms(content, filename):
    """Remove GraFx Publisher references from an llms.txt file's content."""
    result = content
    # Drop the "## GraFx Publisher" section (heading through the next heading or
    # page separator) from the full dump.
    if filename == "llms-full.txt":
        result = re.sub(
            r"^## GraFx Publisher\n.*?(?=^#|^_{3,})",
            "",
            result,
            flags=re.DOTALL | re.MULTILINE,
        )
    # Drop any remaining line that links into an excluded folder.
    segments = tuple(f"/{prefix}" for prefix in EXCLUDE_PREFIXES)
    kept = [
        line
        for line in result.splitlines(keepends=True)
        if not ("](" in line and any(seg in line for seg in segments))
    ]
    return "".join(kept)
