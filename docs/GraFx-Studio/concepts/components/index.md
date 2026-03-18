# Components

A Component is a reusable design element that can be placed inside a template. Think of it as a self-contained building block — with its own layout, brand rules, and business logic — that you design once and reuse across as many templates as you need.

![Components in GraFx Studio navigation](components-nav.png)

## Why components

In traditional template design, every template carries its own copy of every design element. A pricing block, a product badge, a promotional label — each one is rebuilt and maintained independently per template. When the brand updates the look or the business logic of that element, every template needs to be opened and updated manually.

Components change that. You build the design element once, as a component. Every template that uses it references that single source. When the component is updated, the change flows through to every template automatically.

This means:

- **Faster template design** — place a component rather than rebuilding the same element from scratch
- **Consistent brand execution** — the logic and look live in one place, not duplicated across dozens of templates
- **Faster campaign rollouts** — HQ updates the component once, field teams immediately work with the latest version

## How components relate to templates

A Component is a separate resource in GraFx Studio, alongside Templates and Collections. It has its own workspace, its own variables, and its own Brand Kit.

When a template designer places a component on a template, it behaves like a frame — it can be moved, resized, and positioned on the canvas. The component's internal design and logic remain managed within the component itself.

Data flows **one-way**: from the template into the component. The template can pass values to component variables, but a component cannot send data back to the template.

![Components overview — grid of available components](components-overview.png)

## Use cases

### Pricing element on a coupon sheet

A grocery retailer runs weekly promotions. Each coupon on a coupon sheet shows a product image, a product name, and a price — with the price element varying depending on the promotion type: *reduced price*, *two for one*, or *lowest price guarantee*. Each promotion type has a slightly different visual treatment.

Without components, that pricing logic needs to be built into every coupon on every template. With a pricing component:

1. The pricing element is designed once as a component, with all promo type logic built in
2. The component is placed once per coupon on the sheet
3. Each instance is mapped to the price and promo type variables for that specific coupon
4. When the brand updates the look or adds a new promo type, only the component needs to change — all templates using it update automatically

A coupon sheet with six coupons uses the same pricing component six times, each showing different data.

### Full product ad on a leaflet page

A retail leaflet page contains multiple product advertisements. Each ad has a header, a product shot, a product name, a price, and a promo type. Rather than building each ad as a standalone section of the template, the entire ad is a component.

The template designer places the ad component as many times as needed on the page, then maps each instance to the relevant product's variables. The result is a complete leaflet page built from one reusable design, driven by variable data.

When the brand updates the ad design or changes the business logic, the update is made once in the component. All leaflet templates immediately reflect the change — without field teams or store owners needing to do anything.

## Component variables

Each component exposes its own set of variables. These are the values a template designer can connect to template-level variables through [variable mapping](/GraFx-Studio/guides/use-components/#variable-mapping).

Variable mapping is done per component instance. This means the same component placed three times on a page can carry three completely different sets of values — one per instance.

See [Variable mapping](/GraFx-Studio/guides/use-components/#variable-mapping) for the full workflow.

## Resize mode

A component can have multiple layouts — for example a square, a horizontal, and a vertical version of the same design. When a component is placed on a template, the **Resize Mode** setting controls how the component fills its frame and which internal layout is used.

See [Resize mode](/GraFx-Studio/guides/use-components/#resize-mode) for details on Scale, Resize, and Scale and resize.

## Differences from templates

Components are intentionally more constrained than templates. The focus for components is on print and PDF output, as a component is always an ingredient of a template — not a final product in itself.

| Feature | Template | Component |
|---|---|---|
| Digital animated intent | ✅ | ❌ |
| Multi-page | ✅ | ❌ |
| Output / Export | ✅ | ❌ |
| User Interface settings | ✅ | ❌ |
| Bleed & slug | ✅ | ❌ |
| Private data | ✅ | ❌ |
| List variable type | ✅ | ❌ |
| Nesting (components inside components) | ✅ | ❌ |
| Brand Kit | ✅ | ✅ |
| Actions | ✅ | ✅ |
| Connectors (media & data) | ✅ | ✅ |
| Design & Run mode | ✅ | ✅ |

## Get started

- [Build a component](/GraFx-Studio/guides/build-component/) — create a component in the component workspace
- [Use components in a template](/GraFx-Studio/guides/use-components/) — place, configure, and map component variables
