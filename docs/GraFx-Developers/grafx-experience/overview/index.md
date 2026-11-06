# Extend GraFx Experience

With the **GraFx Extension Framework**, you can add your own functionality to GraFx Experience. This section is for developers who build extensions: web apps that run inside the portal or the **Admin Console** and work with platform data.

See also: [The concept of extensions](/GraFx-Experience/concepts/extensions/)

## What you are building

An extension is a web app that GraFx Experience loads in an iframe. GraFx Experience embeds it on the pages the extension registers and passes it the context it needs: the signed-in user, the installation, and a token to call the platform API.

With an extension, you can:

- Add pages to a space in the portal
- Add pages to the **Admin Console**
- Read and change platform data, such as users, groups, projects, or assets

## Hosting your extension

!!! info "You choose where your extension runs"
    You host the extension app yourself, or your customer or a third party hosts it. For now, CHILI GraFx does not host extension apps.

GraFx Experience only needs a URL, not your code. Deploy the app where it suits you, and enter its HTTPS address as the **Base URL** of your [local extension](/GraFx-Developers/grafx-experience/create-local-extension/#capabilities).

Any hosting works if:

- The app is reachable over **HTTPS**
- It serves the page paths you register on the extension
- It is available whenever users open those pages

For the deployment steps, see [Step 4: Host and embed](/GraFx-Developers/grafx-experience/extension-sdk/#step-4-host-and-embed).

## Two ways to integrate

| Option | For | Use it to |
|---|---|---|
| **Extension SDK** | Extension developers | Connect an embedded app to GraFx Experience and make authenticated API calls |
| **REST API** | Integrators with API credentials | Access platform data from your own back end |

The Extension SDK is the npm package `@kadanza/extension-sdk`. It handles the handshake with the portal, the token, and the API calls, so you don't build that messaging yourself.

## Prerequisites

- Admin access to the **Admin Console**
- Experience with JavaScript and TypeScript
- Node.js and npm
- Hosting for the app, reachable over HTTPS

## How to build an extension

New to extensions? Start with the [Hello world tutorial](/GraFx-Developers/grafx-experience/hello-world/). It takes you from an empty folder to a working page in the portal.

For the full picture, read these pages in order:

1. [Create a local extension](/GraFx-Developers/grafx-experience/create-local-extension/): register the extension and choose its permissions and capabilities.
2. [Build with the Extension SDK](/GraFx-Developers/grafx-experience/extension-sdk/): set up the app, connect, call the API, and embed it.
3. [Authentication](/GraFx-Developers/grafx-experience/authentication/): the tokens your extension uses.
4. [Experience Extension API](/GraFx-Developers/grafx-experience/api-reference/): the endpoints you can call.

For API credentials or REST API access outside an extension, contact CHILI publish.
