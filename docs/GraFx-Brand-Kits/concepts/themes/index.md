# Themes

A **theme** is a variation of a Brand Kit.

Every Brand Kit has a **default theme** that holds the complete set of elements — colors, fonts, media, paragraph styles, and character styles. On top of that, you can create additional themes that represent variations of the same brand.

## Inheritance

- New themes **inherit all elements from the default theme**.
- In a theme, you override only what differs — a color value, the font used in a style, a logo.
- Everything you don't override stays linked to the default theme: update an element in the default theme, and every theme that doesn't override it picks up the change automatically.

This makes the default theme the single source of truth, and keeps each theme small: a theme only stores its differences.

If you come from a design-token world: themes are the value-mapping layer. The same named [element](/GraFx-Brand-Kits/concepts/elements/) resolves to a different value per theme — like token modes, where `color.primary` holds an RGB value for digital and a CMYK value for print.

!!! info "Good to know"
    - **The font list is shared across all themes** — by design, a theme does not add or remove fonts. Styles, however, can be overridden per theme to use a different font from the shared list.
    - The **structure** of a Brand Kit (adding, renaming, removing elements) is managed on the default theme; other themes override values only.

## Why themes

Themes let one Brand Kit serve multiple variations of a visual identity — a sub-brand, a print-specific color palette, a regional text style — without duplicating the entire Brand Kit and maintaining the copies separately.

See [Use cases](/GraFx-Brand-Kits/concepts/use-cases/) for typical scenarios, and [Manage themes](/GraFx-Brand-Kits/guides/themes/) for the how-to.

## Themes in GraFx Studio

In the Studio workspace, the Brand Kit panel offers a theme selector: switching the theme updates all Brand Kit elements used in the template — colors, text styles, media — on the canvas and in the property panels. Themes can also be switched programmatically via Actions and the Studio SDK. See [How to use Brand Kits in a template](/GraFx-Studio/guides/brandkits/).
