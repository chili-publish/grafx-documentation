# Manual Crop Override

GraFx Studio supports multiple image crop modes that determine how an image fits into its frame: **Fill**, **Fit**, **Manual**, and **Smart Crop**.

## What is Manual Crop Override?

Manual Crop Override is a designer-driven enhancement on top of existing crop modes. It allows you to fine-tune the positioning of an image *manually*, and store this override so that it is consistently applied.

But only when:

- A specific **asset (image)**  
- Is loaded into a specific **layout**
- Into a specific **frame**

This gives you maximum control for *exactly the images that need it* — without interfering with automation for all the others.

## Why use Manual Crop Override?

While automated crop modes handle most use cases, some visual assets — like lifestyle photography - may need fine-tuning.

Example use case:
- You have 7 lifestyle images.
- Most work well with “Fill” or “Smart Crop.”
- But one image crops off the mountain you wanted in the picture.

Instead of altering the automation rules or editing the image, you manually position / scale it in the frame. The GraFx Studio stores this override just for that image, in that layout and frame. The next time the same image is loaded, the same position will be applied.

This gives you the best of both worlds:
- Automation by default.
- Manual control where it matters.

## How it works

When a designer manually repositions an image within a frame:
- The override is saved in the background.
- It is linked to the combination of **asset ID + layout ID + frame ID**.
- It only affects that exact combination.
- All other images continue to use the automated crop mode (Fill, Fit, Smart Crop, etc.).

If a different image is loaded, or the same image is used in a different frame/layout, the override won’t apply.

## Benefits

- Prevents incorrect auto-cropping for critical visuals.
- Keeps automated workflows intact.
- Requires no changes to templates or logic — it's a designer override.

## See also

- [Image Crop Modes](/GraFx-Studio/concepts/image-crop-modes/)
- [How to Apply a Manual Crop Override](/GraFx-Studio/guides/manual-crop-override/)