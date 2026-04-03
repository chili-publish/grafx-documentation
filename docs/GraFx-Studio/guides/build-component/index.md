# Build a component

This guide walks you through creating a component in GraFx Studio. A component is built in its own workspace, which is similar to the Template Designer Workspace but with a focused set of features for reusable design elements.

!!! info "Output capabilities when using components"
    Templates that use components support **print**, **static digital**, and **animated digital** (GIF, MP4) output.

    When rendering animated output, the component frame can be animated in the template timeline. The content inside the component does not animate.

    **HTML output is not supported** for templates that include components.

See [Components](/GraFx-Studio/concepts/components/) for an introduction to what components are and when to use them. New to components? Start with the [tutorial](/GraFx-Studio/guides/components-tutorial/) for a full end-to-end walkthrough.

## Create a component

In GraFx Studio, select **Components** from the left navigation.

![Components selected in GraFx Studio left navigation](components-nav.png){.screenshot}

The Components overview shows all components in your environment, with the same grid and list view options as the Templates overview.

![Components overview page with grid of components](components-overview.png){.screenshot}

To create a new component, click **+ Create component** in the top right.

## The component workspace

The component workspace opens after you create or open a component. It looks similar to the Template Designer Workspace — the same canvas, the same left toolbar, the same properties panel on the right.

The key difference is what is **not** there, by design:

| Feature | Not available in components | Reason |
|---|---|---|
| Digital animated intent | ❌ | Animation intent is set on the parent template. Component content does not animate — but the component frame can be animated in the template timeline. |
| Multi-page | ❌ | A component is a single reusable element, not a document |
| Output / Export button | ❌ | Output is produced by the parent template, not the component |
| User Interface settings | ❌ | UI settings belong at the template level |
| Bleed & slug | ❌ | Print production settings live on the template |
| Private data | ❌ | Not supported in components |
| Add component as a frame | ❌ | Not supported in V1 |
| Change page size via actions | ❌ | The template determines the frame size — the component adapts to the space it's given |

Everything else works as expected: you can add frames, apply Brand Kit styles, create layouts, define variables, and use actions.

## Actions in a component

Actions are available in the component workspace and work the same way as in templates — you define a trigger and a JavaScript block that runs when the trigger fires. They are useful for controlling visibility, switching layouts, applying styles, or responding to variable changes **within the component's own scope**.

However, there are two important limitations that are easy to overlook.

### Variable changes do not propagate to the template

Data flows one way: from the template into the component. If an Action inside a component sets or modifies a variable value, that change stays within the component. The template never receives it.

This means: if you map a component variable to a template variable, and an Action inside the component updates that component variable at runtime, the template-side variable is **not updated**. At output time, the engine reads the template-side value — which is still whatever it was before the Action ran — and that is what appears in the output.

!!! warning "Component Actions cannot drive template output"
    Do not use Actions inside a component to set values that you expect to appear in the template or in the output. Those values will silently remain empty or unchanged on the template side.

    If you need logic that affects output-level variable values, build that Action on the **template**, not inside the component.

### Output processing order may differ from workspace order

When GraFx Studio generates output, it processes template variables in an internal order that does not necessarily match the order they appear in the workspace or variable list. If an Action in a component fires in response to one variable and changes something (like a frame position), a subsequent variable processed by the engine may overwrite that result.

The consequence: what you see on the canvas in Design Mode or Run Mode may not match what the output renders. The system is working as designed — but the workspace and the output engine apply values in a different sequence.

!!! warning "Canvas ≠ output when Actions affect positions or layout"
    If a component uses Actions that change frame positions, layout selection, or other properties based on variable values, always validate the actual output — not just the canvas preview. Discrepancies between canvas and output are a known consequence of the variable processing order at output time.

### What Actions in a component are safe for

Actions inside a component work reliably for anything that stays within the component's own rendering scope:

- Showing or hiding frames based on component variables
- Switching between internal layouts
- Applying styles or copyfitting rules
- Responding to a variable change to adjust the internal design

For everything else — especially anything that needs to surface in the template or in the output — build the Action on the template side, where it has full visibility over the output rendering process.

### Page size

If an Action inside a component attempts to change the page size, it will fail with an "Action failed" error at output time. A component renders within the frame the template provides — it cannot change the frame itself. To adapt a component's appearance to different frame sizes, use [multiple layouts](#layouts-in-a-component) and [Resize Mode](/GraFx-Studio/guides/use-components/#resize-mode) instead.

## Layouts in a component

