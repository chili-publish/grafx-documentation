
# GraFx Brand Kits

![applogo](/assets/GraFxBrandKitsLogo.svg)

GraFx Brand Kits lets you define and manage your organization’s visual identity in one place. 

Once you’ve set up a Brand Kit, template designers and end users can apply its colors, fonts, images and styles directly in GraFx Studio, ensuring every output stays on-brand and speeding up template creation

---

## Application overview

When you open the GraFx Brand Kits app (via the left-hand nav in the GraFx Platform), you’ll see:

1. **Toolbar**  
   – **Create Brand Kit** button  
   – Search & sort by name  

2. **Brand Kit cards**  
   – Each card shows the kit’s name, description and thumbnail  
   – Click a card to open its details  

![brand-kits-list](path/to/brandkits-list.png)

---

## Core concepts

### Brand Kit  
A container of design tokens and assets (colours, fonts, media, paragraph & character styles) that define your visual identity.  

- Defined at the **environment** level  
- Always has a single editable “Default” theme  
- Themes beyond the default are **not** in scope for today’s release

### Elements  
Within each Brand Kit you can manage:

| Element               | Description                                              |
|-----------------------|----------------------------------------------------------|
| **Colours**           | Named swatches (e.g. Primary, Secondary) in RGB/CMYK     |
| **Fonts**             | OpenType/TrueType fonts to use in GraFx Studio templates |
| **Media**             | Logos or other image assets                              |
| **Paragraph styles**  | Font, size, spacing, alignment for paragraphs            |
| **Character styles**  | Font, size, formatting for inline text                   |

Whenever you **add** or **remove** an element in the Default theme, that change automatically applies to all other themes in the Brand Kit (so structure stays in sync).

---

## How-to

### Create a Brand Kit

1. Navigate to **GraFx Brand Kits** in the platform sidebar.  
2. Click **+ Create Brand Kit**.  
3. Enter a **Name** and an optional **Description**.  
4. Click **Save**.  

You’ll be taken to the new Brand Kit’s detail page, where you can begin adding elements.

---

### Update a Brand Kit

On the Brand Kit detail page:

1. **Add an element**  
   - Click the “+” next to Colours, Fonts, Media, Paragraph styles or Character styles.  
   - Fill in the required fields (e.g. colour value, font family).  
   - Click **Save**.

2. **Edit an element**  
   - Hover over an existing element and click **Edit**.  
   - Make your changes (e.g. adjust a colour’s CMYK values).  
   - Click **Save**.

3. **Remove an element**  
   - Hover over the element and click the **trash** icon.  
   - Confirm deletion.

> **Note:** Removing or renaming an element in the Default theme immediately removes or renames it in every theme—so that templates always map to the same set of element labels.

---

That’s it! You now have a Brand Kit in place. In the next section we’ll show you how to use it in GraFx Studio.