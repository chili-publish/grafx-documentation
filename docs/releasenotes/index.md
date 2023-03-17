# Release notes

CHILI GraFx and the GraFx applications are frequently updated with new features, improvements, and fixes.

Here you can find a summary of what's new!

## Mar 16, 2023 - GraFx Studio

Version 0.114.1, using Studio SDK [0.114.0](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

### Features

- We added [15 blend modes](/GraFx_Studio/concept/blendmodes/) that can be applied to your image and text content to improve your template design

![releasenotes](https://chilipublishdocs.imgix.net/releasenotes/blendmodes_rn.gif)

### Improvements

- Animation snaps to 0,1 seconds on the timeline, which makes it easier to align the animation of multiple frames
- Frames are only selectable and editable on the canvas while they are visible in the animation (this fixes some issues with entering text edit mode)
- While in text edit mode, you can now also edit the frame properties and change the copyfitting settings

### Fixes

- Fixed some issues with the color picker component to select a custom color or a swatch or to change the opacity
- Fixed issue where fonts were not loaded when the dialog to add fonts was opened too quickly

## Mar 6, 2023 - GraFx Media Alpha

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

## Dec 23, 2022 - GraFx Studio

Version 0.97.1, using Studio SDK [0.97.0](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

### Improvements

- You can leave the color of your character style undefined to use the color from the applied paragraph style
- After creating a text or image frame, you now automatically go back to the Select tool

### Fixes

- Fixed issue with loading fonts, which caused the default font to be used instead (ℹ️ because of this fix the text in your template can look different)
- The editor canvas is no longer moving when opening or closing the left side panel

## Dec 16, 2022 - GraFx Studio

Version 0.95.1, using Studio SDK [0.95.0](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

### Features

- Next to paragraph styles, you can now also add character styles to your Stylekit and use them to style your text ([more information](https://docs.chiligrafx.com/GraFx_Studio/how_to/characterstyles/){target="_blank"})
- Added support for most OTF fonts
- Enabled keyboard shortcuts for text navigation, text selection and text cut/copy/paste ([list of shortcuts](https://docs.chiligrafx.com/GraFx_Studio/concept/shortcuts/#text-cursor-manipulation){target="_blank"})

### Improvements

- Added option to remove fonts from your Stylekit
- Added action menu to paragraph styles
- Media assets and fonts are now showing the file type
- It is not possible anymore to add the same font multiple times to your Stylekit
- Frame property values are truncated to 2 decimal places
- Saving your template while in text edit mode now also saves your latest text edits
- Fixed issue with incorrect frame position at the end of an emphasis animation
- Selected frame borders and handles are hidden during animation playback
- Enabled 'T' and 'I' shortcuts to select the Text or Image frame creation tool
- Some general styling improvements

### Fixes

- Fixed issues with fonts
- Fixed issues with renaming a list item
- Fixed issue with resetting a copyfitting override

## Nov 18, 2022 - GraFx Studio

Version 0.88.3, using Studio SDK [0.88.2](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

### Features

- The Media panel shows the assets from your GraFx Publisher Backoffice, allowing you to browse them and place in image frames
- The Stylekit panel shows your styles, swatches and fonts
- Add paragraph styles to your Stylekit and use them to style your text
- Add fonts from your GraFx Publisher Backoffice to your Stylekit
- Insert text variables in text frames
- Change the vertical alignment of your text
- Enable copyfitting for text frames to automatically change the font size to fit the text inside the frame
- Bring frames forward or send them backward to change the way they are rendered on top of each other (changing the z-index)
- Switch between image fill & fit mode to change how your image is placed in an image frame
- Rename your template by clicking the template name in the top toolbar
- Export the selected layout as PNG or JPG (the image is showing all visible frames, ignoring the animation)
- Enabled environment API authentication

### Improvements

- Design and Automate mode are removed, variables are now located under a new tab in the properties panel
- The order of the frames in the Layers panel is changed so that the frame at the top is the one that is rendered in front
- The frames in the Layers panel have the correct frame icon
- Stylekit panel improvements
- Updated primary color to the GraFx Studio color

### Fixes

- Converted number IDs to strings (required by Studio SDK update)
- Fixed padding of layout properties
- Fixed issue with pressing the delete/backspace key while renaming a frame
- Fixed issue with the button to reset overrides not being present after clicking outside the page

## Oct 12, 2022 - GraFx Studio

Version 0.70.3, using Studio SDK [0.70.3](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

### Features

- Text properties panel (work in progress)
- Stylekit panel (work in progress / Feature Flagged)
- Media panel (Feature Flagged)
- Create new paragraph style
- Hamburger menu for saving and exporting template
- Add image from Media panel to image frame

### Improvements

- Scrollbar UX improvements
- Being able to delete a frame
- Editor canvas gets focus back when action is done
- Text fill color to SDK
- Handle typed EditorResponse

### Fixes

- Prevent frame bar jumping to negative values on timeline
- Fix animation duration when resetting
- Bump dependencies for security fixes
- Prevent unnecessary calls to SDK when selecting a frame
- Fix issues regarding sortable variables panel
- General UX/UI fixes
- Reset frame properties when frame has ID 0
- Dialog component styling
