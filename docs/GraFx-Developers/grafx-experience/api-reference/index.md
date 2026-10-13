# Experience Extension API

The Experience Extension API is the public REST API for extension developers. Use it when you build a local or third-party extension that calls GraFx Experience platform endpoints from your own application.

## What you can do with it

Typical use cases:

- Work with **CHILI GraFx** templates, versions, projects, and output
- Manage **users**, **user groups**, and invitations from an extension
- Integrate **translations** and other extension-managed resources

Embedded apps call these endpoints with `sdk.apiCall()` after [connecting with the Extension SDK](/GraFx-Developers/grafx-experience/extension-sdk/#step-3-call-the-platform-api). What an extension may call is limited by the [API permissions](/GraFx-Developers/grafx-experience/create-local-extension/#api-permissions) of the extension. For tokens and claims, see [Authentication](/GraFx-Developers/grafx-experience/authentication/).

## API reference

The interactive OpenAPI reference lists the available endpoints, request and response schemas, and server details. Use it as the source of truth for paths, payloads, and response models.

[Open the Experience Extension API reference](https://api.experience.chiligrafx.com/v1/platform/api/docs/public)
