# Section 12: Get Project JSON

This section details the implementation of a new endpoint to download the Project JSON data to load the a document in an editor.

**Objectives**

- Implement the endpoint for project data retrieval.
- Verify the project download functionality.

## 1. Adding project download endpoint

To enable project testing in `editor.html`, we must introduce the `/project/:projectID/` endpoint. This endpoint retrieves project details in JSON format.

Update `server.js` with the new endpoint as follows:

```js
app.get("/project/:projectid", async (context) => {
  const userType = getUserType(context);

  if (userType == "unauth") {
    return context.text("Unauthorized", 401);
  }

  const {projectid} = context.req.param();

  const dangerousToken = await getDangerousToken(db);

  const projectJSON = await getProjectJSON({
    projectID:projectid,
    token: dangerousToken,
    baseURL: baseURL,
    environment:environment,
  });

  return context.json(projectJSON);

});
```

This endpoint validates user access, obtains the `projectID`, retrieves the project JSON from CHILI, and returns the project data.

Next, we'll need to define the `getProjectJSON` function, which our endpoint relies upon to interact with the GraFx Environment API.

This pattern will repeat as your server code will use functions the encapsulate the GraFx Environment API.

## 2. Adding getProjectJSON

In `chili.js`, add the `getProjectJSON` function to fetch and return the project's JSON

```js
export async function getProjectJSON({ projectID, token, baseURL, environment }) {
  // Construct the URL for the GET request without URI encoding
  const url = `${baseURL}/grafx/api/v1/environment/${environment}/projects/${projectID}/document`;

  try {
    // Make the GET request to the server
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Authorization': `Bearer ${token}` 
      }
    });

    if (!response.ok) {
      // If the response is not 2xx, throw an error
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the JSON response and return it
    return await response.json();
  } catch (error) {
    // Log and rethrow any errors
    console.error("Failed to get project JSON:", error);
    throw error;
  }
}
```

Ensure this new function is imported in `server.js` for use:

```js
import { getTemplateMetaData, createNewProject, getProjectJSON } from "./chili.js"
```

## 3. Testing Loading Project

We are finally ready to test our ability to turn a Template into a Project and open it in an Studio engine editor.

1. Restart your server by running `node server.js`.
2. Navigate to `http://localhost:3000` in your web browser.
3. Log in as an "User".
4. Select a template by pressing "Edit"
5. A page should open, and the Template we selected should open as Project in a Studio engine instance

The "Save Project" and "Order Project" buttons do not work yet.