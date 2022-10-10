# Early Access: Getting Started

GraFx Studio is the second generation of the suite of tools to automate the variants output.

Depending on your profile, we'll guide you through the documentation that is relevant to you.

The Early Access phase started in February 2022, and ends with the release of GraFx Studio Alpha.

## I want to: Integrate the editor

Targeted for: Software engineers, integrators

I am a developer, and I'm looking for the resources where to start, and how to integrate the editor.

``` js
<script src="https://chili-dev.azureedge.net/stable/early-access/sdk/v0.0.3/main.js"></script>
<script src="integration.js"></script>
```

```js
const sdk = new EditorSDK({
    editorLink: 'https://chili-dev.azureedge.net/stable/early-access/editor/v0.0.3/web',
    editorId: 'my-editor', // if not provided, default will be 'chili-editor'
});
```

See the [full integration guide](/GraFx_studio/integration/getting_started/).

To make life even more easy, we have created a [demo integration](https://github.com/chili-publish/editor-sdk-integration-examples), so you don't have to start from scratch.

- For the 'editorLink' you should use the URL provided in the code snippet above.
- For the link to the SDK you can also use the URL above or you can build the SDK yourself. The [code is available here](https://github.com/chili-publish/editor-sdk)

## I want to: Check out the new features

Targeted for: **Template designers**

I am a designer and want to check out the new user interface and create some cool animations for different layouts!

Please go to [Sandbox](https://editor2.chili-publish-sandbox.online/) and log in with your CHILI account to try it out yourself.

Take a look at this page, to get an overview of the [Template designer workspace](/GraFx_studio/workspace_elements/).

## I want to: Convince my boss to use CHILI GraFx

[Let us help you](https://www.chili-publish.com/request-a-demo/). We can setup a Proof of Concept to show you how fast an integration is done, and how fast we can setup a smart template.