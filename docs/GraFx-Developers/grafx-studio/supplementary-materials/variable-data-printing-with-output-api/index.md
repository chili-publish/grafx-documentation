# Variable Data Printing With Output API

Variable Data Printing (VDP) allows you to generate PDF outputs where variables are updated and changed based on a dataset. This guide explains how to use the Output API endpoints to achieve VDP functionality.

!!! warning

    Currently only PDF output is supported

## Requirements

Before proceeding, ensure you are familiar with:

  - Authentication process. (See: [Environment Quickstart](/GraFx-Developers/environment-api/01-overview/))
  - Output generation loop.
  - Difference between Templates and Projects. (See: [Templates vs Projects](/GraFx-Developers/supplementary-materials/templates-vs-projects/))

## Variable Management

### Establishing a Variable Naming Schema


It is very important to build a variable naming schema with acceptable values that is agreed upon by designers and developers when integrating for Variable Data Printing. Outside of other workflows not related to VDP, there should never be a requirement to look up the variable values beyond getting the default values.

If you need to lookup the variables in a document and their values, you will need to look at the document JSON. If you are storing your documents on the CHILI GraFx Platform, you can lookup the JSON with the following endpoints (assuming on a production environment):


- Templates: `GET: htts://{environment}.chili-publish.online/api/v1/environment/{environment}/templates/{templateId}/download`
- Projects: `GET: htts://{environment}.chili-publish.online/api/v1/environment/{environment}/projects/{projectId}/document`


## Updating Variables

!!! warning

    Currently only text (shortText), list, and image variables are supported

Updating variables is really easy. When you go to generate a PDF output, you will make a request similar to this this:

```javascript
const pdfOutput = await fetch(`https://cp-example.chili-publish.online/api/v1/environment/cp-example/output/pdf`, {
  headers: { 
    "authentication": authToken,
    "content-type": "application/json"
  },
  body: JSON.stringify({
    outputSettingsId: outputId,
    layoutsToExport: ["0"],
    documentContent: documentJson
  }),
  method: "POST"
})
```

Where:

  - `authToken` is a variable that holds our bearer token
  - `outputId` is a variable that holds the ID of the output settings
  - `documentContent` is a variable that holds the JSON of our document

Let's pretend in this example that our document JSON contains 4 variables:

  - A text (shortText) variable by the name of `Label`
  - A list variable by the name of `Colors`
  - A image variable by the name of `Product Shot`

If we wanted to update each variable for output we can add a property to our request called `variables`, which takes a limited JSON-like object-array that only accepts strings and null. Numbers, objects, arrays, and booleans are not accepted and will cause a 400 Bad Request.

```javascript
const variables = [
  {
    "Label": "Red Drink",
    "Colors": "Red",
    "Product Shot": "red-bottle"
  }
]

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
})
```

The structure is simple, an object with the key being the name of the variable, and the value being the value you want to set the variable to.

Each variable is typed checked, so trying to set `Label` to a null value, will cause a 500 error.

If you wanted to output a PDF with the document copied twice then you just add another object to the `variables` object-array like so:

```javascript
const variables = [
  {
    "Label": "Red Drink",
    "Colors": "Red",
    "Product Shot": "red-bottle"
  },
  {
    "Label": "Red Drink",
    "Colors": "Red",
    "Product Shot": "red-bottle"
  }
]

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
})
```

Of course, this example would end up with a PDF output that has 2 copies of the document with the same variable data. We could change that data for each object in the `variables` object-array to get unique results. For example:

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
]
```

Be careful, because even though the `variables` property allows you to drop a variable in an object, it will carry over the value from the previous object.

So, imagine we remove `Colors` from the second object.


```javascript
const variables = [
  {
    "Label": "Red Drink",
    "Colors": "Red",
    "Product Shot": "red-bottle"
  },
  {
    "Label": "Blue Drink",
    "Product Shot": "blue-bottle"
  }
]
```

This is legal, and will output, but the value of `Colors` will be "Red" for the second object. If that list variable changed the background color, then you would end up with your `Label` being "Blue Drink", your `Product Shot` being "blue-bottle", and your background color being red.

In general it is good practice that if a document variable might be changed during output, then you should always set it to a value.

!!! tip

  It is good practice that if a document variable might be changed during output, then you should always set it to a value. If you leave a document variable out of the update object, then it will take the value of the previous object.

In addition, if the data is coming from a source that does not enforce the schema you agreed with your designers for the document being integrated (e.g. a CSV file), it is good practice to type check the data before trying to output. Otherwise, the output will fail with a 500 when getting the task status.


!!! tip

  If the data for VDP is coming from a source that does not guarantee that the type of the data will follow GraFx Studio variable typing, then you should type check the data before trying to output.

You can keep adding objects to your object-array to output hundreds or thousands of unique documents. Each object added is typically considered a "row". However, you do have a hard limit of ten thousand rows or 10 mb request body, whichever come first. To get around that limit, you can request multiple outputs, but you will need to merge the results of each output into a single PDF (if that is a requirement).

!!! warning

  There is a ten thousand row (object) limit or a 10 mb request body limit, which ever comes first.

## Variable Type Details

While we have gone through the basics above, below we will go through each document variable type and discuss the specifics.

### Short Text Variable

**Types Supported**

  - string


### List Variable

**Types Supported**

  - string

You cannot set a list variable to a value that does not exist in the list in the document. Doing so will cause a 500 error.

So for example, if the document list variable `Colors` has the list items: "Red", "Blue", and "Green". Then trying to set `Colors` to "Yellow" will cause a 500 error during getting the task status.

### Image Variable

**Types Supported**

  - string

If you are using the default media connector then you can set this to the name of the image in GraFx Media or the ID of the image in GraFx Media. Be careful if you are using the image name, as if there are more than one images with that name, the first image with that name found in the database (not based on a folder structure) will be used. The document should define a folder directory to avoid a conflict.

If the image does not exist, the output will fail with a 500 during getting the task status.

