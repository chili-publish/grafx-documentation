# Tutorial: The Default Template

This tutorial introduces the **Default Template** — a template (plus a supporting component) that is automatically deployed to every new CHILI GraFx environment. It is designed to do two things: give you a ready-made starting point that can output almost anything you'll typically need, and serve as a worked example you can take apart and learn from when you start building your own templates.

**What you'll learn:**

- How the Default Template and its component are structured
- Why the component exists and what it's responsible for
- The different layout types inside the template — basis, animated, and print — and when each one is used
- How layout inheritance ties everything together
- How to safely make changes without breaking the rest of the template

**Before you start:** You should be comfortable with the basics of the Template Designer Workspace and have a working understanding of [Layouts](/GraFx-Studio/concepts/layouts/), [Components](/GraFx-Studio/guides/use-components/), and [Variables](/GraFx-Studio/concepts/variables/).

---

## Step 1 — Structure of the setup

<!-- High-level walkthrough of what actually ships in a new environment:
     - The Default Template itself (where to find it, how it's named)
     - The supporting component (name, purpose at a glance)
     - How the two relate — template uses component, component lives separately
     - A visual of the project/asset structure would go well here. -->

*To do: describe the files/assets that are deployed, where to find them in GraFx Studio, and how the template and component relate to each other.*

---

## Step 2 — Purpose of the component

<!-- Why does the Default Template rely on a component rather than putting
     everything inline?
     - What the component encapsulates (shared design, reusable pieces)
     - What it exposes as variables vs. what it keeps internal
     - Why this separation makes the template easier to maintain and extend -->

*To do: explain what the component is for, what it contains, and why it's separated from the template.*

---

## Step 3 — The different layouts

The Default Template ships with three categories of layouts. Each category is tuned for a specific type of output, and together they cover almost every format a typical brand needs.

### Basis layouts

<!-- The foundation layouts that everything else inherits from.
     - What sizes/formats are included
     - What "basis" means in this context (the common parent for other layouts)
     - Which properties are defined here and inherited downstream -->

*To do: describe the basis layouts — what they define, and why they sit at the top of the hierarchy.*

### Animated layouts

<!-- Layouts intended for animated output (MP4, GIF, HTML).
     - Which formats/aspect ratios are covered
     - How animation is configured at the layout level
     - What's inherited from the basis layouts and what's overridden -->

*To do: describe the animated layouts — formats, sizes, and how they differ from the basis layouts.*

### Print layouts

<!-- Layouts intended for print output (PDF).
     - Which formats are covered (A4, letter, poster sizes, etc.)
     - Print-specific settings (bleed, crop marks, color management)
     - What's inherited from the basis layouts and what's overridden -->

*To do: describe the print layouts — formats, sizes, and the print-specific settings they carry.*

---

## Step 4 — Inheritance

<!-- How layout inheritance works in the Default Template specifically.
     - Diagram/illustration of the inheritance tree would help here
     - Which properties flow from basis → animated / print layouts
     - When an override on a child layout breaks the link to the parent
     - Why this structure makes the template flexible without duplicating work
     Link to the general Layouts concept page: /GraFx-Studio/concepts/layouts/ -->

*To do: explain the inheritance tree of the Default Template, and how a change at the basis level propagates down.*

---

## Step 5 — How to make changes

<!-- Practical guidance on modifying the Default Template safely.
     - When to edit the component vs. the template
     - When to edit a basis layout vs. a specific animated/print layout
     - What to watch out for (breaking inheritance, overriding shared styles)
     - Recommended workflow: duplicate first, then experiment
     - How to reset or re-deploy the Default Template if things go wrong -->

*To do: give a clear, opinionated recipe for making changes — what to edit where, and how to avoid breaking inheritance.*

---

## Next steps

<!-- Suggested follow-ups once the reader has worked through this tutorial.
     Candidates:
     - Build your own component: /GraFx-Studio/tutorials/components-tutorial/
     - Deep-dive on layouts: /GraFx-Studio/concepts/layouts/
     - Output guides: /GraFx-Studio/guides/output/pdf/, /mp4/, /gif/, /html/, /image/ -->

*To do: link to related tutorials, guides, or concept pages the reader should explore next.*
