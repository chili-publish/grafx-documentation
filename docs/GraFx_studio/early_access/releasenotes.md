# Early Access: Release Notes

## Version 0.0.4

July 18th, 2022

### Workspace

Fixes and improvements:

- Fixed inheritance of frame visibility on sub-layouts

### Editor engine

New features:

- Text variables are highlighted when in text edit mode
- Each alternate layout can be made static or animated

Fixes and improvements:

- Fixed inheritance of frame visibility on sub-layouts

### SDK

[SDK Docs](https://github.com/chili-publish/editor-sdk/releases/tag/0.56.0)

 
## Version 0.0.3

July 7th, 2022

### Workspace
New features:

- Enabled undo/redo buttons
- Frames can be renamed

Fixes and improvements:

- Improved use of timeline on tablets
- Optimized removing and sorting of variables
- Fixed moving to top/bottom of variables
- Fixed closing of dialogs and pop-ups when clicking outside the boundaries
- Text input field now goes out of focus when pressing Enter

### Editor engine

New features:

- Text can be edited (double click a text frame to go into edit mode)
- Frames that go outside the page are clipped
- Added undo/redo of changes to the document
- Added animation emphasis styles
- Added animation ease and tween types
- Layout can be selected by clicking the layout name above the page on the canvas

Fixes and improvements:

- Prevented frames from going into hovered state when manipulating another frame
- Fixed exception when renaming a frame
- Fixed issue with playing the animation
- Layout is not automatically selected anymore when clicking outside page
- Prevented frame state from being disposed & recreated

### SDK

[SDK Docs](https://github.com/chili-publish/editor-sdk/releases/tag/0.55.0)

## Version 0.0.2

May 23rd, 2022

### Workspace
New features:

- Added tools to create a text or image frame
- Added dragging support when multiple variables are selected
- Added menu options when multiple variables are selected
- Added option to delete variables
- Added arrow key support on text input fields

Fixes and improvements:

- Refactored animation timeline for a better and smoother user experience
- Fixed issue with toggling the Variables Settings panel
- Limited variable group nesting to 1
- Fixed layout inheritance information being present for frames on the Default layout
- Changed placeholder text in properties panel when nothing is selected
- Fixed issue with multi-key shortcuts
- Added Hotjar integration to gather anonymous feedback
- Added feature flagging on development builds
- Added base to enable localization in the future
- Performance improvements
- Styling improvements

### Editor engine
New features:

- Create text and image frames

Fixes and improvements:

- Fixed broken export to MP4/GIF
- Fixed document jumping to the right when opening the Layouts panel
- Limited variable group nesting to 1
- Performance improvements

### SDK
[SDK Docs](https://github.com/chili-publish/editor-sdk/releases/tag/0.53.0)