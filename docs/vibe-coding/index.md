# AI Developer Reference — CHILI GraFx

This page is written for AI coding assistants, agents, and vibe coding tools (Cursor, Lovable, etc.).

**How to use this page:**

1. Collect the required inputs listed below — ask the user to provide them.
2. Identify which integration path matches what you are building.
3. Follow the steps in order. Each step links to the detailed documentation.

Do not infer or guess environment-specific values. They must be provided explicitly.

---

## Account structure

A CHILI GraFx account is organized as follows:

- A customer has **one or more subscriptions**
- Each subscription has **one or more environments** (production and/or sandbox)
- Each environment has its own Technical Name, GUID, and credentials

Always confirm with the user which **specific environment** they are targeting. Do not assume there is only one.

## Required inputs — collect these before starting

Ask the user to provide the following. All values are specific to their environment.

| Input | Where the user finds it |
|---|---|
| **Technical Name** | In CHILI GraFx: Settings (gear icon, bottom-left) → **Details** → **Technical name** (e.g. `cp-abc-123`) |
| **Environment GUID** | Same page: **Details** → **ID** — or visible in the browser URL: `chiligrafx.com/environments/{ENVIRONMENT_GUID}/...` |
| **Client ID** | **Integrations** → open your integration → **General** tab |
| **Client Secret** | Same tab as Client ID |
| **Environment API Swagger URL** | **Integrations** → open your integration — the direct link is listed there |
| **Platform API Swagger URL** | **Integrations** → open your integration — the direct link is listed there |

!!! tip
    The **Integrations** section is the single place to find your Client ID, Client Secret, and direct links to both the Environment API Swagger and the Platform API Swagger. Send the user there first.

The Technical Name is used as the **subdomain** in all environment-specific URLs:

```
https://{TECHNICAL_NAME}.chili-publish.online/grafx/...
```

Example — if the Technical Name is `cp-abc-123`:

```
https://cp-abc-123.chili-publish.online/grafx/swagger/index.html
```

---

## What do you want to build?

Choose the path that matches the goal:

