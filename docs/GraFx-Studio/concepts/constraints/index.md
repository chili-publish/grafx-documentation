## Constraints

In CHILI GraFx, **constraints** define how much freedom an end user has when interacting with a template. They describe *what is allowed*, *within which boundaries*, and *under which conditions* — all as part of the design system authored by the template designer.

Constraints are not about restricting creativity. They are about making intended flexibility explicit, so end users can confidently adapt designs without breaking layout, structure, or brand rules.

## Why Constraints Matter

Design systems have always protected brand consistency by limiting what end users could change. That approach was safe, but often rigid.

Constraints introduce a more refined model:  
instead of simply locking things down, the template designer can now **open up controlled freedom**. End users gain more room to adapt content, positioning, or structure — while the design system still enforces its rules automatically.

The result is more flexibility for end users, without sacrificing consistency, predictability, or governance at scale.

## What Constraints Do

Constraints govern key interactions, for example:
- Whether an object can be moved or resized.
- How content expands or contracts.
- If rotation is allowed and to what degree.

This ensures edits stay within safe, predictable bounds and that outputs remain structurally sound.

## Constraints per Frame Type

The available constraints depend on the type of frame selected.

**Image and shape frames** support movement (horizontal and vertical), rotation, and resize.

**Text frames** support the same movement, rotation, and resize options — and additionally expose **inline text editing constraints**. When inline editing is enabled, the template designer can further control exactly which styling options are available to the end user: which paragraph styles, character styles, and Brand Kit colors are permitted, and whether font size can be changed (and within what range).

This makes text frame constraints the most granular of all frame types. They control not just *where* the frame can go, but also *what* the end user can do inside it.

See [User Constraints for Text Frames](/GraFx-Studio/guides/text-frame/#user-constraints-for-text-frames) and [User Constraints for Image Frames](/GraFx-Studio/guides/image-frame/#user-constraints-for-image-frames) for the full options per frame type.

## Constraints and Design Systems

A design system defines *standards.* Constraints embed those standards into the template’s interactive behavior. The template designer sets rules such as:
- An image can move within a box but not resize beyond it.
- Text can grow up to a limit, never overflow.
- Rotation is restricted or disabled.

By enforcing these rules at the template level, end users can work efficiently without breaking the design.