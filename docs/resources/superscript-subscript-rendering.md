---
search:
  exclude: true
noindex: true
---

# Upcoming Change: Superscript and Subscript Rendering in GraFx Studio

![CHILI GraFx icon](/assets/icon-CHILI-GraFx.svg){.rn_icon}

**What is changing.** Many fonts include their own instructions for how
superscript and subscript characters should look — how large they are and how
far above or below the baseline they sit. Until now, GraFx Studio ignored those
instructions and applied a single fixed style to all fonts. From GraFx Studio
**1.46.0**, superscript and subscript text follows the settings built into each
font.

**What this means for your templates.** Superscript and subscript text may
render at a slightly different size or position than before. Normal (baseline)
text is unaffected, and content, fonts, and layout are otherwise unchanged.
Because most fonts define these settings, templates that use superscript or
subscript will generally see some change. How noticeable it is depends on the
font — from barely perceptible to clearly visible — so it's worth reviewing any
template where the appearance of this text matters.

!!! note "Visual changes possible"

    If your templates use superscript or subscript text, its size and vertical
    position may change after this update. How noticeable the change is depends
    on the font and the design, so we recommend reviewing templates where the
    appearance of this text matters before adopting the new version.

## How to check if your templates are affected

The most reliable way to see the impact is to compare your own templates before
and after the update:

1. **Identify the templates that use superscript or subscript formatting.** This
   formatting is common in trademark and registered symbols, footnote markers,
   ordinal numbers (1<sup>st</sup>, 2<sup>nd</sup>), prices with raised cents
   ($19<sup>99</sup>), units of measurement (m<sup>2</sup>, cm<sup>3</sup>), and
   chemical formulas (H<sub>2</sub>O, CO<sub>2</sub>).
2. **Before updating**, export each of the identified templates to PDF or image
   on your current version and keep the output as a reference.
3. **After updating to 1.46.0**, export the same templates again.
4. **Compare the before and after output** and confirm the superscript and
   subscript text still looks acceptable.

Where the appearance has changed in a way you are not happy with, adjust the
template on the new version — for example, the font, the text size, or the
surrounding layout — until the result meets your needs.

!!! note "Rolling back a version"

    As long as a template has not been saved on the new version, you can roll
    back to an earlier version. See
    [Manage environment version](/CHILI-GraFx/guides/manage-environment-version/)
    for the steps.

!!! warning "Testing on a live environment"

    If you are testing on a live environment, changing the version could mean
    that end-user projects are saved in the newest version. Check with your
    integration team, or contact our support team to discuss options.

## Technical details

For those who want to know exactly what changed:

- **Source of the metrics.** GraFx Studio now reads the superscript and
  subscript values from the font's **OS/2 table** — the horizontal and vertical
  size (`ySuperscript`/`ySubscript` X and Y size) and the vertical offset
  (`Y offset`) — and applies them when laying out the text.
- **Previous behaviour.** Before 1.46.0, these values were ignored. Superscript
  and subscript were drawn at a single fixed scale and offset derived internally,
  regardless of the font.
- **Fallback.** If a font leaves these OS/2 values unset (zero), GraFx Studio
  keeps the previous default behaviour for that font. In practice almost all
  fonts define them, so the fallback rarely applies.
- **Two things can shift.** Both the **size** and the **vertical position** now
  come from the font. Size is no longer forced to be uniform, so superscript and
  subscript glyphs can be scaled slightly differently in width and height than
  before.
- **Possible reflow.** Because the size of superscript and subscript characters
  can change, the width they occupy can change too. In tightly fitted text
  frames, this may nudge the surrounding text slightly.

---

If you have questions or need more guidance, please open a ticket at
[mysupport.chili-publish.com](https://mysupport.chili-publish.com).
