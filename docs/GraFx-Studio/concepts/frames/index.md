# Frames

A frame is an construct to place elements on a page.

A frame is a rectangular shape that can hold contents, and can have properties of itself.

![screenshot-fullwidth](frame-1.png)

## Basic Properties

Position is defined by the **top left** corner of the rectangle, relative to the **top left** corder of the document.

![screenshot-fullwidth](frame-2.png)

The width and height defines the size of the frame.

The rotation property of the frame, is the angle of rotation, relative to the **center** of the frame.

## Design properties [future version]

The frame-border will have properties in the future

## Frame types

![screenshot](frame-types.png)

Depending on the type of content, you'll need a different type of frame.

### Text Frame

A text frame is made to hold text.

A text frame looks like a rectangular box when selected.

### Image Frame

An image frame is made to hold static images.

An image frame looks like a rectangular box when selected, and has a cross, when no media is available for the frame.

![screenshot-fullwidth](frame-types-2.png)

When media is selected / active for the frame, it will show the media.

Look [here](/GraFx-Studio/concepts/crop/) to see how to work with cropping.

![screenshot-fullwidth](../crop/rectcrop.png)


## Z-index

Z-depth or Z-index refers to the Z-coordinate in the Cartesian coordinate system. 

![screenshot](https://upload.wikimedia.org/wikipedia/commons/6/69/Coord_system_CA_0.svg)

!!! Alert
	There is no actual height difference, but Z-axis is used to refer to the relative position to the other frames.

In GraFx Studio z-index is in line with desktop editing tools. Each frame has a z-depth. 