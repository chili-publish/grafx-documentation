# Hello World: Integrate Studio UI

This tutorial embeds the full **GraFx Studio end-user editor — Studio UI** — into a single HTML page, loads a document into it, and then drives it from your own code through the SDK to **change a variable**.

Studio UI is the complete, ready-made editing interface (variables panel, layouts, output, autosave) that your end users work in. You load it from a CDN bundle; it builds the whole editor into a `<div>` for you. It also exposes the underlying SDK as `window.StudioUISDK`, so your page can send commands to the running editor — for example, set a variable's value programmatically.

To keep the first run simple, we load a small **bundled sample document** into Studio UI. Once that works, the same page can load one of your own **projects** from your environment by entering its ID.

## Studio UI vs the Editor Engine

There are two ways to put GraFx Studio in your page:

- **Editor Engine + [Studio SDK](/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/01-overview/)** — a bare editing canvas. You build every control yourself and talk to it through the SDK. Maximum control, more work.
- **Studio UI** (this tutorial) — the complete end-user interface, pre-built. You configure it and it renders the whole editor. Faster to integrate; you customize through options.

!!! note "Studio UI always authenticates"
    Unlike the bare Editor Engine, Studio UI is built for the authenticated end-user experience. Even when you hand it your own document, it still needs your environment's API URL and an **access token** to initialise (fonts, media, output, and so on). There is no no-authentication mode — the moment you embed Studio UI, you are talking to your environment.

## What you'll need

- A text editor and a modern web browser.
- An **environment** (its technical name) and an **integration** to mint a token.
- Optionally, a **project** to open instead of the bundled sample.

## Step 1 - Generate a token

Studio UI calls the Environment API, so it needs an access token. For a quick local test you can generate one directly in the platform:

1. In CHILI GraFx, open **Integrations** and create a new integration (or open an existing one). See [Managing Integrations](/GraFx-Developers/environment-api/02-managing-integrations/).
2. On the integration's **General** tab, under **Authentication**, you will see its **Client ID** and **Client Secret**.
3. Click **Generate token** to get a ready-to-use access token, and copy it.
4. On the **Permissions** tab, give it at least `myproject:read` and `myproject:write` (needed if you later load a real project).

For the full request-based method, see [Generating a token](/GraFx-Developers/environment-api/03-generating-a-token/).

!!! warning "Keep your Client Secret off the browser"
    The **Generate token** button is meant for testing — the token it produces is short-lived, and using it in the browser is fine locally. Your **Client Secret** must never appear in client-side code. In production, generate the token on your server and hand Studio UI a fresh token through its `refreshTokenAction` — see [Managing Integrations and Authentication](/GraFx-Developers/grafx-studio/integration-overview/04-managing-integrations-and-authentication/).

## Step 2 - Find your environment name

Your **environment technical name** is the subdomain of your environment, e.g. `cp-abc-123` (Settings → Details → Technical name). It builds the API base URL:

```
https://{technical-name}.chili-publish.online/grafx/api/v1/environment/{technical-name}
```

