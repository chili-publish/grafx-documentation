# CHILI GraFx extension

The CHILI GraFx extension is installed inside GraFx Experience and connects the portal to your CHILI GraFx environment. It makes Design Systems from GraFx Studio available to portal users as campaigns.

The initial setup of the extension is performed by CHILI publish. Once configured, the extension can be managed by colleagues, partners, or customers who want to add templates, manage access, or configure output channels.

## How it fits together

GraFx Experience is the branded portal that end users interact with. The CHILI GraFx extension is the layer inside that portal that bridges GraFx Experience and your CHILI GraFx environment.

When an end user opens a campaign and starts editing, the extension loads the Design System from GraFx Studio and presents it inside the portal's editing experience. When the user produces output, the request is sent to your CHILI GraFx environment to generate the file.

## What the extension manages

The extension is configured through its own admin console. The key objects it manages are:

**Templates**
A template in the extension is a record that points to a Design System in GraFx Studio. It holds metadata (name, description, status, main visual) and configuration (fields, workflow settings). The link between the two systems is the **GraFx External ID** — the unique identifier of the Design System in GraFx Studio. Templates appear to end users as campaigns in the portal.

**Fields**
Reusable metadata elements that can be attached to templates, projects, production channels, and outputs. Fields serve two purposes: categorizing content for search and filtering, and controlling which user groups can access which templates. See [Fields](../fields/) for details.

**Template versioning**
Templates support a draft and published version cycle. Changes made in GraFx Studio are synced to the extension and staged as a draft before being published to users. See [Template versioning](../template-versioning/) for details.

**Production channels**
Define where output goes after a user finishes personalizing a template — a download, a print partner, or a digital endpoint. See [Production channels](../production-channels/) for details.

**Projects**
When an end user creates a campaign, the result is a project — a named, saved instance of a template with the user's chosen layouts and variable values. Admins can monitor all projects across the platform from the extension's admin console.

## Connecting the extension to CHILI GraFx

The extension authenticates to your CHILI GraFx environment using a Client ID and Client Secret. These are created in **Integrations** inside CHILI GraFx.

See the [Integrations concept](/CHILI-GraFx/concepts/integrations/) for details on how to generate credentials, and [Connect the extension to CHILI GraFx](../../guides/connect-to-chili-grafx/) for step-by-step setup instructions.
