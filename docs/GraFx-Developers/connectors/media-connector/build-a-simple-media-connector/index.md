# Build a Simple Media Connector

This guide walks you through the process of creating a simple media connector using the Connector CLI tool. The connector will display images from picsum.photos in the image selector of GraFx Studio Designer Workspace.

## Requirements

- Node.js or Bun.js
- [Connector CLI](/GraFx-Developers/connectors/connector-cli/) tool
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
    filtering: false,
    metadata: false,
  };
}
```

!!! note "Requirements"

    The GraFx Studio currently requires at least `query` and `detail` to be set to `true` to make connector functional properly.

### Implementing the Query Method

Next, we'll modify the `query` method to perform the following tasks:

1. Fetch a list of photos from picsum.photos according to provided `pageSize` and `pageToken`
2. Transform the data to match the required `Media` type
3. Return the `Media` data within the expected `MediaPage` type

We'll use the following endpoint to retrieve our photos:

```
https://picsum.photos/v2/list?page=${pageNumber}&limit=${pageSize}
```

This endpoint returns `pageSize` images for `pageNumber` in an array of objects with the following structure:

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
    // We set pageNumber according to pageToken param if it's valid or use default value
    const pageNumber = Number(options.pageToken) || 1;
    const resp = await this.runtime.fetch(
      `https://picsum.photos/v2/list?page=${pageNumber}&limit=${options.pageSize}`,
      {
        method: 'GET',
      }
    );

    // Handle error case
    if (!resp.ok) {
      // Note: Consider to always use "ConnectorHttpError" to handle error case for HTTP response
      throw new ConnectorHttpError(
        resp.status,
        `[PicsumPhoto connector]: Failed to fetch images from picsum.photos: ${resp.status}-${resp.statusText}`
      );
    }

    const data = JSON.parse(resp.text);

    // Transform the data to match the Media type
    const dataFormatted = data.map((d) => ({
      id: d.id,
      name: d.id,
      relativePath: '/', // Note: since picsum doesn't have folder structure, we specify relativePath always as the root directory
      extension: 'png', // Note: Although not required by Media type, it's good practice to define it when the possibility arises in DAM
      type: 0, // Note: define "0" if returned item is asset and "1" if it's a folder
      metaData: {},
    }));

    return {
      pageSize: options.pageSize, // Note: We return same pageSize to keep consistency between different page's request
      data: dataFormatted,
      links: {
        nextPage:
          dataFormatted.length === options.pageSize ? `${pageNumber + 1}` : '', // Calculates next page based on received assets size
      },
    };
  }
```

## Publishing the Connector

### Step 1: Logging In

Before publishing your connector, you need to log in to CHILI GraFx. Run the following command and follow the on-screen instructions:

```bash
connector-cli login
```

### Step 2: Publishing

After successfully logging in, you can publish your connector using the following command:

```bash
connector-cli publish \
        -e <environment-name> \
        -b <base-url> \
        -n <name> \
        --proxyOption.allowedDomains "picsum.photos"
```

#### Command Arguments

- `-e <environment-name>`: The environment where you want to deploy your connector.
- `-b <base-url>`: The base URL for CHILI GraFx API. Use one of the following formats:
    - **Production** Environments: `https://{environment-name}.chili-publish.online/grafx`
    - **Sandbox** Environments: `https://{environment-name}.chili-publish-sandbox.online/grafx`
- `-n <name>`: The name of your connector as it will appear in the GraFx Studio.
- `--proxyOption.allowedDomains "picsum.photos"`: Specifies allowed domains for all requests that we're making from the connector.

!!! note "Grab the Connector ID"

    Make sure to copy and save the resulting Connector ID after publishing. Currently, there is no way to retrieve this ID later without using the Environment API.

### Step 3: Enabling the connector

The connector published in the previous step is initially unavailable for use in GraFx Studio Designer Workspace. To activate it, access the connector's settings in the Platform for the desired environment and turn on the `Availability` switch next to the newly deployed connector.

### Step 4: Verifying

To verify that your connector has been available successfully:

