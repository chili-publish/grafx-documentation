# Custom skills

The [Design Agent](/GraFx-Genie/design-agent/) knows GraFx Studio. It does not know that your campaigns always ship in six formats, that every print layout needs a QR code bottom-right, that image variables must point at the `Campaigns/Approved` folder of your DAM, or that the words "Transition zone" mean something specific in your stores. **Custom skills** are how you teach it.

A skill is a reusable instruction, written in plain language, about *how* the agent should carry out a kind of task in your environment. The agent reads the skills of the environment at the start of every session, picks the ones that match what you ask, and follows them. Think of a skill as a page of your design-system handbook, written for the agent.

## What a skill is good for

Skills shine for anything you would otherwise repeat in every chat:

- **Layout sets.** "For a *Seasonal* campaign, add these layouts: A4 portrait, A3 portrait, 1080×1080, 1080×1920, Full HD landscape (animated). Landscape layouts put the image on the left."
- **Variable and naming conventions.** How variables are named and grouped, which ones are always required, what goes into the description.
- **Image selection guidance.** Which DAM folder, which subject types, when a lifestyle image is appropriate and when a packshot.
- **Connector guidance.** How a custom media or data connector is organized: folder structure, metadata fields, the column that holds the price.
- **Tone of voice.** How placeholder and default copy should sound.
- **Organization-specific vocabulary.** For example the in-store zones a retailer uses (*Transition*, *Impulse*, *Destination*) and what each means for the design.
- **Hard rules.** Legal copy that must be present on print layouts, logo clear space, elements that must never be variable.

A skill is not the place for a single one-line preference you can simply type in the chat, nor for a one-off task. It is for rules and procedures that recur.

Skills complement [Brand Kit descriptions](/GraFx-Genie/design-agent/brand-kit-descriptions/): a description explains one element, a skill explains a way of working.

## Where skills live

Skills are a platform concept, see [Skills](/CHILI-GraFx/concepts/skills/). Subscription Admins and Environment Admins manage them per environment in **Environment settings › Skills**: see [Manage skills](/CHILI-GraFx/guides/manage-skills/) for creating, editing, enabling, importing, exporting and deleting skills, and for the field limits. Every environment can hold up to **10** skills.

Each skill has a **name**, a **description** and **instructions**. The agent reads the names and descriptions of all enabled skills on every prompt to decide which ones to load, then follows the instructions of the skills it loaded. The description is the trigger: the more specific it is, the more reliably the skill is picked up.

The agent reads the skills when a template is opened. Reopen the template to pick up a new or changed skill.

## Let GraFx Genie write the skill

When you create a skill in environment settings, you can describe what it should do in your own words, as if you were briefing a colleague, and let GraFx Genie generate the name, description and Markdown instructions. Concrete facts (folder names, sizes, field names, counts) are copied into the skill as you wrote them, and the result is grounded in what the agent can actually do in GraFx Studio and in the documentation. The prompt you typed is stored with the skill (it is not shown in the UI), so a later edit with **Edit skill with GraFx Genie** knows where the skill came from.

<!-- TODO Bram: screenshot of the Create skill modal -->

!!! info "Facts the agent can look up are not baked in"
    When your brief mentions things the agent can read at runtime (the available layout presets, the deployed connectors, the Brand Kit colors, the templates in the environment), the generated skill instructs the agent to look them up rather than hard-coding a list that would go stale.

    Requests that would expose how the agent works internally are refused. "Explain how a media connector is structured" is fine; "list all the steps the agent takes" is not.

## Best practices for custom skills

The agent decides which skills to load from their **name and description**, then follows the **instructions**. A skill with a vague description is never picked up; one with vague instructions is picked up and ignored.

**Name and description: say when.** Not "Layouts" but "Campaign layout set — use when asked to add layouts for a seasonal or promo campaign". List the phrasings people use: "add the campaign formats", "make all the sizes", "prepare for the November campaign".

**Instructions: say how, in order.** Numbered steps for procedures, bullet lists for rules, a table for sizes. The agent works through a skill top to bottom.

**Be concrete.** Exact sizes in mm or px, exact layout names, exact DAM folder paths, exact variable names. "Reasonable margins" is a guess; "12 mm on print, 48 px on digital" is an instruction.

**Say what not to do.** "Never make the legal disclaimer a variable." "Do not add animation to print layouts." Negative rules prevent the most expensive mistakes.

