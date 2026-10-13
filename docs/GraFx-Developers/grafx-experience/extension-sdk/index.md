# Build with the Extension SDK

This guide walks you through building an embedded GraFx Experience extension with the Extension SDK: scaffold the app, connect to the host, call the platform API, and embed the app through your local extension.

## How it works

Your extension is a web app that GraFx Experience loads in an iframe. The Extension SDK (`@kadanza/extension-sdk`) handles everything between your app and the portal:

- The **handshake** with the host page
- The **scoped JWT** that lets your app act on behalf of the current user
- **Authenticated calls** to the [Experience Extension API](/GraFx-Developers/grafx-experience/api-reference/)

You do not need to build your own `postMessage` protocol. Use `createExtensionSDK()` and the flows documented in the SDK.

## Before you start

- A [local extension](/GraFx-Developers/grafx-experience/create-local-extension/) with **SDK authentication** enabled, and **Experience pages** and/or **Admin Console pages** enabled
- Node.js and npm
- An HTTPS URL where you can host the app

!!! warning "Enable SDK authentication"
    Without **SDK authentication** on the local extension, the iframe does not receive a scoped JWT, and `connect()` cannot complete a useful handshake for API calls.

## Step 1: Scaffold the app

Use React, Vite, and TypeScript:

```bash
npm create vite@latest my-extension -- --template react-ts
cd my-extension
npm install @kadanza/extension-sdk react-router-dom
```

Use **`HashRouter`**, not `BrowserRouter`. Hash routing keeps the `tenantUrl` query parameter that the host adds to the iframe URL intact while your app navigates.

## Step 2: Connect to the host

```typescript
import { createExtensionSDK } from "@kadanza/extension-sdk";

const sdk = createExtensionSDK();

const { authToken, extensionDetails, designTokens } = await sdk.connect({
  routingType: "client-hash",
  authTokenAutoRefresh: true,
});
```

- Create the SDK once per app. Later calls to `createExtensionSDK()` return the same instance.
- Pass `routingType: "client-hash"` so GraFx Experience can change routes without reloading the iframe.
- `connect()` resolves when the host acknowledges the handshake.
- Context fields are `null` when the surface does not provide them. For example, **Admin Console** pages have no `spaceId` or `pageId`.

!!! tip "React apps"
    Wrap your app in a provider that connects once, waits to render the UI until the handshake succeeds, and calls `destroy()` only on `pagehide`. See [Building a React extension](https://github.com/kadanza-io/extension-sdk/blob/main/docs/react-guide.md) in the SDK repository.

## Step 3: Call the platform API

Use `sdk.apiCall()` with root-relative paths from the [Experience Extension API](/GraFx-Developers/grafx-experience/api-reference/). The SDK adds the `Authorization` and `X-Tenant` headers for you.

```typescript
const user = await sdk.apiCall<{ firstName: string }>(
  "/platform/v1/api/users/me",
);
```

Calls are limited to the [API permissions](/GraFx-Developers/grafx-experience/create-local-extension/#api-permissions) of your local extension.

Tokens from `connect()` have `token_type: extension_sdk`. If you validate the token on your own back end, see [Extension SDK JWT claims](/GraFx-Developers/grafx-experience/authentication/#extension-sdk-jwt-claims).

## Step 4: Host and embed

1. Deploy the app over HTTPS.
2. In the **Admin Console**, go to **Extensions** > **Installed** and open your local extension.
3. Set **Base URL** to the origin of your app, and add the page paths your app serves.
4. Enable **Active** and save.

GraFx Experience loads the iframe from your **Base URL** and adds a `tenantUrl` query parameter with the origin of the parent page. The SDK uses that value to validate messages from the host.

Use hash routing so in-app navigation does not drop `tenantUrl`. To let the portal know about route changes, call `emitNavigationChange` — see [Navigation](https://github.com/kadanza-io/extension-sdk/blob/main/docs/flows.md#navigation) in the SDK repository.

## Further reading

| Resource | What it covers |
|---|---|
| [Building a React extension](https://github.com/kadanza-io/extension-sdk/blob/main/docs/react-guide.md) | Provider, handshake gate, API calls, navigation tracker |
| [Flows](https://github.com/kadanza-io/extension-sdk/blob/main/docs/flows.md) | Handshake, design tokens, `apiCall`, token refresh, page settings, navigation |
| [Embedding](https://github.com/kadanza-io/extension-sdk/blob/main/docs/embedding.md) | How the host embeds an extension: iframe `src`, `tenantUrl`, host API |
| [SDK API reference](https://kadanza-io.github.io/extension-sdk/) | Classes, interfaces, and payloads |
| [npm package](https://www.npmjs.com/package/@kadanza/extension-sdk) | Installation and versions |
