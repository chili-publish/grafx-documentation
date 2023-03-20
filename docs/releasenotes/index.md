# Release notes

CHILI GraFx and the GraFx applications are frequently updated with new features, improvements, and fixes.

Here you can find a summary of what's new!

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