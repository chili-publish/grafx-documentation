# Template versioning

Template versioning allows admins to update a template in GraFx Studio and stage those changes as a draft before making them available to end users. This means you can test a new version of a template while the current version remains in use.

## How versions work

Every template in the extension has one or more versions. Each version has one of these statuses:

**Draft**
A draft version is not yet visible to end users. When a new template is first added, it starts as a draft. It must be published before end users can create projects from it. A template has at most one draft at a time.

**Published**
A published version is available to end users. Several versions can be published at the same time. **New projects always use the newest published version.** Older published versions are only used by the existing projects that were created from them.

**Expired**
An expired version is no longer used. Projects on an expired version can no longer be edited.

**Sync failed**
The version could not be created from the Design System in GraFx Studio. Use **Resync** to try again.

!!! note
    Publishing a new version does not affect existing projects. Projects created from older versions that are still published remain available to users — they can still be edited, duplicated, and downloaded.

## The version lifecycle

```
New template added → Draft (version 1)
        ↓
   Publish draft → Published (version 1) — users can now create projects
        ↓
Changes made in GraFx Studio → Create version → Draft (version 2)
        ↓
   Test draft → Publish draft → Published (version 2) — new projects use version 2,
                                existing projects stay on version 1
```

## The Versions tab

The **Versions** tab on the template page shows:

- the **draft**, if there is one, with its state and all its layouts
- the **published version that new projects use**, when and by whom it was published, and how many projects use it
- the **full history** of all versions, each with its status, publication date and project count

The page header also shows which published version new projects use, and links to the draft when there is one.

## Creating a version from GraFx Studio changes

When a Design System is updated in GraFx Studio, those changes are not automatically reflected in the extension. Click **Create version**, in the header's **⋯** menu or on the **Versions** tab, to create a draft from the latest design right away. No name, comment or confirmation is needed.

A template has only one draft at a time. While a draft exists, or a version failed to sync, you can't create another version. Use **Resync** on that version to update it with the latest design, or publish the draft first.

Layout changes compared to the published version can't be detected, so the draft doesn't mark layouts as new or changed. Review the draft's layouts before you publish.

## Publishing

GraFx Experience prepares a preview for every layout in the draft. **Publish** stays disabled, with the reason shown, until all previews are ready, and after a sync failure.

When you publish, new projects start using this version. Existing projects stay on the version they were created from.

## Expiring a version

When you expire a version, the confirmation tells you how many projects are affected. If it was the version new projects use, new projects fall back to the newest remaining published version. If no published version is left, the template becomes **Expired**.

Other version actions are available from the **⋯** menu of each version: **Resync**, **Restore to published**, **View projects** and **Download JSON**.

## Testing a draft version

Before publishing, you can test a draft version by creating a project from it directly in the admin console. All available layouts will be included, and a test project is created for the admin user. This lets you verify the layout, variables, and output before releasing the version to end users.

See [Configure a Design System](../../guides/configure-design-system/) for step-by-step instructions on adding and publishing templates.
