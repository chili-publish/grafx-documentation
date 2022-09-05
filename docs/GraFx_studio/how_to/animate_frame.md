# How to animate my frame

## Introduction

Be sure to first read about the [concept of Animation](/GraFx_studio/concept/animation/)

Also read about the [Animation panel](/GraFx_studio/animation/)

We will refer to terms defined in the concept page.

## Static is the default

(And we're not talking about electricity)

By default, frames are static. This means, they don't have an animation, and appear from frame 1 up to the last frame of the timeline.

Even when you "play" the animation, this frame will appear static in on stage. (on the page)

## Appearance on stage

The blue bar represents the frame. It starts from frame 1, and runs all the way to the last frame.

The frame will appear "immediately", and will stay all the way to the end.

### Move the start - or end point

Scroll all the way to the left, and select the edge (when your cursor changes into a double sided arrow), now drag the edge to the left or right. (left won't work, if it's at the beginning)

![Timeline change](https://chilipublishdocs.imgix.net/GraFx_studio/how_to/timeline1.gif)

You can do the same, for the end of the bar for that frame in the timeline.

## Duration of the animation

Drag the vertical divider to the left or right.

![Duration change](https://chilipublishdocs.imgix.net/GraFx_studio/how_to/timeline_divider.png)

You can always make the duration longer.

Dragging to the left will work up to the longest blue bar. I.e. if a frames shows up to 5 seconds point, you will not be able to reduce the duration below 5 seconds.

![Timeline change](https://chilipublishdocs.imgix.net/GraFx_studio/how_to/timeline_reduce.gif)


## Intro - Emphasis - Outro

By default, no animations are set. By selecting the animation panel in the properties, you can set the **intro**, **emphasis** and **outro**.

![Intro_Outro](https://chilipublishdocs.imgix.net/GraFx_studio/how_to/intro_outro.gif)

### Intro

As the name suggests, the **intro** changes how the animation starts.

Choose 1 or all 4 animations

- Easing type
- Fade
- Rotation
- Scale

Each of the animation types has settings that will appear when you select them. (Except fade, it will just fade in)

### Emphasis

The behaviour in the middle section.

Set the style

- Bounce
- Flash
- ...

Set the Ease Type

- Ease in
- Ease out
- Both

Set the Twee type (how the movement is calculated)

- Quadratic
- ...

[See easing types for more info](https://easings.net/){target="_blank"}

!!! Note
	Will need input here

### Outro

### Length of the intro, outro & emphasis

Control the length and position of each element (lightblue bar), by dragging their respective start- and endpoints.

Intro (start) — Emphasis (middel) - Outro (end)

![Intro_Outro](https://chilipublishdocs.imgix.net/GraFx_studio/how_to/intro_outro_resize.gif)
