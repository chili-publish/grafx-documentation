# Prepare your template for the Design Agent

The [Design Agent](/GraFx-Genie/design-agent/) works on any template as is. It works better with context, and this page is about giving it that context. The agent does not see your screen. It reads the template the way the GraFx Studio SDK exposes it: the names of layouts, frames and variables, the Brand Kit attached to the template, its colors, text styles, media and components, the data source, the Actions. The better that structure describes itself, the better the agent's work. This page explains what the agent reads, and how to set a template up so it reads well, whether you adapt an existing design or start from a blank page.

## What the agent reads

| In the template | What the agent uses it for |
|---|---|
| **Brand Kit** (colors, fonts, media, paragraph and character styles, components) and their [descriptions](/GraFx-Genie/design-agent/brand-kit-descriptions/) | The palette it designs with. The agent uses Brand Kit elements instead of inventing values, and the descriptions tell it which element fits which purpose. |
| **Layout tree**: names, parent/child structure, sizes, intent (print, digital static, digital animated), the selected layout | Knowing which layout it is working on, and which layouts exist when you ask it to add or copy one. |
| **Frames**: names, type (text, image, shape, barcode, component), position, size, constraints, per-layout anchoring, auto-grow and copyfitting | Finding "the headline" or "the lifestyle image", placing new frames sensibly, making layouts responsive. |
| **Variables**: names, types, groups, [descriptions](/GraFx-Studio/guides/template-variables/define/#description), image folders and connectors | Reusing what exists rather than creating duplicates, and knowing what a variable is for. |
| **Actions** and their triggers | Explaining the template, changing existing logic, checking what refers to a frame or variable before deleting it. |
| **Media connectors** and **data connectors** deployed in the environment | Linking image variables to a DAM, configuring batch output. |
| **Canvas presets** of the environment | Adding layouts by preset name ("add an A4 portrait layout"). |
| **Pages** and **animation** on animated layouts | Managing physical pages, and animating frames. |

On top of the template, the agent is guided by your environment's [custom skills](/GraFx-Genie/design-agent/skills/) and, for how-to questions, by the GraFx documentation.

## Attach a Brand Kit

The Brand Kit is the agent's single source of truth for everything visual. A template without colors and text styles cannot be designed on: the design pipeline refuses to compose when it has no palette to work from.

1. Create the Brand Kit in [GraFx Brand Kits](/GraFx-Brand-Kits/guides/create/): colors, fonts, media (logos, lifestyle imagery, badges), paragraph and character styles, and the components the brand uses.
2. [Import it in the template](/GraFx-Studio/guides/brandkits/#import-a-brand-kit) from the Brand Kit panel in GraFx Studio. Keep auto-sync on, so a kit update reaches the template without re-importing.
3. Give elements a [description](/GraFx-Genie/design-agent/brand-kit-descriptions/) that says when to use them. "Primary" is a name; "main brand color, use for headlines and the background of price badges" is an instruction.

The agent takes colors, media, text styles and components from the Brand Kit attached to the template. If the template has local colors and styles as well, those are visible to the agent too, but the Brand Kit is what makes its choices consistent across templates.

## Name things the way you would say them

The agent finds frames, layouts and variables by name. A frame called `Rectangle 12` is hard to refer to; `Price badge` is easy. Before you start, or as a first request to the agent itself, rename the elements you will talk about:

- Frames: `Headline`, `Subhead`, `Lifestyle image`, `Logo`, `Legal disclaimer`, `Promo badge`.
- Layouts: `A4 portrait`, `Instagram square`, `Digital signage landscape`.
- Variables: `Headline`, `Discount badge`, `Lifestyle` — and a short [description](/GraFx-Studio/guides/template-variables/define/#description) when the name alone does not say what it is for. The agent reads variable descriptions, and writes one when it creates a variable.

Two frames or Actions with the same name make the agent ask which one you meant. Unique, descriptive names keep the conversation short.

!!! tip "Let the agent name things"
    "Rename the frames to describe what they contain" is a valid first request on a freshly imported design. Review the result in the Layers panel.

## Structure the layouts

The agent works on the **selected layout** unless you name another one. Select the layout you want to change before you ask, or say it: "on the landscape layouts, move the image to the left".

- Keep the root layout as the master. Child layouts inherit its size and frames; the root is never deleted by the agent.
- Set the [layout intent](/GraFx-Studio/concepts/layout-intent/) correctly. Animation is only applied on digital animated layouts, bleed only on print layouts; the agent checks and reports instead of switching intent on its own.
- [Layout presets](/GraFx-Studio/guides/layouts/#reference-available-layout-preset-sizes) let you add layouts by name. A slightly wrong name ("A4 landscape" where the preset is "A4 Landscape") comes back with a did-you-mean.

## Make frames behave per layout

A design that must work across formats needs anchoring, auto-grow and copyfitting. You can set these yourself, or ask the agent to "make this layout responsive": it takes a snapshot, applies anchors, auto-grow and copyfit where appropriate, resizes the page to a few test sizes to check, restores the original size, and corrects what did not hold. See [Anchoring](/GraFx-Studio/concepts/anchoring/) for the underlying concept.

Frames with [constraints](/GraFx-Studio/concepts/constraints/) (no move, no resize, no inline text edit) are respected and can be set through the chat, so the legal disclaimer stays where it is.

## Components

Components the agent should be able to place must be reachable by name. Add them to the Brand Kit (Brand Kit components carry a description that tells the agent when and how to use them) or keep them in the environment's component library. When a name matches only a platform component that is not in the kit, the agent says so and places it only after you agree. Component fields are mapped to template variables by name, so matching names between component variables and template variables save a mapping step.

## Set up for designing from scratch

The agent can compose a complete page from a description. For that it needs a blank template that is nothing but a brand:

1. Create a new template in GraFx Studio and import the Brand Kit. Make sure the kit has at least a set of colors, a paragraph style for headlines and one for body copy, the logo as media, and descriptions on all of them.
2. Set the root layout to the size and intent of the first format you want ("A4 portrait, print"), or let the agent do that: "create a leaflet page, A4 portrait, with 3 mm bleed".
3. Add the components you want the agent to use (price tags, promo badges, product cards) to the Brand Kit, with descriptions.
4. Describe the page. The agent gathers the brand context, composes a plan, measures text so it fits, places the frames and reports back. Image frames are filled with a fitting asset from the kit.

The [design from scratch guide](/GraFx-Genie/design-agent/design-from-scratch/) walks through a full example.

## Checklist

Before a longer session with the agent:

- Brand Kit imported, auto-sync on
- Colors, media, text styles and components in the kit have descriptions
- Frames, layouts and variables have names you would use in a sentence
- Variables that are not self-explanatory have a description
- Layout intents are correct (print / digital static / digital animated)
- The layout you want to change is selected
- Environment [custom skills](/GraFx-Genie/design-agent/skills/) cover your recurring rules (which layouts a campaign needs, how to pick imagery, naming conventions)
