# Release notes

The GraFx Studio workspace for template designers is frequently updated with new features, improvements and fixes.

Here you can find a summary of what's new!

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