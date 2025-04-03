# Layout Intent

Intents enhance the functionality of layouts. Each layout now includes an "Intent" property with three possible values: 

- Print 
- Digital static
- Digital animated

This property provides contextual guidance for both Template Designers and end users.

![screenshot](intent.png)

<iframe width="690" height="388" src="https://www.youtube.com/embed/4GSNHA6Ypmk?si=f-JNJvbKaV52Pn7T&controls=1&mute=1&showinfo=0&rel=0&autoplay=0&loop=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[All feature videos](https://www.youtube.com/playlist?list=PLLHtQ1R6R-B_m7XAVySM9OjbbUscsgBOH)


## Inheritance model

Intents are part of the [Inheritance model](/GraFx-Studio/concepts/layouts/#inheritance).

An Intent defined for a master layout automatically applies to all sub-layouts. If needed, Intent can be individually adjusted for each sub-layout, overriding the inherited default.

Imagine a Layout setup: an Ad Master layout (Digital static), and a Flyer sub-layout intended for Print.

![screenshot](layouts.png)

Since the Print layout overrides the intent, the overridden values are colored.
The size did not color, since it's converted from Pixels, and will reflect the same size (converting using 72dpi).

![screenshot](inheritance.png)

## Print

- Units will default to Millimeters
- [Bleed](/GraFx-Studio/concepts/bleed/) properties are visible
- Animation properties are hidden
- Animation timeline is hidden

![screenshot](print.png)

## Digital static

- Units will default to Pixels
- [Bleed](/GraFx-Studio/concepts/bleed/) properties are hidden
- Animation properties are hidden
- Animation timeline is hidden

![screenshot](digitalstatic.png)

![screenshot](noanimation.png)


## Digital animated

- Units will default to Pixels
- [Bleed](/GraFx-Studio/concepts/bleed/) properties are hidden
- Animation properties are visible
- Animation timeline is visible

![screenshot](digitalanimated.png)

![ui](animation.png)