- **[Path A](#path-a--headless-output-via-api)** — Generate PDFs, images, or animations from templates. No UI shown to the end user.
- **[Path B](#path-b--embed-the-editor-sdk)** — Embed the GraFx Studio template editor inside your own application.
- **[Path C](#path-c--self-service-portal-studio-ui)** — Embed a self-service customization interface in your web portal, where end users can personalize templates.

---

## Path A — Headless output via API

Use this when you want to programmatically generate output files (PDF, PNG, JPG, GIF, MP4, HTML) from templates — with no editor UI.

### Step 1: Create an integration

An integration is a set of API credentials scoped to your environment.

1. In CHILI GraFx, go to **Integrations**.
2. Click **Create Integration**. Give it a name.
3. Open the **Permissions** tab and set permissions to **All Permissions**.
4. Open the **General** tab and copy the **Client ID** and **Client Secret**.
5. From the same page, copy the direct links to the **Environment API Swagger** and **Platform API Swagger**.

See: [Managing Integrations](/GraFx-Developers/environment-api/02-managing-integrations/)

### Step 2: Generate a token

POST to the auth endpoint:

```
https://integration-login.chiligrafx.com/oauth/token
```

Request body:

```json
{
  "grant_type": "client_credentials",
  "audience": "https://chiligrafx.com",
  "client_id": "{{CLIENT_ID}}",
  "client_secret": "{{CLIENT_SECRET}}"
}
```

The response contains `access_token`. Use it as `Authorization: Bearer {{TOKEN}}` in all API calls.

!!! warning
    Tokens with All Permissions must never be exposed to the frontend. Generate them server-side only.

See: [Generating a Token](/GraFx-Developers/environment-api/03-generating-a-token/)

### Step 3: Get the template GUID

**Option 1 — User provides it directly.**
The template GUID is visible in the browser URL when a template is open in GraFx Studio:

```
chiligrafx.com/environments/{ENVIRONMENT_GUID}/studio/templates/{TEMPLATE_GUID}
```

Ask the user to open the template and copy the GUID from the URL.

**Option 2 — Discover via API.**
To retrieve all templates in a folder, call:

```
GET /api/v1/environment/{{TECHNICAL_NAME}}/templates
```

This returns a list of templates with their GUIDs. Filter by folder if needed.

See: [Environment API Swagger](https://{{TECHNICAL_NAME}}.chili-publish.online/grafx/swagger/index.html)

### Step 4: Request output

Start an output task:

```
POST /api/v1/environment/{{TECHNICAL_NAME}}/output/image
POST /api/v1/environment/{{TECHNICAL_NAME}}/output/animation
```

Then poll for the result:

```
GET /api/v1/environment/{{TECHNICAL_NAME}}/output/tasks/{{TASK_ID}}
```

See: [Making API Calls](/GraFx-Developers/environment-api/04-making-api-calls/)

---

## Path B — Embed the editor (SDK)

Use this when you want to load the GraFx Studio editor inside your own application.

**First, ask the user which type of editor they are building:**

- **Custom designer workspace** — full editor, tools redesigned or extended to the integrator's needs.
- **Custom end-user workspace** — limited toolset, only specific interactions exposed to the end user. May include custom tools to manipulate canvas content.

Both use the Studio SDK. The difference is which controllers and panels you expose. The SDK gives you programmatic control over all editor capabilities.

### Step 1: Decide on integration level

Review the available integration levels to choose how deeply to integrate with the platform:

- Level 3: Custom front-end, documents stored on GraFx
- Level 4: Custom front-end, documents managed externally
- Level 5: Full external management — GraFx used as rendering engine only

See: [Integration Levels](/GraFx-Developers/grafx-studio/integration-overview/02-integration-levels/)

### Step 2: Create two integrations

You need two separate integrations. In CHILI GraFx, go to **Integrations** and create both:

| Integration | Permissions | Used for |
|---|---|---|
| Frontend integration | **Read-only** | Loading the editor in the browser |
| Backend integration | **All Permissions** | Server-side operations (saving, output) |

See: [Managing Integrations](/GraFx-Developers/environment-api/02-managing-integrations/)

### Step 3: Generate tokens

- Use the **read-only** token in the frontend to load the editor. This token is safe to pass to the browser.
- Use the **all-permissions** token on the server only. Never send it to the frontend.

Same token endpoint as Path A.

See: [Generating a Token](/GraFx-Developers/environment-api/03-generating-a-token/)

### Step 4: Set up the SDK project

**Choose how to load the SDK — ask the user which they prefer:**

- **Latest version (live CDN)** — always loads the most recent release. Simpler to set up, but the behavior may change when CHILI GraFx updates.
- **Fixed version (pinned)** — install a specific version via npm. Recommended for production integrations where stability is required.

Install a specific version via npm:

```
npm install @chili-publish/studio-sdk@{VERSION}
```

Or install the latest:

```
npm install @chili-publish/studio-sdk
```

Requirements:

- JavaScript runtime: Node.js (recommended for production)
- Bundler: webpack, esbuild, or parcel
- Web server: required to serve files over HTTP

See: [SDK Quickstart](/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/01-overview/)

### Step 5: Load the editor

The editor runs inside an iframe. Use the SDK to communicate with it via controllers.

Follow the full quickstart sequence:

1. [Project setup](/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/02-project-setup/)
2. [Loading the SDK](/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/03-loading-studio-sdk/)
3. [Communicating with the SDK](/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/04-communicating-with-sdk/)

For a full working example with controllers, connectors, and events:

See: [Workshop — Building a custom UI](/GraFx-Developers/grafx-studio/editor-engine/workshop-building-a-custom-ui/00-workshop-overview/)

---

## Path C — Self-service portal (Studio UI)

Use this when you want end users to customize templates in your web portal, without exposing the full designer interface.

!!! note
    This embeds the **end-user** interface (GraFx Experience / Studio UI), not the designer editor. End users can personalize templates; they cannot design them.

### Step 1: Create an integration (read-only)

In CHILI GraFx, go to **Integrations** and create a new integration with **Read-only** permissions.

See: [Managing Integrations](/GraFx-Developers/environment-api/02-managing-integrations/)

### Step 2: Generate a token (server-side only)

Your server generates the token using the read-only Client ID and Client Secret. The token is passed to the frontend at runtime.

Same token endpoint as Path A and B.

!!! warning
    Never expose your Client Secret to the frontend. Always generate the token server-side.

### Step 3: Embed Studio UI

Add a container to your HTML:

```html
<div id="studio-ui-container"></div>
```

Inject the script:

```html
<script src="https://studio-cdn.chiligrafx.com/studio-ui/latest/bundle.js"></script>
```

Initialize with your token and environment configuration. All configuration options and examples are on GitHub.

See: [Integrate Studio UI](/GraFx-Developers/grafx-studio/editor-engine/integrate-studio-ui/)

See: [Studio UI on GitHub](https://github.com/chili-publish/studio-ui)

For advanced configuration (custom panels, restricted variables, layout selection):

See: [Advanced Integration on GitHub](https://github.com/chili-publish/studio-ui/blob/main/documentation/advanced-integration.md)

---

## API reference

| Resource | URL |
|---|---|
| Platform API Swagger | `https://api.chiligrafx.com/swagger/index.html` |
| Environment API Swagger (production) | `https://{TECHNICAL_NAME}.chili-publish.online/grafx/swagger/index.html` |
| Environment API Swagger (sandbox) | `https://{TECHNICAL_NAME}.chili-publish-sandbox.online/grafx/swagger/index.html` |
| Auth token endpoint | `https://integration-login.chiligrafx.com/oauth/token` |

`{TECHNICAL_NAME}` is the subdomain — replace it with the actual value (e.g. `cp-abc-123`). Each environment has a different Technical Name and therefore a different Swagger URL.

---

## Identifier reference

### Technical Name

- Found in: Settings (gear icon) → **Details** → **Technical name**
- Used as the subdomain in all Environment API URLs: `{{TECHNICAL_NAME}}.chili-publish.online`
- Example: `cp-abc-123`

### Environment GUID

- Found in: Settings (gear icon) → **Details** → **ID**
- Also visible in the browser URL: `chiligrafx.com/environments/{ENVIRONMENT_GUID}/...`
- Example: `aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee`

### Template GUID

- Visible in the browser URL when a template is open:
  `chiligrafx.com/environments/{ENVIRONMENT_GUID}/studio/templates/{TEMPLATE_GUID}`
- Or retrieve all templates via API:
  `GET /api/v1/environment/{{TECHNICAL_NAME}}/templates`

### Client ID and Client Secret

- Found in: **Integrations** → open your integration → **General** tab
- Create a new integration at: **Integrations** → **Create Integration**
- The same page also contains direct links to the **Environment API Swagger** and **Platform API Swagger**
- See: [Managing Integrations](/GraFx-Developers/environment-api/02-managing-integrations/)
