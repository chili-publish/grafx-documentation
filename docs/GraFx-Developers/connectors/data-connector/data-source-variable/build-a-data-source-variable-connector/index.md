# Build a Data Connector — Data Source Variable use case

This guide extends the Mockaroo-based connector from [Build a Simple Data Connector](/GraFx-Developers/connectors/data-connector/build-a-simple-data-connector/) to support the **Data Source Variable** use case.

!!! warning "DSV is an opt-in extension"

    A Data Connector built from the CLI scaffold supports the Output Data Source use case only. To make it usable as the source for a Data Source Variable in Studio, you must explicitly add `dataSourceVariable: true` to `getCapabilities`, a bidirectional `getPage`, a `getPageItemById`, and a `getModel` that returns `itemIdPropertyName` — the steps below walk through each one. Without these additions, the Data Connector will **not** be selectable as a DSV source.

For the contract and type definitions, see [Data Connector Fundamentals — Data Source Variable use case](/GraFx-Developers/connectors/data-connector/data-source-variable/data-source-variable-fundamentals/).

## Requirements

- Node.js or Bun.js
- [Connector CLI](/GraFx-Developers/connectors/connector-cli/)
- Environment Admin user with a Template Designer license applied
- A working Mockaroo connector from [Build a Simple Data Connector](/GraFx-Developers/connectors/data-connector/build-a-simple-data-connector/) (same schema and API key)

## Step 1: Enable the dataSourceVariable capability

Set `dataSourceVariable: true` in `getCapabilities()` and implement `Data.DataSourceVariableCapability` on your connector (see [Data Connector Fundamentals](/GraFx-Developers/connectors/data-connector/data-source-variable/data-source-variable-fundamentals/)).

Update `getCapabilities()` in `connector.ts`:

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

## Step 2: Implement getModel

Add a `getModel` method that returns column definitions and the row ID field name:

```typescript
async getModel(context: Connector.Dictionary): Promise<Data.DataSourceVariableDataModel> {
  return {
    properties: [
      { name: 'id', type: 'singleLine' },
      { name: 'firstName', type: 'singleLine' },
      { name: 'lastName', type: 'singleLine' },
      { name: 'email', type: 'singleLine' },
      { name: 'gender', type: 'singleLine' },
      { name: 'ipAddress', type: 'singleLine' },
    ],
    itemIdPropertyName: 'id',
  };
}
```

The property names must match the keys you return on each `DataItem` from `getPage` and `getPageItemById`.

## Step 3: Upgrade getPage to bidirectional paging

Mockaroo's free API does not support cursor-based pagination. For this tutorial, fetch a larger batch once, keep it in memory for the request lifecycle, and use **opaque tokens** that encode a numeric offset.

Add helpers at the top of your connector class (or in the same file):

```typescript
const TOTAL_MOCK_RECORDS = 200;

type PageToken = { offset: number };

function encodeToken(token: PageToken): string {
  return `offset:${token.offset}`;
}

function decodeToken(token: string | null | undefined): PageToken | null {
  if (!token || !token.startsWith('offset:')) return null;
  const offset = parseInt(token.slice('offset:'.length), 10);
  if (isNaN(offset)) return null;
  return { offset };
}

function formatRow(d: {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  gender: string;
  ip_address: string;
}): Data.DataItem {
  return {
    id: d.id.toString(),
    firstName: d.first_name,
    lastName: d.last_name,
    email: d.email,
    gender: d.gender,
    ipAddress: d.ip_address,
  };
}
```

Replace your `getPage` implementation with:

