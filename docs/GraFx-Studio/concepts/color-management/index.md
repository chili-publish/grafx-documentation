# Color Management in PDF Output

This page helps Design System creators understand how color behaves in print so you can export predictable, brand-accurate PDFs from GraFx Studio.

## Why colors change between screen and print

On screen, you see color made of **light (RGB)**.  
In print, color is created with **ink (CMYK)** on paper.

Light and ink behave differently.

This means:

- Bright RGB colors may not exist in CMYK.
- The same CMYK values can look different on coated vs uncoated paper.
- Without proper settings, brand colors may shift during export or printing.

Color management ensures your design intent survives the transition from screen to press.

## What an ICC profile does

An **ICC profile** describes how a specific device or print condition reproduces color.

You can think of it as a **translation dictionary**.

Examples of print conditions:

- Coated paper (glossy magazines, flyers)
- Uncoated paper (letterheads, envelopes)
- Newspaper
- Web Coated (SWOP)
- GRACoL
- FOGRA

Each condition reflects:

- Ink behavior  
- Paper absorption  
- Total ink limits  
- Press characteristics  

When a PDF contains the correct ICC profile, downstream systems understand how the colors were intended to print.

## When color conversion is needed — a practical example

Imagine this situation:

Your headquarters prepares a campaign brochure for the US market using **Coated GRACoL 2006** (glossy paper).

Later, a European market needs to print the same design on **ISO Coated v2** or even on **uncoated paper** for in-store leaflets.

If you send the original CMYK values without conversion:

- Reds may print darker.
- Blues may shift toward purple.
- Dark areas may lose detail.
- Total ink coverage may exceed the press limits.

Color conversion recalculates the CMYK values for the new destination profile.

The design looks visually consistent — even though the actual CMYK numbers change.

That is the purpose of color transformation.

## What Output Intent means in a PDF

A PDF can contain an embedded ICC profile called the **Output Intent**.

This tells printers and RIP systems:

> “This document was prepared for this specific print condition.”

If no Output Intent is embedded:

- The printer may assume a default profile.
- Colors may be reinterpreted automatically.
- Results may vary between vendors or regions.

Embedding the correct profile increases predictability and reduces production risk.

## Your responsibility as a designer

In modern workflows, color accuracy is defined at export.

When you generate a PDF, you decide:

- Which print condition the file represents.
- Whether CMYK values should be converted.
- Which ICC profile is embedded.

These choices directly influence how your work reproduces in the real world.

You do not need to understand color science in depth.  
You need to align export settings with the intended print condition.

## How this connects to GraFx Studio

In GraFx Studio PDF output settings, you control:

- PDF version  
- Intended CMYK profile  
- Target CMYK profile  
- Output Intent embedding  

When these settings match your production workflow, your exported PDFs remain consistent, compliant, and brand-safe.

For configuration details, see:

- [PDF Output Settings](/GraFx-Studio/guides/output/settings/#pdf-output-settings)