# Connect the extension to CHILI GraFx

This guide explains how to connect the CHILI GraFx extension to your CHILI GraFx environment using an integration.

## Before you start

- You need access to the CHILI GraFx extension admin console in GraFx Experience.
- You need access to **Integrations** in CHILI GraFx to create or retrieve credentials.

## Step 1: Create an integration in CHILI GraFx

In CHILI GraFx, go to **Integrations** and create a new integration for GraFx Experience. This generates a **Client ID** and **Client Secret**.

See the [Integrations concept](/CHILI-GraFx/concepts/integrations/) for details on creating integrations and setting the correct permissions.

Note down the Client ID and Client Secret — you will need them in the next step.

## Step 2: Enter the credentials in the extension

In the CHILI GraFx extension admin console, go to **Settings → Environment settings**.

Enter the Client ID and Client Secret from the integration you created in Step 1, then save.

The extension will authenticate against your CHILI GraFx environment and load the available settings (user interfaces, output settings).

## Step 3: Verify the connection

After saving, use the **Refresh** button in the Environment settings to sync the latest settings from CHILI GraFx. If the connection is successful, the available GraFx Studio user interfaces and output settings will appear in the extension.

## Refreshing after permission changes

If you make changes to the integration in CHILI GraFx — for example, updating permissions — the extension will not automatically pick up those changes. Use the **Refresh access token** button in Environment settings to re-authenticate and apply the updated permissions.
