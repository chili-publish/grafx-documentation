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


def _tokenize_units(text: str) -> list[tuple[str, str]]:
    """Split a block into atomic units: ('code', fenced_block) or ('prose', paragraph).

    A fenced code block is emitted whole, including any blank lines inside it,
    so re.split on blank lines can never tear a fence apart. Prose between
    fences is split on blank lines into paragraphs.
    """
    units: list[tuple[str, str]] = []
    lines = text.split("\n")
    prose: list[str] = []

    def flush_prose():
        if not prose:
            return
        joined = "\n".join(prose)
        for para in re.split(r"\n\s*\n", joined):
            if para.strip():
                units.append(("prose", para.strip()))
        prose.clear()

    i = 0
    while i < len(lines):
        line = lines[i]
        if _FENCE.match(line.strip()):
            flush_prose()
            fence = [line]
            i += 1
            while i < len(lines):
                fence.append(lines[i])
                closed = bool(_FENCE.match(lines[i].strip()))
                i += 1
                if closed:
                    break
            units.append(("code", "\n".join(fence)))
        else:
            prose.append(line)
            i += 1
    flush_prose()
    return units


def _hard_split(text: str, max_chars: int, overlap: int) -> list[str]:
    """Split an oversized prose paragraph into <= max_chars pieces, word-aware,
    carrying a character-overlap tail between consecutive pieces. A lone token
    longer than max_chars (e.g. a huge URL) is character-sliced as a last resort.
    """
    pieces: list[str] = []
    current = ""
    for word in text.split():
        while len(word) > max_chars:
            if current:
                pieces.append(current)
                current = ""
            pieces.append(word[:max_chars])
            word = word[max_chars:]
        candidate = f"{current} {word}".strip() if current else word
        if len(candidate) <= max_chars:
            current = candidate
        else:
            pieces.append(current)
            tail = current[-overlap:] if overlap else ""
            current = f"{tail} {word}".strip() if tail else word
    if current:
        pieces.append(current)
    return pieces


def _split_oversized(text: str, max_chars: int, overlap: int) -> list[str]:
    """Pack an oversized block into <= max_chars chunks.

    Fenced code blocks stay atomic (emitted whole even if they exceed max_chars,
    since splitting code is worse than an oversized chunk). Oversized prose
    paragraphs are hard-split so no non-code chunk exceeds max_chars. Adjacent
    units are greedily packed with a character overlap between chunks.
    """
    atoms: list[tuple[str, str]] = []
    for kind, unit in _tokenize_units(text):
        if kind == "prose" and len(unit) > max_chars:
            atoms.extend(("prose", piece) for piece in _hard_split(unit, max_chars, overlap))
        else:
            atoms.append((kind, unit))

    out: list[str] = []
    current = ""
    for kind, unit in atoms:
        if kind == "code" and len(unit) > max_chars:
            if current:
                out.append(current)
                current = ""
            out.append(unit)
            continue
        candidate = f"{current}\n\n{unit}".strip() if current else unit
        if len(candidate) <= max_chars:
            current = candidate
        else:
            out.append(current)
            tail = current[-overlap:] if overlap else ""
            candidate = f"{tail}\n\n{unit}".strip() if tail else unit
            if len(candidate) > max_chars:  # overlap tail pushed us over; drop it
                candidate = unit
            current = candidate
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
