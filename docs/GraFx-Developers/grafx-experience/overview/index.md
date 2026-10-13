# Extend GraFx Experience

GraFx Experience can be extended with your own functionality through the **GraFx Extension Framework**. This section is for developers who want to build an extension — a web app that runs inside the GraFx Experience portal or the **Admin Console** and works with platform data.

See also: [The concept of extensions](/GraFx-Experience/concepts/extensions/)

## What you are building

An extension is a web app that GraFx Experience loads in an iframe. You host the app yourself, over HTTPS. GraFx Experience embeds it on the pages the extension registers, and passes it the context it needs: who the user is, which installation it runs on, and a scoped token to call the platform API.

With an extension, you can:

- Add pages to a space in the portal
- Add pages to the **Admin Console**
- Read and change platform data — for example users, groups, projects, or assets — through the Experience Extension API

## Two ways to integrate

| Pattern | Who uses it | Purpose |
|---|---|---|
| **Extension SDK** | Extension developers | Connect an embedded iframe app to GraFx Experience, receive a scoped token, and make authenticated API calls |
| **REST API** | Integrators with API credentials | Programmatic access to platform resources from your own back end |

The Extension SDK is the npm package `@kadanza/extension-sdk`. You do not need to build your own messaging between your app and the portal — the SDK handles the handshake with the host, the scoped token, and the authenticated calls.

## Prerequisites

To build an extension, you need:

- Admin access to the **Admin Console** of your GraFx Experience installation
- Familiarity with modern JavaScript and TypeScript
- Node.js and npm
- An HTTPS URL where you can host the extension app

## How to build an extension

Follow these pages in order:

1. [Create a local extension](/GraFx-Developers/grafx-experience/create-local-extension/) — register the extension in the **Admin Console** and choose its permissions and capabilities.
2. [Build with the Extension SDK](/GraFx-Developers/grafx-experience/extension-sdk/) — scaffold the app, connect to the host, call the API, and embed the app.
3. [Authentication](/GraFx-Developers/grafx-experience/authentication/) — understand the OAuth refresh tokens and the JWT your extension receives.
4. [Experience Extension API](/GraFx-Developers/grafx-experience/api-reference/) — the endpoints your extension can call.

For API credentials or REST API access outside an extension, contact CHILI publish.
