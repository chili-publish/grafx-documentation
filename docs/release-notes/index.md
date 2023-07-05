# Release notes

!!! example "Experimental"
	To give you early access to the latest and greatest, we will release some features as "**Experimental**".
	
	These features or endpoints (for the API) are not yet final: syntax might change, response could be different, etc. Don't base your (production) code on experimental features.


## June 28, 2023 - CHILI GraFx

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-04.svg)

This release enables Template designers to create collections and manage templates in collections.

End users can see collections, and create projects from templates in a collection.

Fine grained access management will be added later.

### Features

- Template designers can now make [Collections](/CHILI-GraFx/concepts/template-management/#template-collection)
- Template designers can [manage templates](/CHILI-GraFx/guides/manage-collections/) in collections
- End-users can [create Projects](/CHILI-GraFx/concepts/template-management/#end-user) from Templates in a collection.


## June 28, 2023 - CHILI GraFx

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-04.svg)

CHILI GraFx [Environment API 1.1.6](https://sandbox1.chili-publish-sandbox.online/grafx/swagger/index.html)

### Improvements

- Improved stability of output generation

## June 23, 2023 - CHILI GraFx

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-04.svg)

CHILI GraFx [Environment API 1.1.5](https://sandbox1.chili-publish-sandbox.online/grafx/swagger/index.html)

### Features

**Experimental**

- Introduce temporary POST api/experimental/environment/{environmentId}/output/pdf endpoint that provides ability to generate PDF output

### Fixes

- Fix ‘update Template body’ action to avoid data corruption.
- Fix ‘environment’ case sensitivity for My Project endpoints to avoid not-found errors
- Fix attempting to add My Project based on corrupted Template (avoid creation corrupted My Project)
- Update Environment API endpoints to restrict access for not activated users.


## June 23, 2023 - CHILI GraFx

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-04.svg)

CHILI GraFx [Platform API 1.12](https://api.chiligrafx.com/swagger/index.html)

### Improvements

- Added status in user endpoints
	- GET /api/v1/subscription/{id}/users
	- GET/api/v1/subscription/{subscriptionId}/users/{userId}
- Improved token generation for Integrations

## June 19, 2023 - CHILI GraFx

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-04.svg)

CHILI GraFx [Environment API 1.1.4](https://sandbox1.chili-publish-sandbox.online/grafx/swagger/index.html)

### Features

**Authentication**

- Extended ‘full access’ configuration to support multiple applications having full access to Environment API and Platform API.

**Machine to Machine**

- Add support for scope-based authorization rules
- Enabled integrations access to Environment API endpoints.

**Template Collections**

- Managing the image cover of a Template Collection

**My Projects**

- Introduce GET api/v1/environments/{environmentId}/projects endpoint that provides list of ‘My Project’ data.
- Introduce GET api/v1/environment/{environmentId}/projects/{projectId} endpoint that provides ‘My Project’ data.
- Accessing My Project's previews
- Saving modified json document of a My Project document
- Output: Image and animation output from a Project

### Improvements

**GraFx Media**

- Extended endpoints responses to return media file info
	- GET api/v1/environment/{environmentId}/media
	- GET api/v1/environment/{environmentId}/media/directory

**Output**

- Update ‘output’ endpoints: introduce ‘engineVersion’ parameter to override the engine version that is used during output rendering.
	- POST api/v1/environment/{environmentId}/output/animation
	- POST api/v1/environment/{environmentId}/output/image


### Fixes

- Output: Fixed mp4 output for a template with uneven dimensions
- Fixed return code (from 500 to 400) for template collection creation when the name is duplicate.
- Fixed adding new My Project with invalid Template (prevent storing broken My Project).

**Connectors (Experimental)** 

- Added Connector module


## June 16, 2023 - CHILI GraFx

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-04.svg)

CHILI GraFx Platform API 1.11

### Features

**User management**

- Added endpoints for disabling and enabling users in the subscription

**Manage Integrations**

- Added endpoints to create, update, delete Integrations
- Added endpoint to get details of a single Integration
- Added endpoint to get available scopes for an Integration
- Added endpoint to Rotate client secret
- Added endpoints to manage scopes of Integrations

**Authentication**

- Add support for the bearer token with new grant type
- Add support for scope-based authorization rules

## June 9, 2023 - GraFx Publisher plug-in for Adobe Illustrator®

![rn_icon](/assets/CHILI_publisher_RGB.svg)

### Features

- Added support for Adobe® Illustrator®[^1] 2023 (27.x)

[^1]:
	Adobe and Illustrator are either registered trademarks or trademarks of Adobe in the United States and/or other countries.

### Improvements

- Preflighting a document is no longer adding items to the undo/redo stack
- When converting a document you are no longer prompted with a message for every text frame that contains right alignment

### Resolved issues

- Fixed issue with the plug-in panel going blank when reopening
- Fixed issue with missing images in documents exported to GraFx Publisher from macOS
- Fixed issue with failing conversion for documents containing circular text
- Fixed issue with upload when using heavy assets on Windows
- Fixed issue where the document name was not updated in the plug-in when opening a new document

[Download page (behind login)](https://mysupport.chili-publish.com/hc/en-us/articles/360021250259-Latest-downloads)

This version is compatible with Adobe® Illustrator®[^1] 2022 (26.x) and 2023 (27.x).

This version is compatible with GraFx Publisher and the on-premise version of CHILI publisher (version 5.6 or above).

## Jun 6, 2023 - GraFx Studio

Version 0.123.1, using Studio SDK [0.123.0](https://github.com/chili-publish/studio-sdk/releases){target="_blank"}

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-09.svg)

### Features

- You can change the [corner radius](/GraFx-Studio/guides/shape-frame/) of your rectangle and polygon shapes by dragging the round handles in the shape or by using the corner radius properties in the frame properties panel

![animation](/GraFx-Studio/guides/shape-frame/corner-radius.gif)

### Improvements

- When a new frame is added it is only visible on the selected layout and its sub-layouts, on all other layouts the frame is hidden (if you want a frame to be visible on all layouts you should add it on the top-level layout)

## June 6, 2023 - GraFx Publisher

![rn_icon](/assets/CHILI_publisher_RGB.svg)

### Fixes

- Editor: Fixed issue where iframe caused the page to scroll when partially outside of view
- Editor: Fixed issue with transparent selection
- API: Removed redundant calls to file system to minimize probability for concurrency issues
- API: Fixed issue with ResourceSearchInFolder not returning items in response if includeSubDirectories property was false
- API: Strengthened security on REST API

## May 31, 2023 - GraFx Studio

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-09.svg)

We are working hard on delivering an end-to-end process, from Smart Templates created by designers to output generated by end users. Check out the [template management](/CHILI-GraFx/concepts/template-management/) page to learn more about this new way of working.

The first step in this process is organizing your templates in [collections](/CHILI-GraFx/guides/manage-collections/). This is available now!

In the next step, end users will be able to browse the collections and start a project from one of the templates. The project will be opened in a user-friendly interface where you can make changes and generate output.

![screen](/CHILI-GraFx/concepts/template-management/collections.png)

## May 31, 2023 - CHILI GraFx

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-04.svg)

