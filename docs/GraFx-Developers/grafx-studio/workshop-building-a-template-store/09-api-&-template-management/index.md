# Section 9: API & Template Management

This section outlines the steps for managing templates in our system, including using access tokens, retrieving template metadata, and updating template records via our API.

**Objectives**
- Understand the process of using access tokens within the API.
- Learn to retrieve and handle template metadata.
- Integrate template metadata retrieval into our API endpoint.

## 1. Utilizing Access Tokens

Firstly, integrate the `getDangerousToken` function into the `/templates/:id` route within the `server.js` file:

Import the `getDangerousToken` function by adding it to the existing import statement:

```js
import { setUserCookie, getUserType, getDangerousToken  } from "./utility.js";
```

Modify the `/templates/:id` endpoint to utilize the token:

```js
app.post("/templates/:id", async (context) => {
  const userType = getUserType(context);

  if (userType != "admin") {
    return context.text("Unauthorized", 403);
  }

  const {id} = context.req.param();

  const dangerousToken = await getDangerousToken(db);

  //db.addTemplate(???);
});
```

With our token in hand, we need to actually make an API call to CHILI to get the meta data around this template.

## 2. Retrieving Template Metadata

Create a new function in `chili.js` to make an API call for template metadata:
```js
export async function getTemplateMetaData({ token, baseURL, environment, id }) {
  const url = `${baseURL}/grafx/api/v1/environment/${environment}/templates/${id}`;

  try {
    const response = await fetch(url, {
      method: 'GET', // The method is GET by default for fetch
      headers: {
        'Accept': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    });

    if (response.ok) {
      const jsonResponse = await response.json();
      const { id, name } = jsonResponse.data;
      return { id, name };
    } else {
      console.log(`Response failed with status ${response.status} : ${await response.text()}`);
    }

    return null;
  } catch (error) {
    console.error('Error fetching template metadata:', error);
    return null;
  }
}
```

!!! note

    Currently, the function returns a 500 error code when a template does not exist instead of the more appropriate 404, making it challenging to discern if the template is missing or if there's a server error.

## 3. Integrating Template Metadata

Update the `/templates/:id` endpoint in `server.js` to use the new `getTemplateMetaData` function:

```js
app.post("/templates/:id", async (context) => {
  const userType = getUserType(context);

  if (userType != "admin") {
    return context.text("Unauthorized", 403);
  }

  const {id} = context.req.param();

  // Add a error message to if the template is already registered
  if (db.getTemplates().findIndex(t => t.id == id) != -1) {
    return context.json({error: `Template ${id} already registered`}, 500);
  }

  const dangerousToken = await getDangerousToken(db);

  const templateMeta = await getTemplateMetaData({
    token: dangerousToken,
    baseURL: baseURL,
    environment:environment,
    id:id });

  if (templateMeta == null) {
    return context.json({error:`Unable to locate template ${id} or error`}, 500);
  }

  db.addTemplate(templateMeta);
  return context.json(templateMeta);

});
```

## 5. Creating Config Variables

You might be getting errors in `server.js` because `baseURL` and `environment` do not exist yet.

Create two new variables, and place them anyhere before we call `new Hono()`.

```js
// ...import files
const db = initDB();

// New variables here
const baseURL = process.env["BASEURL"];
const environment = process.env["ENVIRONMENT"];

const app = new Hono();
// ...rest of server.js
```


## 4. 🧪Testing the Registration Function

Conduct tests to ensure the registration function is operational:

1. Obtain a template ID from your environment (you have to open the template in Designer to grab the ID from the URL).
2. Restart your server by running `node server.js`.
3. Navigate to `http://localhost:3000` in your web browser.
4. Log in as an "Admin".
5. Attempt to register a template using an incorrect ID to validate the error response.
6. Register an existing template using a correct ID to confirm successful addition.
7. Register multiple templates for the next section.