1. Open GraFx Studio Designer Workspace.
2. Create or open an existing template.
3. Navigate to the Media Panel.

At this point, you should see missing image placeholders for images numbered 0 through 14. This is expected behavior, as we haven't implemented the `download` method yet.

!!! note "Pagination"
    To test pagination, scroll down until the end of media panel to initiate next page load

## Implementing the Download Method

The images don't load initially because we haven't implemented the `download` method. This method is called by the engine or UI whenever an image needs to be displayed.

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
    case "mediumres": {
      const picture = await this.runtime.fetch(`https://picsum.photos/id/${id}/400`, { method: "GET" });
      return picture.arrayBuffer;
    }
    case "highres": {
      const picture = await this.runtime.fetch(`https://picsum.photos/id/${id}/1000`, { method: "GET" });
      return picture.arrayBuffer;
    }
    default: {
      const picture = await this.runtime.fetch(`https://picsum.photos/id/${id}`, { method: "GET" });
      return picture.arrayBuffer;
    }
  }
}
```

This method:

1. Checks the `previewType` to determine a requested preview type
2. Fetches the appropriate image from picsum.photos
3. Returns the image data as an `ArrayBufferPointer`

!!! note "Download method"

    For more details see [link](/GraFx-Developers/connectors/media-connector/media-connector-fundamentals/#download-method)

## Publishing and Testing the Updated Connector

After implementing the `download` method, you need to republish your connector with the updates.

### Republishing the Connector

Use the following command to republish your connector, including the `--connectorId` argument:

```bash
connector-cli publish \
        -e <environment-name> \
        -b <base-url> \
        -n <name> \
        --proxyOption.allowedDomains "picsum.photos" \
        --connectorId <connector-id>
```

Replace `<connector-id>` with the ID you received when first publishing the connector.

If you've forgotten your connector ID, you can retrieve it using the following API endpoint:

```
GET https://{environment}.chili-publish.online/grafx/api/v1/environment/{environment}/connectors
```

Replace `{environment}` with your environment name.

### Testing the Connector

To test your updated connector:

<!-- #### Media panel use case -->

1. Open GraFx Studio Designer Workspace
2. Navigate to the Media panel
3. Verify that images now appear properly in the Media panel
4. Double-click an image in the Media panel to create image frame with selected image

<!-- #### Image variable use case

1. Open GraFx Studio Designer Workspace
2. Create new Image Variable targeting our connector
3. Select asset for this Variable -->

## Issue: Double-clicking with Nothing Selected

You may notice that double-clicking an image in the Media panel when nothing is selected doesn't have any effect.

If you open the developer console, you'll see an error message:

```
Error: QuickJS cannot evaluate your script: Error: Method not implemented.
```

This error occurs because we haven't implemented the `detail` method in our connector, which is required for this specific functionality.

## Implementing the Detail Method

The `detail` method is used when we need to fetch single asset details. It's important to note that the type signature tells you the `width` and `height` is not mandatory, but it always recommended to provide the actual sizes if possible

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
    relativePath: '/',
    extension: 'png',
    type: 0
  };
}
```

With this implementation, when you double-click an image in the Media panel, it will be added to the design in `default-sized` image frame (the default size when width and height are not specified).

### Return actual image Size

To create frame size taking into account the actual image size, you can include `width` and `height` properties in the returned object.

