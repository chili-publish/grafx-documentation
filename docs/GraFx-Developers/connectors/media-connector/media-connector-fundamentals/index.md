# Media Connector Fundamentals

A media connector is a JavaScript class that provides methods utilized by the Studio Engine and the Studio SDK. This guide offers a high-level overview of connectors.

## Requirements

- Basic understanding of modern JavaScript
- Familiarity with asynchronous programming (Promises)
- Basic experience with the GraFx Studio Template Designer Workspace

## Isolation

Media connectors run in a limited isolated environment, which means they don't have access to many browser APIs or Node.js APIs. This isolation serves two primary purposes:

1. **Security**: JavaScript runs on the server, so it's crucial that it cannot directly access APIs that could compromise customer data.
2. **Performance**: By limiting available APIs, scripts remain small and easier to optimize for performance.

Due to this isolation, you cannot access the `window` object or many commonly used methods like `console.log`. You also cannot import arbitrary npm packages — only local project `.ts` modules and `@chili-publish/studio-connectors` are allowed at build time. See [Connector CLI](/GraFx-Developers/connectors/connector-cli/).

## Runtime

Instead of browser globals, connectors use a `ConnectorRuntimeContext`, which is passed to the constructor of a connector class. It's common practice to store this on a `runtime` property:

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

Your connector class needs to implement five key methods:

1. getCapabilities
2. getConfigurationOptions
3. query
4. download
5. detail

### getCapabilities Method

This method communicates to the SDK what features the connector supports:

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
    To take advantage of a maximum of GraFx Studio features, it's advised to at least implement 'detail' and 'query'

### getConfigurationOptions Method

The `getConfigurationOptions`  method allows connector developers to define customizable settings that template designers can use to modify the behavior of the connector.

```typescript
getConfigurationOptions(): Connector.ConnectorConfigValue[] | null {
  return [{
    name: "example",
    displayName: "Displayed In UI",
    type: "text"
  }];
}
```

When you define configuration options in this method, you're essentially telling the SDK, "My connector supports these customization options." These values can then be accessed and utilized in other methods of your connector through the `context` argument.

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

#### Download Intents
The `intent` parameter tells you what the image will be used for:

- **web**: Display in the browser editor, and PNG / JPEG image output.
- **print**: PDF output.
- **animation**: GIF and MP4 output.

#### Preview Types
The `previewType` parameter tells you which rendition of the asset Studio needs.

Preview type | Where Studio requests it | Recommended size | Formats | Intents Studio uses
-- | -- | -- | -- | --
`thumbnail` | Image variable preview in the Variables panel, and the placeholder shown while `highres` loads | 200–400px | PNG, JPEG | web
`mediumres` | Media panel and the image variable "Select image" modal | 1000–2000px | PNG, JPEG | web
`highres` | Images in frames on the editor canvas, and image drop shadows in PDF output | The largest raster preview your DAM has, ideally 2000–4000px | PNG, JPEG | web, print
`fullres` | Images in frames during output | Print: the original PNG, JPEG or PDF file. Web and animation: a large raster, around 4096px | PNG, JPEG; PDF for print only | web, print, animation

The sizes are recommended targets for the longest side, not required dimensions:

- **Never upscale.** If your DAM has no rendition that large, return the largest one it has. Studio scales the image to the frame.
- **Keep the same framing in every rendition.** Each rendition must show the full image with the same aspect ratio. Do not crop, letterbox or pad it. Studio stores crops and smart-crop areas relative to the image, so they land in the wrong place if the editor image (`highres`) and the output image (`fullres`) are framed differently.
- **Keep files reasonable.** Very large `highres` renditions slow down the browser editor. Smart crop only uses renditions up to 10 MB: it tries `mediumres`, then `highres`, then `thumbnail`.

`original` is also a valid `previewType`, but Studio does not request it today. If an integration calls `download` with `original` through the SDK, return the unmodified source file. Studio passes the bytes to the caller without decoding them, so the format rules below do not apply.

!!! note "Remember Custom UIs"

    Custom GUI editors and SDK integrations can request any combination of `previewType` and `intent`, not only the ones in the table. Apply the same rules whatever the intent: return PNG or JPEG for `thumbnail`, `mediumres` and `highres`, and follow the intent-specific rules below for `fullres`.

!!! note "Deprecated names"

    The deprecated SDK values `HighResolutionWeb` and `LowResolutionWeb` map to `highres` and `thumbnail`.

#### Supported Formats

Return **PNG** or **JPEG** for every raster rendition, and **PDF** only for `fullres` with intent `print`. Studio detects the format from the file contents, not from the file name or headers. Other formats (for example TIFF, SVG, EPS or PSD) are not supported: they cause errors in PDF output and may not display in the editor. Convert them first.

- `thumbnail`, `mediumres` and `highres`: return PNG or JPEG. Never return a PDF; `highres` is also used for drop shadows in PDF output, which fail on a PDF image.
- `fullres` with intent `print`: return PNG, JPEG or PDF files as-is, so the original quality and color space reach the PDF. For any other asset type, generate a PDF that contains the asset.
- `fullres` with intent `web` or `animation`: return PNG or JPEG. Convert any other asset type, including PDF, to PNG or JPEG.

When you return a PDF for print, Studio embeds it in the output without rasterizing or converting it:

- Vectors stay vectors, and the original color spaces (including CMYK) are kept. When you wrap another format (for example EPS, AI or TIFF) as a PDF, keep vectors as vectors and keep the source color space.
- Only the first page is used.
- Studio uses the page's CropBox if it is set, otherwise the MediaBox, and respects the page rotation.

!!! tip "Keep transparency"

    Of the supported formats, only PNG and PDF keep transparency. If an asset has transparency, return PNG for every raster rendition. JPEG cannot store transparency, so a JPEG rendition shows a solid background instead.

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

1. Follow the [Build a Simple Media Connector](/GraFx-Developers/connectors/media-connector/build-a-simple-media-connector/) tutorial to learn how to build a simple connector.
2. Review the [Authorization for Connectors](/GraFx-Developers/connectors/authorization-for-connectors/) for understanding how to add authorization to your connector.
