# Color Management in PDF Output

This page helps graphic designers understand how color behaves in print so you can export predictable, brand-accurate PDFs from GraFx Studio.

## Why colors change between screen and print

On screen, you see color made of **light (RGB)**.  
In print, color is created with **ink (CMYK)** on paper.

Light and ink behave differently.

This means:

- Bright RGB colors may not exist in CMYK.
- The same CMYK values can look different on coated vs uncoated paper.
- Without proper settings, brand colors may shift during export or printing.

Color management ensures your design intent survives the transition from screen to press.


## Color model vs. color space

A **color model** defines how color is expressed numerically.

Examples:
- RGB  
- CMYK  
- Gray  
- Lab  

A **color space** adds real-world meaning to those numbers.

It defines:
- The white point  
- Tone response  
- Gamut boundaries  
- Print condition  

Important:

CMYK is not one universal standard.

For example:

- 100 / 80 / 0 / 0 in **FOGRA39**
- 100 / 80 / 0 / 0 in **FOGRA52**

These are both CMYK values — but they do not produce the same visual result.

CMYK numbers only make sense when tied to a specific color space.


## What an ICC profile does

An **ICC profile** describes how a specific device or print condition reproduces color.

You can think of it as a **translation dictionary**.

Examples of print conditions:

- Coated paper (glossy brochures)
- Uncoated paper (letterheads)
- Newspaper
- Web Coated (SWOP)
- GRACoL
- FOGRA

The ICC profile defines how colors should appear under that condition.

When color conversion is applied, the ICC profiles determine how colors are recalculated for the destination print condition.


## When color conversion is needed — practical example

Imagine this situation:

Your headquarters prepares a campaign brochure for the US market using **FOGRA39** (coated paper).

Later, a regional team needs to print the same design on **FOGRA52** (uncoated paper).

Both workflows use CMYK.

If you send the original CMYK numbers unchanged:

- Blues may become duller.
- Reds may darken.
- Dark areas may lose detail.
- Ink coverage may exceed limits.

Color conversion recalculates the CMYK values for the new destination profile.

The numbers change — but the visual appearance stays as close as possible to the original.

This is CMYK-to-CMYK conversion.

It is one of the most common real-world use cases in multi-region retail production.


## Rendering intent — how out-of-gamut colors are handled

Some colors in the source profile cannot be reproduced exactly in the destination profile.

A **rendering intent** defines how the system handles those colors.

Conceptually, it answers:

> What should be preserved first — accuracy, contrast, or saturation?

In GraFx workflows, the rendering intent defined in the document is preserved.  
If none is defined, a standard default is used.

This influences how color conversion behaves.


## Black preservation and dark colors

Black behaves differently in different print conditions.

During conversion:

- Pure black text (100K) should remain pure black.
- Rich black backgrounds should not shift unexpectedly.
- Very dark areas should retain detail.

Modern color pipelines protect:

- Small black typography  
- Logos using pure black  
- Deep shadows in photography  

Without these safeguards, black elements can become washed out or contaminated with additional color.


## Profile compatibility matters

Not all profiles are interchangeable.

Some print conditions are fundamentally different:

- Newspaper vs coated stock  
- Low ink limit vs high ink limit  
- Different gray balance strategies  

Converting between incompatible profiles can cause visible shifts or production risks.

Always align:

- Intended print condition  
- Destination print condition  


## Your responsibility as a designer

In modern workflows, color accuracy is defined at export.

When you generate a PDF, you decide:

- Which print condition the file represents.
- Whether CMYK values should be converted.

These choices directly influence how your work reproduces in the real world.

You do not need to understand color science in depth.  
You need to align export settings with the intended print condition.


## How this connects to GraFx Studio

In GraFx Studio PDF output settings, you control:

- PDF version  
- Intended CMYK profile  
- Target CMYK profile  

When these settings match your production workflow, your exported PDFs remain consistent, compliant, and brand-safe.

For configuration details, see:

- [PDF Output Settings](../../GraFx-Studio/guides/output/settings/#pdf-output-settings)