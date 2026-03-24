# Use components in a template

This guide explains how to place components on a template canvas, configure how they fill their frame, and map their variables to template variables.

See [Components](/GraFx-Studio/concepts/components/) for an introduction, or [Build a component](/GraFx-Studio/guides/build-component/) to create one first. New to components? Start with the [tutorial](/GraFx-Studio/guides/components-tutorial/) for a full end-to-end walkthrough.

## Place a component

Open the template in the Template Designer Workspace. In the left toolbar, click the **Resources** icon at the bottom.

![Resources icon in the left toolbar of the template workspace](resources-icon.png)

The Resources panel opens. Select **Components**.

![Resources panel with Components highlighted](resources-components.png)

The component browser opens, showing all available components. Use the search field to find a component by name.

![Component browser with search results showing Component-Price](component-browser-search.png)

Click a component to place it on the canvas. The component is placed as a frame at the center of the active layout.

> **Placement rules:** The component is placed at the center of the canvas. If the component's default size is larger than the current layout, it is scaled down to fit within the layout boundaries.

## Multiple instances

You can place the same component multiple times on the same page. Each placement is an independent instance with its own position, size, and variable mapping.

![Three instances of the same pricing component placed on a template canvas](component-multiple-instances.png)

This is the basis for use cases like a coupon sheet (same pricing component, once per coupon) or a leaflet page (same product ad component, once per product).

## Resize Mode

A component can have multiple layouts — for example a square, horizontal, and vertical version of the same design. The **Resize Mode** setting controls how the component fills the frame you've placed it in, and which internal layout is used.

With a component frame selected, find the **Resize Mode** section in the right properties panel.

![Resize Mode dropdown in the properties panel with three options](resize-mode-dropdown.png)

### Scale

The component looks at the size of the frame and automatically **switches to the internal layout whose aspect ratio best matches**. It scales to fill the shortest dimension, preserving the aspect ratio. Any remaining space on the longer dimension appears as white space.

Use Scale when you want the component to always present the most appropriate layout for the frame shape — without distorting the design.

### Resize

The component **stretches to fill the entire frame** by applying the anchoring, copyfitting, and autogrow rules configured inside the component. No layout switching occurs — the component uses its current layout and adapts its contents to the frame size.

Use Resize when the component's internal layout is flexible enough to fill any frame size gracefully.

### Scale and resize

Combines both modes: the component first selects the best-matching layout (Scale), then applies the internal resize rules to eliminate any remaining white space (Resize).

Use Scale and resize when you want automatic layout selection **and** a clean fill of the frame with no white space.

![Three component instances showing Scale, Resize, and Scale and resize behavior](resize-mode-comparison.png)

## Variable mapping

Variable mapping is how you connect the component's variables to variables at the template level. This is what allows each component instance to show different data — even when it's the same component placed multiple times on the same page.

### Open the mapping modal

Select a component frame on the canvas. In the right properties panel, find the **Component Variables** section and click **Manage mapping**.

![Component Variables section in the properties panel with Manage mapping button](manage-mapping-button.png)

The **Map component elements to variables** modal opens.

![Map component elements to variables modal with Not mapped and Mapped tabs](mapping-modal.png)

### The mapping modal

The modal has two tabs:

- **Not mapped** — component variables that are not yet connected to a template variable
- **Mapped** — component variables that have already been connected

Each row shows:

- **Component element** — the variable defined in the component, with its type icon
- **Map to** — how the connection is made: to a new variable or an existing one
- **Variable** — the template variable that will receive or supply the value

### Map to a new variable

If the template does not yet have matching variables, set **Map to** to **New variable**. GraFx Studio creates a new template variable for each component variable, named automatically based on the component variable name.

The summary at the bottom of the modal shows how many mappings will be created and how many new variables will be added. Click **Apply** to confirm.

![Mapping modal showing two component variables mapped to new variables](mapping-new-variables.png)

### Map to an existing variable

If the template already has variables — for example because another instance of the same component was already mapped — set **Map to** to **Variable** and choose the existing template variable from the dropdown.

This is also how you connect two component instances to the **same** template variable, if you want them to always show the same value.

![Map to dropdown expanded showing New variable and Variable options](mapping-existing-variable.png)

### Per-instance mapping

Each component instance on the canvas has its own mapping configuration. A template with three price tag components on one page can map each to a completely different set of template variables — `price_1`, `price_2`, `price_3` — so each coupon shows its own price independently.

### Mapped variables in the variable list

After applying the mapping, the new template variables appear in the variable list under a **Component** group, named after the component instance.

![Variable list showing Component group with mapped variables](variable-list-component-group.png)

These variables work like any other template variable — they can be used in actions, exposed in Studio UI, or driven by a data source.

## Reset a mapping

To remove all mappings for a component instance, open **Manage mapping** and click **Reset**. This clears all connections without deleting the template variables that were created.
