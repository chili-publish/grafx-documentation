# Add Configuration Options To Your Connector

This guide focuses on adding configurable settings to your Connector within the GraFx Studio Designer Workspace, specifically for image variables. The primary goal is to empower designers to tailor your Connector's functionality for various end-user scenarios, enhancing the flexibility and relevance of the final product.

## Requirements

- Node.js or Bun.js installed
- [Connector CLI](/GraFx-Developers/connectors/connector-cli/) tool
- Environment Admin user with a Template Designer license
- Completed [Build a Simple Media Connector](/GraFx-Developers/connectors/media-connector/build-a-simple-media-connector/) tutorial or started from this [git project](https://github.com/seancrowe/simple-media-connector/tree/Build-a-Simple-Media-Connector)

## Understanding Connector Settings

The `getConfigurationOptions` method is crucial for defining settings that appear in the GraFx Studio and are stored in the document JSON. It's important to note that this method, while named similarly, is distinct from `runtime.options` or `QueryOptions` passed to the `query` method.

Settings values are passed via the `context` parameter in the `query`, `download`, and `detail` methods. This allows designers to customize Connector behavior at the individual image variable level.

!!! note "One Way Communication"

    This type of configuration is a one way communication from image variable in template to Connector.

## Adding a Rectangle/Square Image Setting

The picsum.photos API supports both outputting rectangular and square images. We can enhance our connector by adding a setting that allows Designers to choose between these two image crops. This setting will affect how images are displayed in both the image selector and the document frame.

### Step 1: Update `getConfigurationOptions`

```typescript
  getConfigurationOptions(): Connector.ConnectorConfigValue[] | null {
    return [
      {
        name: "wide",
        displayName: "Display images as rectangular instead of square",
        type: "boolean"
      }
    ];
  }
```

This addition introduces a new boolean option named "wide" that users can toggle to switch between rectangular and square image displays.

!!! info "Supported Types"

    Currently, only string (text) and boolean values are supported for settings.

### Step 2: Update the `download` Method

Next, we'll update our `download` method to incorporate this new setting:

```typescript
async download(
  id: string,
  previewType: Media.DownloadType,
  intent: Media.DownloadIntent,
  context: Connector.Dictionary
): Promise<Connector.ArrayBufferPointer> {
  switch (previewType) {
    case "thumbnail": {
      const picture = await this.runtime.fetch(`https://picsum.photos/id/${id}/${(context.wide) ? "400/" : ""}200`, { method: "GET" });
      return picture.arrayBuffer;
    }
    case "mediumres": {
      const picture = await this.runtime.fetch(`https://picsum.photos/id/${id}/400`, { method: "GET" });
      return picture.arrayBuffer;
    }
    case "highres": {
      const picture = await this.runtime.fetch(`https://picsum.photos/id/${id}/${(context.wide) ? "2000/" : ""}1000`, { method: "GET" });
      return picture.arrayBuffer;
    }
    default: {
      const picture = await this.runtime.fetch(`https://picsum.photos/id/${id}`, { method: "GET" });
      return picture.arrayBuffer;
    }
  }
}
```

Key changes in this method:

1. We now use the `context.wide` setting to determine the image dimensions.
2. For thumbnails, we use 400x200 for wide (rectangular) images and 200x200 for square images.
3. For highres, we use 2000x1000 for wide (rectangular) images and 1000x1000 for square images.

### Step 3: Publish and Test

The "wide" setting controls how the image is loaded into the frame. To best observe this effect:

1. Publish your updated connector using the method described in the previously.
2. In your document, add or select an existing image variable using this Connector.
3. Set up an image frame with the mode set to "Fit" and linked to the variable.
4. Locate the new "Display images as rectangular instead of square" setting in the connector options.
5. Toggle this setting and observe how it affects the images in both the selector and the document frame.

This demonstrates that our connector is not just affecting the image selection process, but also how the image is displayed within the document itself.

## Key Accomplishments

By completing this guide, you have:

- Introduction of configurable settings for image variables in the Connector.
- Introduction of an wide option allowing designers to choose between rectangular and square displays.
- Enhancements to the download method to incorporate the new wide setting, affecting some `previewTypes`.

## Next Steps

1. Review the [Comprehensive Connector Documentation](/GraFx-Developers/connectors/connectors-introduction/) for in-depth information on Connector functionality and best practices.
2. Follow the [Add Environment Options to Your Connector](/GraFx-Developers/connectors/media-connector/add-environment-options-to-your-connector/) tutorial to learn how to add environment options in your Connectors.
