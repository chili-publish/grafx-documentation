# GraFx Publisher - Release notes

![rn_icon](/assets/CHILI_publisher_RGB.svg)

## May 16, 2023

### Fixes

- Output: Fixed output failure due to missing font
- Output: Improved reliability of PDF output when the system is under high load

## Apr 20, 2023

### Features
- You can now log into GraFx Publisher via GraFx user account.

## Apr 18, 2023

### Fixes

- API: Fixed issue with ResourceSearchInFolder not returning items in response if includeSubDirectories property was false
- API: Fixed 'ResourceGetTree/ResourceGetTreeLevel' for enabled support 'parentFolder' argument ending with slashes.
- API: Fixed 'rest-api/v1/resources/documents/items/{id}/privateinfo' endpoint to return 'fileInfo.xml' node

## Mar 17, 2023

!!! danger "Sandbox Release"
	
	Information related to your Sandbox.
	
	When the update is in production, another release note will be added.

Your [CHILI GraFx](/CHILI_GraFx/) sandbox has the latest update to [GraFx Publisher](/GraFx_Publisher/)

- Our goal: Improve performance in handling templates, documents, assets.
- Our ask: Test in your sandbox now, and send us your feedback.

With this update, we’re implementing a new platform infrastructure that greatly enhances  performance. We **urge** you to test GraFx Publisher on your sandbox environment to experience this new level of performance for yourself.