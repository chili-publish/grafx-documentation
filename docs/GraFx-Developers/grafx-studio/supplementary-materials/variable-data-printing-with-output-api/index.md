# Variable Data Printing With Output API

Variable Data Printing (VDP) allows you to generate PDF outputs where variables are dynamically updated based on a dataset. This guide explains how to use the Output API endpoints to achieve VDP functionality.

!!! warning

    Currently, only PDF output is supported.

## Requirements

Before proceeding, ensure you are familiar with:

  - Authentication process. (See: [Environment Quickstart](/GraFx-Developers/environment-api/01-overview/))
  - Output generation loop.
  - Difference between Templates and Projects. (See: [Templates vs Projects](/GraFx-Developers/supplementary-materials/templates-vs-projects/))

## Variable Management

### Establishing a Variable Naming Schema

It's crucial to establish a consistent variable naming schema with acceptable values, agreed upon by both designers and developers. This schema should be comprehensive enough to eliminate the need for variable value lookups beyond obtaining default values in VDP workflows.

### Retrieving Variables

If you need to look up variables and their values in a document, you'll need to examine the document JSON. For documents stored on the CHILI GraFx Platform, use the following endpoints (assuming a production environment):

  - Templates: `GET: https://{environment}.chili-publish.online/api/v1/environment/{environment}/templates/{templateId}/download`
  - Projects: `GET: https://{environment}.chili-publish.online/api/v1/environment/{environment}/projects/{projectId}/document`

## Updating Variables

!!! warning

    Currently, only text (shortText), list, and image variables are supported.

To update variables when generating a PDF output, modify your API request with a `variables` property as follows:

```javascript
const variables = [
  {
    "Label": "Red Drink",
    "Colors": "Red",
    "Product Shot": "red-bottle"
  },
  {
    "Label": "Blue Drink",
    "Colors": "Blue",
    "Product Shot": "blue-bottle"
  }
];

const pdfOutput = await fetch(`https://cp-example.chili-publish.online/api/v1/environment/cp-example/output/pdf`, {
  headers: { 
    "authentication": authToken,
    "content-type": "application/json"
  },
  body: JSON.stringify({
    outputSettingsId: outputId,
    layoutsToExport: ["0"],
    variables: variables,
    documentContent: documentJson
  }),
  method: "POST"
});
```

Key points:

  - The `variables` property accepts an array of objects.
  - Each object represents a set of variable updates (a row) for a single output.
  - Variable names are keys, and their new values are the corresponding values.
  - Only string and null values are accepted. Numbers, objects, arrays, and booleans will cause a 400 Bad Request error.
  - Variable values are typed-checked during output and must match what is allowed in GraFx Studio for the type of variable you are setting (see [Variable Type Details](#variable-type-details)).

!!! tip

    Always set a value for variables that might change during output. Omitted variables will inherit values from the previous object in the array, which can lead to unwanted output results.

!!! tip

    If your VDP data comes from a source that doesn't guarantee type consistency with GraFx Studio document variable types (e.g., a CSV file), perform type checking before attempting output to avoid 500 errors.

### Limitations

There's a hard limit of 10,000 rows (objects) or a 10 MB request body, whichever comes first. To exceed these limits, you'll need to make multiple output requests and merge the results if a single PDF is required.

## Variable Type Details

### Short Text Variable

**Supported Types**: string

### List Variable

**Supported Types**: string

List variables can only be set to values that exist in the variable's predefined item list. Attempting to set an invalid value (nonexistent item) will result in an error.

In example, if the document list variable `Colors` has the list items: 

  - Red
  - Blue
  - Green

Then trying to set `Colors` to "Yellow" will cause a 500 Internal Server Error during the PDF output process when calling the task status API.

### Image Variable

**Supported Types**: string

If you are using the default media connector, you can set this to either the name or ID of the image in GraFx Media. Be cautious when using the image name: if multiple images share the same name, the first one found in the database (not based on folder structure) will be used. To prevent conflicts, the document should specify a folder directory.

