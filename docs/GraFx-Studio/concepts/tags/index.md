# Tags

Template designers and environment admins use Tags to organize and filter templates in GraFx Studio.

## What Tags do

A Tag is a label you assign to a template. Tags have no effect on template behavior or output — they exist solely to help you organize and locate templates.

When your template library grows, Tags let you:

- Group templates by brand, campaign, product line, or region
- Filter the Templates list to show only what is relevant
- Keep unrelated Design Systems from cluttering each other's workspace

A template can have multiple tags. Templates with no tag assigned display a dash (`-`) in the **Tags** column.

## Where Tags live

Tags are managed under **GraFx Studio > Manage > Tags**. This section is separate from Templates, Collections, and My Projects — Tags are a management resource, not a content resource.

Tags are scoped to the environment. A tag created in one environment is not available in another.

## How Tags relate to templates

Tags are created independently and then assigned to templates. You build your tag vocabulary first, then apply it across your template library.

| Action | Where |
|---|---|
| Create, rename, delete tags | **Manage > Tags** |
| Assign tags to a template | **Templates** → ··· menu → **Assign tags** |
| Manage tags from a template | **Assign tags to your template** panel → **Edit tags** |
| Filter templates by tag | **Templates** → Filter |

## Practical example

A team managing Design Systems for two brands — `Chill_Home` and `Chill_Chips` — creates one tag per brand. Each template is assigned the relevant tag. Designers working on the Chill Chips campaign filter by `Chill_Chips` and see only those templates immediately.

!!! note
    Deleting a tag removes it from all templates it was assigned to. This action cannot be undone.

## Related

- [Manage & Use Tags](/GraFx-Studio/guides/use-tags/)