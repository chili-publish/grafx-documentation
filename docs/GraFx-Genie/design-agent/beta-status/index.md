# Beta status

The [Design Agent](/GraFx-Genie/design-agent/) is in [Beta](/release-notes/feature-maturity/#maturity-how-finished-it-is). Not every GraFx Studio feature is available to the agent yet; support is added throughout the Beta. This page lists, per area, what the agent can do today.

This is a high-level overview, not a complete reference. For example prompts per area, see [What you can ask](/GraFx-Genie/design-agent/commands/).

- **Supported:** the agent can read and change it.
- **Partial:** the agent can do part of it; the note says what is missing.
- **Not yet:** the agent cannot do it yet. Ask for it, and the agent tells you it is out of reach; make that change by hand in GraFx Studio.

## Layouts and pages

| Feature | Status | Notes |
| --- | --- | --- |
| Create, duplicate and delete layouts | Supported | Duplicating or moving a layout under another parent is not yet possible. |
| Layout name, display name, size and intent | Supported | |
| Bleed | Supported | Extending edge-touching frames into the bleed is not yet automatic. |
| End-user resizable layouts | Supported | |
| Inherited and overridden layout settings | Supported | Read only. |
| Inherited and overridden frame properties per layout | Not yet | |
| Layout fill color | Not yet | |
| Layout private data | Not yet | |
| Pages: add, remove, show and hide | Supported | |

## Frames

| Feature | Status | Notes |
| --- | --- | --- |
| Text frames | Supported | |
| Image frames | Supported | Including fit mode and Smart Crop. |
| Shape frames | Supported | Rectangles, circles, polygons and custom shapes. |
| Barcode frames | Supported | |
| Component frames | Supported | |
| Move, resize and rotate frames | Supported | |
| Fill, stroke, corner radius and opacity | Supported | |
| Gradients | Supported | Linear gradients. |
| Clip an image to a shape | Supported | |
| Stacking order | Supported | |
| Show and hide frames per layout | Supported | |
| Anchoring, auto-grow and copyfitting | Supported | |
| Make a whole design responsive | Supported | |
| Manual image crop | Not yet | |
| Drop shadows and blend modes | Not yet | |
| Overprint | Partial | On text, through character and paragraph styles; not yet on shape and barcode frames. |
| Rename frames | Not yet | |

## Text

| Feature | Status | Notes |
| --- | --- | --- |
| Write and format text | Supported | Including bulleted and numbered lists. |
| Insert a variable into text | Supported | |
| "Prevent line break" | Not yet | |
| "Remove paragraph if empty" | Not yet | |

## Variables

| Feature | Status | Notes |
| --- | --- | --- |
| Single-line text variable | Supported | |
| Multi-line text variable | Supported | |
| Image variable | Supported | Including images from GraFx Media or a connected DAM. Metadata mapping is not yet available. |
| Single-select list variable | Supported | |
| Boolean variable | Supported | |
| Number variable | Supported | |
| Date variable | Supported | Including display format, date range and excluded days. |
| Data source variable | Not yet | |
| Rich text variable | Not yet | |
| Variable groups | Supported | |
| Variable properties | Supported | Required, read-only, placeholder, help text, prefix and suffix, and similar. |
| Variable descriptions | Supported | |
| Display names for variables and list items | Supported | |
| Rename variables | Supported | Renaming variable groups is not yet possible. |
| Variable visibility conditions | Not yet | |
| Variable private data | Not yet | |

## Actions

| Feature | Status | Notes |
| --- | --- | --- |
| Create, change and delete Actions | Supported | |
| Check which Actions refer to a frame or variable | Supported | Before a delete. |
| Rename Actions | Supported | |

## Brand Kit

| Feature | Status | Notes |
| --- | --- | --- |
| Colors | Supported | Including descriptions. The agent can also add colors to the template, in RGB, CMYK or HEX. |
| Fonts | Partial | Through paragraph and character styles; applying a font by name is not yet possible. |
| Media | Supported | Including descriptions. |
| Paragraph styles | Supported | Including descriptions. The agent asks before it changes a style. |
| Character styles | Supported | Including descriptions. The agent asks before it changes a style. |
| Components | Supported | Including descriptions. A component that is not in the Brand Kit is placed only after you confirm. |
| Themes | Supported | |
| Use the Brand Kit by default | Partial | The agent does not yet always prefer Brand Kit styles and colors over new ones. |
| Import a Brand Kit | Not yet | |

## Components

| Feature | Status | Notes |
| --- | --- | --- |
| Place a component | Supported | |
| Map component variables to template variables | Partial | The agent creates and links new template variables; changing an existing mapping is not yet possible. |
| Edit a component in the component workspace | Supported | |

## Animation

| Feature | Status | Notes |
| --- | --- | --- |
| Animate a layout | Supported | |
| Change part of an animation | Supported | |

## Data and output

| Feature | Status | Notes |
| --- | --- | --- |
| Data source and data connectors | Supported | |
| Match data source columns to variables | Supported | |

## Design

| Feature | Status | Notes |
| --- | --- | --- |
| Generate a design from a prompt | Supported | |
| Adapt a design to another format | Supported | |
| Check a design visually | Supported | |
| Copy from another template | Supported | |
| End-user editing constraints | Supported | |

## Custom skills

| Feature | Status | Notes |
| --- | --- | --- |
| Custom skills | Supported | See [custom skills](/GraFx-Genie/design-agent/skills/). |
| Export and import skills between environments | Supported | |
| Check custom skills for conflicts | Not yet | |

## Administration

| Feature | Status | Notes |
| --- | --- | --- |
| Opt out per environment | Supported | See [Availability and usage](/GraFx-Genie/design-agent/manage/). |
| Usage report | Not yet | |

## Outside the Design Agent's scope

The Design Agent works on the open template. It does not handle the following, by design rather than as a Beta limitation:

- generating output, output settings, output tasks and user interfaces
- template management: projects, collections and tags
- changing the assets in your Brand Kit or GraFx Media
