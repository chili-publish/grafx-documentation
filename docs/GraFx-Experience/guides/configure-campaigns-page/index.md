# Configure the campaigns page

This guide explains how to set up the page where end users browse available campaigns and start new projects.

The campaigns page is built using the **GraFx Content Exploration widget**, which is placed on a page in the GraFx Experience portal. The widget controls which campaigns are shown, which filters are available, and which users can see which campaigns.

!!! note
    Page names in GraFx Experience are configurable. Throughout this guide we use "campaigns page" as the default. Your portal may use a different label.

## Before you start

- Templates must exist in the extension and be set to **Active** status.
- Relevant fields must be created and marked as **Used on template**.
- User groups must be set up and users assigned to the correct groups.
- (Optional) Templates have a main visual uploaded for display in the grid.

## Step 1: Create the page

In the GraFx Experience portal admin, create a new page for the campaigns. You can add introductory text or images above the widget to provide context.

## Step 2: Add the widget

Add the **GraFx Content Exploration widget** to the page.

## Step 3: Configure the widget

Click the widget to open its settings panel. Configure the following:

**Component mode**
Set to **Templates** to display the campaign grid.

**Filter fields**
Select which fields appear as filter options for end users. Only fields marked as **Used on template** are available here. Both Select and User Group type fields can be used as filters.

**Field visibility**
Choose which fields are shown on the campaign cards (e.g. output type tags).

**Template view permissions**
Define which users see which campaigns. Each permission rule links a user group to a User Group type field on the template.

| Setting | Description |
|---|---|
| User group | The group of users this rule applies to (e.g. Content Manager) |
| Template field permissions | The User Group field on the template that controls access (e.g. Template Access) |

How it works: a user in the "Content Manager" group will only see campaigns where the template's "Template Access" field includes "Content Manager". Templates with no User Group field assigned are visible to all users.

Click **Add row** to add multiple permission rules for different user groups.

![The GraFx Content Exploration widget settings panel showing the Component mode, Filter fields, Field visibility, and Template view permissions configuration](widget-settings.png){.screenshot-full}

## Step 4: Save and publish

Click **Save** in the widget settings, then **Save & Publish** the page to make it live.

## Troubleshooting

**No campaigns appear for a user**

- Check the template is set to Active.
- Verify the user belongs to a user group that is mapped in the template view permissions.
- Check that the template's User Group field contains that user group.
- Confirm the page is published.

**Filters don't appear**

- Check that the selected fields are marked as **Used on template**.
- Check that Field visibility is set to show the field.
