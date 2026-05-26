# Recipe vs Cookbook

A smart template holds **one set of content** and **many layouts**. The content — product name, price, image, legal line — is the single source of truth, and each layout is one way of presenting it. Content flows into layouts; layouts never write back. A layout decides **how** something looks, never **what** the content is.

## One recipe, many cookbooks

A chef writes **one recipe** — the ingredients, the quantities, the steps. The same recipe appears in a glossy cookbook spread, a magazine sidebar, a 4×6 recipe card, and a cooking app. The presentation differs completely. The recipe does not.

Each outlet decides photo or no photo, one column or two, big type or small. What none gets to do is **change the recipe itself**. A cookbook can't quietly swap butter for margarine because the column was tight — the moment it does, it isn't presenting the recipe anymore; it's publishing a different dish.
| Cookbook world | Smart template |
|---|---|
| The recipe — ingredients, quantities, steps | The content — the single source of truth |
| Each cookbook, card, magazine, app | Each layout in the smart template |
| Photo or no photo, column width, type size | Layout decisions — presentation only |
| Swapping an ingredient to fit the column | A layout editing the content — **forbidden** |

Scaling a recipe from four servings to eight adjusts every quantity, but the recipe still defines the relationships. That's the recipe responding to a presentation choice — not the cookbook rewriting the ingredients. Layouts may adapt; content may be designed to flex. Adaptation is the content responding, never a layout overwriting the source.

## One model, one design system

The logic above only holds while you're describing the same kind of content. A book's **metadata** — ISBN, format, page count, cover image, price — is a different kind of content; its bookstore listing, library record, and retailer product page are layouts of *that* model, not the recipe. Two different kinds of content shouldn't share one design system.

> **One kind of content → one design system, with as many layouts as you need.**
> **A different kind of content → a new design system.**

## What goes wrong when a layout edits content

A product name doesn't fit, so you shorten it. The layout in front of you looks fine — but the layouts now disagree with each other, you can't trust any single one, and content updates at the source stop propagating cleanly. The system breaks silently.

## The rule of thumb

> If the content is wrong, fix the content — never the layout that displays it.

## What's legitimate, and what isn't

Legitimate — change freely inside a layout:

- Position, size, rotation, font, colour, alignment
- Whether an element is shown or hidden
- Image crop and frame proportions
- Adapting to a different format or channel

Forbidden — never inside a layout:

- Changing the actual product name, price, or copy
- Editing or removing legal text and disclaimers
- Replacing an image to "make it work"
- Anything that makes this layout disagree with the others

When a layout wants to do something in the second list, fix the content. Every layout will follow.
