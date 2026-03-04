# CHILI GraFx extension

The CHILI GraFx extension is installed inside GraFx Experience and connects the portal to your CHILI GraFx environment. It makes Smart Templates from GraFx Studio available to portal users.

## What the extension manages

From within the extension, you configure which GraFx Studio templates appear in the portal, who can access them, and how users interact with them.

The extension introduces the following concepts:

**Templates**
A template in the extension is a record that points to a Smart Template in GraFx Studio. It holds metadata (name, description, status, main visual) and configuration (fields, workflow settings). The link between the two systems is the **GraFx External ID** — the unique identifier of the Smart Template in GraFx Studio.

**Fields**
Metadata fields attached to a template. Used to categorize templates and control access. Examples: brand, output type, locale.

**Workflow settings**
Controls which GraFx Studio User Interface is shown to the end user when they open a template, and which user groups have access to it.

**Production outputs and channels**
Define what happens after a user finishes personalizing a template — where the output goes and in what format.

## Connecting the extension to CHILI GraFx

The extension authenticates to your CHILI GraFx environment using a Client ID and Client Secret. These are created in **Integrations** inside CHILI GraFx.

See the [Integrations concept](/CHILI-GraFx/concepts/integrations/) for details on how to generate credentials.
