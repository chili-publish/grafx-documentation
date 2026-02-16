# Color Management in PDF Output

This page helps graphic designers understand how color management works in PDF generation so you can confidently control how your designs reproduce in print and digital workflows.

## Why color management matters

When you design, you see color on a screen.

When your design is printed, those colors are reproduced using ink on paper.

Screens use **RGB light**.  
Print uses **CMYK ink**.

Those two worlds behave differently.

Without color management:
- Brand colors shift
- Dark images lose detail
- Printed output looks dull or oversaturated
- Different print vendors produce inconsistent results

Color management ensures that what you designed is translated predictably to the final output.

---

## The role of ICC profiles

An **ICC profile** is a description of how a device reproduces color.

It defines:
- How a specific press prints
- How a specific paper behaves
- How colors are interpreted

You can think of it as a translation dictionary between devices.

Examples:
- Coated paper profiles
- Uncoated paper profiles
- Newspaper profiles
- Web Coated (SWOP)
- GRACoL
- FOGRA

Choosing the correct ICC profile ensures your colors are converted for the correct printing condition.

---

## Color conversion (Color Transformation)

When converting from one color space to another (for example RGB → CMYK), the system must decide how to handle colors that cannot be reproduced exactly.

This is controlled by the **rendering intent**.

Typical intents:

- **Perceptual** – Adjusts all colors slightly to preserve visual relationships.
- **Relative Colorimetric** – Keeps accurate colors where possible, clips out-of-gamut colors.
- **Absolute Colorimetric** – Simulates the paper color.
- **Saturation** – Prioritizes vividness over accuracy.

For brand and marketing materials, Perceptual or Relative Colorimetric are most common.

---

## Output Intent embedding

A PDF can contain an embedded ICC profile called the **Output Intent**.

This tells the printer:

> “This document was prepared for this exact print condition.”

Without Output Intent embedding:
- The printer may assume a default profile.
- Colors may be reinterpreted incorrectly.
- Brand colors may shift.

Embedding the correct profile increases predictability across print environments.

---

## What this means for designers

As a designer, you do not need to become a color scientist.

You need to:

- Understand the target output (coated, uncoated, newspaper, etc.)
- Choose the correct ICC profile
- Ensure the PDF is exported with proper color transformation
- Embed the correct Output Intent

When these are aligned, your creative intent survives the transition from screen to press.

---

## Related guides

- [PDF Output Settings](/GraFx-Studio/guides/output/settings/#pdf-output-settings)