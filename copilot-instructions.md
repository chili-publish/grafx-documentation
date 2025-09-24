# GitHub Copilot Instructions for CHILI GraFx Documentation

This document provides guidelines for GitHub Copilot when reviewing and assisting with the CHILI GraFx documentation repository. It ensures consistency with the official Documentation Project Instructions.

---

## Project Overview

This is a technical documentation site for CHILI GraFx products, built with MkDocs Material. The documentation covers GraFx Studio, GraFx Publisher, GraFx Media, GraFx Fonts, GraFx Brand Kits, and Developer resources.

---

## Language & Style Guidelines

### Language
- **Primary language**: English (US)
- **Tone**: Neutral, concise, practical  
  - Avoid marketing language.  
  - Do not make roadmap promises or speculate on future features.  
- **Audience**: Developers, Template Designers, administrators, technical users  
- Always write in **second person** (“you”) and **active voice**.

### Spelling & Grammar
- Use US English spelling (`color`, `center`).  
- Correct typos and grammar.  
- Use consistent terminology across all docs.

---

## Terminology & Product Names

### CHILI GraFx product names
- **CHILI GraFx** (platform)  
- **GraFx Studio**  
- **GraFx Publisher**  
- **GraFx Media**  
- **GraFx Fonts**  
- **GraFx Brand Kits**  

❌ Never use: *GraFX*, *Grafx*, *Graphics Studio*, etc.

### Key terms
- **Smart Templates** (capitalized)  
- **Template Designer** (capitalized)  
- **End users** (two words, no hyphen)  

### Technical terms
- Use:  
  - `multichannel` (no hyphen)  
  - `self-service`  
  - `real-time`  
  - `end-to-end`  
  - `plug-and-play`  

### Trademark usage
- First mention must include ® where required (e.g., Adobe® InDesign®).  

---

## File & Directory Structure

- Use **kebab-case** for directory names (`grafx-studio`, `brand-kits`).  
- Follow hierarchy: `docs/[product]/[section]/[subsection]/index.md`.  
- All documentation pages should be named **`index.md`**.  
- Descriptive directory names indicate content.  

---

## Markdown Standards

### Headers
- `#` for main title, `##` for sections, `###` for subsections.  
- Maintain proper hierarchy (don’t skip levels).  

### Links
- Use **relative paths**.  
- **Do not include `.md` extensions** in internal links.  
- Use descriptive link text.  

### Images
- Use this format only:  
~~~markdown
![Alt text](image.png){.screenshot}
![Alt text](image.png){.screenshot-full}
~~~
- Always include descriptive alt text.  

### Code Blocks
- Use fenced code blocks with language identifiers **when it adds clarity**.  
- Ensure examples are complete and functional.  
- Add comments only for complex code.  

### Admonitions
- Use MkDocs Material admonitions with short bodies:  
  - `!!! note` `|` `tip` `|` `warning` `|` `info`

---

## Content Patterns

### Concept Pages
- Define terms and explain why they matter.  
- Provide context, relationships, constraints.  
- No step-by-step instructions.  
- Link to related guides.  

### Guides (How-to)
- Provide step-by-step instructions.  
- Add screenshots where useful.  

### Release Notes
- Always include frontmatter:
~~~yaml
---
draft: false
date: YYYY-MM-DD
categories:
  - Releases
---
~~~
- Categories:  
  - `Releases`  
  - `Operational updates` (downtime, planned changes, behavioral updates)  
- Title: short, descriptive (emoji optional).  
- Version label:  
~~~markdown
![rn_icon](/assets/icon-GraFx-Studio.svg) <span class="version-label">vX.YY</span>
~~~
- Sections:  
  - `## ✨ New & Improved`  
  - `## 🛠️ What's Fixed`  
- Subdivide by product when needed.  
- Bullet points: short, start with action verbs.  
- Add screenshots with alt text and proper formatting.  
- Link to related guides or concept pages using relative links.  

---

## Quality Checks

Before committing:
1. Run spell check.  
2. Verify all internal and external links work.  
3. Confirm all images load, follow `.screenshot` formatting, and have alt text.  
4. Check terminology consistency (product names, hyphens, casing).  
5. Ensure code examples are valid and add clarity.  
6. Confirm release notes use correct structure.  

---

## MkDocs Specific Rules

- Ensure all pages are listed in `mkdocs.yml`.  
- Match page titles with navigation labels.  
- Keep consistent indentation in navigation.  
- Use Material for MkDocs components and icons.  
- Be aware of blog plugin for release notes, redirects plugin for moved content, and RSS implications.  

---

## Best Practices

1. Test changes locally before committing.  
2. Use descriptive commit messages.  
3. Keep screenshots current and relevant.  
4. Provide context for technical concepts.  
5. Link to related content.  
6. Use outcome-oriented headings for clarity.  
7. Apply reader-first techniques (e.g., trigger → action → result, contrast, outcome-first).  

---

## Resources

- MkDocs Material Documentation: https://squidfunk.github.io/mkdocs-material/  
- CHILI GraFx Documentation Site: https://docs.chiligrafx.com/  
- CHILI publish Website: https://www.chili-publish.com/  
