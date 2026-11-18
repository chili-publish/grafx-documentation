# Configure a Design System

This guide explains how to make a GraFx Studio Design System available in GraFx Experience by adding and configuring it as a template in the CHILI GraFx extension.

## Before you start

- The Design System must exist in GraFx Studio.
- The extension must be connected to your CHILI GraFx environment. See [Connect the extension to CHILI GraFx](../connect-to-chili-grafx/).
- You need access to the CHILI GraFx extension admin console in GraFx Experience.

## Step 1: Add the template

In the CHILI GraFx extension admin console, go to **Templates** and click **Add template**.

A picker opens with the templates in your connected CHILI GraFx environment. Each one shows a preview, its name, its folder and when it was last modified. Use search and sort to find the right one.

Templates that are already added to GraFx Experience stay visible in the picker, but you can't select them a second time.

Select the template. The template page opens in create mode, prefilled with the template you picked. You don't need to copy or paste a template ID.

## Step 2: Fill in the general settings

The template page has three tabs: **General**, **Versions** and **Translations**. The **General** tab holds three sections: **General**, **Field values** and **Workflow settings**.

In the **General** section, fill in:

| Setting | Description |
|---|---|
| Reference | Internal identifier for this template. Required. |
| Name | Display name shown to portal users as the campaign name. Required. |
| Description | Optional. Shown on the campaign card in the portal. |
| Main visual | Landscape (16:9) image shown on the campaign card in the portal. You can set, replace or remove it, also while adding the template. If not set, the brand logo is used as fallback. |
| Supported locales | Languages this template supports. Search by language name or code. The tenant's default locale is always included and can't be removed. |
| Layout selection mode | How users choose layouts when they create a project. See [Layout selection mode](#layout-selection-mode). |

### Layout selection mode

| Mode | Effect for users |
|---|---|
| Multiple | Users pick one or more layouts when they create a project, and can add or remove layouts later in the editor. |
| Single | Users pick exactly one layout. It can't be changed afterwards. |
| None | Users don't pick. Every layout is included and can't be removed. |

## Step 3: Set field values

Fields support filtering and access control on the campaigns page. They are defined centrally in **Fields** in the extension. See [Manage fields](../manage-fields/).

The **Field values** section lists every field that is enabled for templates, each with a control that matches its type. There is no separate step to add a field to the template.

- Use **Select** fields to categorize the template (e.g. Template Type = Social Media).
- Use **User Group** fields to restrict which user groups can see this template. If no user group field has a value, the template is visible to all users.

An empty field means the value is not set. Use **Clear** on a row to remove its value. A counter shows how many fields have a value.

## Step 4: Configure workflow settings

A workflow setting links one or more user groups to a GraFx Studio [user interface](/GraFx-Studio/concepts/user-interface/). The user interface decides two things for those users:

- the **editor UI** they see when they open a project from this template
- the **output options** they can download, grouped by Digital, Animated and Print

The **Workflow settings** section is a table with one row per workflow setting. For each row, choose the user interface and the user groups. The row shows the output options of that user interface. These are read-only here; you manage them on the user interface in GraFx Studio.

Two rules decide what a user gets when they belong to groups in several rows:

- **Editor UI** — the **first** matching row, from top to bottom, decides the editor UI. Reorder the rows to change which one wins.
- **Output options** — the output options of **all** matching rows are combined.

A user group can only be used in one row. Groups already used in another row are not offered.

Users who don't match any row get the default GraFx Studio user interface and **no download options**. To cover everyone, add a row with **All users** as the last row.

## Step 5: Save

Changes on the **General** tab are kept until you save or discard them, also when you switch tabs. As soon as something changes, a save bar appears. Click **Save** to store all changes at once, or **Discard** to go back to the saved state. The save bar tells you when **Reference** or **Name** is missing.

## Step 6: Publish the template version

Open the **Versions** tab. The first version of a new template is a draft.

While the previews of the draft's layouts are being prepared, **Publish** is disabled and the tab shows the progress. When all previews are ready, click **Publish** to make the template available to end users. Until a version is published, the template doesn't appear in the portal, even if its status is **Active**.

Version actions such as **Publish** run immediately. They don't require you to save first, and any unsaved changes on the **General** tab stay in the save bar.

See [Template versioning](../../concepts/template-versioning/) for the full version lifecycle.

## Step 7: Verify

Open GraFx Experience as an end user and go to the campaigns page. Confirm the template appears with the correct name, main visual and field values, and that access is restricted as expected.

## Updating a template after changes in GraFx Studio

When a Design System is updated in GraFx Studio, the extension does not automatically pick up those changes. To update the template:

1. Open the template in the extension admin console.
2. Click **Create version**, in the header's **⋯** menu or on the **Versions** tab. The draft is created right away from the latest design in GraFx Studio. If the template already has a draft, or a version that failed to sync, use **Resync** on that version instead.
3. Test the draft if needed.
4. Click **Publish** to make the new version available for new projects.

To open the Design System itself, use **Edit in GraFx Studio** in the page header or in the template list.
