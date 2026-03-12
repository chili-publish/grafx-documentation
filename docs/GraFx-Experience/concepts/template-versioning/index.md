# Template versioning

Template versioning allows admins to update a template in GraFx Studio and stage those changes as a draft before making them available to end users. This means you can test a new version of a template while the current version remains in use.

## How versions work

Every template in the extension has one or more versions. A version is either a **draft** or **published**.

**Draft**
A draft version is not yet visible to end users. When a new template is first created, it starts as a draft. It must be published before end users can create projects from it.

When changes are made to a Design System in GraFx Studio, a new draft version is created in the extension. This lets you review and test the changes before releasing them.

**Published**
The published version is the one end users see and work with. When you publish a version, it becomes the active version. New projects are always created from the most recent published version.

!!! note
    Publishing a new version does not affect existing projects. Projects created from older versions remain available to users — they can still be edited, duplicated, and downloaded.

## The version lifecycle

```
New template created → Draft (version 1)
        ↓
   Publish draft → Published (version 1) — users can now create projects
        ↓
Changes made in GraFx Studio → New draft created (version 2)
        ↓
   Test draft → Publish draft → Published (version 2) — new projects use version 2
```

## Syncing changes from GraFx Studio

When a Design System is updated in GraFx Studio, those changes are not automatically reflected in the extension. An admin must manually sync the template to pull in the latest version.

Syncing is available for both draft and published versions. After syncing, review the changes and publish when ready.

## Testing a draft version

Before publishing, you can test a draft version by creating a project from it directly in the admin console. All available layouts will be included, and a test project is created for the admin user. This lets you verify the layout, variables, and output before releasing the version to end users.

See [Configure a Design System](../../guides/configure-design-system/) for step-by-step instructions on creating and publishing template versions.
