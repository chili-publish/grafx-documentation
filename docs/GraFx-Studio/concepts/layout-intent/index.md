# Layout Intent

Intents enhance the functionality of layouts. Each layout now includes an "Intent" property with three possible values: 

- Print 
- Digital static
- Digital animated

This property provides contextual guidance for both Template Designers and end users.

![The Intent dropdown open on a layout, listing Print, Digital static and Digital animated](intent.png){.screenshot}

<iframe width="690" height="388" src="https://www.youtube.com/embed/4GSNHA6Ypmk?si=f-JNJvbKaV52Pn7T&controls=1&mute=1&showinfo=0&rel=0&autoplay=0&loop=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[All feature videos](https://www.youtube.com/playlist?list=PLLHtQ1R6R-B_m7XAVySM9OjbbUscsgBOH)


## Inheritance model

Intents are part of the [Inheritance model](/GraFx-Studio/concepts/layouts/#inheritance).

An Intent defined for a master layout automatically applies to all sub-layouts. If needed, Intent can be individually adjusted for each sub-layout, overriding the inherited default.

Imagine a Layout setup: an Ad Master layout (Digital static), and a Flyer sub-layout intended for Print.

![Layouts panel with the Ad Master layout and its Flyer sub-layout](layouts.png){.screenshot}

Since the Print layout overrides the intent, the overridden values are colored.
The size did not color, since it's converted from Pixels, and will reflect the same size (converting using 72dpi).

![Flyer sub-layout inheriting from Ad Master, with Intent Print and Unit Millimeters overridden in yellow](inheritance.png){.screenshot}

## Print

- Units will default to Millimeters
- [Bleed](/GraFx-Studio/concepts/bleed/) properties are visible
- Animation properties are hidden
- Animation timeline is hidden

![Layout properties for a Print intent: Millimeters, a size in mm and a visible Bleed section](print.png){.screenshot}

## Digital static

- Units will default to Pixels
- [Bleed](/GraFx-Studio/concepts/bleed/) properties are hidden
- Animation properties are hidden
- Animation timeline is hidden

![Layout properties for a Digital static intent: Pixels, 300 by 250 px and no Bleed section](digitalstatic.png){.screenshot}

![Layers panel listing Image 2 and Image 1, with no timeline next to them](noanimation.png){.screenshot}


## Digital animated

- Units will default to Pixels
- [Bleed](/GraFx-Studio/concepts/bleed/) properties are hidden
- Animation properties are visible
- Animation timeline is visible

![Layout properties for a Digital animated intent, with an arrow pointing at the animation tab](digitalanimated.png){.screenshot}

![Timeline of a digital animated layout, with a five-second bar for Image 2 and Image 1](animation.png){.screenshot-full}

