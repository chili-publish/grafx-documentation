# Create your custom app

Make index.html, include JS file

!!! note
	
	index.html is not part of the "app", could be hosted elsewere, just need to load the js bundle. 
	For the ease of the demo, we'll host it in the root. 
	
	That does define how the link is made to the js file in this case

HTML source:
	
``` html
<!DOCTYPE html>
<html>
<head>
	<title>My First CHILI GraFx app</title>
</head>
<body>
	
	<script src="./dist/bundje.js"></script>
</body>
</html>

```
## Import the Editor SDK

Add this line to your index.js

``` js
import EditorSDK from "@chili-publish/editor-sdk";
```

## Go to your (local) URL in your browser

![Properties](https://chilipublishdocs.imgix.net/GraFx_studio/integration/browse.png?w=680&q=80)

You are now ready to call the Editor SDK in your application

## Basics needed to load Canvas and Basic functions

``` js
import EditorSDK from "@chili-publish/editor-sdk";
// import chilidoc from "../assets/demo.json";

// link to flutter engine
// NEEDS to be kept secret (for now, before release)
// how link is passed to intergrator / customer, needs to be defined / researched
const editorLink = "https://chili-dev.azureedge.net/stable/early-access/editor/v0.0.4/web";

// For this demo, we'll hardcode the link to a document on the server
// Later, you'll access a doc through media or own media server
const documentlink = editorLink+"/assets/assets/documents/demo.json"

// function to load the document fetched, into the editor SDK, convert json to string
const loadDocument = async (chilidoc) => {
  window.SDK.document.loadDocument(JSON.stringify(await chilidoc));
}

// Define function to fetch document, and store data in json
const fetchDocument = async () => {
  const response = 
  await fetch(documentlink);
  loadDocument(response.json());
}

// Define config key-value pairs
// State function definition Might be optional soon (defined by default)
const config = {

  onStateChanged: function (state) {
    return;
  },
  onSelectedFrameLayoutChanged: function (state) {
    return;
  },
  onSelectedFrameContentChanged: function (state) {
    return;
  },
  onPageSelectionChanged: function () {
    return;
  },
  onSelectedLayoutPropertiesChanged: function (
    state) {
    return;
  },
  onScrubberPositionChanged: function (state) {
    return;
  },
  onFrameAnimationsChanged: function (
    animationState
  ) {
    return;
  },
  onVariableListChanged: function (variableList) {
    return;
  },
  onSelectedToolChanged: function (tool) {
    return;
  },

  editorLink,
  editorId: "canvas", // If empty, default is "chili-editor"
};

// define the SDK instance as "SDK"
// initialize SDK
const SDK = new EditorSDK(config);  // (use config when loading)

// execute app
window.SDK = SDK;                   // bind object to window

// execute the load editor, to load engine into the window
SDK.loadEditor();                   // will use config constant

// Fetches, and loads the document into the canvas
fetchDocument();

```

## All available controllers / classes

Documented here (will move to current documentation site)

[Classes](/GraFx_studio/sdk/)