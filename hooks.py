import os


def on_post_build(config, **kwargs):
    """Fix .md URLs in llms.txt and llms-full.txt to use rendered page URLs.

    The mkdocs-llmstxt plugin generates links using source file paths
    (e.g. /renders/index.md) rather than the built page URLs (/renders/).
    Since the static site does not serve .md files, this hook rewrites
    /index.md → / so all links resolve correctly.
    """
    site_dir = config["site_dir"]
    for filename in ("llms.txt", "llms-full.txt"):
        filepath = os.path.join(site_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            content = content.replace("/index.md", "/")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
