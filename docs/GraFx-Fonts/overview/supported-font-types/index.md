# Supported Font Types

## Supported fonts

GraFx Fonts supports [OTF](https://en.wikipedia.org/wiki/OpenType) and [TTF](https://en.wikipedia.org/wiki/TrueType).

	- Open Type Fonts (OTF)
	- True Type Fonts (TTF)

## These fonts are <u>NOT</u> Supported

Except OTF or TTF, other font files are not supported.

Some font types have similar names, we added them below as <u>NOT</u> supported to avoid confusion.

	- Web Open Font Format (WOFF & WOFF2)
	- Variable Fonts a.k.a. OpenType Font Variations
	- Postscript Type 1
	- EOT (Embedded Open Type)
	- SVG Fonts
	- ...
	
## Font-table support in CHILI GraFx

GraFx Fonts stores your **TrueType** (`.ttf`) and **OpenType** (`.otf`) files and delivers them to **GraFx Studio**.  
Whether every typographic feature actually shows up in the editor, however, depends on the **OpenType tables** that the GraFx Studio engine already understands.

### Example: Ligatures

Think of each table as a plug-in that unlocks extra behaviour.  
For example, the `GSUB` table can contain a *ligature* rule that turns the letter sequence “f” + “i” into the single “ﬁ” glyph.  
If GraFx Studio supports the relevant `GSUB` sub-table, the ligature will appear; if not, the two separate letters render instead (the text still prints—just without the fancy substitution).

![screenshot](ligature.svg)

> **In short**  
> *If your font is OpenType/TrueType and the tables required for your language or feature are listed with a **✅**, GraFx Studio will display the full typographic behaviour.*

## How to read the table

| Column | Meaning |
|--------|---------|
| **Table tag** | The four-letter OpenType table identifier (linked to the Microsoft spec). |
| **Sub-table / Format** | Some tables contain different “lookup” formats. Only the formats listed here are evaluated. |
| **Description** | What the table/format is used for. |
| **Supported** |✅ = implemented & fully functional<br>🚫 = not yet implemented (font still loads; feature is ignored). |

If a row shows **no entry** in the *Sub-table* column, the whole table is evaluated as a single unit.

## Supported tables (and those still in progress)

| Table tag | Sub-table / Format | Description | Supported |
|-----------|--------------------|-------------|-----------|
| [`avar`](https://learn.microsoft.com/en-us/typography/opentype/spec/avar) |&nbsp;| Axis Variations Table | 🚫 |
| [`BASE`](https://learn.microsoft.com/en-us/typography/opentype/spec/base) |&nbsp;| Baseline Table | 🚫 |
| [`CBDT`](https://learn.microsoft.com/en-us/typography/opentype/spec/cbdt) |&nbsp;| Color Bitmap Data | 🚫 |
| [`CBLC`](https://learn.microsoft.com/en-us/typography/opentype/spec/cblc) |&nbsp;| Color Bitmap Location | 🚫 |
| [`CFF`](https://learn.microsoft.com/en-us/typography/opentype/spec/cff) |&nbsp;| Compact Font Format (v1) | ✅ |
| [`CFF2`](https://learn.microsoft.com/en-us/typography/opentype/spec/cff2) |&nbsp;| Compact Font Format (v2) | 🚫 |
| [`cmap`](https://learn.microsoft.com/en-us/typography/opentype/spec/cmap) | 0&nbsp;Unicode | Character → Glyph mapping | ✅ |
|  | 1&nbsp;Macintosh |  | ✅ |
|  | 2&nbsp;ISO *(deprecated)* |  | 🚫 |
|  | 3&nbsp;Windows |  | ✅ |
|  | 4&nbsp;Custom (NT compat.) |  | 🚫 |
| [`COLR`](https://learn.microsoft.com/en-us/typography/opentype/spec/colr) |&nbsp;| Colour Layers | 🚫 |
| [`CPAL`](https://learn.microsoft.com/en-us/typography/opentype/spec/cpal) |&nbsp;| Colour Palettes | 🚫 |
| [`cvar`](https://learn.microsoft.com/en-us/typography/opentype/spec/cvar) |&nbsp;| CVT Variations | 🚫 |
| [`cvt `](https://learn.microsoft.com/en-us/typography/opentype/spec/cvt) |&nbsp;| Control Value Table | 🚫 |
| [`DSIG`](https://learn.microsoft.com/en-us/typography/opentype/spec/dsig) |&nbsp;| Digital Signature | 🚫 |
| [`EBDT`](https://learn.microsoft.com/en-us/typography/opentype/spec/ebdt) |&nbsp;| Embedded Bitmap Data | 🚫 |
| [`EBLC`](https://learn.microsoft.com/en-us/typography/opentype/spec/eblc) |&nbsp;| Embedded Bitmap Location | 🚫 |
| [`EBSC`](https://learn.microsoft.com/en-us/typography/opentype/spec/ebsc) |&nbsp;| Embedded Bitmap Scaling | 🚫 |
| [`fpgm`](https://learn.microsoft.com/en-us/typography/opentype/spec/fpgm) |&nbsp;| Font Program | 🚫 |
| [`fvar`](https://learn.microsoft.com/en-us/typography/opentype/spec/fvar) |&nbsp;| Font Variations (axes) | 🚫 |
| [`gasp`](https://learn.microsoft.com/en-us/typography/opentype/spec/gasp) |&nbsp;| Grid-fitting & Scan-conv. | 🚫 |
| [`GDEF`](https://learn.microsoft.com/en-us/typography/opentype/spec/gdef) |&nbsp;| Glyph Definition | ✅ |
| [`glyf`](https://learn.microsoft.com/en-us/typography/opentype/spec/glyf) |&nbsp;| Glyph outlines (TrueType) | ✅ |
| [`GPOS`](https://learn.microsoft.com/en-us/typography/opentype/spec/gpos) | 1 Single adjust | Position a single glyph | ✅ |
|  | 2 Pair adjust | Kerning pairs | ✅ |
|  | 3 Cursive | Cursive attachment | ✅ |
|  | 4 Mark-to-Base |  | ✅ |
|  | 5 Mark-to-Ligature |  | ✅ |
|  | 6 Mark-to-Mark |  | ✅ |
|  | 7 Contextual pos. |  | 🚫 |
|  | 8 Chained context pos. |  | 🚫 |
|  | 9 Extension pos. |  | 🚫 |
| [`GSUB`](https://learn.microsoft.com/en-us/typography/opentype/spec/gsub) | 1 Single | One-to-one substitution | ✅ |
|  | 2 Multiple | One-to-many substitution | ✅ |
|  | 3 Alternate | One-to-many alternate | 🚫 |
|  | 4 Ligature | Many-to-one ligature | ✅ |
|  | 5 Contextual |  | 🚫 |
|  | 6 Chained contexts | see sub-formats |&nbsp;|
|  | 6.1 Simple |  | 🚫 |
|  | 6.2 Class based |  | ✅ |
|  | 6.3 Coverage |  | ✅ |
|  | 7 Extension sub. |  | 🚫 |
|  | 8 Reverse chaining |  | 🚫 |
| [`gvar`](https://learn.microsoft.com/en-us/typography/opentype/spec/gvar) |&nbsp;| Glyph Variations | 🚫 |
| [`hdmx`](https://learn.microsoft.com/en-us/typography/opentype/spec/hdmx) |&nbsp;| Horizontal Device Metrics | 🚫 |
| [`head`](https://learn.microsoft.com/en-us/typography/opentype/spec/head) |&nbsp;| Font Header | ✅ |
| [`hhea`](https://learn.microsoft.com/en-us/typography/opentype/spec/hhea) |&nbsp;| Horizontal Header | ✅ |
| [`hmtx`](https://learn.microsoft.com/en-us/typography/opentype/spec/hmtx) |&nbsp;| Horizontal Metrics | ✅ |
| [`HVAR`](https://learn.microsoft.com/en-us/typography/opentype/spec/hvar) |&nbsp;| Horizontal Metrics Variations | 🚫 |
| [`JSTF`](https://learn.microsoft.com/en-us/typography/opentype/spec/jstf) |&nbsp;| Justification | 🚫 |
| [`kern`](https://learn.microsoft.com/en-us/typography/opentype/spec/kern) | Format 0 | Classic kern table | ✅ |
|  | Format 2 | State-table kern | 🚫 |
| [`loca`](https://learn.microsoft.com/en-us/typography/opentype/spec/loca) |&nbsp;| Index to Location | ✅ |
| [`LTSH`](https://learn.microsoft.com/en-us/typography/opentype/spec/ltsh) |&nbsp;| Linear Threshold | 🚫 |
| [`MATH`](https://learn.microsoft.com/en-us/typography/opentype/spec/math) |&nbsp;| Math Typesetting | 🚫 |
| [`maxp`](https://learn.microsoft.com/en-us/typography/opentype/spec/maxp) |&nbsp;| Maximum Profile | 🚫 |
| [`MERG`](https://learn.microsoft.com/en-us/typography/opentype/spec/merg) |&nbsp;| Merge Table | 🚫 |
| [`meta`](https://learn.microsoft.com/en-us/typography/opentype/spec/meta) |&nbsp;| Metadata | 🚫 |
| [`MVAR`](https://learn.microsoft.com/en-us/typography/opentype/spec/mvar) |&nbsp;| Metrics Variations | 🚫 |
| [`name`](https://learn.microsoft.com/en-us/typography/opentype/spec/name) |&nbsp;| Naming Table | ✅ |
| [`OS/2`](https://learn.microsoft.com/en-us/typography/opentype/spec/os2) |&nbsp;| OS/2 & Windows Metrics | ✅ |
| [`PCLT`](https://learn.microsoft.com/en-us/typography/opentype/spec/pclt) |&nbsp;| PCL 5 data | 🚫 |
| [`post`](https://learn.microsoft.com/en-us/typography/opentype/spec/post) |&nbsp;| PostScript info | ✅ |
| [`prep`](https://learn.microsoft.com/en-us/typography/opentype/spec/prep) |&nbsp;| Control Value Programme | 🚫 |
| [`sbix`](https://learn.microsoft.com/en-us/typography/opentype/spec/sbix) |&nbsp;| Standard Bitmap Graphics | 🚫 |
| [`STAT`](https://learn.microsoft.com/en-us/typography/opentype/spec/stat) |&nbsp;| Style Attributes | 🚫 |
| [`SVG`](https://learn.microsoft.com/en-us/typography/opentype/spec/svg) |&nbsp;| Embedded SVG glyphs | 🚫 |
| [`VDMX`](https://learn.microsoft.com/en-us/typography/opentype/spec/vdmx) |&nbsp;| Vertical Device Metrics | 🚫 |
| [`vhea`](https://learn.microsoft.com/en-us/typography/opentype/spec/vhea) |&nbsp;| Vertical Header | 🚫 |
| [`vmtx`](https://learn.microsoft.com/en-us/typography/opentype/spec/vmtx) |&nbsp;| Vertical Metrics | 🚫 |
| [`VORG`](https://learn.microsoft.com/en-us/typography/opentype/spec/vorg) |&nbsp;| Vertical Origin | 🚫 |
| [`VVAR`](https://learn.microsoft.com/en-us/typography/opentype/spec/vvar) |&nbsp;| Vertical Metrics Variations | 🚫 |

> **Need a table that isn’t supported yet?**  
> Let us know via the regular [GraFx Support](/CHILI-GraFx/support/) feedback channels so we can put it on the feature request list.


## Frequently-asked questions

### “My font loads but kerning is wrong”

Check whether the font relies on:

* **GPOS 7/8** (contextual positioning)&nbsp;not yet implemented, or  
* **kern format 2**&nbsp;also unsupported.

Replacing the font with an updated OpenType that uses `GPOS 1/2` pair-kerning usually solves the issue.

### “Can I use color fonts?”

`COLR` / `CPAL` tables (plus `SVG`, `sbix`, `CBDT/CBLC`) are **not** supported at this moment.  
Colour glyphs will fall back to the primary outline data.

### “Will variable fonts work?”

Variation-axis tables (`fvar`, `gvar`, `HVAR`, `MVAR`, `VVAR`, `avar`, `cvar`) are still in progress.  
Variable fonts load, but only their *default* instance is rendered.

---

## Helpful references

* Microsoft OpenType spec hub  
  <https://learn.microsoft.com/en-us/typography/opentype/spec/>
* Chapter 2&nbsp;**“Structure of OpenType fonts”**  
  <https://learn.microsoft.com/en-us/typography/opentype/spec/chapter2>
* Common variable-font formats  
  <https://learn.microsoft.com/en-us/typography/opentype/spec/otvarcommonformats>

For an interactive check you can also upload any font to <https://fontdrop.info/> to inspect which tables it contains.