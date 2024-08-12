# Add Variable Settings To Your Connector

This guide focuses on adding configurable settings to your Connector within the Studio Designer Workspace, specifically for image variables. The primary goal is to empower designers to tailor your Connector's functionality for various end-user scenarios, enhancing the flexibility and relevance of the final product.

## Requirements

- Node.js or Bun.js installed
- [Connector CLI](link-to-connector-cli-docs) tool
- Environment Admin user with a Template Designer license
- Completed [Build a Simple Media Connector](link-to-simple-media-connector-guide) tutorial or started from this [git project](https://github.com/seancrowe/simple-media-connector/tree/Build-a-Simple-Media-Connector)

## Understanding Connector Settings

The `getConfigurationOptions` method is crucial for defining settings that appear in the GUI and are stored in the document JSON. It's important to note that this method, while named similarly, is distinct from `runtime.options` or `QueryOptions` passed to the `query` method.

Settings values are passed via the `context` parameter in the `query`, `download`, and `detail` methods. This allows designers to customize Connector behavior at the individual image variable level.

!!! note "One Way Communication"

    This type of configuration is a one way communication from image variable in template to Connector.

## Implementing Settings

### Step 1: Update `getConfigurationOptions`

We'll add a setting to control the number of images returned by the picsum.photos API:

```typescript
getConfigurationOptions(): Connector.ConnectorConfigValue[] | null {
  return [{
    name: "limit",
    displayName: "Number (1 to 100) of Images to Display",
    type: "text"
  }];
}
```

!!! info "Supported Types"

    Currently, only string (text) and boolean values are supported for settings.

At this moment, there is no way to communicate to the designer that they entered in a wrong value. So we do our best to communicate the limits in our `displayName` in our `getConfigurationOptions`.

### Step 2: Modify the `query` Method

We'll update our `query` method to handle the newly introduced limit setting. This modification involves several key steps:

1. Adding a `limit` query string parameter to our API call
2. Verifying the existence and validity of `context.limit` as a integer 
3. Ensuring the limit falls within an acceptable range (1 to 100)

Here's the refined implementation:

```typescript
async query(
    options: Connector.QueryOptions,
    context: Connector.Dictionary
  ): Promise<Media.MediaPage> {

    // Set a default user limit
    let limit = 30;

    // Check if a specific limit is provided in the settings (context)
    if (context.limit) {
      // Convert the provided limit to a number
      const parsedLimit = parseInt(context.limit.toString(), 10);

      // Validate and set the user limit between 1 and 100
      if (!isNaN(parsedLimit)) {
        limit = Math.min(Math.max(parsedLimit, 1), 100);
      }
    }


    const resp = await this.runtime.fetch(`https://picsum.photos/v2/list?page=1&limit=${limit}`, {
      method: "GET"
    });

    if (resp.ok) {
      const data = JSON.parse(resp.text);

      // Transform the data to match the Media type
      const dataFormatted = data.map(d => ({
        id: d.id,
        name: d.id,
        relativePath: "/",
        type: 0,
        metaData: {}
      })) as Array<any>;

      return {
        pageSize: options.pageSize, // Note: pageSize is not currently used by the UI
        data: dataFormatted,
        links: {
          nextPage: "" // Pagination is ignored in this example
        }
      }
    }

    // Handle error case
    throw new Error("Failed to fetch images from picsum.photos");
  }
```

### Step 3: Publish and Test

We recommend publishing this as a new connector to test your changes. If you need a refresher on publishing a connector, refer to the [Build a Simple Media Connector](/GraFx-Developers/connectors/media-connector/build-a-simple-media-connector/#publishing-the-connector) guide or consult the [Connector CLI]() documentation.

To publish your connector, use the following command in your terminal:

```bash
connector-cli publish -e <environment-name> \
        -b <base-url> \
        -n <name> \
        --proxyOption.allowedDomains "*.xyz"
```

Once your connector is published, you can test it by following these steps:

1. Open a Template where you can add an image variable.
2. Add a new image variable to your document.
3. In the image selection interface, choose your newly published Connector.
4. Look for the new setting: "Number (1 to 100) of Images to Display".
5. Adjust this setting to different values within the allowed range (1 to 100).
6. Click "Select image" to observe how the number of displayed images changes based on your setting.

## Adding a Rectangle/Square Image Setting


The picsum.photos API supports both outputting rectangular and square images. We can enhance our connector by adding a setting that allows Designes to choose between these two image crops. This setting will affect how images are displayed in both the image selector and the document frame.

### Step 1: Update `getConfigurationOptions`

```typescript
  getConfigurationOptions(): Connector.ConnectorConfigValue[] | null {
    return [
      {
        name: "limit",
        displayName: "Number (1 to 100) of Images to Display",
        type: "text"
      },
      {
        name: "wide",
        displayName: "Display images as rectangluar instead of square",
        type: "boolean"
      }
    ];
  }
  ```

This addition introduces a new boolean option named "wide" that users can toggle to switch between rectangular and square image displays.

### Step 2: Update the `download` Method

Next, we'll update our `download` method to incorporate this new setting:

```typescript
  async download(
    id: string,
    previewType: Media.DownloadType,
    intent: Media.DownloadIntent,
    context: Connector.Dictionary
  ): Promise<Connector.ArrayBufferPointer> {

    // Check to see if we are a thumbnail in the UI or being used in another situation.
    switch (previewType) {
      case "thumbnail": {
        const picture = await this.runtime.fetch(`https://picsum.photos/id/${id}/${(context.wide) ? "400/" : ""}200`, { method: "GET" });
        return picture.arrayBuffer;
      }
      default: {
        const picture = await this.runtime.fetch(`https://picsum.photos/id/${id}/${(context.wide) ? "2000/" : ""}1000`, { method: "GET" });
        return picture.arrayBuffer;
      }
    }
  }
```

Key changes in this method:
1. We now use the `context.wide` setting to determine the image dimensions.
2. For thumbnails, we use 400x200 for wide (rectangular) images and 200x200 for square images.
3. For full-size images, we use 2000x1000 for wide images and 1000x1000 for square images.

### Step 3: Publish and Test

The "wide" setting controls how the image is loaded into the frame. To best observe this effect:

1. Publish your updated connector using the method described in the previously.
2. In your document, add or select an existing image variable using this Connector.
3. Set up an image frame with the mode set to "Fit" and linked to the variable.
4. Locate the new "Display images as rectangular instead of square" setting in the connector options.
5. Toggle this setting and observe how it affects the images in both the selector and the document frame.

This demonstrates that our connector is not just affecting the image selection process, but also how the image is displayed within the document itself.

### Key Accomplishments

By completing this guide, you have:

- Added an environment-level option to your Connector configuration.
- Modified your Connector code to utilize the new environment option.
- Learned how to publish a Connector with required options using the Connector CLI.
- Gained understanding of how environment options can be used to make your Connector more flexible and configurable.


## Next Steps

1. Review the [Comprehensive Connector Documentation](link-to-comprehensive-docs) for in-depth information on Connector functionality and best practices.
2. Follow the [Build a Media Connector With Authorization](link-to-auth-connector-tutorial) tutorial to learn how to implement authentication in your Connectors.
