# Use cases

## The basics

A Brand Kit is the single source of truth for a visual identity: its colors, fonts, media, and text styles are defined once and reused across Design Systems in GraFx Studio.

With [themes](/GraFx-Brand-Kits/concepts/themes/), that single source of truth can carry **variations**. The default theme defines the full brand; each additional theme overrides only what differs. Switching the theme swaps those values throughout the content that uses the Brand Kit — no duplicated Brand Kits, no manual rework.

The variations typically follow one of these dimensions: **brand**, **channel**, or **region**.

## Brand, sub-brand, and flavor

A company rarely has just one face. A master brand often coexists with sub-brands, product lines, or flavors that share most of the identity but differ in a few defining elements.

Model this with the master brand as the default theme, and one theme per sub-brand or flavor:

- A beverage brand where each flavor has its own accent color and packaging imagery, while typography and logo placement stay identical.
- A corporate brand with sub-brands that override the primary color and logo but inherit all text styles.

Only the differences live in each theme — everything else follows the master brand automatically.

## Channel: digital (RGB) vs. print (CMYK)

Digital output wants RGB colors; print-ready PDF wants CMYK. Instead of maintaining two Brand Kits, define your palette in RGB on the default theme and create a **Print** theme that overrides each color with its CMYK counterpart.

The same named color — "Primary", "Accent" — resolves to the right color space for the channel, so designs stay color-accurate from screen to press. In [design-token terms](/GraFx-Brand-Kits/concepts/elements/): one token, two values — `color.primary = #0055FF` for digital, `color.primary.print = cmyk(100, 60, 0, 0)` for print.

Theme switching can be automated with [Actions](/GraFx-Studio/concepts/actions/): using `switchTheme(name)`, a template can for example switch to the Print theme whenever the selected layout changes to a print layout.

## Region: local scripts and fonts

Global brands adapt to local markets. A theme per region can override:

- **Text styles** — an Arabic theme whose paragraph and character styles use a typeface supporting Arabic script. The Brand Kit's font list itself is shared across all themes, so add the script-capable font to the Brand Kit and let the regional theme's styles use it.
- **Media** — region-specific logos, certification marks, or imagery.

The regional theme inherits everything else, so a global brand refresh in the default theme reaches every region instantly.