```typescript
async detail(
  id: string,
  context: Connector.Dictionary
): Promise<Media.MediaDetail> {
  const resp = await this.runtime.fetch(`https://picsum.photos/id/${id}/info`, { method: "GET" });
  // Handle error case
  if(!resp.ok) {
    // Note: Consider to always use "ConnectorHttpError" to handle error case for HTTP response
    throw new ConnectorHttpError(resp.status, `[PicsumPhoto connector]: Failed to fetch images from picsum.photos: ${resp.status}-${resp.statusText}`);
  }
  const assetDetail = JSON.parse(resp.text);
  return {
    name: assetDetail.id,
    id: assetDetail.id,
    metaData: {},
    relativePath: '/',
    extension: 'png',
    type: 0,
    width: assetDetail.width,
    height: assetDetail.height
  };
}
```

## Publishing and Testing

After implementing the `detail` method and fixing `query`

1. Republish your connector using the `connector-cli publish` command (as described in previous sections).
2. Open GraFx Studio Designer Workspace.
3. Test the functionality by double-clicking an image in the Media panel.
4. Verify that the image is added to the design with the correct initial frame size.

## Notes about "filtering"

Now let's make our connector more accessible and introduce another capability - filtering

### Updating Capabilities

First, we need to modify the `getCapabilities()` method and enable `filtering`:

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

### Modify query method

Next step is start consuming filter value during querying of the assets

!!! note "Fake implementation"
    Since Picsum itself doesn't support any filtering, we provide implementation that just logs the filter value in order to demonstrate
    the difference

```typescript
  async query(
    options: Connector.QueryOptions,
    context: Connector.Dictionary
  ): Promise<Media.MediaPage> {
    // Note: we just log the filter value in case if our query suppose to do filtering logic
    if (options.filter !== null) {
      this.runtime.logError(`Filter options are: ${options.filter}`)
    }

    // The rest part of method stays unchanged
    ...
  }
```

### Republishing and Testing

After adding `filtering` capabilities and modifying `query` method

1. Republish your connector using the `connector-cli publish` command (as described in previous sections).
2. Open GraFx Studio Designer Workspace.
3. Open the Media panel. This time you should see the search box above.
4. Enter any value and check logs in the browser `Dev Tools` panel - you should see them according to changes in `query` method.

## Issue: Only first image selection works in Image Variable Selector

You may notice that no matter which image you select in the Image Variable Selector, the displayed `thumbnail` is works only for the first image. This is due to how `download` for `thubmnail` behaves when `filtering` is `true`.

When `filtering` is `false`, `download` is called directly with the selected asset ID. However, when it is set to `true`, `query` is called first and then the first item from the call will be pushed into `download`.

### Fixing `thumbnail` preview

When `query` is called before `download`, the `options.pageSize` will be the value `1` and `options.collection` will be `null`.

```typescript
  async query(
    options: Connector.QueryOptions,
    context: Connector.Dictionary
  ): Promise<Media.MediaPage> {
      // When pageSize is 1 & collection is null, we know that query is called before download for `thubmnail` preview
    if (options.pageSize == 1 && !options.collection) {
      const assetId = options.filter[0] // In this situation the only filter item contains assetId as value
      const asset = await this.detail(assetId, context) // Here we request details for single item
      return {
        pageSize: options.pageSize, // Note: We return same pageSize, although it doesn't matter in this situation
        data: [asset],
        links: {
          nextPage: "" // Pagination is ignored in this situation
        }
      }
    }
    // If pageSize is bigger than 1, we do a normal query

    // The rest part of method stays unchanged
    ...
  }
```

### One more Republishing and Testing

After fixing the preview for `thumbnail`

1. Republish your connector using the `connector-cli publish` command (as described in previous sections).
2. Open GraFx Studio Designer Workspace.
3. Create or use existing Image Variable and configure it to use our connector.
4. Select any image other than first one - your selection should properly work this time.


## Conclusion

Congratulations! You've successfully built your first Media Connector for GraFx Studio. This connector allows you to integrate images from picsum.photos into the GraFx Studio Designer Workspace.

### Key Accomplishments

In this tutorial, you've learned how to:

1. Set up a new connector project
2. Implement the `query` method to fetch and display images taking into account pagination options
3. Create a `download` method to retrieve image data
4. Add a `detail` method to control initial frame sizes
5. Implement a fake `filtering` functionality
5. Publish and test your connector in the GraFx Studio

## Next Steps

1. Review the [Comprehensive Connector Documentation](/GraFx-Developers/connectors/connectors-introduction/) for in-depth information on connector functionality and best practices.
2. Follow the [Add Variable Settings To Your Connector](/GraFx-Developers/connectors/media-connector/add-variable-settings-to-your-connector/) tutorial to learn how to add variable settings in your Connectors.
