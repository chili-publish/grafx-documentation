# Experience Extension API

The Experience Extension API is the public REST API for extension developers. Use it to call GraFx Experience from your extension.

## What you can do with it

- Work with **CHILI GraFx** templates, versions, projects, and output
- Manage **users**, **user groups**, and invitations
- Work with **translations** and other extension resources

Apps in the portal call these endpoints with `sdk.apiCall()` after [connecting with the Extension SDK](/GraFx-Developers/grafx-experience/extension-sdk/#step-3-call-the-platform-api). Your extension can only call what its [API permissions](/GraFx-Developers/grafx-experience/create-local-extension/#api-permissions) allow. For tokens, see [Authentication](/GraFx-Developers/grafx-experience/authentication/).

## API reference

The interactive OpenAPI reference lists all endpoints, with request and response details. Treat it as the source of truth.

[Open the Experience Extension API reference](https://api.experience.chiligrafx.com/v1/platform/api/docs/public)
