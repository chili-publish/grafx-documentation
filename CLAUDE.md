# CLAUDE.md — CHILI GraFx documentation project

Read this file at the start of each session to restore working context.

---

## Project

**Site:** docs.chiligrafx.com — MkDocs Material, hosted on Azure Static Web Apps.
**Repo root:** `/sessions/youthful-amazing-galileo/mnt/grafx-documentation`
**Config:** `mkdocs.yml` — nav, plugins, markdown extensions.

Always run `git branch` at the start of a session to check the current branch before making any changes.

---

## MCP tools

| Tool | Use for |
|---|---|
| `chili-docs` | Search existing documentation — verify terminology, capitalisation, naming conventions before writing |
| `chili-content` | Search CHILI marketing content — align language with approved marketing terms |

Always search `chili-docs` before introducing new terminology or product names. Always search `chili-content` when writing descriptive or marketing-adjacent copy.

---

## Skills

| Skill | When to use |
|---|---|
| `release-notes` | Processing any REL- Jira ticket into a published release note |
| `enablement-hub` | Logging project status, decisions, or next actions to Confluence |

---

## Terminology rules

Established through `chili-docs` searches — do not deviate without verifying:

| Use | Not |
|---|---|
| Design Mode | Design mode |
| Run Mode | Run mode |
| Resize Mode | Resize mode |
| Template Designer Workspace | template designer workspace / designer workspace |
| Brand Kit | brand kit |
| Design & Run Mode | Design & Run mode |
| GraFx Studio | GraFx studio |
| multichannel | omnichannel |
| design automation platform | creative automation platform |
| Design Systems (in llms.txt only) | Smart Templates |

---

## Build command

```bash
cd /sessions/youthful-amazing-galileo/mnt/grafx-documentation
mkdocs build          # normal build
mkdocs build --strict # treats warnings as errors
```
