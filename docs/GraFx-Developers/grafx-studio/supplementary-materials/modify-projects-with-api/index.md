# Modify Projects With the Environment API

The project modification endpoints of the Environment API change a project document on the server, without opening it in an editor. In one request you can set variable values, select a layout, change the page size, and run the document's Actions.

Use them to:

- Prefill a project with data from a CRM, PIM or order system before a user opens it
- Switch a project to another layout or page size as part of an automated flow
- Prepare a document for output in your own integration, without storing it in the environment

## Requirements

Before proceeding, make sure you are familiar with:

- The authentication process (see [Environment API overview](/GraFx-Developers/environment-api/01-overview/))
- The difference between templates and projects (see [Templates vs Projects](/GraFx-Developers/grafx-studio/supplementary-materials/templates-vs-projects/))
- Polling a task until it finishes, as you do for previews and output

The endpoints work with documents from GraFx Studio **1.49** and later. A document made with an older version is upgraded to the GraFx Studio version of your environment during the task.

## Stored project or supplied document

There are two ways to start a modification. Both run as an asynchronous task and use the same request fields.

| | Stored project | Supplied document |
|---|---|---|
| Endpoint | `POST …/projects/{projectId}/modifications` | `POST …/projects/modifications` |
| Source | The project document stored in the environment | The document JSON you send in `document` |
| Result | Saved on the project | Returned in the task result; nothing is stored |
| Use when | Your projects live in CHILI GraFx | You keep documents in your own system |

Start a modification of a stored project:

```
POST /api/v1/environment/{environment}/projects/{projectId}/modifications
```

Start a modification of a document you supply:

```
POST /api/v1/environment/{environment}/projects/modifications
```

Get the status and result of either task:

```
GET /api/v1/environment/{environment}/projects/modifications/tasks/{taskId}
```

## Request fields

| Field | Description |
|---|---|
| `variables` | Values to set, as an array of `{ "name", "value" }` objects |
| `selectedLayoutId` | ID of the layout to select, from the document's `layouts` array |
| `pageSize` | New page size, as `{ "width", "height", "unit" }` |
| `executeActions` | Run the document's Actions during the task. Default `true` |
| `document` | The project document JSON. Required on the supplied-document endpoint only |

Send at least one of `variables`, `selectedLayoutId` or `pageSize`, or leave `executeActions` set to `true`. An empty body (`{}`) on a stored project runs its Actions only.

### Variables

- Use the project document as the reference for variable names and the value each variable accepts. Get it with:

    ```
    GET /api/v1/environment/{environment}/projects/{projectId}/document
    ```

- Variable names are case-insensitive.
- A name that appears twice in `variables` makes the request fail.
- Names that don't exist on the document are ignored.
- A value can be a string, number, boolean, object or array, depending on the variable type.

### Actions

With `executeActions` set to `true`, the document's [Actions](/GraFx-Studio/concepts/actions/) run during the task. Actions can make further changes to the document or call external systems.

Set `executeActions` to `false` to apply only the fields you send.

## Example

The request below fills three variables on a stored project, selects a layout and sets an A4 page size.

```bash
curl -X 'POST' \
  'https://cp-exp-321.chili-publish.online/grafx/api/v1/environment/cp-exp-321/projects/89a704fd-1adc-41ee-9852-c0c70c1a6ad6/modifications' \
  -H 'Authorization: Bearer <BEARER TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "variables": [
      { "name": "Title", "value": "Summer sale" },
      { "name": "Quantity", "value": 3 },
      { "name": "Featured", "value": true }
    ],
    "selectedLayoutId": "d7efa1ad-8bf7-412d-b9fc-cff06bcce5ba",
    "pageSize": { "width": 210, "height": 297, "unit": "mm" },
    "executeActions": true
  }'
```

The response holds the task ID:

```json
{
  "data": { "taskId": "6e39032c-ead5-4c70-8b4b-e378bf1b5c51" },
  "links": { "taskInfo": "…" }
}
```

## Read the result

Poll the task endpoint with the task ID. It returns `202` while the task runs, and `200` when it has finished:

```json
{
  "data": {
    "taskId": "6e39032c-ead5-4c70-8b4b-e378bf1b5c51",
    "modification": {
      "isDocumentModified": true,
      "projectId": "89a704fd-1adc-41ee-9852-c0c70c1a6ad6",
      "document": null,
      "errors": []
    }
  },
  "links": {}
}
```

| Field | Stored project | Supplied document |
|---|---|---|
| `errors` | Empty when the modification succeeded | Empty when the modification succeeded |
| `projectId` | The modified project | `null` |
| `document` | `null` — read the saved document from the project | The modified document JSON |
| `isDocumentModified` | Whether the document changed | Whether the document changed |

Check `errors` first. When it isn't empty, the modification didn't succeed, and a stored project keeps its previous document.

!!! tip "Confirm your changes in the document"
    `isDocumentModified` reports any change to the document, including the upgrade to a newer GraFx Studio version. It can be `true` when none of your values were applied — for example when a variable name didn't match. Read the document to confirm the values you sent.

!!! note "Project already being updated"
    If another operation is updating the same project, the stored-project endpoint returns `409 Conflict`. Retry after a moment.

## Next steps

- Generate output from the modified project with the output endpoints (see [Making API Calls](/GraFx-Developers/environment-api/04-making-api-calls/))
- Produce many variations in one output request with [Variable Data Printing With Output API](/GraFx-Developers/grafx-studio/supplementary-materials/variable-data-printing-with-output-api/)
- Explore every field in the [Environment API reference](/GraFx-Developers/environment-api/reference/)
