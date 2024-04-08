# Section 6: Working with Events
_Note: We will be started off in this section with what we created in the previous section [Setting Up the Project](../1-Setting-up-Project/). If you are starting at this section you can get the project (so far) from the previous section by downloading and navigating to the "GraFx Integration Course" folder in that section._

_Please refer to the [Getting up and running](../README.md#getting-up-and-running) section to get the integration webserver up and running._

---

## Reacting vs Telling
Everything we have done up to this point has been imperative where we tell Studio to do something via the SDK and it does what we tell it. With events, we will turn this process around and instead ask Studio to to tell us when it does something so we can react.

This is how this section will differ from pervious sections:

| Previously | Working With Events|
|----------|----------|
|   You tell Studio what to do via SDK executes instructions.  |   Studio informs you about its actions via event callbacks, and we react to those events.   |

Why would you want to work this way?

Well sometimes you want to know when something happens so your application can react. A good example is if someone selects a frame. When that happens, your customer user interface may want to show or hide specific options if the frame is an image frame or the frame is a text frame.

Let us learn how to react to events.

## Reacting to Events
All events that are fired off in Studio can be listen to via the creation of the `StudioSDK` class.

In our `index.js` file we create the class via the function `initEditor()`.

The function reads:
```js
async function initEditor() {
  const token = await generateToken();
  const environmentAPI = window.SDK.utils.createEnvironmentBaseURL({type: "production", environment: "<ENVIRONMENT>"});

  if (token == null) {
    throw new Error("Token is null or undefined");
  }

  const SDK = new StudioSDK({
    editorId: "studio-editor"
  });

  SDK.loadEditor();
  window.SDK = SDK;

  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioAuthToken, token);
  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioEnvironmentApiUrl, environmentAPI);

  await loadDocument(defaultJSON);
}
```

When we create the `StudioSDK` we pass in a [ConfigType](https://chili-publish.github.io/studio-sdk/types/index.ConfigType.html) object. In our original implementation of the function we are only setting the `editorId` property which is the ID of an element where the Studio editor will appended to in the live site.

If you go an look at the documentation of [ConfigType](https://chili-publish.github.io/studio-sdk/types/index.ConfigType.html), you will find that the [ConfigType](https://chili-publish.github.io/studio-sdk/types/index.ConfigType.html) object allows a number of optional properties.

All the properties that start with "on" are properties that expect a function to be set, which the SDK will call when a specific event is fired.

For example, on the [ConfigType](https://chili-publish.github.io/studio-sdk/types/index.ConfigType.html) object there is a property called `onDocumentLoaded`.

The "on" lets us know this is a callback for an event. The "DocumentLoaded" is the event.

Unfortunately at this moment there is not a comprehensive list of when each event is fired. However, the naming of the event should give you a good hint of when the even event is fired.

Once we know the event property on the [ConfigType](https://chili-publish.github.io/studio-sdk/types/index.ConfigType.html) that we want to react to, we can assign and callback function.

For example, if we want to have a callback function fired when the document is loaded we can add a function to the `onDocumentLoaded` property.

We create a new function called `documentLoaded` and add that function on the `onDocumentLoaded` property.
```js
async function initEditor() {
  const token = await generateToken();
  const environmentAPI = window.SDK.utils.createEnvironmentBaseURL({type: "production", environment: "<ENVIRONMENT>"});

  if (token == null) {
    throw new Error("Token is null or undefined");
  }

  const SDK = new StudioSDK({
    editorId: "studio-editor",
    onDocumentLoaded: documentLoaded
  });

  SDK.loadEditor();
  window.SDK = SDK;

  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioAuthToken, token);
  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioEnvironmentApiUrl, environmentAPI);

  await loadDocument(defaultJSON);
}

function documentLoaded() {
  console.log("DocumentLoaded event called this function")
}
```

If you now test your integration, you will find in your browser dev console the log "DocumentLoaded event called this function".

## Callbacks and Parameters
The `onDocumentLoad` property expects a function of type:
```ts
() => void
```

This is a function signature which is using the [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) syntax.

A quick lesson on arrow functions is that a normal function expression looks like this:
```ts
function(parameter1, parameter2) {
  return;
}
```
This is a function which takes 2 parameters and returns `undefined`.

We could write this same function in the arrow syntax:
```ts
(parameter1, parameter2) => {return;}
```

The arrow syntax is just a more compressed way to write function without a name.

So for example, we could get rid of our `documentLoaded()` function and replace it with:

```js
async function initEditor() {
  const token = await generateToken();
  const environmentAPI = window.SDK.utils.createEnvironmentBaseURL({type: "production", environment: "<ENVIRONMENT>"});

  if (token == null) {
    throw new Error("Token is null or undefined");
  }

  const SDK = new StudioSDK({
    editorId: "studio-editor",
    onDocumentLoaded: function() {
      console.log("DocumentLoaded event called this function");
    }
  });

  SDK.loadEditor();
  window.SDK = SDK;

  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioAuthToken, token);
  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioEnvironmentApiUrl, environmentAPI);

  await loadDocument(defaultJSON);
}

// function documentLoaded() {
//   console.log("DocumentLoaded event called this function")
// }
```

Or we can make it more compact and use an arrow function:

```js
async function initEditor() {
  const token = await generateToken();
  const environmentAPI = window.SDK.utils.createEnvironmentBaseURL({type: "production", environment: "<ENVIRONMENT>"});

  if (token == null) {
    throw new Error("Token is null or undefined");
  }

  const SDK = new StudioSDK({
    editorId: "studio-editor",
    onDocumentLoaded: () => {
      console.log("DocumentLoaded event called this function");
    }
  });

  SDK.loadEditor();
  window.SDK = SDK;

  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioAuthToken, token);
  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioEnvironmentApiUrl, environmentAPI);

  await loadDocument(defaultJSON);
}

// function documentLoaded() {
//   console.log("DocumentLoaded event called this function")
// }
```

Either of the three ways gets you the same result, a function that is called when the DocumentLoaded event is fired.

So the `onDocumentLoad` property expects a function of type:
```ts
() => void
```

Meaning it expects a function with zero parameters and that returns `undefined`. In TypeScript, which is what the SDK was written in, `void` is the same as `undefined`.

All of the callback event properties on an object of [ConfigType](https://chili-publish.github.io/studio-sdk/types/index.ConfigType.html) have a type signature which tells you what type of function the property expects to call when the event is fired.

For example, the `onSelectedToolChanged` property expects a function of type:
```ts
(tool: ToolType) => void
```

When the SelectedToolChanged event is fired, the function provided to `onSelectedToolChanged` will be called and the SDK will call that function by passing in a property of type `ToolType`.

In TypeScript, which is what the SDK is written in, the semicolon `:` described the type of the property.

If you are interested, you can read more about TypeScript types here: [everyday types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html).

Now `ToolType` is a custom type, if you click on the [ToolType](https://chili-publish.github.io/studio-sdk/enums/index.ToolType.html) name in the documentation, it will take you to page to describe the type of type it is.

It is a enumeration type, an enum.

TypeScript is really cool, but unfortunately it can make things a bit more complicated if you are not use to typed languages.

You can read about enums here: [enums](https://www.typescriptlang.org/docs/handbook/enums.html), but the basics is that is type that can only be specific values.

In the case of [ToolType](https://chili-publish.github.io/studio-sdk/enums/index.ToolType.html) that would be: 
- HAND
- IMAGE_FRAME
- SELECT
- SHAPE_ELLIPSE
- SHAPE_POLYGON
- SHAPE_RECT
- TEXT_FRAME
- ZOOM

On the [ToolType](https://chili-publish.github.io/studio-sdk/enums/index.ToolType.html) documentation page it even gives you the underline value of each options. HAND = "hand" and TEXT_FRAME = "textFrame".

Again, this might seem complicated, but really all this documentation means is that if we want to write a function for `onSelectedToolChanged` we need to write a function that takes in one parameter and returns nothing.

So we could write a function like:
```js
function(tool) {
  console.log(tool);
}
```

We can then add this function to when we create our `StudioSDK` class.

```js
async function initEditor() {
  const token = await generateToken();
  const environmentAPI = window.SDK.utils.createEnvironmentBaseURL({type: "production", environment: "<ENVIRONMENT>"});

  if (token == null) {
    throw new Error("Token is null or undefined");
  }

  const SDK = new StudioSDK({
    editorId: "studio-editor",
    onDocumentLoaded: function() {
      console.log("DocumentLoaded event called this function");
    },
    onSelectedToolChanged: function(tool) {
      console.log(tool);
    }
  });

  SDK.loadEditor();
  window.SDK = SDK;

  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioAuthToken, token);
  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioEnvironmentApiUrl, environmentAPI);

  await loadDocument(defaultJSON);
}
```

Now, if you test your integration and you press one of the buttons we added in section 4 to change the tool, you will get log in your browser dev console telling you what tool you selected.

So if you click the the `Hand Tool` button you get the log:
```
hand
```

If you click the `Text Tool` button you get the log:
```
textFrame
```

## Writing a reaction
We can use our new found abilities to react to events to something useful.

We have three buttons for three different tools. It looks like this in our `index.html` file:
```html
<button onclick="setTool('select')">Select Tool</button>
<button onclick="setTool('hand')">Hand Tool</button>
<button onclick="setTool('text')">Text Tool</button>
```

Let's add a ID to each button and update our `index.html` file making sure the ID contains the same string that would be found in the the enum `ToolType`. So in this case: "select", "hand", "textFrame".
```html
<button id="selectButton" onclick="setTool('select')">Select Tool</button>
<button id="handButton" onclick="setTool('hand')">Hand Tool</button>
<button id="textFrameButton" onclick="setTool('textFrame')">Text Tool</button>
```

Now that our `index.html` is updated we can update our `onSelectedToolChanged` function in `index.js` to disable the button related to the tool that is selected.

First, lets get all the button elements and place them in an array.

```js
async function initEditor() {
  const token = await generateToken();
  const environmentAPI = window.SDK.utils.createEnvironmentBaseURL({type: "production", environment: "<ENVIRONMENT>"});

  if (token == null) {
    throw new Error("Token is null or undefined");
  }

  const SDK = new StudioSDK({
    editorId: "studio-editor",
    onDocumentLoaded: function() {
      console.log("DocumentLoaded event called this function");
    },
    onSelectedToolChanged: function(tool) {
      const buttonElements = [
        document.getElementById("selectButton"),
        document.getElementById("handButton"),
        document.getElementById("textFrameButton"),
      ]
    }
  });

  SDK.loadEditor();
  window.SDK = SDK;

  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioAuthToken, token);
  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioEnvironmentApiUrl, environmentAPI);

  await loadDocument(defaultJSON);
}
```

Second, we will go through every element in the array and if the id of that element contains the string of our `tool` property we will set `disabled` to `true` otherwise we will set `disabled` to `false`.

```js
async function initEditor() {
  const token = await generateToken();
  const environmentAPI = window.SDK.utils.createEnvironmentBaseURL({type: "production", environment: "<ENVIRONMENT>"});

  if (token == null) {
    throw new Error("Token is null or undefined");
  }

  const SDK = new StudioSDK({
    editorId: "studio-editor",
    onDocumentLoaded: function() {
      console.log("DocumentLoaded event called this function");
    },
    onSelectedToolChanged: function(tool) {
      const buttonElements = [
        document.getElementById("selectButton"),
        document.getElementById("handButton"),
        document.getElementById("textFrameButton"),
      ]

      for (const element of buttonElements) {
        if (element.id.includes(tool)) {
          element.disabled = true;
        }
        else {
          element.disabled = false;
        }
      }
    }
  });

  SDK.loadEditor();
  window.SDK = SDK;

  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioAuthToken, token);
  SDK.configuration.setValue(WellKnownConfigurationKeys.GraFxStudioEnvironmentApiUrl, environmentAPI);

  await loadDocument(defaultJSON);
}
```

Now we have a function that reacts when the SelectedToolChanged event is fired because we set that function to the `onSelectedToolChanged` property during the creation of our `StudioSDK` class.

If you load up your integration, you will find that when you click any of the tool buttons, that specific button you clicked is disabled and all others are enabled.

## Conclusions
Now that you you know how to react to events, you can both react to Studio and tell Studio what you want to do. With these to abilities you are ready to build your own integration.