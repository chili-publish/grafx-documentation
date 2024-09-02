# Add Environment Options to Your Connector

This guide is about adding options that are set at the environment level for your Connector code. This is typically used of defining a value that will be shared among your Connector that is tied to every variable and document. For example, defining a base URL.

## Requirements

- Node.js or Bun.js installed
- [Connector CLI]() tool
- Environment Admin user with a Template Designer license
- Completed  [Add Variable Settings To Your Connector](/GraFx-Developers/connectors/media-connector/add-variable-settings-to-your-connector) tutorial or started from this [git project](https://github.com/seancrowe/simple-media-connector/tree/Add-Settings-To-Your-Connector)


## Adding an Environment Option

We'll add an option to define the base URL for the picsum.photos API that our Connector will use throughout the published environment.

Modify the `options` property in your `package.json` to add the new option:

```json
{
  ...
  "config": {
    "type": "media",
    "options": {"baseURL": null},
    "mappings": {}
  },
}
```

Setting the value to `null` requires you to define the value during publishing using the [Connector CLI]() tool. Alternatively, you can provide a default value instead of `null`. Note that only strings and booleans are allowed; numbers will be converted to strings.

!!! Bug "Default Values Issue"
    There is a known issue in the Connector CLI tool where default values are not applied correctly.

## Implementing the Option in Code

### Updating the `query` Method

In the `query` method, access the new option via the `runtime` object. Update the fetch request by replacing the hardcoded base URL with the new option:

```typescript
const resp = await this.runtime.fetch(`https://${this.runtime.options["baseURL"]}/v2/list?page=1&limit=${limit}`, {
  method: "GET"
});
```

### Updating the `download` Method

Similarly, update the `download` method:

```typescript
async download(
  id: string,
  previewType: Media.DownloadType,
  intent: Media.DownloadIntent,
  context: Connector.Dictionary
): Promise<Connector.ArrayBufferPointer> {
  switch (previewType) {
    case "thumbnail": {
      const picture = await this.runtime.fetch(`https://${this.runtime.options["baseURL"]}/id/${id}/${context.wide ? "400/" : ""}200`, { method: "GET" });
      return picture.arrayBuffer;
    }
    default: {
      const picture = await this.runtime.fetch(`https://${this.runtime.options["baseURL"]}/id/${id}/${context.wide ? "2000/" : ""}1000`, { method: "GET" });
      return picture.arrayBuffer;
    }
  }
}
```

## Publishing and Testing

When publishing your Connector with the new environment option, include the `-ro` (required option) argument in your command.

We recommend publishing this as a new connector to test your changes. If you need a refresher on publishing a connector, refer to the [Build a Simple Media Connector](/GraFx-Developers/connectors/media-connector/build-a-simple-media-connector/#publishing-the-connector) guide or consult the [Connector CLI]() documentation.

To publish your updated connector:

```bash
connector-cli publish -e <environment-name> \
        -b <base-url> \
        -n <name> \
        --proxyOption.allowedDomains "*.xyz" \
        -ro baseURL="picsum.photos"
```

After publishing, test your connector as we did in [Add Variable Settings To Your Connector](/GraFx-Developers/connectors/media-connector/add-variable-settings-to-your-connector/#step-3:-publish-and-test). For an additional test, try re-publishing with an incorrect `baseURL` to verify that it doesn't work, demonstrating the importance of the environment option.

## Key Accomplishments

By completing this guide, you have:

- Added an environment-level option to your Connector configuration.
- Modified your Connector code to utilize the new environment option.
- Learned how to publish a Connector with required options using the Connector CLI.
- Gained understanding of how environment options can be used to make your Connector more flexible and configurable.

## Next Steps

1. Review the [Comprehensive Connector Documentation]() for in-depth information on Connector functionality and best practices.
