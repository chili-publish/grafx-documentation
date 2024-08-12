# Media Connector Fundamentals

A Media Connector is a JavaScript class that provides methods utilized by the Studio Engine and the Studio SDK. This guide offers a high-level overview of Connectors. For an in-depth exploration of all technical details, refer to the [Comprehensive Media Connector Reference Guide]().

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
    filtering: true,
    metadata: false,
  };
}
```

!!! note "Requirements"

    The built-in CHILI GUI currently requires `query` support, and `filtering` must be set to `true` even if not implemented.

### getConfigurationOptions method

The `getConfigurationOptions`  method allows Connector developers to define customizable settings that template designers can use to modify the behavior of the Connector.

```typescript
getConfigurationOptions(): Connector.ConnectorConfigValue[] | null {
  return [];
}
```

When you define configuration options in this method, you're essentially telling the SDK, "My Connector supports these customization options." These values can then be accessed and utilized in other methods of your Connector through the context argument.

### query Method

The `query` method is called by the SDK when selecting an image for an image variable or using the media panel:

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

Currently, only the `data` property is crucial for displaying image options in built-in GUIs.

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

- thumbnail: Used for image selection in built-in GUIs.
- mediumres: Not currently used, but may be used in the future.
- highres: Used when loading images into frames.
- fullres: Used only during `intent` type "print".

#### Download Intents
The `intent` parameter specifies the platform the `download` was called:

- web: For in-browser display.
- print: For PDF or image output.
- animation: For GIF and MP4 output.

#### Supported Formats

- For all combinations of `previewType` and `intent`, PNG and JPEG formats are acceptable.
- When `intent` is "print", PDF format is also acceptable in addition to PNG and JPEG.

### detail Method

The `detail` method is called when a user double-clicks an image in the media panel to set the image frame size:

```typescript
async detail(
  id: string,
  context: Connector.Dictionary
): Promise<Media.MediaDetail> {
  // Implement your detail logic here
}
```

Although not strictly required by the type signature, the Template Designer Workspace expects width and height information. It's acceptable to return default values as this only set the initial frame size.
