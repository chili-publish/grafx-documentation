# Hello World: Load Studio and Set a Variable

This tutorial builds the smallest possible GraFx Studio integration: a **single HTML file, with no build tools and no authentication**, that loads the GraFx Studio editor in the browser and then sends it a command through the [Studio SDK](https://github.com/chili-publish/studio-sdk) to change a variable in the loaded template.

It is the fastest way to see the SDK working end to end. Once that works, the final section shows how to point the same page at **your own environment** and load a specific template by ID. When you are ready for a production setup with a bundler, a JavaScript runtime, and your own templates, continue with the [Studio SDK Quickstart](/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/01-overview/).

## What you'll build

A page that:

1. Loads the Studio SDK from a CDN.
2. Loads the editor engine into a `<div>` on the page.
3. Loads a ready-made demo document — no token required.
4. Reads the variables in that document and sets one of them from a text field.

!!! note "Why no authentication is needed"
    Loading one of your own templates from an environment requires a token, because the editor has to call the Environment API on your behalf. This tutorial instead loads a **public demo document** that CHILI hosts on its CDN, so nothing here is behind authentication. The moment you want to load your own templates or use the built-in Media and Font connectors, you will need a token — see [Managing Integrations and Authentication](/GraFx-Developers/grafx-studio/integration-overview/04-managing-integrations-and-authentication/).

## What you'll need

Only two things:

- A text editor.
- A modern web browser.

There is no `npm install`, no bundler, and no server framework. The Studio SDK ships a browser build, so a plain `<script>` tag is enough.

## Step 1 - Create the page

Create a file called `index.html` and add the page structure. There are three parts: a small control bar (a text field and a button), the `<div>` that the editor will render into, and — later — a script.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>GraFx Studio — Hello World</title>
  </head>
  <body>
    <input id="valueInput" type="text" value="Hello, World!" />
    <button id="applyBtn" disabled>Apply to template</button>
    <span id="status">Starting…</span>

    <!-- The editor engine will be rendered into this element -->
    <div id="studio" style="width: 100vw; height: 90vh">Loading GraFx Studio…</div>
  </body>
</html>
```

The one element that matters most is `<div id="studio">`. Its `id` is how you tell the SDK where to place the editor.

## Step 2 - Load the Studio SDK

Add this `<script>` tag just before the closing `</body>` tag. It loads the SDK's browser build from a CDN.

```html
<script src="https://cdn.jsdelivr.net/npm/@chili-publish/studio-sdk@1.44.1/_bundles/main.js"></script>
```

??? question "What does this line do?"

    This loads the pre-bundled, browser-ready version of the Studio SDK. Once the script has run, the SDK is available on the global `window.StudioSDK` object. The class you construct is its default export, `window.StudioSDK.default`.

    Pinning a version (`@1.44.1`) keeps the tutorial reproducible. You can move to a newer release later — see the [SDK releases](https://github.com/chili-publish/studio-sdk/releases).

## Step 3 - Initialise the SDK and load the editor

Add a second `<script>` after the one above and start with initialising the SDK.

```html
<script>
  // The browser build exposes the SDK on window.StudioSDK; the class is the default export.
  const StudioSDK = window.StudioSDK.default;

  // Point the SDK at our <div id="studio"> and load the editor into it.
  const studio = new StudioSDK({ editorId: "studio" });
  studio.loadEditor();
</script>
```

??? question "What does this do?"

    `new StudioSDK({ editorId: "studio" })` creates an SDK instance and tells it which HTML element to use — the `editorId` must match the `id` of your `<div>`. `studio.loadEditor()` then loads the editor engine into that element. At this point you would see the editor's loading state on the page.

    The `studio` variable is your handle for everything else. Its properties are called **controllers** — for example `studio.document`, `studio.variable`, and `studio.configuration` — and each controller has functions for talking to the editor.

## Step 4 - Load a document

The editor engine does not care where a document's JSON comes from, as long as the format is correct. In production you would fetch it from the [Environment API](/GraFx-Developers/environment-api/reference/) or your own storage. Here we fetch the public demo document, which needs no token.

Add this inside the second `<script>`, below `studio.loadEditor()`:

```javascript
const DEMO_DOCUMENT_URL =
  "https://studio-cdn.chiligrafx.com/editor/1.4.1/web/assets/packages/runtime_assets/assets/documents/demo.json";

async function init() {
  const documentJson = await (await fetch(DEMO_DOCUMENT_URL)).text();
  await studio.document.load(documentJson);
}
init();
```

`studio.document.load()` returns a promise that resolves to a response object of the form `{ success, status, data, parsedData }`, so you can check `success` if you want to handle failures.

## Step 5 - Read the variables in the template

Before you can set a variable, it helps to know what the document contains. `studio.variable.getAll()` returns every variable; the array is on the response's `parsedData` field.

Extend `init()` so it inspects the variables after the document loads:

```javascript
let editableVariables = [];

async function init() {
  const documentJson = await (await fetch(DEMO_DOCUMENT_URL)).text();
  await studio.document.load(documentJson);

  const all = (await studio.variable.getAll()).parsedData || [];
  console.log("Variables in this template:", all);

  // Keep the variables we can set from a simple input field.
  editableVariables = all.filter(
    (v) => v.type === "shortText" || v.type === "longText" || v.type === "number"
  );

  document.getElementById("applyBtn").disabled = editableVariables.length === 0;
}
init();
```

Each variable has an `id`, a `name`, a `type` (such as `shortText`, `longText`, `number`, `image`, or `date`), and a `value`. Opening your browser console after loading the page shows the full list, which is the easiest way to discover the names and IDs in any template.

## Step 6 - Set a variable value through the SDK

This is the command we send to the editor. `studio.variable.setValue(id, value)` takes the variable's `id` and a new value (a string, number, boolean, or `null`).

Wire it to the button:

```javascript
document.getElementById("applyBtn").addEventListener("click", async () => {
  const target = editableVariables[0];
  if (!target) return;

  const raw = document.getElementById("valueInput").value;
  const value = target.type === "number" ? Number(raw) : raw;

  const result = await studio.variable.setValue(target.id, value);
  document.getElementById("status").textContent = result.success
    ? '✓ "' + target.name + '" set to: ' + raw
    : "✗ Could not set the variable";
});
```

!!! tip "Setting a specific variable"
    This example targets the first editable variable it finds. When you already know the variable, you can look it up by name instead of scanning the list:

    ```javascript
    const headline = (await studio.variable.getByName("headline")).parsedData;
    await studio.variable.setValue(headline.id, "Hello, World!");
    ```

## The complete file

Here is everything together. Save it as `index.html`.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>GraFx Studio — Hello World</title>
  </head>
  <body>
    <input id="valueInput" type="text" value="Hello, World!" />
    <button id="applyBtn" disabled>Apply to template</button>
    <span id="status">Starting…</span>

    <!-- The editor engine will be rendered into this element -->
    <div id="studio" style="width: 100vw; height: 90vh">Loading GraFx Studio…</div>

    <!-- 1. Load the Studio SDK from a CDN (UMD build → window.StudioSDK) -->
    <script src="https://cdn.jsdelivr.net/npm/@chili-publish/studio-sdk@1.44.1/_bundles/main.js"></script>

    <!-- 2. Our hello-world logic -->
    <script>
      // The browser build exposes the SDK on window.StudioSDK; the class is the default export.
      const StudioSDK = window.StudioSDK.default;

      // A ready-made demo document, hosted by CHILI. It loads without a token.
      const DEMO_DOCUMENT_URL =
        "https://studio-cdn.chiligrafx.com/editor/1.4.1/web/assets/packages/runtime_assets/assets/documents/demo.json";

      const statusEl = document.getElementById("status");
      const inputEl = document.getElementById("valueInput");
      const applyBtn = document.getElementById("applyBtn");

      let editableVariables = [];

      // Point the SDK at our <div id="studio"> and load the editor into it.
      const studio = new StudioSDK({ editorId: "studio" });
      studio.loadEditor();

      // Load a document, then read the variables it contains.
      async function init() {
        try {
          statusEl.textContent = "Loading demo document…";
          const documentJson = await (await fetch(DEMO_DOCUMENT_URL)).text();

          const loaded = await studio.document.load(documentJson);
          if (!loaded.success) {
            throw new Error("document.load returned status " + loaded.status);
          }

          const all = (await studio.variable.getAll()).parsedData || [];
          console.log("Variables in this template:", all);

          editableVariables = all.filter(
            (v) => v.type === "shortText" || v.type === "longText" || v.type === "number"
          );
          applyBtn.disabled = editableVariables.length === 0;
          statusEl.textContent = editableVariables.length
            ? 'Ready. Type a value and click "Apply to template".'
            : "No text/number variables in this template — check the console.";
        } catch (err) {
          console.error(err);
          statusEl.textContent = "Could not load the document: " + err.message;
        }
      }
      init();

      // Send a command to Studio through the SDK: set a variable value.
      applyBtn.addEventListener("click", async () => {
        const target = editableVariables[0];
        if (!target) return;

        const raw = inputEl.value;
        const value = target.type === "number" ? Number(raw) : raw;

        statusEl.textContent = 'Setting "' + target.name + '"…';
        const result = await studio.variable.setValue(target.id, value);
        statusEl.textContent = result.success
          ? '✓ "' + target.name + '" set to: ' + raw
          : "✗ Could not set the variable (status " + result.status + ")";
      });
    </script>
  </body>
</html>
```

## Run it

Open `index.html` in your browser. For the most reliable results — some browsers restrict `fetch` on pages opened directly from disk — serve the folder over HTTP instead. Any static server works, for example:

```bash
python3 -m http.server 3000
```

Then visit `http://localhost:3000`. You should see the editor load the demo document. Type a value, click **Apply to template**, and the targeted variable updates in the document.

!!! note "About the demo document"
    The demo document is only meant for trying things out. Images in it are served through the built-in Media connector, which needs a token, so they may not appear on this no-authentication page — that is expected. The point of this tutorial is loading the editor and driving it through the SDK; the text variable will still update.

## Load a document from your environment

The demo document needed no token because it is public. To load one of **your own** templates, the page has to link to a specific environment and authenticate. That means three extra pieces of information: the environment's technical name (which builds its API URL), a template ID, and an access token.

### Step 1 - Create an integration and generate a token

Loading a template calls the Environment API, so you need an access token. Create an integration and generate a token as described in [Generating a token](/GraFx-Developers/environment-api/03-generating-a-token/). A **read-only** integration is enough for loading templates.

!!! warning "Keep your Client Secret off the browser"
    The token in this tutorial is pasted into a field for local testing only. A token is generated from your Client ID and **Client Secret**, and the secret must never appear in client-side code. In production, generate the token on your server and pass only the short-lived token to the browser — see [Managing Integrations and Authentication](/GraFx-Developers/grafx-studio/integration-overview/04-managing-integrations-and-authentication/).

### Step 2 - Find your environment name and template ID

- **Environment technical name** is the subdomain of your environment, for example `cp-abc-123`. Find it under Settings → Details → Technical name. It is used to build the API URL:

    ```
    https://{technical-name}.chili-publish.online/grafx/api/v1/environment/{technical-name}
    ```

    Environments on sandbox use `chili-publish-sandbox.online` instead.

- **Template ID** is the template's GUID. It is visible in the browser URL when a template is open, or you can list templates with `GET …/templates`.

### Step 3 - Add inputs for the environment, template, and token

Add a few fields to the page so you can enter these values instead of hard-coding them:

```html
<input id="envName" type="text" placeholder="Environment technical name (e.g. cp-abc-123)" />
<select id="envType">
  <option value="production">Production</option>
  <option value="sandbox">Sandbox</option>
</select>
<input id="templateId" type="text" placeholder="Template ID (GUID)" />
<input id="token" type="password" placeholder="Access token (read-only)" />
<button id="loadEnvBtn">Load template from environment</button>
```

### Step 4 - Link the editor to the environment and load the template

Two things happen here. First, `studio.configuration.setValue` tells the editor which environment and token to use — the editor needs this so its fonts, media, and connectors resolve against your environment. Second, you fetch the template's document JSON from the Environment API and hand it to `studio.document.load`.

```javascript
const { WellKnownConfigurationKeys } = window.StudioSDK;

document.getElementById("loadEnvBtn").addEventListener("click", async () => {
  const env = document.getElementById("envName").value.trim();
  const type = document.getElementById("envType").value; // "production" | "sandbox"
  const templateId = document.getElementById("templateId").value.trim();
  const token = document.getElementById("token").value.trim();

  // Build the Environment API base URL for this environment.
  const host = type === "sandbox" ? "chili-publish-sandbox" : "chili-publish";
  const envApiBase =
    "https://" + env + "." + host + ".online/grafx/api/v1/environment/" + env;

  // Link the editor to this environment + token.
  await studio.configuration.setValue(
    WellKnownConfigurationKeys.GraFxStudioEnvironmentApiUrl,
    envApiBase
  );
  await studio.configuration.setValue(
    WellKnownConfigurationKeys.GraFxStudioAuthToken,
    token
  );

  // Fetch the template's document JSON, then load it into the editor.
  const url = envApiBase + "/templates/" + templateId + "/download";
  const resp = await fetch(url, { headers: { Authorization: "Bearer " + token } });
  if (!resp.ok) throw new Error("Download failed: HTTP " + resp.status);

  await studio.document.load(await resp.text());

  // Read the variables from the freshly loaded template (see Step 5 above).
  const all = (await studio.variable.getAll()).parsedData || [];
  console.log("Variables in this template:", all);
});
```

!!! tip "The SDK can build the URL for you"
    Instead of assembling the URL by hand, the SDK offers a helper: `studio.utils.createEnvironmentBaseURL({ type: "production", environment: "cp-abc-123" })` returns the same base URL.

Enter your environment name, template ID, and token, then click **Load template from environment**. The editor replaces the demo with your template, and the **Set a variable** step works exactly the same — now against your own document.

## Where to go next

- [Communicating with the SDK](/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/04-communicating-with-sdk/) — controllers and events in more depth.
- [Studio SDK Quickstart](/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/01-overview/) — the same ideas in a production-style project with a bundler.
- [Generating a token](/GraFx-Developers/environment-api/03-generating-a-token/) — required once you load your own templates instead of the demo document.
- [StudioSDK class reference](https://chili-publish.github.io/studio-sdk/) — every controller and function.
