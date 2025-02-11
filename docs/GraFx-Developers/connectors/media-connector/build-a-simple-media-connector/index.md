# Build a Simple Media Connector

This guide walks you through the process of creating a simple media connector using the Connector CLI tool. The connector will display images from picsum.photos in the image selector of GraFx Studio Designer Workspace.

## Requirements

- Node.js or Bun.js
- [Connector CLI](../../connector-cli/) tool
- Environment Admin user with a Template Designer license applied

## Creating a New Connector Project

1. Execute the command to create a new connector project:

```bash
connector-cli new
```

and follow the prompts to configure the project settings.

2. Enter to the project directory:

```bash
cd <projectName>
```

3. Install dependencies:

=== "NPM"

    ```bash
    npm install
    ```

=== "Bun"

    ```bash
    bun install
    ```

4. Open `connector.ts` as this is the main connector file we will be modifying.

## Modifying the Query Method

Our goal is to display images from picsum.photos in the image selector. The `query` method is utilized by the default Studio GUIs to retrieve a list of `Media` objects for display.

### Updating Capabilities

First, we need to modify the `getCapabilities()` method to inform the UI about our connector's supported capabilities:

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

Note: We set both `query` and `filtering` to `true`. Ideally, we only want to support `query`, but currently, it's not possible to have `query` without `filtering` for the default Studio GUIs. This limitation may be addressed in future updates.

### Implementing the Query Method

Next, we'll modify the `query` method to perform the following tasks:

1. Fetch a list of photos from picsum.photos
2. Transform the data to match the required `Media` type
3. Return the `Media` data within the expected `MediaPage` type

We'll use the following endpoint to retrieve our photos:

```
https://picsum.photos/v2/list?page=1
```

This endpoint returns 30 images per page in an array of objects with the following structure:

```typescript
{
  "id": string;
  "author": string;
  "width": number;
  "height": number;
  "url": string;
  "download_url": string;
}
```

Now, let's update our `query` method to handle this data and return the expected `MediaPage` type:

```typescript
async query(
  options: Connector.QueryOptions,
  context: Connector.Dictionary
): Promise<Media.MediaPage> {
  const resp = await this.runtime.fetch("https://picsum.photos/v2/list?page=1", {
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

### Notes on Query Options

- The `options` parameter provides query options set by the UI. Currently, only the `pageToken` property is utilized and it is only for pagination.
- The returned `nextPage` in the `MediaPage.links` is meant to be passed back as `pageToken` during pagination, but it only works in a very specific use-case.
- The `pageSize` property within `options` is intended to specify the number of elements the UI can display. However, it is currently hardcoded and not functional.
- The returned `pageSize` in the `MediaPage` object also has no effect at present.


## Publishing the Connector

### Step 1: Logging In

Before publishing your connector, you need to log in to your environment. Run the following command and follow the on-screen instructions:

```bash
connector-cli login
```

### Step 2: Publishing

After successfully logging in, you can publish your connector using the following command:

```bash
connector-cli publish -e <environment-name> \
        -b <base-url> \
        -n <name> \
        --proxyOption.allowedDomains "*.xyz"
```

#### Command Arguments

- `-e <environment-name>`: The name of the environment you logged into in the previous step.
- `-b <base-url>`: The base URL for GraFx API calls. Use one of the following formats:
  - Production Environments: `https://{environment}.chili-publish.online/grafx`
  - Sandbox Environments: `https://{environment}.chili-publish-sandbox.online/grafx`
- `-n <name>`: The name of your connector as it will appear in the Studio UI.
- `--proxyOption.allowedDomains "*.xyz"`: Specifies allowed domains for OAuth, but is required even though not used.

!!! note "Grab the Connector ID"

    Make sure to copy and save the resulting Connector ID after publishing. Currently, there is no way to retrieve this ID later without using the Environment API.

### Step 3: Verifying the Publication

To verify that your connector has been published successfully:

1. Open GraFx Studio Designer Workspace.
2. Create or open an existing template.
3. Navigate to the media panel.

At this point, you should see missing image placeholders for images numbered 0 through 29. This is expected behavior, as we haven't implemented the `download` method yet.

## Implementing the Download Method

The images don't load initially because we haven't implemented the `download` method. This method is called by the engine or UI whenever an image needs to be displayed.

### Understanding the Download Method

The `download` method handles two main scenarios:

1. Fetching thumbnails for the image selector UI
2. Fetching full-size images for other use cases (editor and output)

### Implementing the Download Method

Here's the implementation of the `download` method:

