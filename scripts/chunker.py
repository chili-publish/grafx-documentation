"""Heading-aware chunking for documentation pages.

Pure text logic — no MkDocs, no network — so it is unit-testable in isolation.
Splits a page into chunks that each stay under a target size, breaking on
heading boundaries first and only splitting within an oversized section as a
fallback. Code fences are kept whole (never split mid-block).
"""
from __future__ import annotations

import re
from dataclasses import dataclass

# A heading line: 1-6 '#' then text. We chunk on h2/h3 boundaries; h1 is the
# page title and rarely repeats.
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_FENCE = re.compile(r"^(```|~~~)")


@dataclass
class Chunk:
    section: str      # nearest heading text above this chunk ("" if none yet)
    text: str


def _split_into_blocks(markdown: str) -> list[tuple[str, str]]:
    """Split markdown into (section, block_text) pairs on h2/h3 headings.

    Content before the first h2/h3 is attributed to the h1 title if present,
    else "". Code fences are opaque: heading-looking lines inside a fence are
    not treated as headings.
    """
    lines = markdown.splitlines()
    blocks: list[tuple[str, str]] = []
    current_section = ""
    buffer: list[str] = []
    in_fence = False

    def flush():
        if buffer and any(line.strip() for line in buffer):
            blocks.append((current_section, "\n".join(buffer).strip()))
        buffer.clear()

    for line in lines:
        if _FENCE.match(line.strip()):
            in_fence = not in_fence
            buffer.append(line)
            continue
        if not in_fence:
            m = _HEADING.match(line)
            if m:
                level = len(m.group(1))
                title = m.group(2).strip()
                if level == 1 and not current_section:
                    current_section = title  # page title seeds section
                    continue
                if level in (2, 3):
                    flush()
                    current_section = title
                    continue
        buffer.append(line)
    flush()
    return blocks


def _split_oversized(text: str, max_chars: int, overlap: int) -> list[str]:
    """Greedy paragraph-packing with character overlap for a too-long block.

    Never splits inside a code fence: a fenced block is emitted whole even if
    it exceeds max_chars (splitting code is worse than an oversized chunk).
    """
    paragraphs = re.split(r"\n\s*\n", text)
    out: list[str] = []
    current = ""
    for para in paragraphs:
        if not para.strip():
            continue
        candidate = f"{current}\n\n{para}".strip() if current else para
        if len(candidate) <= max_chars or not current:
            current = candidate
        else:
            out.append(current)
            tail = current[-overlap:] if overlap else ""
            current = f"{tail}\n\n{para}".strip() if tail else para
    if current:
        out.append(current)
    return out


def chunk_page(markdown: str, *, max_chars: int = 1200, overlap: int = 150) -> list[Chunk]:
    """Chunk a page's markdown heading-aware. Empty/whitespace pages -> []."""
    if not markdown or not markdown.strip():
        return []
    chunks: list[Chunk] = []
    for section, block in _split_into_blocks(markdown):
        if len(block) <= max_chars:
            chunks.append(Chunk(section=section, text=block))
        else:
            for piece in _split_oversized(block, max_chars, overlap):
                chunks.append(Chunk(section=section, text=piece))
    return chunks
