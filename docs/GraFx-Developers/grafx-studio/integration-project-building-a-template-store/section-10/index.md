# Section 10: Implementing Editable Projects

In this section, we'll cover how to create an editable Projects within our application. This process involves creating a new Project from a Template, enabling editing in our storefront, and handling the backend server configuration to support these features.

**Objectives**

- Transform templates into editable projects.
- Implement necessary backend endpoints.
- Integrate Studio egine editing functionality into our `editor.html` page.

## 1. Converting Templates to Projects
To initiate template editing, the user will press the `Edit` button in the storefront, which triggers a request to our server. Here's the process to handle this action:

In `server.js`, incorporate the following code to define an endpoint, called by `store-front.html` that creates a new project based on a template:

```js
app.post("/user/project/:templateid", async (context) => {
    const userType = getUserType(context);

    if (userType == "unauth") {
        return context.text("Unauthorized", 401);
    }

    const {templateid} = context.req.param();

    const dangerousToken = await getDangerousToken(db);

    const project = await createNewProject({
      templateID:templateid,
      token: dangerousToken,
      baseURL: baseURL,
      environment:environment,
    });

    db.addProjectToUser({userID:"user", projectID: project.id, projectName: project.name});

    return context.json({id:project.id});
});
```

This endpoint validates the user, creates a new project using the specified template ID, and then adds this project to the database.

## 2. Implementing the New Project Creation Function

To convert a template into a project, we define the `createNewProject` function in `chili.js`:

```js
export async function createNewProject({ templateID, token, baseURL, environment }) {
  const url = `${baseURL}/grafx/api/v1/environment/${environment}/projects`;
  const headers = {
    'Accept': '*/*',
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`,
  };
  const body = {
    template: {
      id: templateID
    }
  };

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      const errorBody = await response.text();
      throw new Error(`Error ${response.status}: ${errorBody}`);
    }

    // Parse the JSON response
    const responseData = await response.json();

    // Only need the id and name from the response
    const result = {
      id: responseData.id,
      name: responseData.name,
    };

    return result;
  } catch (error) {
    // Handle errors, such as network issues
    console.error("Failed to create new project:", error);
    throw error;
  }
}
```

This function makes an API request to create a new project from the specified template and returns the resulting project's ID and name.

Don't forget to import our new function in `server.js`.

```js
import { getTemplateMetaData, createNewProject } from "./chili.js"
```

## 4. Setting Up the Editor Page Endpoint

The editor page allows users to modify their project. In `server.js`, add the endpoint for serving the editor page:

```js
app.get("/editor/:projectid", async (context) => {
  const userType = getUserType(context);

  if (userType == "unauth") {
    return context.redirect("/")
  }

  const storefrontPage = await fs.promises.readFile("public/editor.html", "utf8");
  return context.html(storefrontPage);
});
```

This endpoint serves `editor.html` when the project needs to be edited.

### Updating `editor.html`

Below you will find the content (open the tab) to update `editor.html`.

??? abstract "editor.html content"

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Editor</title>
    <script src="http://spicy-labs.com/external/allow/bundle.js" ></script>

    </head>
    <body>
      <h1>Project Editor</h1>
      <button onclick="saveProject()">Save Project</button>
      <button onclick="orderProject()">Order Project</button>
      <div id="studio-editor" style="height:70vh"></div>
      <script>

        // Extract the project ID from the URL
        const pathArray = window.location.pathname.split('/');
        const projectID = pathArray[pathArray.length - 1];

        document.addEventListener("DOMContentLoaded", loadProject);

        // Load Project Function
        async function loadProject() {

          const SDK = new StudioSDK({
            editorId: "studio-editor"
          });

          SDK.loadEditor();
          window.SDK = SDK;

          try {
            // Fetch the auth token first
            const authResponse = await fetch('/user/authdata');
            const authData = await authResponse.json();

            if (authData.success && authData.token) {
              // Store the token in a variable
              const authToken = authData.token;
              const environmentAPI = authData.apiURL;

              window.SDK.configuration.setValue("GRAFX_AUTH_TOKEN", authToken);
              window.SDK.configuration.setValue("ENVIRONMENT_API", environmentAPI);

              // Now fetch the project data using the project ID
              const projectResponse = await fetch(`/project/${projectID}`);
              const projectData = await projectResponse.json();
              
              // Load the document using SDK
              window.SDK.document.load(projectData);

            } else {
              throw new Error('Failed to authenticate or receive a valid token.');
            }
          } catch (error) {
            console.error('An error occurred while loading the project:', error);
            alert(error.message);
          }
        }

        // Save Project Function
        async function saveProject() {
          // Get the current state from the SDK
          const currentStateResp = (await window.SDK.document.getCurrentState());

          try {
            if (currentStateResp.success != true) {
            console.log(currentStateResp);
              throw new Error("Getting document state failed")
            }

            // Send the current state data to the server using PUT request
            const response = await fetch(`/project/${projectID}`, {
              method: 'PUT',
              headers: {
                'Content-Type': 'application/json',
              },
              body: currentStateResp.data
            });

            if (!response.ok) {
              // If the response is not ok, throw an error
              const errorText = await response.text();
              throw new Error(`Failed to save project: ${errorText}`);
            }

            // Handle a successful save
            console.log('Project saved successfully!');
          } catch (error) {
            console.error('An error occurred while saving the project:', error);
            alert(error.message);
          }
        }

        async function orderProject() {
          await saveProject();

          try {
            // Send the current state data to the server using PUT request
            const response = await fetch(`/order/${projectID}`, {
              method: 'POST'
            });

            if (!response.ok) {
              // If the response is not ok, throw an error
              const errorText = await response.text();
              throw new Error(`Failed to order project: ${errorText}`);
            }

            // Handle a successful save
            alert("Project ordered successfully!");
            window.location.href = "/";
          } catch (error) {
            console.error('An error occurred while ordering the project:', error);
            alert(error.message);
          }

        }
    </script>
      </body>
    </html>
    ```

