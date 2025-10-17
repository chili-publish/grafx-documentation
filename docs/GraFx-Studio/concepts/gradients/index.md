# Gradients

## What it is

A gradient is a smooth transition between two or more colors used to fill an object. 

GraFx Studio currently supports linear gradients in addition to solid color fills.

Stops: points along the gradient where a specific color is applied. New gradients start with 2 stops.

- Color sources per stop
- Custom colors
- Brand Kit colors (to stay on brand)
- Color spaces per stop: RGB, CMYK, HEX, and Spot.

Spot colors can include a display value (RGB, CMYK, or HEX) for on-screen preview while remaining spot for print.

Why it matters
	•	Readable, adaptable backgrounds: Use a gradient behind dynamic text or images to enhance contrast when content varies across locales or data feeds.
	•	Brand consistency: Tie stops to GraFx Brand Kits so gradients stay within approved palettes.
	•	Design flexibility: Use as fills for elements or as overlays combined with blend modes to subtly tone imagery without manual retouching.

Key concepts & relationships
	•	Stops & direction: You control both the colors at each stop and the direction of the gradient across the object.
	•	Brand governance: Stops can reference Brand Kit colors to enforce governance.
	•	Printing: Spot stops remain spot for print (color separations).

Constraints
	•	Gradient type: Linear only.
	•	Default: 2 stops (you can add more).
	•	Applies where fill is supported for the selected element.