```typescript
async getPage(
  config: Data.BidirectionalPageConfig,
  context: Connector.Dictionary
): Promise<Data.BidirectionalDataPage> {
  const resp = await this.runtime.fetch(
    `https://my.api.mockaroo.com/users.json?key=YOUR_API_KEY&count=${TOTAL_MOCK_RECORDS}`,
    { method: 'GET' }
  );

  if (!resp.ok) {
    throw new ConnectorHttpError(
      resp.status,
      `[Mockaroo connector]: Failed to fetch data: ${resp.status}-${resp.statusText}`
    );
  }

  const raw = JSON.parse(resp.text) as Array<{
    id: number;
    first_name: string;
    last_name: string;
    email: string;
    gender: string;
    ip_address: string;
  }>;

  const allRows = raw.map(formatRow);
  const limit = config.limit;

  let offset = 0;
  const previous = decodeToken(config.previousPageToken);
  const next = decodeToken(config.continuationToken);

  if (previous) {
    offset = Math.max(0, previous.offset - limit);
  } else if (next) {
    offset = next.offset;
  }

  const page = allRows.slice(offset, offset + limit);
  const hasPrevious = offset > 0;
  const hasNext = offset + limit < allRows.length;

  return {
    data: page,
    previousPageToken: hasPrevious ? encodeToken({ offset }) : null,
    continuationToken: hasNext ? encodeToken({ offset: offset + limit }) : null,
  };
}
```

!!! note "Production connectors"
    Loading the full dataset on every `getPage` call is acceptable for a tutorial only. In production, use your API's native paging and encode API cursors in the tokens instead. The same applies to `getPageItemById` below — fetch only the row needed plus the adjacent-page tokens, not the entire dataset.

## Step 4: Implement getPageItemById

Return a single row by ID plus navigation tokens for adjacent pages. For simplicity, this tutorial assumes the default sort order — a production implementation should also respect `pageOptions.sorting` when computing the row's page position so that the returned `previousPageToken` and `continuationToken` match the order Studio is paging through.

```typescript
async getPageItemById(
  id: string,
  pageOptions: Data.PageItemOptions,
  context: Connector.Dictionary
): Promise<Data.BidirectionalDataPageItem> {
  const resp = await this.runtime.fetch(
    `https://my.api.mockaroo.com/users.json?key=YOUR_API_KEY&count=${TOTAL_MOCK_RECORDS}`,
    { method: 'GET' }
  );

  if (!resp.ok) {
    throw new ConnectorHttpError(
      resp.status,
      `[Mockaroo connector]: Failed to fetch data: ${resp.status}-${resp.statusText}`
    );
  }

  const raw = JSON.parse(resp.text) as Array<{
    id: number;
    first_name: string;
    last_name: string;
    email: string;
    gender: string;
    ip_address: string;
  }>;

  const allRows = raw.map(formatRow);
  const index = allRows.findIndex((row) => row.id?.toString() === id);

  if (index < 0) {
    throw new Error(`[Mockaroo connector]: Item not found: ${id}`);
  }

  const limit = pageOptions.limit;
  const pageStart = Math.floor(index / limit) * limit;
  const hasPrevious = pageStart > 0;
  const hasNext = pageStart + limit < allRows.length;

  return {
    data: allRows[index],
    previousPageToken: hasPrevious ? encodeToken({ offset: pageStart }) : null,
    continuationToken: hasNext ? encodeToken({ offset: pageStart + limit }) : null,
  };
}
```

## Step 5: Publish and enable the connector

Publish an updated version of your connector (same steps as [Build a Simple Data Connector](/GraFx-Developers/connectors/data-connector/build-a-simple-data-connector/#publishing-the-connector)):

```bash
connector-cli login
```

```bash
connector-cli publish \
        -e <environment-name> \
        -b <base-url> \
        -n <name> \
        --proxyOption.allowedDomains "my.api.mockaroo.com"
```

Enable it if needed:

```bash
connector-cli update \
        -e <environment-name> \
        -b <base-url> \
        --connectorId <connectorId> \
        --enabled true
```

## Step 6: Test in GraFx Studio

1. Open **GraFx Studio Designer Workspace** and create or open a template.
2. In the **Variables** panel, add a **Data Source Variable**.
3. With the variable selected, open the **Connector** tab and choose your newly published connector.
4. Switch to **Run mode** and confirm that rows load, selection works, and forward and backward pagination behave as expected.

If the connector does not appear on the Connector tab, confirm `dataSourceVariable: true` in `getCapabilities` and that the connector is enabled in your environment.

## Conclusion

You added `dataSourceVariable: true`, bidirectional `getPage`, `getPageItemById`, and `getModel` with `itemIdPropertyName` to your connector.

## Next Steps

1. Review [Data Connector Fundamentals](/GraFx-Developers/connectors/data-connector/data-source-variable/data-source-variable-fundamentals/) for the full contract reference.
2. Implement [Authorization for Connectors](/GraFx-Developers/connectors/authorization-for-connectors/) before production deployment.
3. See [Data Connector Introduction](/GraFx-Developers/connectors/data-connector/data-connector-introduction/) for the full learning path.
