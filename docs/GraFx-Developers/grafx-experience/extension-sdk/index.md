# Build with the Extension SDK

This guide shows how to build an extension app with the Extension SDK: set up the app, connect to GraFx Experience, call the platform API, and embed the app.

## How it works

GraFx Experience loads your app in an iframe. The Extension SDK (`@kadanza/extension-sdk`) handles:

- The **handshake** with the portal
- The **token** that lets your app act for the signed-in user
- **API calls** to the [Experience Extension API](/GraFx-Developers/grafx-experience/api-reference/)

You don't need to write your own `postMessage` code. Use `createExtensionSDK()` and the flows in the SDK.

## Before you start

- A [local extension](/GraFx-Developers/grafx-experience/create-local-extension/) with **SDK authentication** on, and **Experience pages** and/or **Admin Console pages** on
- Node.js and npm
- Hosting for the app, reachable over HTTPS. See [Hosting your extension](/GraFx-Developers/grafx-experience/overview/#hosting-your-extension).

!!! warning "Turn on SDK authentication"
    Without it, your app doesn't receive a token and can't call the API.

## Step 1: Set up the app

Use React, Vite, and TypeScript:

```bash
npm create vite@latest my-extension -- --template react-ts
cd my-extension
npm install @kadanza/extension-sdk react-router-dom
```

Use **`HashRouter`**, not `BrowserRouter`. GraFx Experience adds a `tenantUrl` parameter to the iframe URL, and hash routing keeps it in place while your app navigates.

## Step 2: Connect to GraFx Experience

```typescript
import { createExtensionSDK } from "@kadanza/extension-sdk";

const sdk = createExtensionSDK();

const { authToken, extensionDetails, designTokens } = await sdk.connect({
  routingType: "client-hash",
  authTokenAutoRefresh: true,
});
```

- Create the SDK once. Later calls to `createExtensionSDK()` return the same instance.
- `routingType: "client-hash"` lets GraFx Experience change routes without reloading the iframe.
- `connect()` resolves when GraFx Experience answers the handshake.
- Fields the page doesn't provide are `null`. For example, **Admin Console** pages have no `spaceId` or `pageId`.

!!! tip "React apps"
    Wrap your app in a provider that connects once, shows the UI only after the handshake, and calls `destroy()` on `pagehide`. See [Building a React extension](https://github.com/chili-publish/experience-extension-sdk/blob/main/docs/react-guide.md).

## Step 3: Call the platform API

Use `sdk.apiCall()` with paths from the [Experience Extension API](/GraFx-Developers/grafx-experience/api-reference/). The SDK adds the `Authorization` and `X-Tenant` headers.

```typescript
const user = await sdk.apiCall<{ firstName: string }>(
  "/platform/v1/api/users/me",
);
```

Calls are limited to the [API permissions](/GraFx-Developers/grafx-experience/create-local-extension/#api-permissions) of your extension. To validate the token on your own back end, see [Extension SDK JWT claims](/GraFx-Developers/grafx-experience/authentication/#extension-sdk-jwt-claims).

## Step 4: Host and embed

You host the app yourself, or your customer or a third party hosts it. For now, CHILI GraFx does not host extension apps.

1. Deploy the app over HTTPS.
2. In the **Admin Console**, go to **Extensions** > **Installed** and open your extension.
3. Set **Base URL** to your app's address, and add the page paths it serves.
4. Turn on **Active** and save.

GraFx Experience loads your app from the **Base URL** and adds a `tenantUrl` parameter with the portal's address. The SDK only accepts messages from that address.

When your app changes route, call `emitNavigationChange` so the portal knows. See [Navigation](https://github.com/chili-publish/experience-extension-sdk/blob/main/docs/flows.md#navigation).

## Further reading

| Resource | Covers |
|---|---|
| [Building a React extension](https://github.com/chili-publish/experience-extension-sdk/blob/main/docs/react-guide.md) | Provider, handshake, API calls, navigation |
| [Flows](https://github.com/chili-publish/experience-extension-sdk/blob/main/docs/flows.md) | Handshake, design tokens, `apiCall`, token refresh, page settings, navigation |
| [Embedding](https://github.com/chili-publish/experience-extension-sdk/blob/main/docs/embedding.md) | How GraFx Experience embeds your app |
| [SDK API reference](https://kadanza-io.github.io/extension-sdk/) | Classes, interfaces, and payloads |
| [npm package](https://www.npmjs.com/package/@kadanza/extension-sdk) | Installation and versions |
