# Section 13: Project Save and Order Endpoints

This section provides instructions for setting up server endpoints to save and order projects.

**Objectives**

- Implement and test the save functionality for projects.
- Implement and test the order functionality for projects.

## 1. Implementing Save Functionality

We are going to follow the same pattern of creating an endpoint in `server.js` and at least one helper function in `chili.js`

In `server.js`, set up a new endpoint to handle project saves:

```js
app.put("/project/:projectid", async (context) => {

  const userType = getUserType(context);

  if (userType == "unauth") {
    return context.text("Unauthorized", 401);
  }

  const projectJSON = await context.req.json();

  // Quick dirty check to see we got a document
  if (projectJSON.selectedLayoutId == null) {
    return context.text("Error: not valid document", 500);
  }

  const {projectid} = context.req.param();

  const dangerousToken = await getDangerousToken(db);

  const success = await updateProjectJSON({
    projectID: projectid,
    token: dangerousToken,
    baseURL: baseURL,
    environment:environment,
    json: projectJSON
  })

  if (success) {
     return context.text("Success", 200);
  }
  else
  {
    return context.text("Error saving", 500);
  }

});
```

The endpoint captures the project JSON and updates it using the `updateProjectJSON` function from `chili.js`. 

Don't be fooled. This endpoint is using "put" instead of "get".

!!! warning

    The current document validation is basic. In a production environment, a more thorough validation should be performed.

Now, let's define the `updateProjectJSON` helper function in `chili.js`:

```js
export async function updateProjectJSON({ projectID, token, baseURL, environment, json }) {
  const url = `${baseURL}/grafx/api/v1/environment/${environment}/projects/${projectID}/document`;

  try {
    const response = await fetch(url, {
      method: 'PUT',
      headers: {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(json) // Make sure that `json` is an object or array, not a JSON string
    });

    if (response.ok) {
      // 204 No Content means the update was successful
      return true;
      console.log('Project JSON updated successfully.');
    } else {
      // If the response status code is not 204, throw an error
      const errorBody = await response.text();
      throw new Error(`Error ${response.status}: ${errorBody}`);
    }
  } catch (error) {
    // Log and rethrow any errors
    console.error("Failed to update project JSON:", error);
    throw error;
  }
}
```

!!! warning

    Remember to import `updateProjectJSON` in `server.js`.

## Setting Up Order Functionality

To handle project orders, define an endpoint in `server.js` as follows:

```js
app.post("/order/:projectid", async (context) => {

  const userType = getUserType(context);

  if (userType == "unauth") {
    return context.text("Unauthorized", 401);
  }

  const {projectid} = context.req.param();

  const dangerousToken = await getDangerousToken(db);

  const taskID = await outputProject({
    projectID: projectid,
    token: dangerousToken,
    baseURL: baseURL,
    environment:environment,
  });

  if (taskID != null) {
    db.addOrder({taskID, projectID:projectid});

    return context.json({success:true})
  }
});
```

This endpoint initiates an output request to the GraFx Environment API and saves the returned task ID in an order database.

The corresponding helper function in `chili.js` is:

```js
export async function outputProject({projectID, token, baseURL, environment}) {
  const outputUrl = `${baseURL}/grafx/api/v1/environment/${environment}/output/image?projectId=${projectID}&outputType=png&layoutToExport=0&pixelRatio=1`;

  try {
    const response = await fetch(outputUrl, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Authorization': `Bearer ${token}` 
      }
    });

    if (response.status === 200) {
      const jsonResponse = await response.json();
      return jsonResponse.data.taskId;
    } else {
      // Handle other HTTP status codes appropriately
      throw new Error(`Unexpected response status: ${response.status}`);
    }
  } catch (error) {
    console.error("Failed to output project:", error);
    throw error;
  }
}
```

!!! warning

    Remember to import `outputProject` in `server.js`.

## 3. Show Past Projects

Finally, to finish off our mini-project, we will should add the endpoint `/user/projects` to `server.js`, which `store-front.html` calls to get all the former Projects the user created.

```js
app.get("/user/projects", async (context) => {
  const userType = getUserType(context);

  if (userType == "unauth") {
    return context.text("Unauthorized", 401);
  }

  return context.json(db.getUserProjects("user"))
});
```

## 4. Testing The Workflow

After setting up the endpoints, you can now test the "Save Project" and "Order Project" functionalities:

- Restart the server using `node server.js`.
- Use the "Save Project" button to save changes. Refresh the page to ensure persistence.
- Use the "Order Project and check to see orders were added to the `database.json` file.
