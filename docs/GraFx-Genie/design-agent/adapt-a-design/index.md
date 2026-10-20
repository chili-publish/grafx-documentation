# Guide: turn an existing design into a Design System

This guide follows a typical first session with the [Design Agent](/GraFx-Genie/design-agent/): a finished creative comes in from a desktop application, and in one conversation it becomes a template that end users can produce from in [GraFx Experience](/GraFx-Experience/). The example is an in-store sign for prepackaged holiday meals, needed in print and on digital displays.

You can follow the same steps with a design drawn in GraFx Studio; the import is optional.

## Before you start

- The design is open in the GraFx Studio workspace. Imported from [Figma](/GraFx-Studio/convert/Figma/), [Adobe InDesign](/GraFx-Studio/convert/Adobe-InDesign/) or [Adobe Photoshop](/GraFx-Studio/convert/Adobe-Photoshop/), or built in GraFx Studio.
- A Brand Kit is imported, with [descriptions](/GraFx-Genie/design-agent/brand-kit-descriptions/) on its elements.
- Frames have recognizable names, or you are happy to let the agent rename them.

See [Prepare your template](/GraFx-Genie/design-agent/template-setup/) for the full checklist.

## 1. Ask for a plan

Open the chat from the GraFx Genie button at the bottom of the left sidebar and start with a question rather than an instruction:

> How do I turn this design into a design system?

The agent reads the document and reports what it finds: which text frames look like they should be editable, where an image could become an image variable, what looks like a promotional element that needs a toggle, which frames should be locked. It proposes; it does not change anything yet. Read the plan, and adjust it in the conversation ("the price is not editable here, it comes from the data source later").

## 2. Make the right things editable

> Make the lifestyle image, the headline and the deck editable. Lock the legal disclaimer so teams can't touch it.

The agent creates an image variable seeded with the current lifestyle photo, two text variables with the current copy as default (styling is kept), links each to its frame, and sets [constraints](/GraFx-Studio/concepts/constraints/) on the disclaimer frame. Check the Variables panel: names and descriptions are there, ready for the form end users will see.

If you prefer your own naming or grouping, say so now, or capture it once in a [custom skill](/GraFx-Genie/design-agent/skills/) so you never have to say it again.

## 3. Add layouts for the channels

> Add layouts for A4 and A3 portrait posters, and a Full HD landscape layout for the digital displays.

Layouts are added by [preset](/GraFx-Studio/guides/layouts/#reference-available-layout-preset-sizes) name or size, as children of the root layout, inheriting its frames. A landscape display rarely wants a portrait arrangement, so:

> On the landscape layouts, put the image on the left and all other elements on the right.

The agent rearranges the frames on those layouts only. Select a layout in the Layouts panel to look at the result; ++ctrl+z++ reverts the whole turn if you want to describe it differently.

## 4. Animate the digital layouts

> Add animations on the animated layouts.

Set the intent of the Full HD layout to *digital animated* first (or ask the agent to). The agent resets any existing schedule, sets a duration and animates the frames, showing the stages as it goes. Fine-tune in the [timeline](/GraFx-Studio/guides/animate-frame/) or in the chat: "make the headline fade in later and loop the whole thing".

## 5. Add a choice and a toggle

> Add a dropdown so users can pick a badge: 25% off, 50% off, BOGO, BOGO 50.
> Add a toggle so users can show or hide the badge.

The first request creates a list variable and the logic to swap the badge artwork or copy; the second adds a boolean variable and an Action that shows or hides the badge frame. Both are regular Actions you can open in the Actions panel.

## 6. Connect imagery to the DAM

> Link the lifestyle image to the *Campaigns/Approved* folder in our DAM.

If a media connector is deployed in the environment, the agent points the image variable at that connector and folder; otherwise GraFx Media is used. End users can now pick another approved lifestyle image.

## 7. Make it resize well (optional)

> Make this design resizable for end users, minimum 100 × 100 mm, keep the aspect ratio.

and, for a layout that must survive different proportions:

> Make this layout responsive.

The agent sets [anchors](/GraFx-Studio/concepts/anchoring/), auto-grow and copyfitting, tests a few sizes, and restores the original size.

## 8. Test, then publish

Switch to Run Mode and go through the form as an end user would: pick a layout, change the image, edit the headline and deck, choose a badge, toggle it off. Ask the agent "what did you change?" for a recap you can paste into a handover note.

Save the template and make it available in GraFx Experience as you would any other template. Nothing about a template built with the agent is different from one built by hand.

## Variations

- **Several brands or a print palette:** "Switch to the *Print* theme on the print layouts" uses Brand Kit [themes](/GraFx-Brand-Kits/concepts/themes/).
- **Weekly offers from a sheet:** "Connect this template to the *Weekly offers* data source and match the columns to the variables" sets up batch output.
- **A campaign you run every quarter:** put the layout set, arrangement rules and naming in a [custom skill](/GraFx-Genie/design-agent/skills/), and the whole of steps 3 to 5 becomes "prepare this design for the Spring campaign".
