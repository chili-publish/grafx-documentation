# Template Information Service

The Template Information Service is a stateless HTTP service. You send it the JSON of a GraFx Studio document (a Template or a Project), and it returns structured information about that document: its layouts, variables, data connector, Brand Kit, translatable text, and version information.

The service reads the document with the same document loader that the GraFx Studio engine uses. That loader understands every document version the engine supports and migrates older documents before the service reads them, so you get the same answer the editor would.

!!! warning "Do not parse the document JSON yourself"

    The GraFx document JSON format is internal. **It can change at any time without notice, and its structure is not guaranteed or versioned as a public contract.**

    Do not read layouts, variables, or any other information directly from the raw Template or Project JSON. Code that does this can break whenever GraFx Studio updates its document format.

    Use the Template Information Service instead. It understands every document version the engine supports and returns a stable output shape.

## When to use it

Use the Template Information Service when your integration needs to know something about a Template or Project **without opening it in the editor**. For example:

- Show a list of layouts, with their sizes and intents, in your own portal before the end user opens the editor.
- Build an input form or a CSV mapping from the variables in a Template.
- Check which data connector a Template is set up to use.
- Collect all end user-facing text (variable labels, help text, list items, layout display names) for translation.
- Predict whether the layout selector will appear in Studio UI. See [Example: Will the layout selector appear in Studio UI?](#example-will-the-layout-selector-appear-in-studio-ui).

## Base URL and endpoints

The service is available at:

```
https://template-information.chiligrafx.com
```

| Verb | Endpoint                | Usage                                                        |
| ---- | ----------------------- | ------------------------------------------------------------ |
| POST | `/query`                | Run one or more queries on a document                        |
| GET  | `/ping`                 | Health check. Returns `pong` as plain text                   |
| GET  | `/swagger`              | Interactive Swagger UI for the API                           |
| GET  | `/swagger/swagger.yaml` | The OpenAPI 3.0 definition, as YAML                          |

!!! warning "The Swagger schemas are not fully accurate"

    Use the Swagger UI to explore the endpoints, but don't rely on its schemas for response types:

    - The variable `value` in `allVariables`, the `variables` and `layouts` maps in `allTranslatables`, and the connector `options` and `mappings` in `dataConnector` are typed as maps of strings. They aren't: they contain numbers, booleans, arrays, and nested objects.
    - No `400` error responses are listed.

    This page and the actual responses of the service are the reference.

The Template Information Service itself doesn't require an `Authorization` header. A token is only needed if you fetch the Template JSON from your GraFx environment using the Environment API. If your Template JSON lives elsewhere, such as an S3 bucket, you can send it straight to the endpoint.

!!! note "Call the service from your server"

    The service doesn't send CORS headers, so browsers block `fetch` calls to it from a web page. Call it from your backend. This also keeps your Environment API token and your document JSON out of the browser.

## How it works, end to end

To get information about a Template stored in your environment:

1. Get an Environment API token.
2. Download the Template JSON from the Environment API.
3. Put the JSON, as a string, in the `documentJson` field of the request body.
4. Send a `POST /query` request with the queries you need.
5. Read the results. They come back in the same order as your queries.

### 1. Get a token

Request a token with the client credentials of an integration that can read templates. See [Generating A Token](/GraFx-Developers/environment-api/03-generating-a-token/).

### 2. Download the Template JSON

Use the Environment API to download the Template:

```
GET https://{environment}.chili-publish.online/grafx/api/v1/environment/{environment}/templates/{templateId}/download
```

For a sandbox environment, use `chili-publish-sandbox.online` instead of `chili-publish.online`. See [Making API Calls](/GraFx-Developers/environment-api/04-making-api-calls/).

The service accepts Projects as well as Templates. To read a Project, download its JSON with `GET /api/v1/environment/{environment}/projects/{projectId}/document`.

### 3. Build the request body

The request body is a JSON object with two required fields:

| Field          | Type   | Description                                                                                           |
| -------------- | ------ | ----------------------------------------------------------------------------------------------------- |
| `documentJson` | string | The document (Template or Project) JSON, **stringified**. Don't send it as a nested JSON object.     |
| `queries`      | array  | The queries to run, each as `{ "property": "<query name>" }`. See the [query reference](#query-reference). |

```json
{
  "documentJson": "{\"engineVersion\":\"...\",\"layouts\":[...], ...}",
  "queries": [
    { "property": "allLayouts" },
    { "property": "allVariables" }
  ]
}
```

!!! tip

    `documentJson` is a string that contains JSON, so the document is encoded twice. If you have the raw response text from the download call, use that text as-is. If you parsed the document into an object, convert it back to a string with `JSON.stringify(document)` first.

### 4. Send the query

Send the request body to `POST /query` with `Content-Type: application/json`.

=== "cURL"
    ```sh
    ENVIRONMENT="<YOUR ENVIRONMENT>"
    TEMPLATE_ID="<YOUR TEMPLATE ID>"
    TOKEN="<YOUR TOKEN>"

    # Download the Template JSON
    curl -s "https://$ENVIRONMENT.chili-publish.online/grafx/api/v1/environment/$ENVIRONMENT/templates/$TEMPLATE_ID/download" \
      -H "Authorization: Bearer $TOKEN" \
      -o template.json

    # Build the request body with jq (1.6+), which stores the Template JSON as a string in documentJson
    jq -n --rawfile documentJson template.json \
      '{documentJson: $documentJson, queries: [{property: "allLayouts"}, {property: "layoutsAvailableForUser"}]}' \
      > request.json

    # Query the service, reading the request body from the file
    curl -s -X POST "https://template-information.chiligrafx.com/query" \
      -H "Content-Type: application/json" \
      --data-binary @request.json
    ```
=== "Node v18+"
    ```javascript
    const environment = '<YOUR ENVIRONMENT>';
    const templateId = '<YOUR TEMPLATE ID>';
    const token = '<YOUR TOKEN>';

    // 1. Download the Template JSON as text
    const downloadResponse = await fetch(
      `https://${environment}.chili-publish.online/grafx/api/v1/environment/${environment}/templates/${templateId}/download`,
      { headers: { Authorization: `Bearer ${token}` } }
    );
    if (!downloadResponse.ok) {
      throw new Error(`Template download failed: ${downloadResponse.status}`);
    }
    const documentJson = await downloadResponse.text();

    // 2. Query the Template Information Service
    const queries = [
      { property: 'allLayouts' },
      { property: 'layoutsAvailableForUser' },
    ];

    const queryResponse = await fetch('https://template-information.chiligrafx.com/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ documentJson, queries }),
    });

    if (!queryResponse.ok) {
      // Errors are returned as plain text
      throw new Error(`Query failed (${queryResponse.status}): ${await queryResponse.text()}`);
    }

    // 3. Results are in the same order as the queries
    const { results } = await queryResponse.json();
    const [allLayouts, availableLayouts] = results;

    console.log(`${allLayouts.value.length} layouts, ${availableLayouts.value.length} available for the end user`);
    ```
=== "TypeScript"
    ```typescript
    type QueryProperty =
      | 'engineVersion'
      | 'documentVersion'
      | 'layoutsAvailableForUser'
      | 'allLayouts'
      | 'dataConnector'
      | 'allVariables'
      | 'allTranslatables'
      | 'brandKitInfo';

    interface LayoutInformation {
      id: string;
      name: string;
      displayName?: string;
      width: number;
      height: number;
      unit: 'px' | 'mm' | 'cm' | 'inch' | 'pt';
      selectedByUser: boolean;
      parentId?: string;
      resizeableByUser: boolean;
      minWidth?: number;
      minHeight?: number;
      maxWidth?: number;
      maxHeight?: number;
      intent: 'digitalStatic' | 'digitalAnimated' | 'print';
    }

    interface QueryResult {
      type: QueryProperty;
      value: unknown;
    }

    async function queryTemplate(documentJson: string, properties: QueryProperty[]): Promise<QueryResult[]> {
      const response = await fetch('https://template-information.chiligrafx.com/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          documentJson,
          queries: properties.map((property) => ({ property })),
        }),
      });

      if (!response.ok) {
        throw new Error(`Query failed (${response.status}): ${await response.text()}`);
      }

      const { results } = (await response.json()) as { results: QueryResult[] };
      return results;
    }

    // Usage: documentJson is the raw text returned by the Template download endpoint
    const [layouts] = await queryTemplate(documentJson, ['allLayouts']);
    const allLayouts = layouts.value as LayoutInformation[];
    ```

### 5. Read the results

A successful request returns `200 OK` with a JSON body. The `results` array has one entry per query, **in the same order as the `queries` array**. Each entry has:

- `type`: the query name, the same as the `property` you sent.
- `value`: the query result. Its shape depends on the query.

```json
{
  "results": [
    { "type": "allLayouts", "value": [ ... ] },
    { "type": "allVariables", "value": [ ... ] }
  ]
}
```

If you send the same query twice, you get two results.

!!! note "Empty fields are left out"

    The service omits fields whose value is empty (`null`). For example, a layout without a display name has no `displayName` field, and a Template without a selected data connector returns `"value": {}` for the `dataConnector` query. Treat a missing field as `null`.

## Query reference

The service supports eight queries. Use the query name as the `property` value in your request.

| Query                                                 | Returns                                                       |
| ----------------------------------------------------- | ------------------------------------------------------------- |
| [`engineVersion`](#engineversion)                     | The engine version recorded in the document                   |
| [`documentVersion`](#documentversion)                 | The document model version the service read the document as  |
| [`allLayouts`](#alllayouts)                           | Every layout in the document                                  |
| [`layoutsAvailableForUser`](#layoutsavailableforuser) | Only the layouts marked as **Available** for end users        |
| [`allVariables`](#allvariables)                       | Every variable, with its type, required flag, and value       |
| [`dataConnector`](#dataconnector)                     | The data connector selected in the document                   |
| [`allTranslatables`](#alltranslatables)               | End user-facing text of variables and layouts                 |
| [`brandKitInfo`](#brandkitinfo)                       | The ID and name of the Brand Kit linked to the document       |

### engineVersion

Returns the GraFx Studio engine version recorded in the document, as a string.

```json
{ "type": "engineVersion", "value": "2.32.0" }
```

**Use it to** log or audit which engine version a Template comes from, for example when you investigate a difference in output.

### documentVersion

Returns the document model version, as a string.

The service migrates every document to the latest model version it supports before it runs your queries. So this query returns **the latest document version the service supports** (for example `0.27.3`), not the version stored in the JSON you sent.

```json
{ "type": "documentVersion", "value": "0.27.3" }
```

**Use it to** check which document model version the service used to read your document.

### allLayouts

Returns every layout in the document, in document order, as an array of layout objects.

Child layouts inherit their size, unit, and intent from their parent layout when they don't set their own. The service resolves this inheritance for you, so every layout object contains its effective values.

| Field              | Type    | Description                                                                                  |
| ------------------ | ------- | -------------------------------------------------------------------------------------------- |
| `id`               | string  | Layout ID                                                                                    |
| `name`             | string  | Layout name                                                                                  |
| `displayName`      | string  | Name shown to end users. Omitted if not set                                                  |
| `width`            | number  | Width, in `unit`                                                                             |
| `height`           | number  | Height, in `unit`                                                                            |
| `unit`             | string  | Measurement unit: `px`, `mm`, `cm`, `inch`, or `pt`                                          |
| `selectedByUser`   | boolean | Whether an end user has selected this layout in a Project. See [Which layout did the end user pick?](#which-layout-did-the-end-user-pick). `false` if not set |
| `parentId`         | string  | ID of the parent layout. Omitted for the top-level layout                                    |
| `resizeableByUser` | boolean | Whether end users can resize the layout                                                      |
| `minWidth`         | number  | Minimum width an end user can resize to, in `unit`. Omitted if not set                       |
| `minHeight`        | number  | Minimum height an end user can resize to, in `unit`. Omitted if not set                      |
| `maxWidth`         | number  | Maximum width an end user can resize to, in `unit`. Omitted if not set                       |
| `maxHeight`        | number  | Maximum height an end user can resize to, in `unit`. Omitted if not set                      |
| `intent`           | string  | Layout intent: `print`, `digitalStatic`, or `digitalAnimated`                                |

```json
{
  "type": "allLayouts",
  "value": [
    {
      "id": "0",
      "name": "Master",
      "width": 210.0,
      "height": 297.0,
      "unit": "mm",
      "selectedByUser": false,
      "resizeableByUser": false,
      "intent": "print"
    },
    {
      "id": "1",
      "name": "A5",
      "displayName": "A5 flyer",
      "width": 148.0,
      "height": 210.0,
      "unit": "mm",
      "selectedByUser": false,
      "parentId": "0",
      "resizeableByUser": true,
      "minWidth": 100.0,
      "maxWidth": 200.0,
      "intent": "print"
    }
  ]
}
```

The layout object doesn't say whether a layout is available for end users. Use [`layoutsAvailableForUser`](#layoutsavailableforuser) for that.

**Use it to** show a Template's formats and sizes in your own portal, or to pick a layout ID for an output request.

#### Which layout did the end user pick?

`selectedByUser` marks the layout or layouts an end user has chosen in a **Project**. An integration sets it with the Studio SDK method `layout.setSelectedByUser(id, isSelected)`, and it's saved on the layout in the document.

- It can only be set in a Project, not in a Template. On Templates it's normally `false`.
- It can only be set on layouts that are available for end users.
- More than one layout can have `selectedByUser: true`.

To find out which layouts the end user picked in a saved Project, download the Project JSON, run `allLayouts` (or `layoutsAvailableForUser`), and keep the layouts where `selectedByUser` is `true`.

`selectedByUser` is not the layout that is currently open in the editor. The document tracks the open layout separately, in an internal document property (`selectedLayoutId`). The service doesn't return that property, and you shouldn't read it from the document JSON.

### layoutsAvailableForUser

Returns only the layouts that are marked as **Available** in the Template, in the same format as [`allLayouts`](#alllayouts). These are the layouts an end user can switch between in Studio UI. See [Layouts in the Studio UI](/GraFx-Studio/guides/layouts/#layouts-in-the-studio-ui).

```json
{
  "type": "layoutsAvailableForUser",
  "value": [
    {
      "id": "1",
      "name": "A5",
      "displayName": "A5 flyer",
      "width": 148.0,
      "height": 210.0,
      "unit": "mm",
      "selectedByUser": false,
      "parentId": "0",
      "resizeableByUser": true,
      "minWidth": 100.0,
      "maxWidth": 200.0,
      "intent": "print"
    }
  ]
}
```

**Use it to** show end users only the layouts they can choose, or to predict whether the layout selector appears. See [the example below](#example-will-the-layout-selector-appear-in-studio-ui).

### allVariables

Returns every variable in the document, as an array.

| Field        | Type    | Description                                                                                                             |
| ------------ | ------- | ----------------------------------------------------------------------------------------------------------------------- |
| `name`       | string  | Variable name                                                                                                           |
| `type`       | string  | Variable type: `shortText`, `longText`, `richText`, `image`, `list`, `boolean`, `group`, `number`, `date`, or `dataSource` |
| `isRequired` | boolean | Whether the variable is required                                                                                        |
| `value`      | varies  | The current value. Omitted if the variable has no value                                                                 |

The format of `value` depends on the variable type:

| Variable type             | `value`                                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| `shortText`, `longText`   | String                                                                                          |
| `number`                  | Number                                                                                          |
| `boolean`                 | `true` or `false`                                                                               |
| `date`                    | ISO 8601 date-time string                                                                       |
| `list`                    | Object with `selected` (the selected item's value, omitted if none) and `items` (array of `{ value, displayValue }`) |
| `image`                   | Object with `connectorId`, `assetId`, and `context`                                             |
| `richText`, `dataSource`  | Structured value (array or object)                                                              |
| `group`                   | Always omitted                                                                                  |

!!! warning "Don't depend on the structure of `richText` and `dataSource` values"

    The service passes `richText` and `dataSource` variable values straight through from the engine's internal model. Their shape isn't guaranteed and may change without notice. Don't build parsing that depends on their inner structure.

```json
{
  "type": "allVariables",
  "value": [
    { "name": "Headline", "type": "shortText", "isRequired": true, "value": "Summer sale" },
    { "name": "Price", "type": "number", "isRequired": false, "value": 19.99 },
    { "name": "Show logo", "type": "boolean", "isRequired": false, "value": true },
    {
      "name": "Size",
      "type": "list",
      "isRequired": false,
      "value": {
        "selected": "m",
        "items": [
          { "value": "s", "displayValue": "Small" },
          { "value": "m", "displayValue": "Medium" }
        ]
      }
    },
    { "name": "Product", "type": "group", "isRequired": false }
  ]
}
```

**Use it to** build your own input form or data mapping (for example, the column headers of a CSV for batch output) from the variables in a Template.

### dataConnector

Returns the data connector that is selected as the data source in the document.

| Field          | Type   | Description                                                                                     |
| -------------- | ------ | ----------------------------------------------------------------------------------------------- |
| `dataSourceId` | string | ID of the connector inside the document                                                         |
| `connectorId`  | string | ID of the connector in your GraFx environment. Only for connectors registered in GraFx          |
| `url`          | string | URL the connector is loaded from. Only for connectors loaded from a URL                         |
| `options`      | object | The connector options set in the document                                                       |
| `mappings`     | array  | The connector mappings set in the document                                                      |

If no data connector is selected, `value` is an empty object:

```json
{ "type": "dataConnector", "value": {} }
```

With a data connector selected:

```json
{
  "type": "dataConnector",
  "value": {
    "dataSourceId": "4f6e1d1c-...",
    "connectorId": "a1b2c3d4-...",
    "options": {},
    "mappings": []
  }
}
```

!!! warning "Don't depend on the structure of `mappings` items"

    The service passes each `mappings` item straight through from the engine's internal model. Its shape isn't guaranteed and may change without notice. Don't build parsing that depends on its inner structure.

**Use it to** find out which data connector a Template expects, so your integration can check that the connector exists in the environment or prepare the matching data.

### allTranslatables

Returns the end user-facing text of all variables and layouts, so you can send it for translation.

The result has two maps:

- `variables`: keyed by **variable name**. Each entry can have `label`, `placeholder`, `helptext`, and, for list variables, `listItems` (an object that maps each item value to its display value).
- `layouts`: keyed by **layout name**. Each entry can have `displayName`.

Text that isn't set is omitted, so an entry can be an empty object.

```json
{
  "type": "allTranslatables",
  "value": {
    "variables": {
      "Headline": {
        "label": "Headline",
        "placeholder": "Type your headline",
        "helptext": "Maximum 40 characters"
      },
      "Size": {
        "label": "Size",
        "listItems": { "s": "Small", "m": "Medium" }
      }
    },
    "layouts": {
      "Master": {},
      "A5": { "displayName": "A5 flyer" }
    }
  }
}
```

**Use it to** extract all end user-facing strings of a Template for a translation workflow.

### brandKitInfo

Returns the ID and name of the Brand Kit linked to the document. If the document has no Brand Kit, `value` is an empty object.

```json
{ "type": "brandKitInfo", "value": { "id": "8d5c1b9e-...", "name": "Corporate" } }
```

**Use it to** check which Brand Kit a Template depends on, for example before you copy Templates between environments.

## Example: Will the layout selector appear in Studio UI?

Suppose your portal opens Templates in [Studio UI](/GraFx-Developers/grafx-studio/editor-engine/integrate-studio-ui/), and you want to know in advance whether end users will see the layout selector, without loading the editor.

Studio UI shows the layout selector only when **2 or more layouts are available for the end user**. The `layoutsAvailableForUser` query returns exactly those layouts, so you only need to count them:

```javascript
const response = await fetch('https://template-information.chiligrafx.com/query', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    documentJson, // raw text from the Template download endpoint
    queries: [{ property: 'layoutsAvailableForUser' }],
  }),
});