```typescript
async download(
  id: string,
  previewType: Media.DownloadType,
  intent: Media.DownloadIntent,
  context: Connector.Dictionary
): Promise<Connector.ArrayBufferPointer> {
  switch (previewType) {
    case "thumbnail": {
      const picture = await this.runtime.fetch(`https://picsum.photos/id/${id}/200`, { method: "GET" });
      return picture.arrayBuffer;
    }
    default: {
      const picture = await this.runtime.fetch(`https://picsum.photos/id/${id}/1000`, { method: "GET" });
      return picture.arrayBuffer;
    }
  }
}
```

This method:

1. Checks the `previewType` to determine whether a thumbnail or full-size image is required
2. Fetches the appropriate image from picsum.photos
3. Returns the image data as an `ArrayBufferPointer`

## Publishing and Testing the Updated Connector

After implementing the `download` method, you need to republish your connector with the updates.

### Republishing the Connector

Use the following command to republish your connector, including the `--connectorId` argument:

```bash
connector-cli publish -e <environment-name> \
        -b <base-url> \
        -n <name> \
        --proxyOption.allowedDomains "*.xyz" \
        --connectorId <connector-id>
```

Replace `<connector-id>` with the ID you received when first publishing the connector.

If you've forgotten your connector ID, you can retrieve it using the following API endpoint:

```
GET https://{environment}.chili-publish.online/grafx/api/experimental/environment/{environment}/connectors
```

Replace `{environment}` with your environment name.

### Testing the Connector

To test your updated connector:

1. Open GraFx Studio Designer Workspace
2. Navigate to the Media panel
3. Verify that images now appear properly in the Media panel
4. Then add an image frame to your design
5. Double-click an image in the Media panel to fill the frame

## Some Issues
### Issue: Only First Image

You may notice that no matter which image you select in the Media panel, the image displayed in the template is instead the first image. This is due to how `download` behaves when `filtering` is `true`.

When `filtering` is `false`, `download` is called directly with the selected asset ID. However, when it is set to `true`, `query` is called first and then the first item from the call will be pushed into `download`.

### Issue: Double-clicking with Nothing Selected

You may notice that double-clicking an image in the Media panel when nothing is selected doesn't have any effect. This is due to a missing capability in our connector.

If you open the developer console, you'll see an error message:

```
Connector <connector-id> doesn't have capability: detail
```

This error occurs because we haven't implemented the `detail` method in our connector, which is required for this specific functionality.

## Fixing `query`

When `query` is called before `download`, the `options.pageSize` will be the value `1` and `options.collection` will be `null`.

```typescript
async query(
  options: Connector.QueryOptions,
  context: Connector.Dictionary
): Promise<Media.MediaPage> {

  // When pageSize is 1 & collection is null, we know that query is called before download
  if (options.pageSize == 1 && !options.collection) {
    return {
      pageSize: options.pageSize, // Note: pageSize is not currently used by the UI

      data: [{

        id: options.filter[0],
        name: "",
        relativePath: "",
        type: 0,
        metaData: {}
      }],

      links: {
        nextPage: "" // Pagination is ignored in this example
      }
    }
  }

  // If pageSize is bigger than 1, we do a normal query

  const resp = await this.runtime.fetch("https://picsum.photos/v2/list?page=1&limit=4", {
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

## Implementing the Detail Method

The `detail` method is used to define the initial width and height of the image frame when selected from the Media panel. Although this method accepts several parameters, only the width and height are relevant for this purpose. However, it's important to note that the type signature tells you the width and height is not mandatory, but the behavior of the method requires them present.

### Basic Implementation

Here's a basic implementation of the `detail` method:

```typescript
async detail(
  id: string,
  context: Connector.Dictionary
): Promise<Media.MediaDetail> {
  return {
    name: id,
    id: id,
    metaData: {},
    relativePath: "/",
    type: 0
  }
}
```

With this implementation, when you double-click an image in the Media panel, it will be added to the design in a 100x100 pixel frame (the default size when width and height are not specified).

### Customizing Frame Size

To customize the initial frame size, you can include `width` and `height` properties in the returned object. For example, to set a 200x200 pixel frame:

```typescript
async detail(
  id: string,
  context: Connector.Dictionary
): Promise<Media.MediaDetail> {
  return {
    name: id,
    id: id,
    metaData: {},
    relativePath: "/",
    type: 0,
    width: 200,
    height: 200
  }
}
```

### Publishing and Testing

After implementing the `detail` method:

1. Republish your connector using the `connector-cli publish` command (as described in previous sections).
2. Open GraFx Studio Designer Workspace.
3. Test the functionality by double-clicking an image in the Media panel.
4. Verify that the image is added to the design with the correct initial frame size.

## Conclusion

Congratulations! You've successfully built your first Media Connector for GraFx Studio. This connector allows you to integrate images from picsum.photos into the GraFx Studio Designer Workspace.

### Key Accomplishments

In this tutorial, you've learned how to:

1. Set up a new connector project
2. Implement the `query` method to fetch and display images
3. Create a `download` method to retrieve image data
4. Add a `detail` method to control initial frame sizes
5. Publish and test your connector in the GraFx Studio environment

## Next Steps

1. Review the [Comprehensive Connector Documentation](../../../../GraFx-Studio/concepts/connectors/) for in-depth information on connector functionality and best practices.
2. Follow the [Add Variable Settings To Your Connector](../add-variable-settings-to-your-connector) tutorial to learn how to add variable settings in your Connectors.
