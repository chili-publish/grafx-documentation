# Manage fields

This guide explains how to create fields in the CHILI GraFx extension and assign them to templates, projects, production channels, and outputs.

See [Fields](../../concepts/fields/) for a conceptual explanation of what fields are and how they work.

## Before you start

- You need access to the CHILI GraFx extension admin console in GraFx Experience.

## Create a field

In the extension admin console, go to **Fields** and click **New field**. Fill in:

| Setting | Description |
|---|---|
| Name | The field name as shown in the admin console and, where applicable, in the portal (e.g. "Template Type", "Template Access") |
| Description | Short explanation of what the field controls |
| Type | **Select** for a list of options, or **User Group** for access control |
| Used on | Select one or more: Template, Project, Production channel, Production output |

Click **Save** to create the field.

!!! note
    Fields in use cannot be deleted. To remove a field, first remove it from all templates, projects, and channels where it is assigned.

## Add options to a Select field

After creating a Select field, open it and add the available options — for example, "Employer Branding", "Campaign", "Social Media" for a "Template Type" field. These options will be available to admins when assigning the field to a template.

## Assign a field to a template

Open a template in the extension admin console and go to the **Fields** section. Select the field from the list of available fields and set its value.

- For **Select** fields: choose one or more options from the predefined list.
- For **User Group** fields: select the user groups that should have access to this template.

Click **Save** to apply.

## Configure field visibility on the campaigns page

To make a Select field available as a filter on the campaigns page, the field must be flagged as **Used on template** when it was created. The field then becomes available in the campaigns page widget configuration.

See [Configure the campaigns page](../configure-campaigns-page/) for instructions on enabling filters.

## Assign a field to a project

Fields marked as **Used on project** appear in the project overview. They can be used to filter the projects list and to display metadata on project cards.

To assign a field to a project, open the relevant template and enable the field for projects. The field value from the template is inherited by projects created from it.
