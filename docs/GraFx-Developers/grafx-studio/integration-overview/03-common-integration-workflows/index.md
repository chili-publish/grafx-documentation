# Common Integration Workflows

This guide covers two fundamental approaches for integrating GraFx into your application. Both approaches give you full control over the end-user experience—the key difference is where your documents are stored.

## Which Workflow Is Right for You?

| | GraFx-Managed Documents | Self-Managed Documents |
|---|---|---|
| **Document storage** | GraFx platform | Your own system |
| **Asset storage** | GraFx platform (or custom connector) | Your asset management system (via custom connector) |
| **Best for** | Teams who want to leverage GraFx infrastructure | Teams with existing storage systems, require data analytics, or strict data residency requirements |
| **Setup effort** | Lower | Higher (requires custom connector) |

---

## Workflow 1: GraFx-Managed Documents

**Choose this if** you want to store documents on GraFx while managing the end-user experience in your own application.

In this workflow, end-users log into your application (not chiligrafx.com). Your application communicates with GraFx via the [Environment API](/GraFx-Developers/environment-api/reference/), and documents are stored on GraFx while you manage their lifecycle through your own database using document IDs.

### What You Will Need

- Fonts stored on your GraFx environment
- Integration client credentials with **all permissions** (for output and document management)
- Integration client credentials with **read-only permissions** (for the editor)
- A custom UI
- A database to manage document references

### Optional

- Custom Media Connector to your asset management system

### Phase 1: Setup

1. **Register your integrations** in GraFx to obtain two sets of client credentials:
   - One with all permissions (for output operations)
   - One with read-only permissions (for the editor)
   - See [Integration Permissions](/GraFx-Developers/environment-api/02-managing-integrations/?h=#the-permissions-tab)

2. **Create a template registration workflow** for your designers. When a designer creates a Template in GraFx Studio, they register it in your application by storing its ID in your database. Optionally, allow them to register specific output settings as well.

### Phase 2: End-User Flow

When an end-user selects a product in your application:

1. **Generate tokens** for both integrations:
   - `POST https://integration-login.chiligrafx.com/oauth/token`

2. **Create a Project from the Template** using the all-permissions token:
   - `POST /api/v1/environment/{environment}/projects`
   - Store the new Project ID in your database
   - See [Understanding Templates and Projects](/GraFx-Developers/grafx-studio/supplementary-materials/templates-vs-projects/)

3. **Download the Project JSON**:
   - `GET /api/v1/environment/{environment}/projects/{projectId}/document`

4. **Load the editor** in your custom UI using the read-only token:
   - See [Studio SDK Quickstart](/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/01-overview/)
   - See [Studio UI](/GraFx-Developers/grafx-studio/editor-engine/integrate-studio-ui/)

5. **Save the document** when the user is done using the all-permissions token:
   - `PUT /api/v1/environment/{environment}/projects/{projectId}`

6. **Generate a preview** (optional) either:
   - In the browser via [Studio SDK](https://github.com/chili-publish/studio-sdk/blob/5b063bb16c58966de4298317786e497ff66aa1d8/packages/sdk/src/controllers/LayoutController.ts#L19): `layout.getSelectedSnapshot()`
   - Via the REST API: `GET /api/v1/environment/{environment}/projects/{projectId}/preview/{previewType}`

### Phase 3: Output Generation

When your application is ready to produce final output:

1. **Download the Output Settings**:
   - `GET /api/v1/environment/{environment}/output/settings`

2. **Download the Project JSON**:
   - `GET /api/v1/environment/{environment}/projects/{projectId}/document`

3. **Generate output** using the all-permissions token (match the endpoint to your desired format):
   - `POST /api/v1/environment/{environment}/output/pdf`
   - `POST /api/v1/environment/{environment}/output/jpg`
   - `POST /api/v1/environment/{environment}/output/png`
   - `POST /api/v1/environment/{environment}/output/gif`
   - `POST /api/v1/environment/{environment}/output/mp4`

---

## Workflow 2: Self-Managed Documents

**Choose this if** you want to store documents in your own system and only use GraFx for editing and output rendering.

In this workflow, assets are stored externally via Connectors, documents are stored in your own system, and the [Environment API](/GraFx-Developers/environment-api/reference/) is used only for editing and generating output. This minimizes your dependency on the GraFx platform.

### What You Will Need

- Custom Media Connector to your asset management system
- Fonts stored on your GraFx environment (until Font Connectors are released)
- Integration client credentials with **all permissions** (for output)
- Integration client credentials with **read-only permissions** (for the editor)
- A custom UI
- Storage for document JSON (your own system)

### Phase 1: Setup

1. **Create and register a Custom Media Connector** for your asset management system:
   - See [Build a Simple Media Connector](/GraFx-Developers/connectors/media-connector/build-a-simple-media-connector/)

2. **Register your integrations** in GraFx to obtain two sets of client credentials:
   - One with all permissions (for output operations)
   - One with read-only permissions (for the editor)
   - See [Integration Permissions](/GraFx-Developers/environment-api/02-managing-integrations/?h=#the-permissions-tab)

3. **Create a template registration workflow** for your designers. When a designer creates a Template in GraFx Studio, download and store the JSON in your own system:
   - `GET /api/v1/environment/{environment}/templates/{templateId}/download`

### Phase 2: End-User Flow

Your application controls the entire user experience. GraFx is only involved when the user opens the editor:

1. **Generate a token** with read-only permissions:
   - `POST https://integration-login.chiligrafx.com/oauth/token`

2. **Load your custom UI** with the document JSON (from your storage) and the token:
   - See [Studio SDK Quickstart](/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/01-overview/)
   - See [Studio UI](/GraFx-Developers/grafx-studio/editor-engine/integrate-studio-ui/)

3. **Save the document** when the user is done by storing the JSON back to your system.

4. **Generate a preview** (optional) either:
   - In the browser via [Studio SDK](https://github.com/chili-publish/studio-sdk/blob/5b063bb16c58966de4298317786e497ff66aa1d8/packages/sdk/src/controllers/LayoutController.ts#L19): `layout.getSelectedSnapshot()`
   - Via the REST API: `GET /api/v1/environment/{environment}/projects/{projectId}/preview/{previewType}`

### Phase 3: Output Generation

When your application is ready to produce final output:

1. **Generate a token** with all permissions:
   - `POST https://integration-login.chiligrafx.com/oauth/token`

2. **Download the Output Settings**:
   - `GET /api/v1/environment/{environment}/output/settings`

3. **Generate output** using the all-permissions token (match the endpoint to your desired format):
   - `POST /api/v1/environment/{environment}/output/pdf`
   - `POST /api/v1/environment/{environment}/output/jpg`
   - `POST /api/v1/environment/{environment}/output/png`
   - `POST /api/v1/environment/{environment}/output/gif`
   - `POST /api/v1/environment/{environment}/output/mp4`
