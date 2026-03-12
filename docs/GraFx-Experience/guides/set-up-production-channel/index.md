# Set up a production channel

This guide explains how to create a production channel in the CHILI GraFx extension and make it available to end users.

See [Production channels](../../concepts/production-channels/) for a conceptual explanation of what production channels are.

## Before you start

- You need access to the CHILI GraFx extension admin console in GraFx Experience.
- User groups must be set up if you want to restrict channel access.

## Step 1: Create a production channel

In the extension admin console, go to **Production Channels** and click **New production channel**. Fill in:

| Field | Description |
|---|---|
| Name | The channel name as shown to end users (e.g. "Printer West", "Digital Distribution") |
| Type | Select **Print** or **Digital** |
| Contact phone | Phone number of the production contact |
| Contact email | Email address of the production contact |
| Available for user groups | Which user groups can see and use this channel |
| Production outputs available for user group | Which outputs from this channel are visible to specific groups |

Click **Save** to create the channel.

## Step 2: Add custom fields (optional)

If you need to capture additional order information — such as a cost center or internal reference — you can add custom fields to the channel. These fields appear when a user places an order via this channel.

## Step 3: Configure output settings (optional)

In **Settings → Production output settings**, you can set a default output reference prefix (up to 5 alphanumeric characters). This prefix is automatically added to all order references generated through this channel.

## Step 4: Verify

Place a test order from a project using this channel. Confirm that the channel appears for the correct user groups and that the order details are captured correctly.

## Editing an existing channel

From the Production Channels overview, select **Edit** from the context menu next to a channel. You can update the name, contact details, type, user group access, and custom fields.
