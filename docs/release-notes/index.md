# Release notes

## Jan 9, 2024 - CHILI GraFx

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-04.svg)

### Improvements

- Full enforcement of user groups on the backend for authorization decisions
- Additional features for modifying user groups and related entities
- Allowed length for user group name increased to 100 characters
- Optimization of authorization pipelines

### Fixes

- Improved reliability of user management operations
- Monthly renders of the last range weren't returned

CHILI GraFx [Platform API](https://api.chiligrafx.com/swagger/index.html)

## Jan 4, 2024 - GraFx Studio

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-09.svg)

### Features

- You can now cut (Ctrl/Cmd+X), copy (Ctrl/Cmd+C), paste (Ctrl/Cmd+V), and duplicate (Ctrl/Cmd+D) frames in the Template Designer workspace. This is possible with the shortcuts or via the quick actions in the Layers panel

### Improvements

- Added more tooltips to the Template Designer workspace and made some improvements to them
- Assigning an image to an image variable is now possible via a single click
- Changed the min and max values for copyfitting to 1% and 10.000% (it was 10% and 1.000%)
- Moved the "Clear style overrides" button to another location in the Template Designer workspace

### Fixes

- Fixed issue with low quality image previews in the Studio UI
- Fixed issue with variable text not being updated after undo/redo
- Fixed issue with the number of triggers not being shown in red when hovered while in error state
- Fixed issue with the media connector sending multiple download requests
- Fixed issue with actions throwing the same error twice
- Fixed issue where a font that is used in the template could be deleted without getting a confirmation dialog

## Jan 2, 2024 - GraFx Publisher

![rn_icon](/assets/CHILI_publisher_RGB.svg)

### Fixes

- Fixed issue where datasource output with one record does not respect the PDF Name Pattern
- Fixed issue when deletion of a resource may cause deletion of other resources with similar name
- Improved error messaging when output generation fails

## 2023

See [this page](/release-notes/2023/) for 2023 release notes.