A component can have multiple layouts, just like a template. Each layout can have its own design — for example a square, a horizontal, and a vertical version of the same pricing element.

These layouts are what makes [Resize mode](/GraFx-Studio/guides/use-components/#resize-mode) powerful: when the component is placed on a template, GraFx Studio can automatically pick the best-matching layout based on the frame size.

![Component workspace showing multiple layouts](component-layouts.png){.screenshot-full}

## Variables in a component

Variables work the same way as in templates, with one difference: **the List variable type is not available** in components.

List variables present a dropdown of predefined options to the end user. Since variable mapping flows one-way from template into the component, a list variable on the component side would create a conflict — the template variable driving the value wouldn't know which options to respect. For this reason, only mappable variable types are supported in components.

Supported variable types in components:

- Single-line text
- Multi-line text
- Number
- Image
- Boolean (toggle)
- Date

!!! note "Image variables require a different setup"
    Image variables can be created in a component and used to drive image frames. Because each image variable is tied to a specific connector, they cannot be directly mapped from a template image variable. See [Passing an image into a component](#passing-an-image-into-a-component) for the setup.

![Variables panel in the component workspace](component-variables.png){.screenshot-full}

![Variables panel in the component workspace](component-variable-types.png){.screenshot}

Variables defined in a component are the values that template designers can connect to template variables through [variable mapping](/GraFx-Studio/guides/use-components/#variable-mapping). Keep your variable names clear and descriptive — they appear by name in the mapping modal.

## Brand Kit

A component has its own Brand Kit, separate from the template's Brand Kit. This means a component can carry its own colors, fonts, and paragraph styles that are managed independently from the templates that use it.

If you want the template to be able to change a color or style inside a component, that value needs to be exposed as a variable and mapped from the template.

## Component Canvas

In template designs, elements can extend beyond the canvas boundary. This is commonly used to hide part of an image — when templates render for end users, any elements outside the canvas are not visible.

However, with components, elements outside the canvas **will** be rendered when the component is used in a template. This can lead to unwanted results.

To avoid this, you should either [crop the image in Studio](GraFx-Studio/guides/cropping) or crop the underlying asset before importing it into Studio, so that it fits entirely within the component canvas.

## Design & Run Mode

Both Design Mode and Run Mode are available in the component workspace. Use Run Mode to test how variables and actions behave inside the component before placing it in a template.

When a component is placed inside a template, it always runs as a project — both in the template's Design Mode and Run Mode.

## Next step

Once your component is built, place it in a template:

[Use components in a template →](/GraFx-Studio/guides/use-components/)

## Passing an image into a component

Because each image variable is tied to a specific connector, image variables cannot be directly mapped between a template and a component — the template has no visibility into how the component's connector is configured. The solution is to pass the asset ID through a text variable and use Actions to apply it on each side.

**Both the template and the component must use the same connector.** The asset ID is only valid if both sides can resolve it through the same source.

### Set up the component side

In the component workspace, you need two variables and one Action:

1. An **Image** variable — for example, `Product Image` — connected to your connector, driving the image frame.
2. A **Single-line text** variable — for example, `ImageID` — this is the bridge that receives the asset ID from the template.
3. An Action with trigger **Variable value changed → ImageID**, and the following script:

```javascript
setVariableValue("Product Image", getTriggeredVariableValue());
```

When `ImageID` receives a new value through the mapping, this Action immediately applies it to the image variable.

### Set up the template side

For each component instance placed on the template, you need two variables and one Action:

1. An **Image** variable — for example, `ProductImage1` — connected to the same connector as the component. This is what the end user interacts with to pick an image.
2. A **Single-line text** variable — for example, `ProductImageID1` — this carries the asset ID to the component.
3. An Action with trigger **Variable value changed → ProductImage1**, and the following script:

```javascript
setVariableValue("ProductImageID1", getTriggeredVariableValue());
```

When the end user selects an image, the asset ID is written to `ProductImageID1` automatically.

### Map the variables

In the template, open **Manage mapping** for the component instance and map the component's `ImageID` to the template's `ProductImageID1`. Text-to-text mapping works without restriction.

### How it works at runtime

When an end user picks an image through `ProductImage1`, the template Action writes its asset ID to `ProductImageID1`. That value flows through the mapping into the component's `ImageID`. The component Action fires and sets `Product Image` to that ID — the correct image appears inside the component.

For templates with multiple instances of the same component, repeat the template-side variable pair and Action for each instance (`ProductImage2` / `ProductImageID2`, and so on), mapping each instance to its own ID variable.
