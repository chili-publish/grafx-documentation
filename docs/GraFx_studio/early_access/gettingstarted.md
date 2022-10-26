# Early Access: Getting Started

GraFx Studio is the second generation of the suite of tools to automate the variants output.

Depending on your profile, we'll guide you through the documentation that is relevant to you.

The Early Access phase started in February 2022, and ends with the release of GraFx Studio Alpha.

## I want to: Integrate the editor

Targeted for **software engineers, integrators**

I am a developer, and I'm looking for the resources where to start, and how to integrate the editor.

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

### Debug panel

On the top left of the editor canvas there is a button to open the debug panel. This panel shows a log of all interactions with the editor engine. This can help while building your integration.

### GraFx Connector

With a GraFx Connector you can connect GraFx Studio to a resource provider.

We prepared a [GraFx Connector template](https://github.com/chili-publish/grafx-connector-template){target="_blank"} that you can use to create a custom media connector to connect with your DAM system or to add hardcoded image URLs. With this media connector you can assign your own assets to image frames in GraFx Studio.

In the demo integrations project there is an [example](https://github.com/chili-publish/editor-sdk-integration-examples/tree/main/ts-connector-example){target="_blank"} that shows how to set up and use a very simple media connector. When your custom connector is ready, you can use this example as inspiration to set it up and start using it.

## I want to: Check out the new features

Targeted for **Template designers**

I am a designer and want to check out the new user interface and create some cool animations for different layouts!

Please go to [Sandbox](https://editor2.chili-publish-sandbox.online/) and log in with your CHILI account to try it out yourself.

Take a look at this page, to get an overview of the [Template designer workspace](/GraFx_studio/workspace_elements/).


![appscreen](https://chilipublishdocs.imgix.net/GraFx_studio/earlyaccess.png?w=800)

## I want to: Convince my boss to use CHILI GraFx

[Let us help you](https://www.chili-publish.com/request-a-demo/). We can setup a Proof of Concept to show you how fast an integration is done, and how fast we can setup a smart template.