const { results } = await response.json();
const availableLayouts = results[0].value;

const hasEnoughLayoutsForSelector = availableLayouts.length >= 2;
```

The layout count is one condition. Studio UI also hides the layout selector when the User Interface configuration turns it off:

- The **Layouts** section must be enabled in the User Interface, or in the `uiOptions` your integration passes to Studio UI.
- The **Layout selector** option must be on. See [Layout-specific options](/GraFx-Studio/concepts/user-interface/#layout-specific-options).

The Template Information Service reads only the document, not the User Interface, so check these settings separately.

## Troubleshooting

Error responses use HTTP status `400 Bad Request` and a **plain-text** body (not JSON). Read the body with `response.text()`, not `response.json()`.

| Response body                                                                                         | Cause                                                                                            | What to do                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Invalid JSON body: FormatException: ...`                                                             | The request body isn't valid JSON.                                                               | Check that you send a JSON object as the body. Build it with `JSON.stringify` instead of concatenating strings.                                 |
| `Invalid JSON body format`                                                                            | The body is JSON, but `documentJson` or `queries` is missing or has the wrong type, or a `property` value isn't a supported query name. | Check that `documentJson` is a **string** (not an object), that `queries` is an array of `{ "property": "..." }` objects, and that each query name is spelled exactly as in the [query reference](#query-reference). Names are case-sensitive. |
| `Failed to load document: Document has an unknown newer version (X). Supported versions should be <= Y` | The document was saved by a newer GraFx Studio version than the service supports.                | Don't retry with the same document. Wait until the service supports the newer version, or contact CHILI publish support.                        |
| `Failed to load document: ...` (other message)                                                        | `documentJson` isn't a valid GraFx document. For example, it's truncated, isn't JSON, or isn't a Template or Project. | Check that you send the full, unmodified response of the download endpoint. Don't edit the document JSON before you send it.                    |

### The result describes an empty document

If `documentJson` is an empty string (`""`) or an empty object (`"{}"`), the service doesn't return an error. It creates a new, empty document and returns information about that: one layout named `Default` and no variables. If you see this result, check that your download call returned the Template JSON and that you passed it to `documentJson`.

### A field I expected is missing

The service omits empty fields. See [Read the results](#5-read-the-results). Treat a missing field as `null`.

### Check the service version

Every response has an `X-Powered-By` header with the GraFx Studio version the service runs, for example `GraFx Studio 2.32.0`. Include it when you contact support.

## Limitations

- **Read-only.** The service returns information about a document. It can't change a Template or Project, and it doesn't save anything.
- **Only the JSON you send.** The service doesn't connect to your environment. It doesn't download Templates, look up assets, or call connectors. It works only with the document you put in `documentJson`.
- **Supported versions only.** The service can't read documents that are newer than the document version it supports. See [Troubleshooting](#troubleshooting).
- **Document information only.** The service doesn't read environment settings such as the User Interface configuration, and it doesn't return pages or frames.
