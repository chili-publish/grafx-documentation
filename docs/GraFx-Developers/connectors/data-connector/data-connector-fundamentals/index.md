# Data Connector Fundamentals

A Data Connector is a JavaScript class that implements the `Data.DataConnector` interface, providing methods utilized by the Studio Engine and the Studio SDK. This guide offers a high-level overview of Data Connectors.

## Requirements

- Basic understanding of modern JavaScript
- Familiarity with asynchronous programming (Promises)
- Basic experience with the GraFx Studio Template Designer Workspace

## Isolation

Data Connectors run in a limited isolated environment, which means they don't have access to many browser APIs or Node.js APIs. This isolation serves two primary purposes:

1. **Security**: JavaScript runs on the server, so it's crucial that it cannot directly access APIs that could compromise customer data.
2. **Performance**: By limiting available APIs, scripts remain small and easier to optimize for performance.

Due to this isolation, you cannot access the `window` object or many commonly used methods like `console.log`.

## Runtime

Instead of browser globals, Connectors use a `ConnectorRuntimeContext`, which is passed to the constructor of a Connector class. It's common practice to store this on a `runtime` property:

```typescript
export default class MyConnector implements Data.DataConnector {
  private runtime: Connector.ConnectorRuntimeContext;

  constructor(runtime: Connector.ConnectorRuntimeContext) {
    this.runtime = runtime;
  }
}
```

The `runtime` object provides methods like `fetch` and `logError` to replace similar functionality found in browser environments.

## Connector Methods

Your Data Connector class needs to implement four key methods:

1. getCapabilities
2. getConfigurationOptions
3. getPage
4. getModel (optional, based on capabilities)

### getCapabilities Method

This method communicates to the SDK what features the Connector supports:

```typescript
getCapabilities(): Data.DataConnectorCapabilities {
  return {
    filtering: false,
    sorting: false,
    model: false,
  };
}
```

### getConfigurationOptions Method

The `getConfigurationOptions` method allows Connector developers to define customizable settings that template designers can use to modify the behavior of the Connector.

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

### getPage Method

The `getPage` method is responsible for retrieving a specific page of data from your data source. It's called when a template loads initially and subsequently whenever pagination is required to fetch the next batch of data items. This method handles the core data retrieval functionality of your connector.

```typescript
async getPage(
  config: Data.PageConfig,
  context: Connector.Dictionary
): Promise<Data.DataPage> {
  // Implement your data retrieval logic here
}
```

The `PageConfig` interface includes:

```typescript
interface PageConfig {
    continuationToken?: string | null; // Optional token for pagination
    limit: number; // Maximum number of items to return
}
```

The method should return a `DataPage` object:

```typescript
interface DataPage {
    data: DataItem[]; // Array of data items
    continuationToken?: string | null; // Optional token for the next page
}
```

!!! note

    The returned `continuationToken` in the `DataPage` is meant to be passed back as `continuationToken` during pagination

### getModel Method

The `getModel` method is used to retrieve the data model of your data source. This method should only be implemented if you have set `model: true` in your connector's capabilities.

```typescript
async getModel(context: Connector.Dictionary): Promise<Data.DataModel> {
  // Implement your model retrieval logic here
}
```

The returned `DataModel` structure is used to define the types of data that your connector will return. Each property in the model represents a field in your data with its corresponding type:

- `number`: For numeric values
- `boolean`: For true/false values
- `singleLine`: For single-line text
- `multiLine`: For multi-line text
- `date`: For date values

## Next Steps

1. Follow the [Build a Simple Data Connector](/GraFx-Developers/connectors/data-connector/build-a-simple-data-connector/) tutorial to learn how to build your first Data Connector.
2. Review the [Authorization for Connectors](/GraFx-Developers/connectors/authorization-for-connectors/) for understanding how to add authorization to your Connector.
3. Explore the [Connector CLI](/GraFx-Developers/connectors/connector-cli/) documentation to learn about the tools available for connector development.