# Rich text variables

A rich text variable takes text that already carries its own markup — for example `<h1>Title</h1><p>Body with <b>bold</b> words</p>` from a product information management (PIM) system, a content management system (CMS) or a data feed — and formats it with the paragraph and character styles of your template.

The tags themselves never show on the canvas. A set of **rich text import rules** decides what each tag becomes: a paragraph style, a character style, a line break, or an inline format such as underline.

This makes rich text variables the right choice when the formatting is decided upstream, in the system that supplies the content, and the template only has to translate it into on-brand styling.

!!! info "Rich text vs multi-line text"
    A [multi-line text variable](/GraFx-Studio/guides/template-variables/multi-line-text/) holds plain text: whatever comes in is shown as-is. A rich text variable reads the markup in its value and applies styling to it.

## How it fits together

There are two parts:

1. **Rich text import rules** — defined once per environment, in GraFx Studio on the platform. A rule set maps tags (and, optionally, their attributes) to styles.
2. **The rich text variable** — defined in the template. You assign one rule set to it. Whenever the variable receives a value, the rules are applied.

The rules refer to styles **by name**. The paragraph and character styles themselves live in the template or its [Brand Kit](/GraFx-Studio/guides/brandkits/). That means the same rule set can serve several templates, and switching a Brand Kit theme restyles the content without touching the rules.

## Set up rich text import rules

<!-- TODO Bram: confirm the exact menu path and add screenshots (rule set list, rule set details with a few rules, Import structure from Brand Kit modal). Zeplin/Figma refs on GRAFX-5982, GRAFX-5985, GRAFX-5991. -->

In your environment, open **GraFx Studio** and go to **Rich text import rules**, next to **User interfaces**.

Rich text import rules use the same roles and permissions as Brand Kits.

### Create a rule set

Click **Create rule set** and give it a name. Names are unique within the environment; if the name is already taken, a number is added.

A new rule set starts with one rule: a **Linebreak** for the `br` element. Remove it if you don't need it.

From the list of rule sets you can **Edit**, **Rename** or **Delete** a rule set. Changes are saved automatically as you edit — there is no Save button.

### Add rules

Click **Add rule**. Each rule is one row:

| Field | What it does |
|---|---|
| **Apply style** | What the matched element becomes: **Paragraph style**, **Character style**, **Linebreak**, **Underline**, **Subscript**, **Superscript** or **Strikethrough** |
| **With style name** | The name of the paragraph or character style to apply. Only used for **Paragraph style** and **Character style** |
| **When element is** | The tag name to match, without angle brackets — for example `h1`, `span` or `strong` |

You decide the tag names. They don't have to be HTML: if your source system writes `<headline>` or `<price>`, use those names in your rules.

The elements `p`, `ol`, `ul` and `li` are reserved for paragraphs. A rule for one of them always applies a **Paragraph style**.

### Match on attributes

Under a rule, click **Add attribute** to narrow it down to elements that carry a specific attribute:

| Field | What it does |
|---|---|
| **With attribute** | The attribute name, for example `class` or `data-highlight` |
| **Value** | The value the attribute must have, for example `intro` |

A few things to know about attribute matching:

- When a rule has several attributes, **all of them** must match.
- Matching is not case-sensitive, for both tag names and attribute values.
- An attribute with an empty **Value** also matches an attribute written without a value, such as `<p enabled>`.
- Attributes are not inherited: an attribute on a parent element doesn't count for the elements inside it.

### Import the structure from a Brand Kit

Instead of typing every style name, click **Import structure from Brand Kit** and choose a Brand Kit. GraFx Studio adds a rule for each paragraph style and character style in that Brand Kit, with **Apply style** and **With style name** already filled in. You then only add the element names (and attributes, where needed).

Importing never removes rules or attributes you added yourself.

### Example rule set

| Apply style | With style name | When element is | Attribute |
|---|---|---|---|
| Paragraph style | Title | `h1` | |
| Paragraph style | Subtitle | `h2` | |
| Paragraph style | Body | `p` | |
| Paragraph style | Intro | `p` | `class` = `intro` |
| Character style | Highlight | `span` | `class` = `green` |
| Character style | Bold | `strong` | |
| Linebreak | - | `br` | |
| Underline | - | `u` | |
| Strikethrough | - | `s` | |
| Subscript | - | `sub` | |
| Superscript | - | `sup` | |

## Create a rich text variable

Under the Automate icon, click Variables, and add a variable with the "+" sign — the same way as [any other template variable](/GraFx-Studio/guides/template-variables/define/).

Choose **Rich text** as the **Variable type**.

### Assign a rule set

In the **General** tab, the **Rich text import rules** section has a dropdown with the rule sets of your environment. Pick the one this variable should use.

