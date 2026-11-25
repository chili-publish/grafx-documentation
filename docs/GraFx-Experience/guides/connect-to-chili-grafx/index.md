# Connect the extension to CHILI GraFx

This guide explains how to connect the CHILI GraFx extension to your CHILI GraFx environment using an integration.

## Before you start

- You need tenant admin access to the GraFx Experience admin console, with the CHILI GraFx extension enabled.
- You need access to **Integrations** in CHILI GraFx to create or retrieve credentials.

## Step 1: Create an integration in CHILI GraFx

In CHILI GraFx, go to **Integrations** and create a new integration for GraFx Experience. This generates a **Client ID** and **Client Secret**.

See the [Integrations concept](/CHILI-GraFx/concepts/integrations/) for details on creating integrations and setting the correct permissions.

Note down the Client ID and Client Secret — you will need them in the next step.

## Step 2: Enter the credentials on the GraFx Authentication page

In the admin console, open **Installed Extensions** and click **Authentication** (key icon) on the GraFx row. This opens the **GraFx Authentication** page.

The page holds the connection details for your CHILI GraFx environment. Required fields are marked with a red asterisk.

| Field | What to enter |
|---|---|
| Enable GraFx Studio integration | Turns the connection on or off |
| Environment ID | The identifier of your CHILI GraFx environment |
| Environment API base URL | The base URL of your environment's Environment API |
| Auth URL | The endpoint used to request access tokens |
| Client ID | The Client ID of the integration from Step 1 |
| Client Secret | The Client Secret of the integration from Step 1 (masked) |

Click **Save Authentication**. When you save, GraFx Experience checks the environment against your CHILI GraFx subscription. If the Environment ID is not valid, an error message is shown and the previous values are kept.

Once connected, every template of the environment is added to the extension's **Templates** list with the status **Needs configuration**. Users don't see these templates until you configure and activate them. See [Configure a Design System](../configure-design-system/).

## Step 3: Verify the connection

Open the extension's **Settings → Environment settings** and check that the access token has a recent refresh time. If the connection is successful, the GraFx Studio user interfaces and output settings from your environment are available when you configure templates in the extension.

## Settings are read live from CHILI GraFx

GraFx Experience reads the following from your CHILI GraFx environment each time it needs them, so a change in CHILI GraFx applies without any action in GraFx Experience:

- **GraFx Studio version** — the next editing session that opens runs on the version set in the [environment settings](/CHILI-GraFx/guides/manage-environment-version/). A session that is already open keeps its version.
- **User interfaces and output settings** — the next settings view, preview or output uses the changed value.

If CHILI GraFx can't be reached, GraFx Experience uses the last values it read successfully, and the editor shows a warning. When no earlier values exist, the editor loads the latest GraFx Studio version.

## Changing the environment

You can point the extension to another CHILI GraFx environment by changing the **Environment ID** or the **Environment API base URL** on the **GraFx Authentication** page. Because this affects every template, GraFx Experience asks you to confirm before it saves. **Cancel** keeps your edits in the form and saves nothing.

When you confirm:

- **Templates that are not on the new environment become Inactive** and are hidden from users. Expired templates stay Expired. Nothing is deleted: templates, versions, layouts and projects are kept.
- **Templates of the new environment are added** with the status **Needs configuration**.
- **Templates that exist on both environments** (with the same template ID) keep their status.
- **Existing projects** on templates of the previous environment can no longer be reliably edited or output.
- **Output settings and user interfaces** selected in the extension and in workflow settings still point to the previous environment. They are kept as they are; check and update them.

Switching back to an earlier environment does not restore anything. Templates stay Inactive until an admin activates them again.

Saving new credentials (Client ID, Client Secret or Auth URL) for the same environment, or connecting for the first time, doesn't show the warning and doesn't change any template.

## Refreshing after permission changes

When you change the permissions of the integration in CHILI GraFx, open **Environment settings** and click **Refresh** under **Access token** to re-authenticate with the updated permissions.

## Subscription sync

GraFx Experience reads your CHILI GraFx subscription each time you save the GraFx authentication, and keeps it in sync every hour after that. Changes to your subscription in CHILI GraFx reach GraFx Experience within about an hour.