**Refer to Brand Kit elements by name.** "Use *Price Red* for discount badges" works when the kit has a color called Price Red. Keep skills and kit in sync.

**One topic per skill.** A skill for the campaign layout set, one for image selection, one for naming. Smaller skills trigger more reliably and are easier to maintain than one large handbook. With a cap of 10, group related rules by topic rather than by campaign.

**Expect style skills to be applied on request.** A skill about tone of voice or general style is picked up when a request matches it. Mention the style in the chat ("write the placeholder copy, use our tone of voice") if you want to be sure.

**Where a skill overlaps with the agent's built-in way of working, the built-in behavior generally wins.** Skills are for adding your rules, not for overriding how GraFx Studio features work.

**Test in the chat.** After saving, ask the agent for the task the skill covers and check the canvas. If it did not pick the skill up, sharpen the description. If it picked it up and got a step wrong, sharpen that step.

## Example skills

### Campaign layout set

**Name:** Campaign layout set

**Description:** Use when asked to add, create or prepare the layouts, formats or sizes for a campaign (seasonal, promo, weekly offers), or when asked for "all the formats". Defines which layouts a campaign needs and how each one is arranged.

**Instructions:**

```markdown
# Campaign layout set

Every campaign template needs these child layouts of the root layout.
Use the layout preset where one exists; otherwise create a custom size.

| Layout name            | Size            | Intent            |
|------------------------|-----------------|-------------------|
| A4 portrait            | preset A4       | print, bleed 3 mm |
| A3 portrait            | preset A3       | print, bleed 3 mm |
| Shelf talker           | 90 × 50 mm      | print, bleed 2 mm |
| Social square          | 1080 × 1080 px  | digital static    |
| Story                  | 1080 × 1920 px  | digital static    |
| Signage landscape      | 1920 × 1080 px  | digital animated  |

## Arrangement rules

1. Portrait layouts: lifestyle image top half, headline over the image, promo slots bottom half.
2. Landscape layouts: lifestyle image left 40 %, everything else right.
3. Shelf talker: no lifestyle image, no footer; product, price and badge only.
4. Signage landscape: apply the standard animation (fade-in headline 0.5 s,
   slide-in promo slots from the right, 8 s total). Loop.

## Always

- Logo top-left on every layout, 10 % of the layout width, clear space of one logo height.
- Legal disclaimer in the footer on all print layouts, style "Legal". Never on digital layouts.
- A QR code frame bottom-right on all print layouts, 20 mm, linked to the "Landing URL" variable.

## Never

- Do not change the root layout.
- Do not make the legal disclaimer or the logo editable.
```

### Image selection

**Name:** Image selection from the DAM

**Description:** Use when asked to add, link, replace or choose images, lifestyle photography or packshots, or to make an image editable. Explains where approved imagery lives and how to pick it.

**Instructions:**

```markdown
# Image selection

- Approved campaign imagery lives in the "Campaigns/Approved" folder of the Bynder connector.
  Link image variables to that folder; never to the root.
- Packshots live in "Products/Packshots". Product images in promo slots come from here,
  through the data source column "image_url".
- Lifestyle images are chosen by the products in the promotion: dairy and bakery → breakfast
  scenes, meat and barbecue → outdoor scenes, ready meals → dinner scenes.
- Use Smart Crop on every image frame that is variable-driven.
- When no image is specified, use the Brand Kit media whose description matches the request
  rather than leaving the frame empty.
```

### Naming and variables

**Name:** Variable naming and grouping

**Description:** Use whenever variables are created, renamed, grouped or made editable. Defines naming, grouping, defaults and descriptions.

**Instructions:**

```markdown
# Variables

- Names are Title Case, in the language of the brand team: "Headline", "Subhead", "Promo price 1".
- Group variables by what the end user edits together: "Copy", "Prices", "Images", "Options".
  Reuse an existing group with the same name; do not create "Copy 2".
- Every variable gets a one-sentence description that says where it appears and any length limit.
- Text variables for headlines are required, with a default taken from the current frame text.
- Toggle variables are booleans named after what they show: "Show discount badge".
- Never create variables for the logo, the legal disclaimer or the QR code.
```

## Related

- [Brand Kit descriptions](/GraFx-Genie/design-agent/brand-kit-descriptions/): per-element guidance.
- [What you can ask](/GraFx-Genie/design-agent/commands/): the commands skills can build on.
- [Environments](/CHILI-GraFx/concepts/environments/): where environment settings live.
