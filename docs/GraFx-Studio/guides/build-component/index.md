# Build a component

This guide walks you through creating a component in GraFx Studio. A component is built in its own workspace, which is similar to the Template Designer Workspace but with a focused set of features for reusable design elements.

See [Components](/GraFx-Studio/concepts/components/) for an introduction to what components are and when to use them.

## Create a component

In GraFx Studio, select **Components** from the left navigation.

![Components selected in GraFx Studio left navigation](components-nav.png)

The Components overview shows all components in your environment, with the same grid and list view options as the Templates overview.

![Components overview page with grid of components](components-overview.png)

To create a new component, click **+ Create component** in the top right.

You can also import an existing component from a `.ZIP` file using the **Import .ZIP** button.

## The component workspace

The component workspace opens after you create or open a component. It looks similar to the Template Designer Workspace — the same canvas, the same left toolbar, the same properties panel on the right.

The key difference is what is **not** there, by design:

| Feature | Not available in components | Reason |
|---|---|---|
| Digital animated intent | ❌ | Components focus on print and PDF output |
| Multi-page | ❌ | A component is a single reusable element, not a document |
| Output / Export button | ❌ | Output is produced by the parent template, not the component |
| User Interface settings | ❌ | UI settings belong at the template level |
| Bleed & slug | ❌ | Print production settings live on the template |
| Private data | ❌ | Not supported in components |
| Nesting (components inside components) | ❌ | Not supported in V1 |

Everything else works as expected: you can add frames, apply Brand Kit styles, create layouts, define variables, and use actions.

## Layouts in a component

A component can have multiple layouts, just like a template. Each layout can have its own design — for example a square, a horizontal, and a vertical version of the same pricing element.

These layouts are what makes [Resize mode](/GraFx-Studio/guides/use-components/#resize-mode) powerful: when the component is placed on a template, GraFx Studio can automatically pick the best-matching layout based on the frame size.

![Component workspace showing multiple layouts](component-layouts.png)

## Variables in a component

Variables work the same way as in templates, with one difference: **the List variable type is not available** in components.

List variables present a dropdown of predefined options to the end user. Since variable mapping flows one-way from template into the component, a list variable on the component side would create a conflict — the template variable driving the value wouldn't know which options to respect. For this reason, only mappable variable types are supported in V1.

Supported variable types in components:

- Single-line text
- Multi-line text
- Number
- Image
- Boolean (toggle)
- Date

![Variables panel in the component workspace](component-variables.png)

Variables defined in a component are the values that template designers can connect to template variables through [variable mapping](/GraFx-Studio/guides/use-components/#variable-mapping). Keep your variable names clear and descriptive — they appear by name in the mapping modal.

## Brand Kit

A component has its own Brand Kit, separate from the template's Brand Kit. This means a component can carry its own colors, fonts, and paragraph styles that are managed independently from the templates that use it.

If you want the template to be able to change a color or style inside a component, that value needs to be exposed as a variable and mapped from the template.

## Design & Run Mode

Both Design Mode and Run Mode are available in the component workspace. Use Run Mode to test how variables and actions behave inside the component before placing it in a template.

When a component is placed inside a template, it always runs as a project — both in the template's Design Mode and Run Mode.

## Next step

Once your component is built, place it in a template:

[Use components in a template →](/GraFx-Studio/guides/use-components/)
