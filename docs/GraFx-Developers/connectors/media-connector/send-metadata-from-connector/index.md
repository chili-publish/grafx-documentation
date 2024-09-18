# Add Environment Options to Your Connector

This guide is about passing more than just images from your connector to variables in your document. This is typically used to pass over data to update the document, like pricing, or data to cause document behavior changes, like passing over the product type to cause an action to change the template design.

## Requirements

- Node.js or Bun.js installed
- [Connector CLI]() tool
- Environment Admin user with a Template Designer license
- Completed  [Add Environment Options to Your Connector](/GraFx-Developers/connectors/media-connector/add-environment-options-to-your-connector) tutorial or started from this [git project](https://github.com/seancrowe/simple-media-connector/tree/media-connector-meta-folders)


## Adding an Metadata Support

Modify the `getCapabilities` in the `connector.ts` to set `metadata` to `true`.

```typescript
getCapabilities(): Media.MediaConnectorCapabilities {
    return {
      query: true,
      detail: true,
      filtering: true,
      metadata: true,
    };
  }
```
## Implementing the Metadata in Code

Info Picsum also includes info about the author which we can pull into any document via metadata.

### Updating the `query` Method

In the `query` method, we need to update the behavior when `options.pageSize` is 1 and `options.collection` is null. Remember this is when `query` is called before `download`.

We will update this method to use the info API endpoint to get the info and set the author on our metadata.

```typescript
if (options.pageSize == 1 && !options.collection) {
  const id = options.filter[0];
  const resp = await this.runtime.fetch(`https://${this.runtime.options["baseURL"]}/id/${id}/info`, {
    method: "GET"
  });

  if (!resp.ok) {
    throw new Error("Failed to fetch info from picsum.photos");
  }
  
  const data = JSON.parse(resp.text);

  return {
    pageSize: options.pageSize, // Note: pageSize is not currently used by the UI
    
    data: [{
      id: id,
      name: "",
      relativePath: "",
      type: 0,
      metaData: {
        "author": data.author
      }
    }],

    links: {
      nextPage: "" // Pagination is ignored in this example
    }
  }
}
```

## Publishing and Testing

When publishing your Connector don't forget the environment option, include the `-ro` (required option) argument in your command.

We recommend publishing this as a new connector to test your changes. If you need a refresher on publishing a connector, refer to the [Build a Simple Media Connector](/GraFx-Developers/connectors/media-connector/build-a-simple-media-connector/#publishing-the-connector) guide or consult the [Connector CLI]() documentation.

To publish your updated connector:

```bash
connector-cli publish -e <environment-name> \
        -b <base-url> \
        -n <name> \
        --proxyOption.allowedDomains "picsum.photos" \
        -ro baseURL="picsum.photos"
```

After publishing, test your connector by:

1. Add an text variable, and place it in a text frame
2. Add a image variable
3. Go to the image variable settings and see the new METADATA MAPPING
4. Add a mapping from `author` to the name of your text variable
5. Select and image and see your data get pushed from Info Picsum to the document variable

## Key Accomplishments

By completing this guide, you have:

