# Release notes

## Jan 26, 2024 - CHILI GraFx

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-04.svg)

### Fixes

- Fixed an error where you could not access the platform

## Jan 25, 2024 - CHILI GraFx

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-04.svg)

CHILI GraFx [Environment API 1.3.4](/GraFx-Developers/#environment-api)

### Improvements

- Introduce png variable output endpoint  
api/v1/environment/{environmentId}/output/png
- Introduce gif variable output endpoint  
api/v1/environment/{environmentId}/output/gif
- Introduce jpg variable output endpoint  
api/v1/environment/{environmentId}/output/jpg
- Introduce 'default' output settings
- Add 'scaling' option to output settings
- Sort font styles by weight

### Fixes

- Update authorization rules for Content Administrator role
- Fix video output issues
- Avoid potential resources duplicates
- Ignore font style 'width' property on upload

### Experimental

- Introduce oauth-authorization-code endpoints  
(api/experimental/environment/{environment}/connectors/{connectorId}/auth/oauth-authorization-code)
- Introduce 'none' auth for connector definition

## Jan 24, 2024 - GraFx Publisher

![rn_icon](/assets/CHILI_publisher_RGB.svg)

### Fixes

- When outputting a PDF with a variable in the path name, the value of the variable is now used correctly.
- Fixed the issue where an asset could end up as duplicate using ResourceItemAdd, when a path was malformed.
- Fixed vulnerability where code details were shown in an error message
- Fixed incorrect behavior for the ResourceSearchInFolder API endpoint related to the parentFolderPath parameter. Previously, when includeSubDirectories was set to true, the endpoint performed a prefix search. This behavior has been corrected to conduct an exact search, aligning with expectations set in prior versions of CHILI.
- Fixed issue where some characters in REST endpoint query parameters cause the endpoint to fail

### Improvements

- A download will now be served from a more sustainable location
- Improved performance when copying a file with an existing name

## Jan 19, 2024 - CHILI GraFx

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-04.svg)

### Improvements

- Deprecated endpoints were deleted from the API  

### Fixes

- Render visualization showed wrong metrics

CHILI GraFx [Platform API](https://api.chiligrafx.com/swagger/index.html)

## Jan 16, 2024 - GraFx Publisher

![rn_icon](/assets/CHILI_publisher_RGB.svg)

### Fixes

- Fixed issues where specific PDF assets caused corruption in the PDF output file

## Jan 9, 2024 - CHILI GraFx

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-04.svg)

### Improvements

- User groups  
User groups allow admins to set permissions and access to user groups next to individual users. This release integrates user group permissions into our authorization process, available through the API.

### Fixes

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
