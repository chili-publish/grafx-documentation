# Release notes

CHILI GraFx and the GraFx applications are frequently updated with new features, improvements, and fixes.

## Apr 19, 2023 - CHILI GraFx

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-04.svg)

### Features

- You can invite users to CHILI GraFx
- When you invite a user to CHILI GraFx you can assign this user to an GraFx environment and assign the role this user needs to have in this environment
- You can remove the role 'Subscription Admin' from other users
- You can add an existing user to additional GraFx environments and assign the role this user needs to have in this environment
- You can access GraFx Publisher within the CHILI GraFx environment with SSO
- You can login in GraFx Publisher from the direct URL with your CHILI GraFx account

![2023-04-14_16-26-11](https://user-images.githubusercontent.com/122599725/233287606-4ef0e434-7af6-4b11-b148-a4abe1c6cbc7.gif)

Read more about [User Management](https://docs.chiligrafx.com/CHILI_GraFx/user_management_intro/).

## Apr 14, 2023 - GraFx Studio

Version 0.117.1, using Studio SDK [0.117.0](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-09.svg)


### Improvements

- When applying a blend mode to a text frame you automatically go out of text edit mode (this way you can see the effect of the blend mode, because it is not applied while in text edit mode)
- You can now easily download the JSON file of the template with a "Download doc" trigger in the debug panel

### Fixes

- Fixed issue with MacBook being detected as a mobile device, causing issues with frame handles
- Fixed issue with opacity not being applied to fill and stroke for shapes
- Fixed issue when using a swatch as fill color for shapes, which caused the shape color to not change immediately on the canvas when the swatch color is changed
- Fixed issue with text not being selectable with the Text tool when a blend mode is applied to the text frame

??? note "Note for integrators"
	
	There is a minor breaking change in the Studio SDK's typings.
	It basically boils down to changing the import for the Id type, you can do it as follows:<br>
	Change `#!typescript import { Id } from '@chili-publish/editor-sdk/lib/types/CommonTypes'`<br>
	To `#!typescript import { Id } from '@chili-publish/editor-sdk'`<br>
	For more information, please check out the [SDK release notes](https://github.com/chili-publish/editor-sdk/releases/tag/0.117.0){target="_blank"}.

## Mar 31, 2023 - Infrastructure update

Your [CHILI GraFx](/CHILI_GraFx/) infrastructure has been upgraded to have the latest update.

With this update, we’re implementing platform infrastructure changes that greatly enhance  performance.

The update does require planned downtime, and will be transparant for you.

The update will be implemented (starting April 5) gradually on all tenants, and will happen over the following days and weeks.


## Mar 29, 2023 - GraFx Studio

Version 0.116.2, using Studio SDK [0.116.0](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-09.svg)

### Features

- You can now add rectangle, ellipse, and polygon shapes to your design, by using a new Shape tool in the left toolbar. In the properties panel, you can set a blend mode and change the fill and stroke color, to customize as you want. (There are still a couple of known issues, which will be addressed in the next release!)

![releasenotes](https://chilipublishdocs.imgix.net/releasenotes/shapes.gif)

### Improvements

- You can select text on the page when the Text tool is active (previously it would create a new text frame instead)
- The layout name above the page is not scaled when zooming in or out
- Blend mode is not applied when in text edit mode (this makes editing text easier)
- Internal optimization to significantly increase the performance or rendering frames on the canvas

### Fixes

- Fixed issue with the Width and Height properties both getting an override when only one of the two was changed
- Fixed issue with changing a font in a text frame when the animation is paused inside an animation block for that frame

## Mar 17, 2023 - GraFx Publisher

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK_publisher.svg)

!!! danger "Sandbox Release"
	
	Information related to your Sandbox.
	
	When the update is in production, another release note will be added.

Your [CHILI GraFx](/CHILI_GraFx/) sandbox has the latest update to [GraFx Publisher](/GraFx_Publisher/)

- Our goal: Improve performance in handling templates, documents, assets.
- Our ask: Test in your sandbox now, and send us your feedback.

With this update, we’re implementing a new platform infrastructure that greatly enhances  performance. We **urge** you to test GraFx Publisher on your sandbox environment to experience this new level of performance for yourself.

## Mar 16, 2023 - GraFx Studio

Version 0.114.1, using Studio SDK [0.114.0](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-09.svg)

### Features

- We added [15 blend modes](/GraFx_Studio/concept/blendmodes/) that can be applied to your image and text content to improve your template design

![releasenotes](https://chilipublishdocs.imgix.net/releasenotes/blendmodes_rn.gif)

### Improvements

- Animation snaps to 0,1 seconds on the timeline, which makes it easier to align the animation of multiple frames

![releasenotes](https://chilipublishdocs.imgix.net/releasenotes/snap_rn.gif)

- Frames are only selectable and editable on the canvas while they are visible in the animation (this fixes some issues with entering text edit mode)
- While in text edit mode, you can now also edit the frame properties and change the copyfitting settings

### Fixes

- Fixed some issues with the color picker component to select a custom color or a swatch or to change the opacity
- Fixed issue where fonts were not loaded when the dialog to add fonts was opened too quickly

## Mar 6, 2023 - GraFx Media Alpha

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-11.svg)

### Features

- You can sort your assets on name
- You can see a preview of your asset

![releasenotes](https://chilipublishdocs.imgix.net/releasenotes/media_20230307.gif)

## Mar 1, 2023 - GraFx Studio

Version 0.111.2, using Studio SDK [0.111.0](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

### Features

- You can constrain the proportions of a frame while resizing to preserve the aspect ratio

![releasenotes](https://chilipublishdocs.imgix.net/releasenotes/proportions.gif)

- There is a new dropdown menu that allows you to control the zoom level
- A warning icon appears when part of your text is not visible because it doesn't fit inside the text frame

![releasenotes](https://chilipublishdocs.imgix.net/releasenotes/overflow3.gif)

### Improvements

- Variable settings panel does not close automatically anymore, it stays open until you manually close it

### Fixes

- Fixed issue where copyfitting property was not shown in yellow when it has an override
- Fixed issue where variable settings panel was only opened on second click
- Fixed issue with Media panel being empty when opened too fast

## Feb 16, 2023 - GraFx Studio

Version 0.107.4, using Studio SDK [0.107.0](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

### Features

- You can make the content of an image frame variable by inserting an image variable
- You can browse your media and assign an image to an image variable

### Improvements

- The template is automatically zoomed to page when opened or when switching to another layout
- Added tooltips to the sidebar and header bar
- Added a loading indication while media previews are loading
- The variable settings panel is not opened when a new variable is created
- The variable name is truncated in the variable tag when it doesn't fit in the text frame, to prevent text overflow

### Fixes

- Fixed issue with resetting an override on the image fit mode
- Fixed issue with undo/redo of creating a new variable
- Fixed issue with undo/redo of creating a new layout
- Because of issues with calculating the number of occurrences of a variable, it's hidden in the variable list until the number is reliable
- Fixed infinite API calls when navigating to the bottom of the Media panel
- Media details are now retrieved using the new *details(id)* connector method
- Fixed issues with server-side rendering

## Feb 16, 2023 - GraFx Media Alpha

### Features

- You can [browse](/GraFx_Media/how_to/browse/) between your assets in GraFx Media Alpha
- You can [search](/GraFx_Media/how_to/search/) for an asset in GraFx Media Alpha

## Jan 30, 2023 - GraFx Studio

Version 0.104.1, using Studio SDK [0.104.0](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

### Fixes

- Fixed issue with loading media
- Fixed issue with font size and line height properties of a character style being set to 0 when clicked upon, and it was not possible to clear them (now you can leave them empty again to use the values from the applied paragraph style)
- Fixed issue with text rendering when line height is 0
- Fixed issue with deleted font being shown in font dropdown menu
- Fixed issue with loading the default template
- Fixed weird behavior when using the Hand tool to move the page

## Jan 23, 2023 - GraFx Studio

Version 0.102.2, using Studio SDK [0.102.0](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

### Features

- You can now add [swatches](/GraFx_Studio/how_to/swatches/) to your Stylekit and use them in your template, e.g. to change the color of your text via a paragraph or character style (👉 click the color field to open the color picker, where you can go to the swatches tab to select a swatch)
- The [color picker](/GraFx_Studio/how_to/swatches/#color-picker) now comes in two versions, one for defining a swatch (where you cannot set the opacity or select another swatch) and one for applying a color (where you can choose between a custom color or a swatch and where you can change the opacity)
- You can [pan and zoom](/GraFx_Studio/mouse_trackpad/) the canvas by using two-finger gestures on the trackpad, even if the Hand or Zoom tool is not selected

### Improvements

- Improved text selection and text cursor positioning
- Simplified the character style settings by removing the indeterminate state for fill color (👉 when you leave the fill color unchecked the color is not applied, which means the default black or the color from the applied paragraph style is used)
- The default Arial Regular font is always available in the dropdown menu where you can select a font
- Renaming a font in the Stylekit is blocked (👉 you cannot rename a font in the Stylekit, but this was not blocked and caused an incorrect rename state)
- Removed variable name input field from the variables settings panel (👉 you can rename a variable by double clicking the variable name in the list)

### Fixes

- Fixed issue with loading fonts
- Fixed issue where the default Arial Regular font was selected in the text properties panel, but it was not used for new text frames
- Fixed issue where the applied character style was not shown correctly in the text properties panel
- Fixed issue where color swatches were converted to custom colors in paragraph and character styles
- Fixed issue with using Ctrl/Command+A to select all text with a keyboard with Azerty layout
- Fixed issue with replacing selected text with copied text
- Fixed issue where changes to variable settings were not saved when clicking on another panel
- Fixed icon misalignment on Uppercase button in text properties panel
- Fixed issue with inconsistent truncation of list items
- Fixed issue where several action menus could be opened at the same time in the Layouts panel
- Fixed issue with hidden action menu on sortable lists when using Safari
- Fixed issue with hamburger menu being shown behind other panels
- Fixed issue with blocked Media panel when an image frame was selected
- Fixed issue with output generation being triggered after renaming a template
- Fixed issue that resulted in an error when removing a frame


## Jan 9, 2023 - CHILI GraFx


### Improvements

- If you have multiple clients you can easily switch between these clients and get a list with environments of that client
- If you have multiple clients you can search for a specific client by typing the name of the client in the search bar
