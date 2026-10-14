# Brand Kit descriptions for the Design Agent

A Brand Kit tells GraFx Studio *what* your brand elements are: a color named Primary, a paragraph style named Heading, a logo file. It does not say *when* to use them. That is what **descriptions** are for. Every color, media asset, paragraph style, character style and component in a Brand Kit can carry a short description, and the [Design Agent](/GraFx-Genie/design-agent/) reads those descriptions whenever it picks an element for a design or a change.

Descriptions are optional. Without them, the agent still works from the kit, guessing from names and properties. With them, it makes the choices your brand team would make: the right red for a price, the logo version for a dark background, the style meant for legal copy, the badge component for a promotion.

See [Elements](/GraFx-Brand-Kits/concepts/elements/#descriptions) for the concept, and [Edit a Brand Kit](/GraFx-Brand-Kits/guides/edit/) for the application itself.

## Where to add descriptions

Open the Brand Kit in **GraFx Brand Kits**. Each element type sits in its own card (Colors, Media, Fonts, Paragraph Styles, Character Styles, Components). Selecting an element shows its preview on the left and its name, properties and a **Description** text area on the right.

<!-- TODO Bram: screenshot of a color card with the description text area filled in -->

A few rules:

- Descriptions are edited on the **default theme**. On every other [theme](/GraFx-Brand-Kits/concepts/themes/), the description is shown read-only: a theme changes an element's value, not its purpose. The print variant of Primary is still the primary color.
- One description per element, shared by all themes.
- Templates that have the Brand Kit imported pick up new descriptions through Brand Kit [sync](/GraFx-Studio/guides/brandkits/#keep-a-brand-kit-in-sync). The agent reads the descriptions at the start of a session, so start a new chat after a kit update.
- Fonts do not carry a description; describe the use of a font through the paragraph and character styles that apply it.

Integrations can set the same `description` field through the Brand Kit endpoints of the Environment API.

## How the agent uses them

When the agent designs or changes something, it first gathers the brand context: the kit's colors, text styles, media, components and effects, each with its description. It then composes with that context, so "add a promo badge in the top-right corner" resolves to the component described as the promo badge, filled with the color described as the promo color, with the text style described for badge copy. When you ask "what logos are in the brand kit?", the reply quotes the descriptions.

Descriptions are also what makes an instruction such as "use the secondary palette for this layout" or "pick a lifestyle image that fits a breakfast promotion" work. The agent matches your words against the descriptions.

## Writing good descriptions

Write for a colleague who has never seen your brand guidelines and has thirty seconds. State the purpose, the context, and the restrictions. One to three sentences is plenty.

**Say when to use it, not what it is.** The agent can see that a color is red; it cannot see that red is reserved for prices.

| Weak | Better |
|---|---|
| `Red` | `Price and discount color. Use for price badges, "% off" callouts and sale headlines. Never for body copy or backgrounds.` |
| `Logo` | `Primary logo, full color, for light backgrounds. Minimum width 25 mm in print, 120 px digital. Keep clear space of one logo height around it.` |
| `Heading` | `Main headline style, one per page, maximum two lines. Use for the campaign message, not for product names.` |
| `Badge` | `Promo badge component for discounts. Use top-right of the product image when a product is on promotion. Map its Discount field to the template's discount variable.` |

**Include the alternatives.** If there is a light and a dark logo, say in each which one is for which background. If two colors are close, say which wins ("prefer Primary; use Primary Dark only for text on light backgrounds").

**Give numbers where the brand has them.** Minimum sizes, maximum line counts, margins, the ratio of image to copy. The agent measures what it places and can respect concrete limits.

**Mention the channel when it matters.** "Print only", "digital signage only", "social square formats".

**Keep names short and descriptions specific.** The name is what you will say in the chat ("use Accent"); the description is what the agent reasons with.

### Per element type

**Colors.** Role (primary, accent, background, text, price, legal), the pairings that are allowed, and what the color must not be used for. If the kit has a print theme with CMYK values, no need to mention it: themes handle that.

**Media.** What the asset shows and when it fits: "lifestyle image, family breakfast, use for dairy and bakery promotions"; "certification mark, place bottom-left on print layouts only". For logos, the background it is designed for and the clear space.

**Paragraph styles.** The kind of copy the style is for (headline, subhead, body, price, legal, caption), typical length, and position on the page.

**Character styles.** The emphasis the style carries ("highlight for the discount percentage inside a sentence", "product name in running text").

**Components.** What the component is for, where it goes, which of its fields map to which template variables, and when not to use it. Components do not have themes; they are added and described on the default theme.

## Example: a grocery retail kit

A compact set of descriptions that lets the agent build promotional material unattended:

- **Colors**: `Fresh Green` — brand color, backgrounds of headers and footers, never for text smaller than 24 pt. `Price Red` — prices, discount badges, sale callouts only. `Ink` — all body and legal copy. `Paper` — page backgrounds and text on Fresh Green.
- **Media**: `Logo on light` — default logo for white or Paper backgrounds. `Logo on green` — logo for Fresh Green backgrounds. `Lifestyle – breakfast`, `Lifestyle – barbecue`, `Lifestyle – dinner` — full-bleed background photography; pick by the products in the promotion.
- **Paragraph styles**: `Headline` — campaign message, top of the page, max two lines. `Product name` — inside promo slots. `Price` — price in a promo slot, right-aligned. `Legal` — disclaimer, bottom of the page, 7 pt in print.
- **Components**: `Promo slot` — one product with image, name, old price, new price; place in a grid, map Product, Old price, New price to the template's data variables. `Discount badge` — rotated badge for "% off"; top-right of a promo slot, only when a discount applies.

With this in place, "create a leaflet page with five promo slots, a breakfast lifestyle image in the background, a headline at the top and a footer with the disclaimer" is enough for the agent to produce a page that looks like the brand.

## Related

- [Prepare your template](/GraFx-Genie/design-agent/template-setup/): everything else the agent reads.
- [Custom skills](/GraFx-Genie/design-agent/skills/): rules that go beyond a single element, such as how layouts for a campaign are built.
- [Brand Kit elements](/GraFx-Brand-Kits/concepts/elements/) and [themes](/GraFx-Brand-Kits/concepts/themes/).
