# Configure a Design System

This guide explains how to make a GraFx Studio Design System available in GraFx Experience by linking and configuring it in the CHILI GraFx extension.

## Before you start

- The Design System must exist in GraFx Studio.
- The extension must be connected to your CHILI GraFx environment. See [Connect the extension to CHILI GraFx](../connect-to-chili-grafx/).
- You need access to the CHILI GraFx extension admin console in GraFx Experience.

## Step 1: Get the GraFx External ID

The GraFx External ID is the unique identifier of the Design System in GraFx Studio.

You can find it in two ways:

- **In the GraFx Studio URL:** Open the template in GraFx Studio. The GUID appears in the browser URL bar.
- **In the extension template list:** The GraFx External ID column shows the ID once a template is linked.

## Step 2: Create a template record in the extension

In the CHILI GraFx extension admin console, go to **Templates** and click **New template**. Fill in:

| Field | Description |
|---|---|
| Reference | Internal identifier for this template record |
| Name | Display name shown to portal users as the campaign name |
| Description | Optional — shown on the campaign card in the portal |
| GraFx External ID | Paste the GUID from GraFx Studio |
| Status | Set to Active to make it visible in the portal |
| Supported locales | Languages this template supports |
| Main visual | Thumbnail shown on the campaign card in the portal. If not set, the brand logo is used as fallback. |

Click **Save** to create the template.

![The New template form in the extension admin console with fields for Reference, Name, Description, GraFx External ID, Status, Supported locales, and Main visual](new-template-form.png){.screenshot-full}

!!! note
    A newly created template starts as a draft. It must be published before end users can create projects from it. See Step 5.

## Step 3: Add fields

Attach fields to the template to support filtering and access control on the campaigns page.

Fields are defined centrally in **Fields** in the extension. Once defined, assign them to this template and set their values.

- Use **Select** fields to categorize the template (e.g. Template Type = Social Media).
- Use **User Group** fields to restrict which user groups can see this template. If no user group field is assigned, the template is visible to all users.

See [Manage fields](../manage-fields/) for instructions on creating and assigning fields.

## Step 4: Configure workflow settings

Under **Workflow settings**, you can link specific GraFx Studio user interfaces to specific user groups. This controls which editing experience a user sees when they open the template.

Workflows are defined in GraFx Studio. Select the user group and assign the corresponding user interface.

If no workflow settings are configured, all users see the default GraFx Studio user interface for this template.

## Step 5: Publish the template version

After saving, open the template detail page and go to **Versions**. The first version will be in draft status.

Click **Publish** to make the template available to end users. Until a version is published, the template will not appear in the portal even if its status is set to Active.

![The Versions tab on a template showing the first version in Draft status with the Publish button visible](template-versions-publish.png){.screenshot-full}

## Step 6: Verify

Open GraFx Experience as an end user and go to the campaigns page. Confirm the template appears with the correct name, thumbnail, intent tags, and that access is restricted as expected.

## Updating a template after changes in GraFx Studio

When a Design System is updated in GraFx Studio, the extension does not automatically pick up those changes. To update the template:

1. Open the template in the extension admin console.
2. Create a new version using the **Resync** option.
3. Test the draft version if needed.
4. Click **Publish** to release the updated version to end users.

See [Template versioning](../../concepts/template-versioning/) for a full explanation of the version lifecycle.
