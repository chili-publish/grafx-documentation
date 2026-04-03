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

## Git workflow

### Branch naming

| Work type | Convention | Example |
|---|---|---|
| Release note | `REL-x/App-Name/short-description` | `REL-20/GraFx-Studio/text-constraints` |
| Documentation feature | `topic/short-description` | `grafx-studio/components` |
| Bug fix / misc | `Docs/short-description` | `Docs/broken-link-fix` |

**App-Name slugs for REL branches:** `CHILI-GraFx`, `GraFx-Studio`, `GraFx-Media`, `GraFx-Experience`, `GraFx-Fonts`, `GraFx-Publisher`, `GraFx-Genie`

### Rules

- All branches must be derived from `main` — never from another feature branch
- Never commit directly to `main`
- Always verify the active branch with `git branch --show-current` before writing any files

### Switching branches safely

When switching branches with uncommitted work in progress, stash first using the GitHub Desktop naming convention — it auto-restores the stash when you switch back to that branch:

```bash
CURRENT_BRANCH=$(git branch --show-current)
git stash push --include-untracked -m "!!GitHub_Desktop<$CURRENT_BRANCH>"
```

Then switch:

```bash
git checkout main
git pull origin main
git checkout -b new-branch-name   # or: git checkout existing-branch
git branch --show-current         # verify before touching any files
```

### Commit message format

```
[Short summary of what and why]

- Specific change 1
- Specific change 2

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

For release note commits, prefix with the ticket key: `[REL-x] Add release note for [Product]: [topic]`

### PR title format (release notes)

```
[Product Name] Rel XX - Product Name - Main Topic
```

Example: `[GraFx Studio] Rel 20 - GraFx Studio - Text Constraints, Page Duplication`

---

## Build command

```bash
cd /sessions/youthful-amazing-galileo/mnt/grafx-documentation
mkdocs build          # normal build
mkdocs build --strict # treats warnings as errors
```
