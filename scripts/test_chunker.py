from scripts.chunker import Chunk, chunk_page


def test_empty_page_yields_nothing():
    assert chunk_page("") == []
    assert chunk_page("   \n\n  ") == []


def test_splits_on_h2_headings():
    md = "# Title\n\nIntro text.\n\n## First\n\nAlpha.\n\n## Second\n\nBeta."
    chunks = chunk_page(md)
    sections = [c.section for c in chunks]
    assert sections == ["Title", "First", "Second"]
    assert chunks[0].text == "Intro text."
    assert chunks[1].text == "Alpha."


def test_h1_seeds_section_for_intro():
    md = "# Page Title\n\nSome intro before any subheading."
    chunks = chunk_page(md)
    assert len(chunks) == 1
    assert chunks[0].section == "Page Title"


def test_code_fence_not_treated_as_heading():
    md = "## Example\n\n```python\n# this is a comment, not a heading\nx = 1\n```"
    chunks = chunk_page(md)
    assert len(chunks) == 1
    assert chunks[0].section == "Example"
    assert "# this is a comment" in chunks[0].text


def test_oversized_section_splits_with_overlap():
    para = "word " * 100  # ~500 chars
    md = "## Big\n\n" + "\n\n".join([para] * 5)  # ~2500 chars, one section
    chunks = chunk_page(md, max_chars=800, overlap=50)
    assert len(chunks) > 1
    assert all(c.section == "Big" for c in chunks)
    assert all(len(c.text) <= 800 for c in chunks)  # bounded by the passed max_chars


def test_oversized_single_paragraph_is_bounded():
    para = "word " * 400  # ~2000 chars in ONE paragraph (no blank lines)
    md = "## Wall\n\n" + para
    chunks = chunk_page(md, max_chars=800, overlap=50)
    assert len(chunks) > 1
    assert all(c.section == "Wall" for c in chunks)
    assert all(len(c.text) <= 800 for c in chunks)


def test_code_block_kept_whole_even_if_oversized():
    big_code = "```\n" + ("x = 1\n\ny = 2\n" * 100) + "```"  # blank lines INSIDE the fence
    md = f"## Code\n\n{big_code}"
    chunks = chunk_page(md, max_chars=200)
    fenced = [c for c in chunks if "```" in c.text]
    assert len(fenced) == 1                    # the fence was not split apart
    assert fenced[0].text.count("```") == 2    # both markers in one chunk