Environments on sandbox use `chili-publish-sandbox.online` instead. That is all you need for the bundled sample; a project ID is only required for the optional [load a real project](#load-a-real-project) step.

## Step 3 - Add the container and load the bundle

Studio UI builds itself into a `<div>` you provide. Create `index.html` with that container, the bundle, and the sample document embedded in a `<script type="application/json">` tag so we can hand it to Studio UI later.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>GraFx Studio UI — Hello World</title>
  </head>
  <body>
    <!-- Studio UI is constructed into this element -->
    <div id="studio-ui-container" style="width: 100vw; height: 90vh"></div>

    <!-- The sample document (full JSON is in the complete file below) -->
    <script type="application/json" id="hello-doc">{ … the document JSON … }</script>

    <!-- Exposes window.StudioUI (and window.StudioUISDK once loaded) -->
    <script src="https://studio-cdn.chiligrafx.com/studio-ui/latest/bundle.js"></script>
  </body>
</html>
```

## Step 4 - Load the bundled document into Studio UI

Instead of pointing Studio UI at a stored project, we give it the document ourselves through the `onProjectDocumentRequested` callback. You still supply the environment URL and token so Studio UI can initialise.

```javascript
const environment = "cp-abc-123";       // your environment technical name
const token = "<YOUR ACCESS TOKEN>";
const helloDocument = document.getElementById("hello-doc").textContent;

const envBase =
  "https://" + environment + ".chili-publish.online/grafx/api/v1/environment/" + environment;

window.StudioUI.studioUILoaderConfig({
  selector: "studio-ui-container",
  graFxStudioEnvironmentApiBaseUrl: envBase,
  authToken: token,
  refreshTokenAction: () => Promise.resolve(token),
  projectName: "Hello World",

  // Provide the document ourselves instead of loading a stored project.
  onProjectInfoRequested: async () => ({ id: "hello-world", name: "Hello World", template: { id: "hello-world" } }),
  onProjectDocumentRequested: async () => helloDocument,
  onProjectSave: async () => ({ id: "hello-world", name: "Hello World", template: { id: "hello-world" } }),
});
```

Serve the page and the full editor opens with the sample document — variables panel, canvas, and toolbar included. An end user can already change the `Message` variable straight from the panel.

## Step 5 - Change a variable through the SDK

You can also drive the running editor from your own code. Studio UI exposes the same SDK the Editor Engine uses, as the global `window.StudioUISDK`. Once the document has loaded, look the variable up by name and set its value:

```javascript
async function setMessage(newValue) {
  const sdk = window.StudioUISDK;
  const variable = (await sdk.variable.getByName("Message")).parsedData;
  if (!variable) return;
  await sdk.variable.setValue(variable.id, newValue);
}
```

`variable.setValue(id, value)` is the same call you would use with the bare Editor Engine — the difference is that here it drives the full Studio UI, and the change is reflected on the canvas and in the variables panel. This is how a host application can pre-fill or override values around the editor.

!!! tip "Wait until the document is loaded"
    The SDK is only ready once the project/document has finished loading. Enable your controls from the `onProjectLoaded` callback, or guard your calls with `if (!window.StudioUISDK) return;`.

## Load a real project

To open one of your own projects instead of the bundled sample, drop the `onProject…` callbacks and point Studio UI at the project's document endpoint. A **project** (not a template) is what an end user works on — its GUID comes from *My Projects*; see [Templates vs Projects](/GraFx-Developers/grafx-studio/supplementary-materials/templates-vs-projects/).

```javascript
const projectId = "859dd405-bfed-467f-b833-...";

window.StudioUI.studioUILoaderConfig({
  selector: "studio-ui-container",
  projectId: projectId,
  projectDownloadUrl: envBase + "/projects/" + projectId + "/document",
  projectUploadUrl: envBase + "/projects/" + projectId,   // enables autosave
  graFxStudioEnvironmentApiBaseUrl: envBase,
  authToken: token,
  refreshTokenAction: () => Promise.resolve(token),
  projectName: "Hello World",
});
```

## The complete file

Save this as `index.html`. It adds a small form so you can enter your environment and token, load Studio UI (the bundled sample by default, or a project if you provide its ID), and set the `Message` variable through the SDK.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>GraFx Studio UI — Hello World</title>
    <style>
      body { font-family: system-ui, sans-serif; margin: 0; }
      header { padding: 12px 16px; background: #f5f5f7; border-bottom: 1px solid #e0e0e0; }
      .row { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-bottom: 8px; }
      input, select { padding: 8px 10px; border: 1px solid #c8c8c8; border-radius: 6px; }
      button { padding: 8px 14px; border: 0; border-radius: 6px; background: #e2380f; color: #fff; cursor: pointer; }
      button:disabled { background: #c8c8c8; cursor: not-allowed; }
      summary { cursor: pointer; font-weight: 600; }
      #status { font-size: 13px; color: #555; }
      #studio-ui-container { width: 100vw; height: calc(100vh - 190px); }
    </style>
  </head>
  <body>
    <header>
      <div class="row">
        <label for="valueInput">Message</label>
        <input id="valueInput" type="text" value="Hello, John!" />
        <button id="applyBtn" disabled>Set variable via SDK</button>
        <span id="status">Enter your environment and token, then load Studio UI.</span>
      </div>
      <details open>
        <summary>Advanced — connect to your environment</summary>
        <div class="row">
          <input id="envName" type="text" placeholder="Environment technical name (e.g. cp-abc-123)" />
          <select id="envType">
            <option value="production">Production</option>
            <option value="sandbox">Sandbox</option>
          </select>
          <input id="token" type="password" placeholder="Access token" />
          <input id="projectId" type="text" placeholder="Project ID (GUID) — leave empty for the sample" />
          <button id="loadBtn">Load Studio UI</button>
        </div>
      </details>
    </header>

    <!-- Studio UI is constructed into this element -->
    <div id="studio-ui-container"></div>

    <!-- The bundled sample document: one text frame + one shortText variable named "Message". -->
    <script type="application/json" id="hello-doc">{"selectedLayoutId":"623890eb-06fa-4929-af0e-abb6024b672b","sdkVersion":"1.44.1","engineVersion":"2.27.0","documentVersion":"0.23.0","properties":{"type":"template"},"pages":[{"id":"62bed8dc-d42f-4a7b-97dc-f548eb60f726","number":0,"frames":[{"id":"62e9f0cb-673f-43a3-bda7-23f759de4ea4","name":"Text","opacity":1,"type":"text","textContent":[{"type":"paragraph","style":{"textAlign":"center"}},{"type":"span"},{"type":"variable","id":"c6aa9481-a885-40a6-b534-585132be4c8a"}],"paddingLeft":0,"paddingTop":0,"paddingRight":0,"paddingBottom":0,"numberOfColumns":1,"columnGap":24000,"textDirection":"auto","flowDirection":"horizontal","verticalAlign":"top","hasClippingPath":false,"blendMode":"normal"}],"isVisible":true}],"layouts":[{"id":"623890eb-06fa-4929-af0e-abb6024b672b","name":"A4","frameProperties":[{"id":"62e9f0cb-673f-43a3-bda7-23f759de4ea4","horizontal":{"start":0.1060644240057117,"end":0.10606442400571164,"target":{"type":"page"},"type":"relative"},"vertical":{"start":0.14248908871289137,"end":0.7019084506301811,"target":{"type":"page"},"type":"relative"},"width":335000,"height":66161,"rotationDegrees":0,"isVisible":true,"imageFit":{"mode":"fill","position":"center"},"type":"top","copyfittingSettings":{"type":"top","min":0.1,"max":10,"enabled":true},"autoGrowSettings":{"type":"top","directions":[],"enabled":false}}],"width":425196,"height":425196,"childLayouts":[],"type":"top","unit":"mm","intent":"print","fillColor":{"color":{"r":255,"g":255,"b":255,"type":"rgb"},"opacity":1,"type":"local"},"fillColorEnabled":true,"bleed":{"value":8503,"type":"combined"},"privateData":{},"availableForUser":true,"resizableByUser":{"enabled":false,"constraintMode":"none"}}],"brandKit":{"colors":[],"gradients":[],"characterStyles":[],"paragraphStyles":[],"fontFamilies":[],"media":[],"themes":[],"isAutoSync":false},"variables":[{"id":"c6aa9481-a885-40a6-b534-585132be4c8a","type":"shortText","parentId":"","name":"Message","visibility":{"type":"visible"},"isReadonly":false,"isRequired":false,"value":"Hello world","privateData":{},"removeParagraphIfEmpty":false,"dontBreak":false}],"connectors":[{"id":"grafx-media","name":"GraFx Media","source":{"source":"local","url":"grafx-media.json"},"options":{},"mappings":[]},{"id":"grafx-fonts","name":"GraFx Fonts","source":{"source":"local","url":"grafx-fonts.json"},"options":{},"mappings":[]},{"id":"grafx-components","name":"GraFx Components","source":{"source":"local","url":"grafx-components.json"},"options":{},"mappings":[]}],"actions":[],"constraints":{"frames":{}},"flags":0,"resignerMetadata":[],"checkSum":"a97eabd35e62484f5b197f5130b20c1656d002df86a012e4536ad9274b6be0ec7a1fcd81e67fdcfda4cd7a42581e3b330db8f1061771c5975eaa7d7bc67f3421a694e3043a3a429466708d6b87a990103162ef2c5e8be5b3e0f8175803e3ec951aad3360d60443b3041f5fa825996533f1150d6c4ce1f2b01b503900f684012745e2c742f41cee4ef6f3a97342ce09b74448b7b62b6f8103b8513a56a27fc8411c193169cd4e30caf14bc951497c3f6802231598daefcd304b25a52b7e45c739656a7b12c42e4f1d147fb85e877ab4e19ed43a6c12e71b4b55980cd96f133e7fec54ea9fb7831a604c8f3f913f1db231a7ad1ee8c0557a67203b237371fb2884"}</script>

    <!-- Studio UI bundle (exposes window.StudioUI, and window.StudioUISDK once loaded) -->
    <script src="https://studio-cdn.chiligrafx.com/studio-ui/latest/bundle.js"></script>

    <script>
      const $ = (id) => document.getElementById(id);
      const setStatus = (msg) => ($("status").textContent = msg);
      const HELLO_DOCUMENT = $("hello-doc").textContent;

      // Load Studio UI. With a Project ID it loads that project; otherwise it loads
      // the bundled sample document via onProjectDocumentRequested.
      $("loadBtn").addEventListener("click", () => {
        const env = $("envName").value.trim();
        const type = $("envType").value;
        const projectId = $("projectId").value.trim();
        const token = $("token").value.trim();

        if (!env || !token) {
          setStatus("Enter at least an environment name and a token.");
          return;
        }

        const host = type === "sandbox" ? "chili-publish-sandbox" : "chili-publish";
        const envBase =
          "https://" + env + "." + host + ".online/grafx/api/v1/environment/" + env;

        const config = {
          selector: "studio-ui-container",
          graFxStudioEnvironmentApiBaseUrl: envBase,
          authToken: token,
          refreshTokenAction: () => Promise.resolve(token),
          projectName: "Hello World",
          onProjectLoaded: () => {
            $("applyBtn").disabled = false;
            setStatus('Loaded. Edit "Message" in the panel, or set it via the SDK.');
          },
        };

        if (projectId) {
          config.projectId = projectId;
          config.projectDownloadUrl = envBase + "/projects/" + projectId + "/document";
          config.projectUploadUrl = envBase + "/projects/" + projectId;
        } else {
          const info = { id: "hello-world", name: "Hello World", template: { id: "hello-world" } };
          config.onProjectInfoRequested = async () => info;
          config.onProjectDocumentRequested = async () => HELLO_DOCUMENT;
          config.onProjectSave = async () => info;
        }

        setStatus("Loading Studio UI…");
        window.StudioUI.studioUILoaderConfig(config);
        $("applyBtn").disabled = false; // fallback if onProjectLoaded isn't emitted
      });

      // Drive the loaded Studio UI through its SDK (window.StudioUISDK).
      $("applyBtn").addEventListener("click", async () => {
        const sdk = window.StudioUISDK;
        if (!sdk) {
          setStatus("Studio UI is still loading — try again in a moment.");
          return;
        }
        const variable = (await sdk.variable.getByName("Message")).parsedData;
        if (!variable) {
          setStatus('This document has no "Message" variable.');
          return;
        }
        const result = await sdk.variable.setValue(variable.id, $("valueInput").value);
        setStatus(result.success ? "Variable updated via SDK." : "Could not update the variable.");
      });
    </script>
  </body>
</html>
```

## Run it

Serve the folder over HTTP (Studio UI needs a real origin, not a `file://` page):

```bash
python3 -m http.server 3000
```

Visit `http://localhost:3000`, enter your environment name and the token from Step 1 (leave **Project ID** empty), and click **Load Studio UI**. The editor opens the sample document. Type into the Message field and click **Set variable via SDK** — the value updates on the canvas and in the variables panel. To open one of your own projects instead, fill in its **Project ID**.

## Customize and go further

- **Theming and widgets** — colors, fonts, and which controls appear are set through `uiOptions`. See the [advanced integration guide](https://github.com/chili-publish/studio-ui/blob/main/documentation/advanced-integration.md).
- **Validate before submitting** — the object returned by `studioUILoaderConfig` has a `validateVariables()` method for gating your own Save/Submit button.

## Where to go next

- [Integrate Studio UI](/GraFx-Developers/grafx-studio/editor-engine/integrate-studio-ui/) — overview and links.
- [Studio UI on GitHub](https://github.com/chili-publish/studio-ui) — the source and full integration guide.
- [Studio SDK Quickstart](/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/01-overview/) — build on the bare Editor Engine instead.
- [Generating a token](/GraFx-Developers/environment-api/03-generating-a-token/) — the full authentication flow.
