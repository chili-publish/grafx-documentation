# Text direction in GraFx Studio

GraFx Studio supports both **left-to-right (LTR)** and **right-to-left (RTL)** writing systems. This is essential for working with global content, including Latin-based scripts, Cyrillic, Greek, Indic scripts, Arabic and others.

## Script-based direction

In GraFx Studio, you do not need to set the text direction manually.  
The platform automatically determines direction based on the script in use:

- Latin, Cyrillic, Greek, Indic, Chinese, ... → **Left to Right**  
- Arabic, Persian (Farsi), Urdu, ... → **Right to Left**  

This means that as soon as you type or paste text in an RTL script (for example, Arabic), the text will render correctly in that direction.

!!! note "Important"
    To display complex scripts correctly (for example Arabic with ligatures), the font must include the required OpenType features.

## Paragraph alignment

Text alignment is separate from text direction. You can align a paragraph **left, right, or center** regardless of whether the script flows left-to-right or right-to-left.

- Example: Arabic (RTL) text aligned **left**  
- Example: English (LTR) text aligned **right**

This flexibility lets you control the visual layout of a document without affecting the inherent reading direction of the text.

## Why this matters

- **Consistency**: Editors and end users don’t need to worry about choosing the “right” text direction.  
- **Accuracy**: Script rules (ligatures, joining forms, diacritics) are applied automatically based on supported OpenType tables (`GSUB`, `GPOS`).  
- **Flexibility**: Alignment is a layout choice, independent of the natural reading order of the script.  

!!! tip "Remember"
    Direction is determined by the **script**, not by a setting in the editor.
