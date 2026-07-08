# Manage themes

Themes are managed on the Brand Kit detail page. See [Themes](/GraFx-Brand-Kits/concepts/themes/) for the concept.

## The theme bar

The top of the Brand Kit detail page shows the theme bar:

- A **back button**, returning to the overview of all Brand Kits.
- A **theme dropdown**, listing all themes of this Brand Kit. The default theme is marked **(Default)** and always listed first.
- A **manage icon**, opening the theme management panel.

Selecting a theme in the dropdown loads that theme, with all inherited and overridden values resolved.

## The theme management panel

Click the manage icon to open the **Brand Kit themes** panel. It has two sections:

- **Default theme** — the default theme. It can only be renamed.
- **Themes** — the list of additional themes. Each can be renamed or deleted, and the **+** icon adds a new theme.

### Add a theme

1. Click **+** next to the **Themes** section title.
2. Enter a name for the new theme.
3. Click **Add**.

The new theme is added to the list and inherits all elements from the default theme.

### Edit a theme

Select the theme in the dropdown and edit its elements as you would [edit a Brand Kit](/GraFx-Brand-Kits/guides/edit/). Changes are saved automatically:

- A value that **differs** from the default theme is stored as an override on the theme.
- A value **equal** to the default theme is not stored — the element keeps following the default.

!!! info "Good to know"
    - **The font list is shared across all themes** — by design, a theme does not add or remove fonts. Styles, however, can be overridden per theme to use a different font from the shared list.
    - **Structural changes** (adding, renaming, removing elements) are made on the default theme; other themes override values only.

### Rename or delete a theme

Use the rename and delete actions in the theme management panel. Deleting the theme you are currently viewing switches you back to the default theme.
