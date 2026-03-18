import os
from datetime import date


def on_post_build(config, **kwargs):
    """Post-build fixes for llms.txt and llms-full.txt.

    1. Rewrites /index.md URLs to trailing-slash URLs, since the static site
       does not serve .md files (the mkdocs-llmstxt plugin uses source paths).
    2. Injects a 'Last updated' date into llms-full.txt so AI assistants can
       assess content freshness when the file is cached or mirrored.
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
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