### Fixes

- Updated error message if you want to invite more than 10 users at once to CHILI GraFx
- Disable 'Add Template Designer Seat' button when all Template Designer seats are assigned
- Fix issue with logout button on 'MyAccount' page

## May 26, 2023 - GraFx Studio



Version 0.122.1, using Studio SDK [0.122.0](https://github.com/chili-publish/studio-sdk/releases){target="_blank"}

![rn_icon](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS_OK-09.svg)

### Features

- You can [crop an image](/GraFx-Studio/concepts/crop/) to manually resize and position it inside an image frame
- [Snap guides](/GraFx-Studio/concepts/snapping/) show up when creating, moving or resizing a frame to help you to nicely align the frames in your design

![screenshot-fullwidth](/GraFx-Studio/concepts/crop/rectcrop.png)

![screenshot-fullwidth](/GraFx-Studio/concepts/snapping/snapping.gif)

### Improvements

- You can use the arrow keys to move a frame in steps of 1 pixel, holding down the Shift key moves it in steps of 10 pixels
- Creating, moving or resizing a frame is now done on a pixel grid, meaning that the x, y, width, and height properties have non-decimal values
- Punctuation marks stay together with the preceding word and will not move to the next line

### Fixes

- Fixed issue where the animation sometimes blinked at the beginning or the end
- Fixed issue where changing the width or height of a frame also caused an override on other properties
- Fixed issue with constraining proportions when changing the width or height of a frame in the properties panel

## May 23, 2023 - GraFx Publisher

![rn_icon](/assets/CHILI_publisher_RGB.svg)

### Fixes

- Output: Improved stability of VDP outputs with a large amount of rows and variables
- Output: Fixed output failure due to missing font
- Output: Improved reliability of PDF output when the system is under high load

## May 16, 2023 - CHILI GraFx - Environment API

![rn_icon](/assets/CHILI_LOGOS_OK-04.svg)

### Added Endpoints

User is able to **rename** template attached to collection

- PATCH /api/v1/template-collections/{collectionId}/templates/{templateId}

User is able to **create**, **rename** and **delete** project.

- POST	/api/v1/environments/{environmentId}/projects
- PATCH /api/v1/environments/{environmentId}/projects/{projectId}
- DELETE /api/v1/environments/{environmentId}/projects/{projectId}
	
User is able to **download** project json.

- GET /api/v1/environments/{environmentId}/projects/{projectId}/document

### Updated Endpoints

When a user attempts to **delete** a template attached to a collection, an error is returned. User is now able to use ‘force’ request parameter, the template will be deleted.

- DELETE /api/v1/templates/{templateId}

Http **method** is changed from ‘PUT’ to ‘PATCH’.

The endpoint now allows partial update of template collection instead of full update.

- PATCH /api/v1/template-collections/{templateCollectionId}


See Swagger [Environment API](https://sandbox1.chili-publish-sandbox.online/grafx/swagger/index.html).


## May 10, 2023 - GraFx Studio SDK

We renamed our repository and package for the SDK.
The new name is studio-sdk, coming from editor-sdk.

Also a new version has been pushed, we're now at version 0.121.0

??? note "Note for integrators"

	This means you'll have to update your integration dependency, and change it from @chili-publish/editor-sdk to @chili-publish/studio-sdk inside your `package.json`.


## Apr 20, 2023 - GraFx Publisher

![rn_icon](/assets/CHILI_publisher_RGB.svg)

### Features

- You can now log into GraFx Publisher via GraFx user account.


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

Read more about [User Management](/CHILI-GraFx/users/intro/).

## Apr 14, 2023 - GraFx Studio

Version 0.117.1, using Studio SDK [0.117.0](https://github.com/chili-publish/studio-sdk/releases){target="_blank"}

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
	Change `#!typescript import { Id } from '@chili-publish/studio-sdk/lib/types/CommonTypes'`<br>
	To `#!typescript import { Id } from '@chili-publish/studio-sdk'`<br>
	For more information, please check out the [SDK release notes](https://github.com/chili-publish/studio-sdk/releases/tag/0.117.0){target="_blank"}.


## Apr 18, 2023 - GraFx Publisher

**Boost Platform Performance**

GraFx Publisher comes with more than just a name change, this year it is all about improving platform performance. We've listened to your feedback and revamped our platform infrastructure to deliver blazing-fast file operations, including moving, copying, and deleting. This means you can work efficiently even in large environments! 🚀

Note: Smaller environments might not notice significant changes in performance.

🔔 Heads up: We've fine-tuned the ResourceItemGetTree and ResourceItemGetTreeLevel API endpoints to optimize performance. Now, these endpoints return only the first 10,000 items, ensuring a smoother experience for all users.

![rn_icon](/assets/CHILI_publisher_RGB.svg)

### Fixes

- API: Fixed issue with ResourceSearchInFolder not returning items in response if includeSubDirectories property was false
- API: Fixed 'ResourceGetTree/ResourceGetTreeLevel' for enabled support 'parentFolder' argument ending with slashes.
- API: Fixed 'rest-api/v1/resources/documents/items/{id}/privateinfo' endpoint to return 'fileInfo.xml' node


## Mar 31, 2023 - Infrastructure update

Your [CHILI GraFx](/CHILI_GraFx/) infrastructure has been upgraded to have the latest update.

With this update, we’re implementing platform infrastructure changes that greatly enhance  performance.

The update does require planned downtime, and will be transparant for you.

The update will be implemented (starting April 5) gradually on all tenants, and will happen over the following days and weeks.


## Mar 29, 2023 - GraFx Studio

Version 0.116.2, using Studio SDK [0.116.0](https://github.com/chili-publish/studio-sdk/releases){target="_blank"}

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

Version 0.114.1, using Studio SDK [0.114.0](https://github.com/chili-publish/studio-sdk/releases){target="_blank"}

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

Version 0.111.2, using Studio SDK [0.111.0](https://github.com/chili-publish/studio-sdk/releases){target="_blank"}

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

Version 0.107.4, using Studio SDK [0.107.0](https://github.com/chili-publish/studio-sdk/releases){target="_blank"}

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

Version 0.104.1, using Studio SDK [0.104.0](https://github.com/chili-publish/studio-sdk/releases){target="_blank"}

### Fixes

- Fixed issue with loading media
- Fixed issue with font size and line height properties of a character style being set to 0 when clicked upon, and it was not possible to clear them (now you can leave them empty again to use the values from the applied paragraph style)
- Fixed issue with text rendering when line height is 0
- Fixed issue with deleted font being shown in font dropdown menu
- Fixed issue with loading the default template
- Fixed weird behavior when using the Hand tool to move the page

## Jan 23, 2023 - GraFx Studio

Version 0.102.2, using Studio SDK [0.102.0](https://github.com/chili-publish/studio-sdk/releases){target="_blank"}

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
