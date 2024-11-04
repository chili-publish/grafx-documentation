# Anchoring

## Default

Upon creation of a new frame (text, image, ...) the anchoring is set to Relative.

![screenshot-full](anchor_guide_02.png)

## Properties menu

Select a frame, and you'll see the **Anchoring** section in the properties panel.

The properties will reveal more depending on the chosen options.

![screenshot-full](anchor_guide_01.png)

## Types of anchors

Select a frame, and change the Horizontal and/or Vertical anchor

![screenshot-full](anchor_guide_05.gif)

## Relative (%)

The image frame below, has relative anchors to the page (by default).

Left and right are set to 5%, top 14% and bottom 38%.

![screenshot-full](anchor_guide_03.png)

The canvas is set to 1080 px width and height.

When now adjusting the canvas to e.g. 1200 px, the position of the image frame will remain 5% of the left, and 5% of the right. The actual x and y position will differ.

![screenshot-full](anchor_guide_04.gif)

This means, the actual pixel count from the left (and right) will increase. 

- 5% of 1080 = 54 px
- 5% of 1200 = 60 px

## Left, Right or Left & Right

Choosing of of these anchors, will anchor the selected frame with a fixed amount of units from the chosen side(s).

Reminder: by default, the anchor is set to the page

### Left

A fixed amount of units (pixels, mm, inches, ...) will be set to keep from the left side.

When the canvas is made wider, the left-hand side spacing will remain the exact amount of units.

![screenshot-full](anchor_guide_06.gif)

### Right

A fixed amount of units (pixels, mm, inches, ...) will be set to keep from the right side.

When the canvas is made wider, the right-hand side spacing will remain the exact amount of units.

![screenshot-full](anchor_guide_07.gif)

### Left & Right

A fixed amount of units (pixels, mm, inches, ...) will be kept from the left-hand side & the right-hand side.

When the canvas is made wider, both sides will remain the exact amount of units from the respective sides.

![screenshot-full](anchor_guide_08.gif)

### Center

The selected frame will **not change size**, and will keep centered relative to the changed dimensions of the canvas.

![screenshot-full](anchor_guide_09.gif)

## Anchor Targets

By default, the anchor target is set to the page. This means, the choice you made above (relative, left, ...) is set to page.

You can modify the target with the property element below the Horizontal and Vertical anchor choice.

![screenshot](anchor_guide_10.png)

The box with the 4 circles around, represents your frame.

The animation right to the box, represents the impact of your choice. In the animation, the blue box represents your frame, and the gray area your cancas.

Select elements in the box representing the left, top, right and bottom anchor. Select the center cross to adjust the center anchor.

Depending on the choice you made above, different anchor targets can be set.

E.g. When the left side of the frame is anchored, the right anchor target cannot be set.

![screenshot](anchor_guide_11.png)

## Anchoring effect on a frame

See the effect of changing the canvas or page size, when a frame is anchored with these settings.

Horizontal setting is mentioned first.

The blue box represents your frame, and the gray area your canvas (or page).

<script src="https://unpkg.com/@dotlottie/player-component@2.7.12/dist/dotlottie-player.mjs" type="module"></script>


| Anchor settings effect      | | |
| -- | -- | -- |
| Center-Bottom              | Center-Center             | Center-Relative             |
|<dotlottie-player src="animations/Center-Bottom.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player>|<dotlottie-player src="animations/Center-Center.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player>|<dotlottie-player src="animations/Center-Relative.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player>|
| Center-Top              | Center-Top&Bottom             | Left-Bottom             |
|<dotlottie-player src="animations/Center-Top.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player>|<dotlottie-player src="animations/Center-Top&Bottom.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player>|<dotlottie-player src="animations/Left-Bottom.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player>|
| Left-Center       | Left-Relative     | Left-Top      |
|<dotlottie-player src="animations/Left-Center.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> | <dotlottie-player src="animations/Left-Relative.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> | <dotlottie-player src="animations/Left-Top.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player>|
| Left-Top & Bottom       | Left & Right - Bottom | Left & Right - Center      |
| <dotlottie-player src="animations/Left-Top&Bottom.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> | <dotlottie-player src="animations/Left&Right-Bottom.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> | <dotlottie-player src="animations/Left&Right-Center.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> |
| Left-Right & Relative       | Left & Right - Top | Left & Right - Top & Bottom      |
| <dotlottie-player src="animations/Left&Right-Relative.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> | <dotlottie-player src="animations/Left&Right-Top.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> | <dotlottie-player src="animations/Left&Right-Top&Bottom.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> |
| Relative - Bottom       | Relative - Center | Relative - Relative      |
| <dotlottie-player src="animations/Relative-Bottom.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> | <dotlottie-player src="animations/Relative-Center.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> | <dotlottie-player src="animations/Relative-Relative.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> |
| Relative - Top | Relative - Top & Bottom| Right - Bottom |
| <dotlottie-player src="animations/Relative-Top.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> | <dotlottie-player src="animations/Relative-Top&Bottom.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> | <dotlottie-player src="animations/Right-Bottom.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> |
| Right - Center | Right - Relative | Right - Top |
| <dotlottie-player src="animations/Right-Center.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> | <dotlottie-player src="animations/Right-Relative.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> | <dotlottie-player src="animations/Right-Top.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player> |
| Right - Top & Bottom |  |  |
<dotlottie-player src="animations/Right-Top&Bottom.json" background="transparent" speed="1" style="width: 200px; height: 200px" direction="1" playMode="normal" loop autoplay></dotlottie-player>| | |

## Anchor to Page

By default, your frame is anchored (relative) to the page.

## Anchor to Frame

Choose an anchor target (one of 4 circles around the box), and set a new anchor point.

Let's use the picture below as example

- Chosen frame is the image frame of the house
- Horizontal anchoring is set to "Left". This means there will be a fixed amount of pixels on the left.
- Left anchor target is selected, this means: To what target should we anchor the image frame?
- Anchor left is set to "Frame" (not page)
- Target Frame is set to "Realtor" (the name of the frame)
- Target Anchor Point is set to Left

This means: The image of house is set to anchor on the left-hand side to the left side of the realtor image.

The Interface displays the amount of pixels will be kept as offset. (i.e. 79.50).

![screenshot-full](anchor_guide_12.png)

The solid anchor line on the left of the house image shows the offset (79.50) and stops where the left-hand side of the realtor image is.

![screenshot-full](anchor_guide_13.png)