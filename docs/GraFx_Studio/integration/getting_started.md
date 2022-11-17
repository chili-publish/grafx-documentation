---
tags:
  - studioAPI
---

# GraFx studio integration

GraFx studio is a client side browser application.
It contains 3 elements

- The Editor SDK
- The workspace
- Your application 

The **Editor SDK** is an open source SDK that connects the Editor Engine (also referenced as “The Canvas”) which renders your document. This engine does not have tools (aka the Editor Engine).
 
The **Workspace** is the set of panels and elements pre-built by CHILI publish to interact with your document canvas aka the **Editor SDK**.
The **workspace** will NOT be covered in this first version.

**Your application** is the custom code that will make it your application, also referenced as "the integration".

[Next up: setting up your Local environment](local_environment.md)

Or click "Next" on the bottom right of the page to see the next page.

---

## I want to: Integrate the editor

### SDK

To integrate GraFx Studio you will make use of the editor SDK. This SDK dynamically loads the editor engine and can be integrated in a custom application.

We have an [SDK reference documentation](/GraFx_studio/sdk/){target="_blank"} and the [SDK codebase](https://github.com/chili-publish/editor-sdk){target="_blank"} is open sourced.

### Demo integrations

To make life easier, we have created a couple of [demo integrations](https://github.com/chili-publish/editor-sdk-integration-examples){target="_blank"}, so you don't have to start from scratch.

You can use this script in your HTML to always get the latest SDK version:


``` js
<script src="https://cdnepgrafxstudioprd.azureedge.net/sdk/latest/main.js"></script>
```

Or you can use NPM to install a specific SDK version, with the following command:

``` bash
npm install @chili-publish/editor-sdk
```

#### stateChanged event will be deprecated

You should subscribe to specific events instead of the global stateChanged event, which will be deprecated soon. You can find the available events in the [documentation](https://docs.chiligrafx.com/GraFx_studio/sdk/classes/controllers_SubscriberController.SubscriberController/){target="_blank"} or in the [code](https://github.com/chili-publish/editor-sdk/blob/main/src/controllers/SubscriberController.ts){target="_blank"}.

### Debug panel

On the top left of the editor canvas there is a button to open the debug panel. This panel shows a log of all interactions with the editor engine. This can help while building your integration.

### GraFx Connector

With a GraFx Connector you can connect GraFx Studio to a resource provider.

We prepared a [GraFx Connector template](https://github.com/chili-publish/grafx-connector-template){target="_blank"} that you can use to create a custom media connector to connect with your DAM system or to add hardcoded image URLs. With this media connector you can assign your own assets to image frames in GraFx Studio.

In the demo integrations project there is an [example](https://github.com/chili-publish/editor-sdk-integration-examples/tree/main/ts-connector-example){target="_blank"} that shows how to set up and use a very simple media connector. When your custom connector is ready, you can use this example as inspiration to set it up and start using it.