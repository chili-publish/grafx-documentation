# CLAUDE.md — CHILI GraFx documentation project

Read this file at the start of each session to restore working context.

---

## Project

**Site:** docs.chiligrafx.com — MkDocs Material, hosted on Azure Static Web Apps.
**Repo root:** `/sessions/youthful-amazing-galileo/mnt/grafx-documentation`
**Config:** `mkdocs.yml` — nav, plugins, markdown extensions.
**Hooks:** `hooks.py` — post-build processing for `llms.txt` and `llms-full.txt`.

---

## Active branches

| Branch | Purpose | Status |
|---|---|---|
| `grafx-studio/components` | Components documentation (concept, guides, tutorial, release note) | Open — needs PR |
| `feature/llms-txt` | llms.txt optimisation (prospect/procurement sections, marketing language, site_description update) | Open — needs PR |

**Current branch is likely `grafx-studio/components`.** Always check with `git branch` before starting work.

---

## MCP tools

| Tool | Use for |
|---|---|
| `chili-docs` | Search existing documentation — verify terminology, capitalisation, naming conventions |
| `chili-content` | Search CHILI marketing content — align language, check approved terms |

Always run a `chili-docs` search before introducing new terminology or product names.

---

## Terminology rules

These were established through `chili-docs` searches and explicit decisions — do not deviate without checking:

| Use | Not |
|---|---|
| Design Mode | Design mode |
| Run Mode | Run mode |
| Resize Mode | Resize mode |
| Template Designer Workspace | template designer workspace / designer workspace |
| Brand Kit | brand kit |
| Design & Run Mode | Design & Run mode |
| multichannel | omnichannel |
| design automation platform | creative automation platform |
| Design Systems (in llms.txt descriptions) | Smart Templates |
| GraFx Studio | GraFx studio |

---

## Components documentation (grafx-studio/components)

### Files created or modified

| File | Type | Notes |
|---|---|---|
| `docs/GraFx-Studio/concepts/components/index.md` | Concept | What components are, when to use, lifecycle/update behaviour, use cases |
| `docs/GraFx-Studio/concepts/component-mapping/index.md` | Concept | Variable mapping patterns — scenario-driven, Mermaid diagrams as collapsible support |
| `docs/GraFx-Studio/concepts/components-strategy/index.md` | Concept | Design studio manager perspective — production-to-assembly shift, investment model, governance |
| `docs/GraFx-Studio/guides/build-component/index.md` | Guide | Component workspace, restrictions (with reasons), layouts, variables, Brand Kit, Design & Run Mode |
| `docs/GraFx-Studio/guides/use-components/index.md` | Guide | Place, Resize Mode (Scale / Resize / Scale and resize), variable mapping workflow |
| `docs/GraFx-Studio/guides/components-tutorial/index.md` | Tutorial | End-to-end: build a pricing component → place twice in coupon sheet → map variables |
| `docs/release-notes/releaseposts/2026031901.md` | Release note | March 19 2026, Components for GraFx Studio — **version number missing, fill before publish** |
| `docs/index.md` | Home page | Mar 19 entry added at top of Latest updates |
| `mkdocs.yml` | Nav | Components entries in Concepts, How to: Design (Build + Use), new Tutorials section |

### Nav additions in mkdocs.yml

```
Concepts:
  - Components
  - Components - Variable mapping
  - Components - Studio strategy

How to: Design:
  - Components - Build
  - Components - Use

Tutorials:                          ← new section, below last How to block
  - Components: Build a pricing component
```

### Pending before PR

- [ ] **Version number** in `2026031901.md` — not available from Jira, needs to be filled in
- [ ] **Screenshots** — 17 placeholder images across the three main pages (concept, build guide, use guide) plus tutorial screenshots; alt text is already written, real screenshots need to be dropped in
- [ ] **Verify component update propagation behaviour** — the lifecycle section in the concept page states updates flow automatically; confirm exact behaviour with CHILI before publishing
- [ ] **Raise PR** on `grafx-studio/components`

---

## llms.txt documentation (feature/llms-txt)

### Changes made

- `mkdocs.yml`: updated `site_description` and `markdown_description` in llmstxt plugin config — prospect/procurement framing, "design automation platform", "multichannel", "Design Systems" (not "Smart Templates"), two new sections added
- `hooks.py`: bug fix (missing `filepath` construction in loop) + last-updated date injection into `llms-full.txt` only

### Pending before PR

- [ ] **Raise PR** on `feature/llms-txt`

---

## Build command

```bash
cd /sessions/youthful-amazing-galileo/mnt/grafx-documentation
mkdocs build          # normal build
mkdocs build --strict # treats warnings as errors (will fail on missing screenshot placeholders)
```

---

## Key decisions log

- **"Design System" in llms.txt only** — replaces "Smart Template" in llmstxt plugin descriptions only, not in actual doc pages or nav
- **Phase 1 scope for components** — data-driven/Phase 2 features (dataset variable, data source mapper, dropdown/data table views) explicitly out of scope
- **List variable not supported in components** — because mapping is one-way; only mappable types supported in V1
- **Tutorials nav section** — placed between last "How to" block and "Connectors: Media" under GraFx Studio
- **Component mapping page** — Mermaid diagrams kept but demoted to collapsible `??? note` blocks; scenarios are the primary explanation
