# Elements  

Within each Brand Kit you can manage:

| Element               | Description                                              |
|-----------------------|----------------------------------------------------------|
| **Colors**            | Named swatches (e.g. Primary, Secondary) in RGB/CMYK/HEX/...     |
| **Fonts**             | OpenType/TrueType fonts to use in GraFx Studio templates |
| **Media**             | Logos or other image assets                              |
| **Paragraph styles**  | Font, size, spacing, alignment for paragraphs            |
| **Character styles**  | Font, size, formatting for inline text                   |

Elements are defined on the Brand Kit's default [theme](/GraFx-Brand-Kits/concepts/themes/) and can be overridden per theme.

!!! info "Brand Kit elements and design tokens"
    If you know [design tokens](https://en.wikipedia.org/wiki/Design_system#Design_tokens){target="_blank"} from design systems: a design token is an atomic value (`color.primary = #0055FF`, `color.primary.print = cmyk(100, 60, 0, 0)`, `font.size.body = 16px`). Brand Kit elements sit one level above. Colors come closest to tokens — named values defined once and reused — while a paragraph or character style combines multiple design decisions (font family, size, weight, line height) into one reusable style. [Themes](/GraFx-Brand-Kits/concepts/themes/) then map different values onto the same elements, much like token modes.

    Design tokens (atomic values) → Brand Kit elements (styles) → Themes (value mapping) → Templates

    So while we don't use the token terminology, a Brand Kit is fully compatible with a token-based design system.

![screenshot-full](brandkits_01.png)