# Anchoring

Anchoring allows you to attach frames to the **canvas** or other **frames** in your Smart Template.

Imagine you would like to have a logo positioned 10% of the top and 15% of the left of your design?

![screenshot-full](anchor01.png)

## Speed of creation

Why would I want to position my frame relative to the page or another frame?

Since GraFx Studio is all about automation of creation of variants, your output will take different sizes.

To **speed up the creation of variants**, anchoring will help you to get there faster.

## Anchor to Page

The first concept enables you to **anchor a frame to the page**.

This method will anchor the frame to a side of the page or canvas. By default, this anchor will be relative.

This means, when you position the frame on the canvas, the frame will also remember where it sits relative to the page.

![screenshot-full](anchor02.png)

## Anchor to Frame

A second concept enables you to **anchor a frame to another frame**.

![screenshot-full](anchor03.png)

The text frame will keep the same offset to the logo frame, when the canvas or page size is different.

## Inheritance

The settings for the anchors will be inherited to the sub layouts (see [Inheritance Model](/GraFx-Studio/concepts/layouts/#inheritance)).

This means, if you create a sub layout, and change the size of this layout, the anchors will make sure your frames are positioned as you intended with the anchors.

In the example below, a default Layout is Square. Where all frames are set to be positioned relative to the page.

![screenshot-full](anchor04.png)

A landscape sub layout inherits all settings, with a different canvas size.

The position of the frames will follow the relative positioning set by the anchors.

![screenshot-full](anchor05.png)

The same story goes when making a vertical sub layout. Only the canvas or page size is different, the relative position of the frames remains.

![screenshot-full](anchor06.png)

If you still want to make (subtle) changes, you can move the frame manually, or change the type of anchoring.

This will break the inheritance (with the parent). In the properties panel you'll see the new values in yellow that are now overrides of the parent layout.

![screenshot-full](anchor07.png)

## What's next?

Anchoring can work by itself. But it will be even more powerfull, if you combine it with other Smart Template concepts:

- [Actions](/GraFx-Studio/concepts/actions/)
- Autogrow
- [Copyfitting](/GraFx-Studio/guides/text-frame/#auto-resize)
- [Inheritance](/GraFx-Studio/concepts/layouts/#inheritance)
- [Layouts](/GraFx-Studio/concepts/layouts/)
- [Variables](/GraFx-Studio/concepts/variables/)