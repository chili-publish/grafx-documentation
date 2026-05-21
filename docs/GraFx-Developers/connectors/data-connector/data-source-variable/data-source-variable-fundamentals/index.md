# Data Connector Fundamentals — Data Source Variable use case

This page covers the additions a Data Connector needs in order to support the **Data Source Variable** use case. Set `dataSourceVariable: true` in `getCapabilities` and implement **`Data.DataSourceVariableCapability`** on your connector class. The sections below describe each method. For general connector concepts (isolation, runtime, `getConfigurationOptions`), see [Data Connector Fundamentals](/GraFx-Developers/connectors/data-connector/data-connector-fundamentals/).

!!! warning "Required for DSV"

    DSV support is an **opt-in extension** on top of a Data Connector. The CLI scaffold (`connector-cli new --type=data`) produces only the Output Data Source basics. Without `dataSourceVariable: true` in `getCapabilities` plus the methods described below, the Data Connector will **not** be selectable as the source for a Data Source Variable in Studio.

!!! note "One connector, two use cases"

    The same Data Connector can serve both use cases. Studio calls `getPage` for both; Output Data Source relies on forward paging via `continuationToken` only and does not call `getPageItemById`.

```typescript
export default class MyConnector implements Data.DataConnector, Data.DataSourceVariableCapability {
  // getCapabilities, getConfigurationOptions, getPage, getPageItemById, getModel
}
```

## Requirements

- Completed [Data Connector Fundamentals](/GraFx-Developers/connectors/data-connector/data-connector-fundamentals/)
- Basic understanding of modern JavaScript and asynchronous programming (Promises)

### getCapabilities Method

```typescript
getCapabilities(): Data.DataConnectorCapabilities {
  return {
    filtering: false,
    sorting: false,
    model: true,
    dataSourceVariable: true,
  };
}
```

| Capability | Value |
|---|---|
| `dataSourceVariable` | `true` |
| `model` | `true` |
| `filtering` | Optional — set `true` if your connector honors `filters` in page config |
| `sorting` | Optional — set `true` if your connector honors `sorting` in page config |

### getPage Method (bidirectional)

```typescript
async getPage(
  config: Data.BidirectionalPageConfig,
  context: Connector.Dictionary
): Promise<Data.BidirectionalDataPage> {
  // Implement your data retrieval logic here
}
```

Studio passes a `BidirectionalPageConfig`. Your connector reads `limit`, optional `filters` and `sorting`, and whichever navigation tokens Studio includes (`continuationToken`, `previousPageToken`, or neither), then returns the matching page:

```typescript
interface PageConfigBase {
  limit: number;
  filters?: DataFilter[] | null;
  sorting?: DataSorting[] | null;
}

interface BidirectionalPageConfig extends PageConfigBase {
  continuationToken?: string | null;
  previousPageToken?: string | null;
}
```

Return a `BidirectionalDataPage` with the rows for that page and the tokens Studio needs for further navigation:

```typescript
interface BidirectionalDataPage {
  data: DataItem[];
  continuationToken?: string | null;
  previousPageToken?: string | null;
}
```

Set `continuationToken` when a next page exists, `previousPageToken` when a previous page exists, or `null` when there is no page in that direction. Use opaque, connector-specific token strings (for example, an encoded offset or API cursor) that you can decode on the next call.

### getPageItemById Method

```typescript
async getPageItemById(
  id: string,
  pageOptions: Data.PageItemOptions,
  context: Connector.Dictionary
): Promise<Data.BidirectionalDataPageItem> {
  // Return the item and navigation tokens for adjacent pages
}
```

Studio passes `pageOptions` with the page size and optional sort order. Your connector returns the item and the navigation tokens for adjacent pages:

```typescript
interface PageItemOptions {
  limit: number;
  sorting?: DataSorting[] | null;
}
```

The response is a `BidirectionalDataPageItem`:

```typescript
interface BidirectionalDataPageItem {
  data: DataItem;
  continuationToken?: string | null;
  previousPageToken?: string | null;
}
```

The `data` object must include the field named in `itemIdPropertyName` (see `getModel`), with a value matching the requested `id`. Return `continuationToken` and/or `previousPageToken` when additional pages exist relative to that item, using the same encoding scheme as in `getPage`.

### getModel Method

```typescript
async getModel(context: Connector.Dictionary): Promise<Data.DataSourceVariableDataModel> {
  return {
    properties: [
      { name: 'id', type: 'singleLine' },
      { name: 'firstName', type: 'singleLine' },
      { name: 'lastName', type: 'singleLine' },
      { name: 'email', type: 'singleLine' },
    ],
    itemIdPropertyName: 'id',
  };
}
```

`DataSourceVariableDataModel` extends `DataModel` with:

| Field | Description |
|---|---|
| `properties` | Column definitions |
| `itemIdPropertyName` | Name of the property on each `DataItem` that holds the stable row ID (must match a `properties[].name` entry) |

Each row returned from `getPage` and `getPageItemById` must include `itemIdPropertyName` with a string-convertible value.

Property types: `singleLine`, `multiLine`, `number`, `boolean`, and `date`. See [Template variable mapping](/GraFx-Developers/connectors/data-connector/data-connector-fundamentals/#getmodel-method) in Data Connector Fundamentals for how model types map to template variables.

## Next Steps

1. Follow [Build a Data Connector](/GraFx-Developers/connectors/data-connector/data-source-variable/build-a-data-source-variable-connector/) to add this capability to an existing connector.
2. Review [Authorization for Connectors](/GraFx-Developers/connectors/authorization-for-connectors/) for secure credential handling in production.
3. Explore the [Connector CLI](/GraFx-Developers/connectors/connector-cli/) for publishing and enabling your connector.
