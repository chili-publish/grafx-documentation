# Release notes

The GraFx Studio workspace for template designers is frequently updated with new features, improvements and fixes.

Here you can find a summary of what's new!

## January 30, 2023

Version 0.104.1, using Studio SDK [0.104.0](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

### Fixes

- Fixed issue with loading media
- Fixed issue with font size and line height properties of a character style being set to 0 when clicked upon, and it was not possible to clear them (now you can leave them empty again to use the values from the applied paragraph style)
- Fixed issue with text rendering when line height is 0
- Fixed issue with deleted font being shown in font dropdown menu
- Fixed weird behavior when using the Hand tool to move the page

## January 23, 2023

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

## December 23, 2022

Version 0.97.1, using Studio SDK [0.97.0](https://github.com/chili-publish/editor-sdk/releases){target="_blank"}

### Improvements

- You can leave the color of your character style undefined to use the color from the applied paragraph style
- After creating a text or image frame, you now automatically go back to the Select tool

### Fixes

- Fixed issue with loading fonts, which caused the default font to be used instead (ℹ️ because of this fix the text in your template can look different)
- The editor canvas is no longer moving when opening or closing the left side panel

## December 16, 2022

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

## November 18, 2022

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

## October 12, 2022

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