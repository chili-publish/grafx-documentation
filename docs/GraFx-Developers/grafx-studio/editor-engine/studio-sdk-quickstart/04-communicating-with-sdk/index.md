# Communicating With SDK

## Controllers

Now that we have a loaded editor, we can interact with it via our `studio` variable which contains and instance of the `StudioSDK` class. We can interact with our document.

The `StudioSDK` class has properties, which are called controllers in the documentation. Each controller has functions that allow you to interact with Editor Engine.

We have already seen a few examples already `studio.configuration` and `studio.document`.

- [Configuration Controller](https://chili-publish.github.io/studio-sdk/classes/controllers_ConfigurationController.ConfigurationController.html) allows setting editor session data. This data is not stored in the document and can only be used at runtime. Amongst others, the configuration store is available to the editor connectors and JavaScript actions running in the editor.
- [Document Controller](https://chili-publish.github.io/studio-sdk/classes/controllers_DocumentController.DocumentController.html) is responsible for all communication regarding loading and getting the state of the document.

When you call a function on a controller like `studio.document.load` you will get back a Promise that will resolve into a specific data form that looks like:

```typescript
{
  "success": boolean,
  "status": number,
  "data": string,
  "parsedData": any
}
```

You can see all the controllers and functions here: [StudioSDK Class Documentation](https://chili-publish.github.io/studio-sdk/).

## Events

Functions on controllers are acting, while events are reactiving. You need to register to them when you create your `StudioSDK` class. There are many events like `onZoomChanged` or `onLayoutsChanged`.

To register to an event, you just need to add a callback function to the correct property on `ConfigType` passed to the initialization of the `StudioSDK` class.

```javascript
const studio = new StudioSDK({
  editorId: "studio",
  onSelectedFramesContentChanged: (frames) => { console.log(frames) }
});
```

Give it a try, and update your `index.ts` file with a callback function on `onSelectedFramesContentChanged` as provided in the code example about. After restarting your server, when you move select a frame, take a look at the console.

You can see all the options in [ConfigType](https://chili-publish.github.io/studio-sdk/types/types_CommonTypes.ConfigType.html)