The `editor.html` page provided includes three JavaScript functions:

- `loadProject`: Initializes the editor with the project data on page load.
- `saveProject`: Saves the current state of the project to the server.
- `orderProject`: Finalizes the project and submits an order.


??? note "loadProject"

    This function is responsible for initializing and loading the project into the editor when the web page has finished loading (as it's called by the `DOMContentLoaded` event). Here's how it works:

    - **Initialization**: It creates an instance of `StudioSDK` with the `editorId` corresponding to the HTML element where the editor is placed
    - **Authentication**: It fetches an authentication token by making an API call (`/user/authdata`). This token is required to ensure that the user has the necessary permissions to load the project.
    - **Configuration**: Sets necessary configuration values for the SDK, such as the authentication token and the environment API endpoint.
    - **Project Loading**: The function retrieves the project ID from the current URL path, makes an API call to `/project/${projectID}` to fetch the project data using this ID, and then uses the SDK's `document.load` method to load the project data into the editor.

??? note "saveProject"

    This function is invoked when a user clicks the "Save Project" button. Its main goal is to save the current state of the project back to the server:

    - **State Retrieval**: It uses the SDK's `document.getCurrentState` method to get the current state of the project from the editor.
    - **Project Identification**: Extracts the project ID from the URL similar to the `loadProject` function.
    - **API Communication**: Sends the current state data to the server with a PUT request to the endpoint corresponding to the project ID (`/project/{projectID}`).
    - **Error Handling**: If the saving process fails, it throws an error with a message indicating the failure.

??? note orderProject

    This function is intended to be called when a user wants to finalize and order the project which generates an image:

    - **Prerequisite Action**: Calls `saveProject` to ensure the latest state of the project is saved before ordering.
    - **Order Request**: Makes a POST request to the `/order/{projectID}` endpoint to create an order for the current project.
    - **Success and Redirection**: If successful, alerts the user that the project was ordered and redirects them to the home page.
    - **Error Handling**: In case of an error, it displays an alert with the error message.


For these to work, the following endpoints must be defined:

- `/user/authdata`: To authenticate the user and retrieve necessary tokens.
- `/project/{projectID}`: To handle saving and loading of project data.
- `/order/{projectID}`: To send our order to generate an image.
