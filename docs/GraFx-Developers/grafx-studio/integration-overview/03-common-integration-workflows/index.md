# Common Integration Workflows

Let take a look at two fundamental workflows for integrating with GraFx, catering to different levels of customization and control. These examples demonstrate how to effectively incorporate GraFx's capabilities into your application, from a straightforward integration to a more complex, fully-customized setup.

## Workflow 1: Advanced Custom Integration: End-User and Document Management Externally

This workflow decreases development time while still allowing you to integrate GraFx into your application.

In this integration, documents are stored in GraFx, but end-users do not log into [chiligrafx.com](https://www.chiligrafx.com). Instead, they log into your custom application. Your application uses the [Environment API]() to communicate with GraFx, and when an end-user loads a document, it is loaded via a custom UI and then saved back to GraFx when they are done. Instead of managing documents on GraFx, you manage them in your application, usually via a database. The JSON documents are stored on GraFx, and you manage their life cycle in your application via their IDs.

### What You Will Need

- Fonts stored on your GraFx environment
- Integration client secret and ID with all permissions for output
- Integration client secret and ID with read-only permissions for the editor
- A custom UI
- A database to manage documents

### Optional

- Custom Media Connector to your asset management system

### The Plan

1. Create a workflow for template designers to register their Templates into your application from GraFx Studio. They would just be registering the ID of the Template in a database.
2. Generate a token with your client secret and ID with all permissions:
    - `https://integration-login.chiligrafx.com/oauth/token`
    - See [Integration Permissions]()
3. Generate a token with your client secret and ID with read-only permissions:
    - `https://integration-login.chiligrafx.com/oauth/token`
    - See [Integration Permissions]()
4. End-users, through your application, will pick a product, which will cause the following:
    - Copy the Template or create a Project using the all-permissions token:
        - Create a Project from a Template:
            - POST `/api/v1/environment/{environment}/projects`
        - Copy a Template:
            - GET `/api/v1/environment/{environment}/templates/{templateId}/download`
            - POST `/api/v1/environment/{environment}/templates`
        - See [Understanding Templates and Projects]()
    - Store the copied Template or Project ID in your application database
    - Download the JSON of your Template or Project:
        - Template: GET `/api/v1/environment/{environment}/templates/{templateId}/download`
        - Project: GET `/api/v1/environment/{environment}/projects/{projectId}/document`
    - Open the JSON Template or Project in a custom UI using the read-only token:
        - See [Studio SDK Quickstart]()
        - See [Studio UI]()
    - Save JSON back to Template or Project:
        - Template: UPDATE `/api/v1/environment/{environment}/projects/{projectId}/document` 
        - Project: UPDATE `/api/v1/environment/{environment}/templates/{templateId}`
    - You can generate a preview either:
        - With [Studio SDK]() layout controller: `layout.getSelectedSnapshot()`
        - With REST API:
            - Template: GET `/api/v1/environment/{environment}/templates/{templateId}/preview/{previewType}`
            - Project: GET `/api/v1/environment/{environment}/projects/{projectId}/preview/{previewType}`
5. In your application workflow, when ready for output, download the JSON again and output using the token with all permissions:
    - POST `/api/v1/environment/{environment}/output/animation`
    - POST `/api/v1/environment/{environment}/output/image`
    - New outputs coming out of experimental which require output settings:
        - POST `/api/v1/environment/{environment}/output/jpg`
        - POST `/api/v1/environment/{environment}/output/png`
        - POST `/api/v1/environment/{environment}/output/mp4`
        - POST `/api/v1/environment/{environment}/output/gif`
        - POST `/api/v1/environment/{environment}/output/pdf`

## Workflow 2: Full Custom Integration: External Management for All Aspects

This workflow allows for maximum customization, as GraFx Studio becomes a very small part of your application.

This integration removes the need for [chiligrafx.com](https://www.chiligrafx.com) outside of template designers. Assets are stored externally via Connectors, documents are stored externally, and the [Environment API]() is used only when outputting a render.

### What You Will Need

- Custom Media Connector to your asset management system
- Fonts stored on your GraFx environment (until Font Connectors are released)
- Integration client secret and ID with all permissions for output
- Integration client secret and ID with read-only permissions for the editor
- A custom UI
- Storage for document JSON

### The Plan

1. Create a [Custom Media Connector]() for your asset management system and register it in your environment.
2. Create a workflow for template designers to register their Templates into your application from GraFx Studio, which at minimum will just download a Template's JSON to store in your application's storage:
    - GET `/api/v1/environment/{environment}/templates/{templateId}/download`
3. End-user workflow is completely decided by your application, and the integration application only interacts with GraFx Studio at two locations in the workflow:
    - When the end-user in your workflow opens an editor, you do the following:
        - Generate a token with your client secret and ID with read-only permissions:
            - `https://integration-login.chiligrafx.com/oauth/token`
            - See [Integration Permissions]()
        - Load your custom UI with your document JSON and token for authentication:
            - See [Studio SDK Quickstart]()
            - See [Studio UI]()
        - When done, get the JSON and store it back into your application storage
            - It is also a good time to generate a preview with [Studio SDK]() layout controller: `layout.getSelectedSnapshot()`
    - When the application is ready to make an output (PDF, image, video):
        - Generate a token with your client secret and ID with all permissions:
            - `https://integration-login.chiligrafx.com/oauth/token`
            - See [Integration Permissions]()
        - Use the all-permissions token to generate output:
            - POST `/api/v1/environment/{environment}/output/animation`
            - POST `/api/v1/environment/{environment}/output/image`
            - New outputs coming out of experimental which require output settings:
              - POST `/api/v1/environment/{environment}/output/jpg`
              - POST `/api/v1/environment/{environment}/output/png`
              - POST `/api/v1/environment/{environment}/output/mp4`
              - POST `/api/v1/environment/{environment}/output/gif`
              - POST `/api/v1/environment/{environment}/output/pdf`
