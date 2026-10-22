# What you can ask the Design Agent

The [Design Agent](/GraFx-Genie/design-agent/) understands plain language; there is no command syntax to learn. This page lists what it can do, grouped by area of GraFx Studio, with example requests you can adapt. Where the agent asks a question or refuses something, that is noted too.

A few habits make every request land better:

- **Name the thing.** "Make the *Headline* frame editable" beats "make the text editable". The agent works with [frame, layout and variable names](/GraFx-Genie/design-agent/template-setup/#name-things-the-way-you-would-say-them). If you select a text frame on the canvas first, "change the copy to …" targets that frame.
- **Name the layout, or select it.** Changes apply to the selected layout unless you say otherwise: "on all landscape layouts …".
- **One intention per message** for predictable results; "and then" chains are fine for related steps.
- **Ask first if unsure.** "What would you change to make this a template?" costs nothing and gives you a plan to react to.

## Ask about the template and about GraFx Studio

| You want to | Say for example |
|---|---|
| Understand a template | "Explain this template", "How does this template work?" — the reply walks through the variables and where they appear, the layouts, and the Actions as trigger → effect, in plain language. |
| Inspect another template | "What's in template *Summer leaflet*?" |
| See what is on the canvas | "List the frames on this layout", "Which layouts does this template have?", "What variables exist?", "What data source is configured?" |
| Troubleshoot | "Why is the *Discount* variable not visible?", "Why does the headline overflow on the Story layout?" |
| Learn a Studio feature | "How do image variables work?", "What's the difference between layouts and pages?", "Walk me through anchoring", "Help me set up copyfitting myself" — answered from the GraFx documentation, with a link to the page. |
| Know what it did | "What did you change?" after a turn. |

## Layouts and pages

| You want to | Say for example | Notes |
|---|---|---|
| Add layouts | "Add an A4 portrait layout", "Add 1080×1080 px and 1080×1920 px layouts", "Add a layout called *Shelf talker*" | By [preset](/GraFx-Studio/guides/layouts/#reference-available-layout-preset-sizes) name, custom size in mm or px, or name only (inherits the parent's size). A near-miss preset name gets a did-you-mean. New layouts inherit intent, units and bleed from the parent unless you specify them. |
| Rename, resize, change intent | "Rename *Layout 2* to *Instagram square*", "Make this layout 210 × 297 mm", "Set the intent of *Signage* to digital animated" | |
| Hide a layout from end users | "Hide the *Master* layout in Run Mode" | |
| Delete layouts | "Delete the *Test* layout", "Delete all child layouts" | The root layout is never deleted. Deleting all asks for confirmation. |
| Bleed | "Set 3 mm bleed on all print layouts", "Set the top bleed to 5 mm" | Print layouts only; on a digital layout the agent explains instead of switching the intent. |
| Copy settings | "Apply the settings of *A4 portrait* to this layout" | Includes bleed. |
| Rework the arrangement | "On the landscape layouts, put the image on the left and the rest on the right", "Rearrange this layout for the Story format" | |
| Make resizable for end users | "Make this design resizable for end users, minimum 100 × 100 mm, keep the aspect ratio" | See [layout size constraints](/GraFx-Studio/concepts/layout-size-constraints/). |
| Pages | "Add a page", "Duplicate page 1", "Hide page 3", "Go to page 2" | Pages are physical sheets, not layouts. |

## Frames

| You want to | Say for example | Notes |
|---|---|---|
| Add frames | "Add a text frame for the subhead under the headline", "Add an image frame 80 × 80 mm top-right", "Add a QR code bottom-right, 20 mm", "Add a shape behind the price" | Text, image, shape and barcode frames. Without a position, a new frame lands as a visible, roughly centered box. |
| Style shapes | "Make the badge shape *Price Red* with a 2 mm white stroke and 4 mm corner radius" | Fill, stroke and corner radius apply to shape frames. |
| Clip an image | "Clip the lifestyle image to a circle" | Circle, ellipse, rounded, polygon, rectangle, or none. |
| Order | "Bring the logo to the front", "Send the background one step back" | |
| Lock and constrain | "Lock the legal disclaimer so users can't move, resize or edit it", "Allow inline text editing on the headline" | Inline text editing is refused on a variable-driven frame; the agent explains the form-versus-canvas distinction. See [constraints](/GraFx-Studio/concepts/constraints/). |
| Show or hide per layout | "Hide the QR code on the digital layouts" | If hiding leaves an obvious hole, the agent asks whether to reflow the layout or leave it. |
| Delete | "Delete the *Old badge* frame" | Checks whether an Action refers to the frame first. |
| Rename | "Rename the frames to describe what they contain" | |

## Text

| You want to | Say for example | Notes |
|---|---|---|
| Change copy | "Change the headline to *Holiday meals, ready to go*", "Add a paragraph about delivery under the body copy" | Selected text frame when none is named. |
| Format | "Make the headline 48 pt, centered, in *Fresh Green*", "Apply the *Legal* paragraph style to the footer" | |
| Turn text into a variable | "Turn the word *Christmas* in the headline into a variable", "Make the headline, subhead and body editable" | Keeps the current styling; the current text becomes the default. |

## Variables

| You want to | Say for example | Notes |
|---|---|---|
| Create | "Create a short text variable *Store name*", "Create an image variable *Lifestyle* linked to the *Campaigns/Approved* folder in Bynder", "Add a dropdown *Discount badge* with the options 25% off, 50% off, BOGO, BOGO 50" | A duplicate name fails only that variable. Image variables can use GraFx Media or any deployed media connector. |
| Make frames editable | "Make the lifestyle image, headline and deck editable", "Turn the *Logo* frame into an image variable" | Image variables are seeded with the current asset. |
| Link | "Link the *Lifestyle* variable to the *Hero* image frame" | Changing the variable then updates the frame. |
| Change settings | "Make *Headline* required", "Set the default of *Store name* to *Ghent*", "Rename *txt_1* to *Subhead*", "Change the display name of *Discount badge* to *Promotion*" | |
| Describe | "Add a description to each variable that says where it appears" | Descriptions are also read by GraFx Genie, see [variable descriptions](/GraFx-Studio/guides/template-variables/define/#description). |
| Group | "Put the price variables in a group called *Prices*", "Dissolve the *Misc* group" | If a matching group exists, say whether to reuse it; the agent asks when unsure. |
| Delete | "Delete the *Old price* variable", "Delete all variables" | Checks Action references; deleting all asks for confirmation. |

## Actions and logic

| You want to | Say for example | Notes |
|---|---|---|
| Add logic | "Add a toggle so users can show or hide the badge", "Hide the *Discount badge* frame when *Discount* is empty", "Switch to the *Print* theme when a print layout is selected" | The agent writes the Action (through [GraFx Genie for Actions](/GraFx-Genie/concepts/actions/)), using current helper functions only. |
| Change logic | "Change action *Toggle badge* to also hide the price strike-through" | Updates the script; name and triggers when you ask. Two Actions with the same name make the agent ask which one. |
| List, find, delete | "Which actions are there?", "What refers to the *Badge* frame?", "Delete the *Test* action" | |

## Responsiveness, anchoring and copyfitting

| You want to | Say for example | Notes |
|---|---|---|
| Make a layout responsive | "Make this layout responsive" | The agent snapshots the layout, sets anchors, auto-grow and copyfit, resizes to test sizes, restores the original size and corrects what did not hold. If restoring fails it tells you the page may still be at the test size. |
| Specific behavior per layout | "Pin the logo to the top-left on all layouts", "Let the body copy grow with its content", "Copyfit the headline on the Story layout" | Anchor (pin/stretch), [auto-grow](/GraFx-Studio/guides/text-frame/), copyfit. |

## Animation

| You want to | Say for example | Notes |
|---|---|---|
| Animate a layout | "Add animations on the animated layouts", "Animate the Full HD layout: fade in the headline, slide the promo slots in from the right, 8 seconds" | Digital animated layouts only; on a static or print layout the agent reports an error and leaves the existing animation untouched. Resets the previous schedule, sets the duration, animates the frames you asked for, extends background visibility when requested. Progress is shown per stage and can be stopped. |
| Reset | "Remove the animation from this layout" | |

See [Animation](/GraFx-Studio/concepts/animation/).

## Brand Kit, colors and styles

| You want to | Say for example | Notes |
|---|---|---|
| Themes | "What themes does this kit have?", "Switch to the *Print* theme" | |
| Media | "What logos and images are in the brand kit?", "Place the logo top-left" | Answers quote the [descriptions](/GraFx-Genie/design-agent/brand-kit-descriptions/). |
| Colors | "What colors are on this template?", "Add a color *Primary* #F40009", "Change *Accent* to #FFB400", "Delete the unused colors" | Deleting checks usage and confirms. |
| Text styles | "Create a paragraph style *Price*, 36 pt bold right-aligned", "Change the *Body* style to 10 pt", "List the character styles" | |

Changes to colors and styles made in the chat are made in the template's copy of the Brand Kit. Manage the source of truth in [GraFx Brand Kits](/GraFx-Brand-Kits/).

## Components

| You want to | Say for example | Notes |
|---|---|---|
| Place | "Add the *Promo slot* component five times in a grid in the bottom half", "Place the *Discount badge* top-right of the product image" | Resolved by name, Brand Kit first, then the environment's components. A partial name gives you chips to pick from; a platform-only match is placed only after you agree. |
| Map fields | "Map the badge's *Discount* field to the *Discount* variable", "Map the promo slot fields to the matching template variables" | Mapped fields stay linked. |

See [Components](/GraFx-Studio/concepts/components/) and [variable mapping](/GraFx-Studio/concepts/component-mapping/).

## Media and connectors

| You want to | Say for example | Notes |
|---|---|---|
| Which connectors exist | "Which media connectors are available?", "Which data connectors can I use?" | |
| Link imagery | "Link the lifestyle image to the *Campaigns/Approved* folder in our DAM" | Creates or updates an image variable with that folder and connector. |

## Data source and batch output

| You want to | Say for example | Notes |
|---|---|---|
| Set up | "Connect this template to our *Weekly offers* data source", "Set up batch output with the Google Sheets connector" | The agent offers the deployed data connectors as chips, configures the one you pick, then matches columns to variables. For columns with no matching variable it asks whether to create them or skip. After that, use Run Mode to step through records. |
| Inspect, remove | "What data source is on this template?", "Turn off batch output" | |

See [Connectors for Data](/GraFx-Studio/concepts/connectors-data/).

## Copy from another template

| You want to | Say for example | Notes |
|---|---|---|
| Reuse pieces | "Copy the *Price* variable and the fade animation from *Summer leaflet* onto this layout", "Copy the layouts from template *Master formats*" | Variables, Actions, layouts and animations. An ambiguous template name gives you chips. |

## Generate a design

| You want to | Say for example | Notes |
|---|---|---|
| Design a page | "Create a leaflet page with five promo slots, a lifestyle image in the background, a headline at the top and a footer with the disclaimer", "Design a vertical web banner with one promo slot and no lifestyle image" | Needs a Brand Kit with colors and text styles. Progress shows brand → compose → measure → placement → place. Image frames are filled with fitting media. |
| Iterate | "Add the brand logo top-left", "Make the headline bigger and move the promo slots down", "Use the breakfast lifestyle image instead" | Each change is a new turn, undoable on its own. |

See the [design from scratch guide](/GraFx-Genie/design-agent/design-from-scratch/).

## Session

| You want to | Do |
|---|---|
| Stop a running turn | Click **Stop**. What already landed stays; the request returns to the text box. |
| Undo a turn | ++ctrl+z++ / ++cmd+z++, one step per turn. |
| Repeat an earlier prompt | ++up++ / ++down++ in the text box. |
| Start over | Choose **Clear chat history** in the **…** menu at the top of the chat. Your template is not changed. |
