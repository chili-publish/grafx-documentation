# Blend modes

## Blend who?

Blend Modes determine how two graphics or colors blend together. Each blend mode has a different effect on the resulting blend.

## Overview of supported blend modes

| Examples      | | | |
| -- | -- | -- | -- |
| Normal              | Screen             | Overlay             | Darken |
|![Normal: the white bottle sits fully opaque over the green splash background](normal.png){.screenshotsmall}| ![Screen: the bottle lightens until its label text almost disappears](screen.png){.screenshotsmall}|![Overlay: the splash shows faintly through the bottle and the label turns yellow-green](overlay.png){.screenshotsmall}|![Darken: the darker green splash takes over the bottle, leaving only the cap clear](darken.png){.screenshotsmall}|
| Lighten             | Color Dodge             | Color Burn            | Hard light |
|![Lighten: the bottle keeps its white body and the darker splash stays behind it](lighten.png){.screenshotsmall}| ![Color dodge: the bottle is blown out to near-white with a bright yellow band at its base](colordodge.png){.screenshotsmall}|![Color burn: the bottle darkens to deep green with the splash burned through it](colorburn.png){.screenshotsmall}|![Hard light: a high-contrast result with a bright bottle and the splash pushed back](hardlight.png){.screenshotsmall}|
| Soft light            | Difference              | Exclusion             | Multiply |
|![Soft light: the splash reads softly through the bottle and the label fades to pale green](softlight.png){.screenshotsmall}| ![Difference: the bottle inverts to deep purple with a dark red droplet logo](difference.png){.screenshotsmall}|![Exclusion: the bottle inverts to a softer mauve and most of the label washes out](exclusion.png){.screenshotsmall}|![Multiply: the green splash shows through the whole bottle, darkening it](multiply.png){.screenshotsmall}|
| Hue             | Saturation              | Color             | Luminosity |
|![Hue: the bottle turns pale mint and the logo outlines shift to pink](hue.png){.screenshotsmall}| ![Saturation: the bottle drops to grey while the background stays green](saturation.png){.screenshotsmall}|![Color: a grey bottle keeping its green droplet logo against the green background](color.png){.screenshotsmall}|![Luminosity: the bottle picks up a pale green tint from the background](luminosity.png){.screenshotsmall}|

The above examples show blend modes in action on a graphic. You can also apply them to a frame with text.

![A text frame reading "chill water the purest" with Color burn chosen in the Blend mode dropdown](blendmode-text.png){.screenshot-full}

### Normal
The default blend mode which draws the new graphics over the existing graphics.

### Screen
Lightens the colors in the bottom layer by blending them with the inverse of the colors in the top layer.

### Overlay
Combines the multiply and screen blend modes. It darkens the bottom layer where the top layer is dark, and lightens it where the top layer is light.

### Darken
Compares the colors in both layers and selects the darker color for the resulting blend.

### Lighten
Compares the colors in both layers and selects the lighter color for the resulting blend.

### Color Dodge
Lightens the bottom layer color depending on the color of the top layer. It produces a brighter and more vibrant effect.

### Color Burn
Darkens the bottom layer color depending on the color of the top layer. It produces a darker and more contrasted effect.

### Hard Light
Multiplies or screens the colors, depending on the top layer's color value. It produces an intense and dramatic effect.

### Soft Light
Darkens or lightens the colors, depending on the top layer's color value. It produces a soft and subtle effect.

### Difference
Subtracts the bottom layer's color from the top layer's color. It produces an inverted effect.

### Exclusion
Subtracts the bottom layer's color from the top layer's color, but with less intensity than the difference blend mode. It produces a softer inverted effect.

### Multiply
Multiplies the colors in the top and bottom layers. It produces a darker effect.

### Hue
Uses the hue of the top layer with the saturation and luminance of the bottom layer. It produces a hue-based color effect.

### Saturation
Uses the saturation of the top layer with the hue and luminance of the bottom layer. It produces a saturation-based color effect.

### Color
Uses the hue and saturation of the top layer with the luminance of the bottom layer. It produces a color-based effect.

### Luminosity
Uses the luminance of the top layer with the hue and saturation of the bottom layer. It produces a luminosity-based effect.