- If the environment has no rule sets yet, the dropdown is empty.
- If the assigned rule set is renamed on the platform, it stays assigned.
- If the assigned rule set is deleted, the dropdown returns to its empty state.

### General properties

- **Required**
- **Remove paragraph if empty** — removes the paragraph that holds the variable when the variable has no value
- [Private data](/GraFx-Studio/concepts/private-data/)

Once a rich text variable is placed in a text frame, its type can no longer be changed.

### Place it in a text frame

Insert the variable into a text frame like any other text variable. See [How to work with template variables](/GraFx-Studio/guides/template-variables/assign/#insert-template-variable-in-a-text-frame).

## Where the value comes from

A rich text variable is filled by automation, not typed in by the end user:

- A [data connector](/GraFx-Studio/concepts/connectors-data/)
- A [data source variable](/GraFx-Studio/guides/template-variables/data-source/) column, for a rich text variable inside a component (see [below](#rich-text-variables-in-components))
- An [Action](/GraFx-Studio/concepts/actions/), with `setVariableValue`
- An integration, through the [GraFx Studio SDK](https://github.com/chili-publish/studio-sdk)

The rules are loaded when a template or project opens, in the Template Designer, Run mode and Studio UI alike. Changes to a rule set show up the next time the template or project is opened.

!!! tip "Reading the value in an Action"
    `getVariableValue` on a rich text variable returns the plain text, without tags or styles.

## How the value is formatted

### Elements with a matching rule

Each element is formatted by the rule that matches it. When more than one rule matches the same element, the rule with the most matches wins — so a rule for `p` with `class` = `intro` beats a plain rule for `p`.

Elements can be nested. With nested character styles, the innermost one wins.

### Elements without a rule

An element that has no matching rule is ignored: its tags are removed and its text is kept. That also applies to `p` — without a rule for `p`, no new paragraph is started.

If a rule points to a style name that doesn't exist in the template, the text is shown without that style.

### Line breaks

- A line break rule needs a closed tag: write `<br />` or `<br></br>`, not `<br>`. The same applies to your own line break elements, such as `<lb />`.
- A single newline (`\n` or `\r\n`) in the value is a line break within the paragraph.
- A double newline (`\n\n` or `\r\n\r\n`) starts a new paragraph.

### Malformed markup

Tags must be properly closed and nested. A value with an unclosed or mismatched tag — for example `<p>Paragraph A` without `</p>` — is rejected with an error.

Script tags, HTML comments and event attributes such as `onclick` are never executed. Their tags are ignored like any other element without a rule.

### Styles and the surrounding text

A rich text variable doesn't affect the text around it:

- Styles that are active **before** the variable stay active for the variable.
- Styles the variable applies stay **inside** the variable. After the variable, the text continues with the style it had before.

Paragraph and character styles from the rules take precedence over the styles on the surrounding text. Inline formatting that you apply to the variable in the text frame overrides the rules, except for horizontal alignment.

The first paragraph of the variable belongs to the paragraph the variable is placed in, so it takes that paragraph's alignment and paragraph settings. To give the first paragraph its own paragraph style, place the variable in a paragraph of its own.

### Works with

Rich text variables work together with [copyfitting](/GraFx-Studio/guides/text-frame/#copyfitting), auto-grow, multiple columns, text constraints, drop shadow, opacity, blend modes and overprint, and with switching a Brand Kit theme through an Action.

## Rich text variables in components

A component can contain rich text variables, and its rule sets are applied inside the component as well.

When you [map the component](/GraFx-Studio/guides/use-components/#variable-mapping), a component rich text variable can be mapped to:

- A **new variable** — GraFx Studio creates a **Multi-line text** template variable
- An existing **Single-line text** or **Multi-line text** template variable
- A text column of a [data source variable](/GraFx-Studio/guides/template-variables/data-source/)

Mapping to a template rich text variable isn't available.

## Example

With the rule set from the [example above](#example-rule-set), this value:

```html
<h1>Summer collection</h1><p class="intro">Light fabrics, bright colors.</p><p>Now with <span class="green">free shipping</span> on orders over €50.<br />H<sub>2</sub>O-resistant finish.</p>
```

is shown as a paragraph in the **Title** style, a paragraph in the **Intro** style, and a paragraph in the **Body** style with "free shipping" in the **Highlight** character style, a line break, and a subscript 2.

## For developers

The variable type in the SDK and the document JSON is `richText`. The assigned rule set is stored as `ruleSetId`.

- Assign a rule set: `setRuleSetId` on the variable controller
- Set a value: `setVariableValue`, with the tagged text as a string

Rule sets are read from the Environment API. To let an integration read them, give it the **Rich text import rules** scope.

See the [GraFx Studio SDK](https://github.com/chili-publish/studio-sdk) for the full reference.
