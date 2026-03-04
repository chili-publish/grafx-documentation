# Configure a Smart Template for GraFx Experience

This guide explains how to make a GraFx Studio Smart Template available in GraFx Experience by linking and configuring it in the CHILI GraFx extension.

## Before you start

- The Smart Template must exist in GraFx Studio.
- You need access to the CHILI GraFx extension in GraFx Experience.

## Step 1: Get the GraFx External ID

The GraFx External ID is the unique identifier of the Smart Template in GraFx Studio.

You can find it in two ways:

- **In the GraFx Studio URL:** Open the template in GraFx Studio. The GUID appears in the browser URL bar.
- **In the extension template list:** The GraFx External ID column shows the ID once a template is linked.

## Step 2: Create a template record in the extension

In the CHILI GraFx extension, go to **Templates** and create a new template. Fill in:

| Field | Description |
|---|---|
| Reference | Internal identifier for this template record |
| Name | Display name shown to portal users |
| Description | Optional — helps users understand what the template is for |
| GraFx External ID | Paste the GUID from GraFx Studio |
| Status | Set to Active to make it visible in the portal |
| Supported locales | Languages this template supports |
| Main visual | Thumbnail shown to portal users in the template browser |

## Step 3: Add fields

Attach metadata fields to the template to support filtering and access control. Examples: Brand, Output type, Region.

Fields are defined in **Fields** in the extension. Once defined, assign values on the template.

## Step 4: Configure workflow settings

Under **Workflow settings**, select:

- **GraFx User Interface** — which Studio UI the end user sees when they open the template
- **User groups** — which groups in GraFx Experience can access this template

## Step 5: Verify

Open GraFx Experience as an end user and confirm the template appears in the portal with the correct name, thumbnail, and access settings.
