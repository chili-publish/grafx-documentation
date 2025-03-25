# Media Connector Fundamentals

A Media Connector is a JavaScript class that provides methods utilized by the Studio Engine and the Studio SDK. This guide offers a high-level overview of Connectors.

## Requirements

- Basic understanding of modern JavaScript
- Familiarity with asynchronous programming (Promises)
- Basic experience with the GraFx Studio Template Designer Workspace

## Isolation

Media Connectors run in a limited isolated environment, which means they don't have access to many browser APIs or Node.js APIs. This isolation serves two primary purposes:

1. **Security**: JavaScript runs on the server, so it's crucial that it cannot directly access APIs that could compromise customer data.
2. **Performance**: By limiting available APIs, scripts remain small and easier to optimize for performance.

Due to this isolation, you cannot access the `window` object or many commonly used methods like `console.log`.

## Runtime

Instead of browser globals, Connectors use a `ConnectorRuntimeContext`, which is passed to the constructor of a Connector class. It's common practice to store this on a `runtime` property:

```typescript
export default class MyConnector implements Media.MediaConnector {
  private runtime: Connector.ConnectorRuntimeContext;

  constructor(runtime: Connector.ConnectorRuntimeContext) {
    this.runtime = runtime;
  }
}
```

The `runtime` object provides methods like `fetch` and `logError` to replace similar functionality found in browser environments.

Think of your JavaScript as running inside a limited JavaScript engine, with `runtime` functions serving as a bridge to the outside world.

## Connector Methods

Your Connector class needs to implement five key methods:

1. getCapabilities
2. getConfigurationOptions
3. query
4. download
5. detail

### getCapabilities Method

This method communicates to the SDK what features the Connector supports:

```typescript
getCapabilities(): Media.MediaConnectorCapabilities {
  return {
    query: true,
    detail: true,
    filtering: false,
    metadata: false,
  };
}
```

!!! note "Requirements"

    The built-in CHILI GUI currently requires at least `query` and `detail` to be set to `true` to make connector functional properly.

### getConfigurationOptions Method

The `getConfigurationOptions`  method allows Connector developers to define customizable settings that template designers can use to modify the behavior of the Connector.

```typescript
getConfigurationOptions(): Connector.ConnectorConfigValue[] | null {
  return [{
    name: "example",
    displayName: "Displayed In UI",
    type: "text"
  }];
}
```

When you define configuration options in this method, you're essentially telling the SDK, "My Connector supports these customization options." These values can then be accessed and utilized in other methods of your Connector through the `context` argument.

### query Method

The `query` method is called by the SDK and the engine in two scenarios:

- When browsing assets for an image variable or using the media panel.
- Before `download` for `thumbnail` previewType if `filtering` is set to `true` in `getCapabilities`.

!!! warning "query can be called in different scenarios"

    This may seem inconsequential, but is important to understand that this method can be called in multiple scenarios and the arguments and response in each scenario have different expectations.

```typescript
async query(
  options: Connector.QueryOptions,
  context: Connector.Dictionary
): Promise<Media.MediaPage> {
  // Implement your query logic here
}
```

It should return a `MediaPage` object:

```typescript
export interface MediaPage {
  pageSize: number;
  data: Media[];
  links: {
    nextPage: string;
  };
}
```

Currently, only the `data` and `links.nextPage` properties are crucial for displaying image options in the built-in GUIs. The `pageSize` has no effect at present.

#### Notes on "query"

- The `options` parameter provides query options set by the UI.
    - `pageToken` and `pageSize` properties are for pagination.
    - `filter` property is to filter out your results based on some condition.
    - `collection` property is when you have a folder structure in your DAM and want to request particular assets from selected folder. Specifies as path string, i.e. `/folder-1/sub-folder-2/sub-sub-folder-3`. `Root` is defined as `/`.
- The returned `nextPage` in the `MediaPage.links` is meant to be passed back as `pageToken` during pagination

### download Method

The `download` method is responsible for retrieving image data for display in built-in GUIs and image frames in the Studio engine.

```typescript
download(
  id: string,
  previewType: Media.DownloadType,
  intent: Media.DownloadIntent,
  context: Connector.Dictionary
): Promise<Connector.ArrayBufferPointer> {
  // Implement your download logic here
}
```

The method returns a `Promise<Connector.ArrayBufferPointer>`. This `ArrayBufferPointer` must be obtained from a successful `runtime.fetch` request.

The `download` method is invoked in various scenarios to retrieve image data. Its behavior should adapt based on the `previewType` and `intent` parameters to provide the most appropriate image format and quality.

#### Preview Types
The `previewType` parameter can have these values:

- **thumbnail**: Used when requesting the image preview in the Variable panel.
- **mediumres**: Used when requesting images in the media panel and the variable "Select image" modal.
- **highres**: Used when loading images into frames in the editor in the browser.
- **fullres**: Used during output for requesting the images to be loaded in frames.

!!! note "Remember Custom UIs"

    Custom GUI editors may request previewTypes for different scenarios.

#### Download Intents
The `intent` parameter specifies the platform the `download` was called:

- **web**: For in-browser display and image output.
- **print**: For PDF output.
- **animation**: For GIF and MP4 output.

#### Supported Formats

DownloadType / DownloadIntent | *web* (= browser based editing session) | *print* (= PDF output, High res image output) | *animation* (= Gif, mp4 output, compression will be applied)
-- | -- | -- | --
*thumbnail* | ✓ (e.g., Displaying small preview images on a webpage) |   |
*mediumres* | ✓ (e.g., Displaying larger images on a webpage without slowing down load times) | ✓ (e.g., Printing a decent-quality image where high resolution is not crucial) |
*highres* | ✓ (e.g., Downloading a high-quality image for use on a high-resolution display) | ✓ (e.g., Printing a high-quality, large-scale image) | ✓ (e.g., Using as a frame in a high-quality animation)
*fullres* (PDF / PNG / JPEG) For image types other then PNG / JPEG one should serve the asset wrapped as a PDF file |   | ✓ (e.g., Printing the original PDF or image file in its highest quality) |
*original* | ✓ | ✓ | ✓

### detail Method

The `detail` method is called in two scenarios:

- When a user double-clicks an image in the media panel to create the image frame and set assets to it or set assets to the selected image frame.
- Before `download` for `thumbnail` previewType if `filtering` is set to `false` in `getCapabilities`.

```typescript
async detail(
  id: string,
  context: Connector.Dictionary
): Promise<Media.MediaDetail> {
  // Implement your detail logic here
}
```

Although not strictly required by the type signature, the Template Designer Workspace expects width and height information to set the initial image frame size. If omitted, built-in GUI’s defaults are used instead.

## Next Steps

1. Follow the [Build a Simple Media Connector](/GraFx-Developers/connectors/media-connector/build-a-simple-media-connector/) tutorial to learn how to build a simple Connectors.
2. Review the [Authorization for Connectors](/GraFx-Developers/connectors/authorization-for-connectors/) for understanding how to add authorization to your Connector.
