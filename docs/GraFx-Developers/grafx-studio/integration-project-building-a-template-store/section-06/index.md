# Section 6: Displaying Mock Templates

This section focuses on enhancing the server-side handling of our application to dynamically display content based on user roles. By leveraging mock data and utility functions, we'll create routing system that serves different experience for admins and users. This prepares the groundwork for integrating our mock database to deliver content dynamically.

**Objectives**

- **Implement Role-Based Routing:** Modify the root route in `server.js` to display different content for admin and user roles.
- **Optimize Cookie Handling:** Create a utility function to streamline the process of checking user types from cookies, which aids in maintaining clean and DRY (Don't Repeat Yourself) code.
- **Refactor Server Code:** Utilize the newly created utility function within `server.js` to check user types and serve the appropriate content.
- **Update HTML Content:** Modify `store-front.html` where templates for our users to pick will be displayed.
- **Create a Templates Endpoint:** Set up an endpoint in `server.js` to serve mock data representing templates, simulating the future dynamic data delivery from the database.
  

## 1. Configuring Route Handlers Based on User Roles
After setting up cookie handling, it's time to direct requests to the appropriate handlers depending on the user's role (admin or user). Update the root route (`/`) in the `server.js` file to differentiate the traffic:

```javascript
app.get("/", async (context) => {
  const userCookie = getCookie(context, "user");

  if (!userCookie) {
    const loginPage = await fs.promises.readFile("public/login.html", "utf8");
    return context.html(loginPage);
  }

  const user = JSON.parse(userCookie);

  if (user.type === "admin") {
    // Admin-specific routing will be added later
  }
  else {
    const storefrontPage = await fs.promises.readFile("public/store-front.html", "utf8");
    return context.html(storefrontPage);
  }
});
```

## 2. Creating a Utility Function for User Type Checks
Repeatedly checking cookies for user types is common, thus we'll encapsulate this logic into a reusable utility function. Define the `getUserType` function in `utility.js`:

```javascript
export function getUserType(context) {
  const userCookie = getCookie(context, "user");

  if (!userCookie) {
    return "unauth";
  }

  const user = JSON.parse(userCookie);
  return user.type;
}
```

Ensure `getCookie` is imported in `utility.js`:

```javascript
import { setCookie, getCookie } from "hono/cookie";
```

Then, import and utilize `getUserType` in `server.js`:

```javascript
import { getUserType } from "./utility.js";

app.get("/", async (context) => {
  const userType = getUserType(context);

  if (userType === "unauth") {
    const loginPage = await fs.promises.readFile("public/login.html", "utf8");
    return context.html(loginPage);
  }

  if (userType === "admin") {
    // Admin routing will be added later
  }
  else {
    const storefrontPage = await fs.promises.readFile("public/store-front.html", "utf8");
    return context.html(storefrontPage);
  }
});
```

## 3. Modifying `store-front.html`

Update `store-front.html` with the HTML below (open the tab):

??? abstract "store-front.html content"

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Templates Gallery</title>
    <style>
      .template-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px; /* Add some space between the template divs */
      }
      .template {
        border: 1px solid #ccc;
        padding: 10px;
        width: 200px;
      }
      .template img {
        width: 200px; /* Fixed width for all images */
        height: auto; /* Maintain aspect ratio */
      }
      .template h3 {
        margin: 0;
        font-size: 1.2em;
        color: #333;
      }
      .template button {
        margin-top: 10px;
      }
    </style>
    </head>
    <body>
    <h2>Templates</h2>
    <div id="templates" class="template-container">
      <!-- Templates will be loaded here -->
    </div>
    <h2>User Projects</h2>
    <div id="projects" class="template-container">
      <!-- Projects will be loaded here -->
    </div>

    <script>
      window.onload = function() {
        fetch('/templates')
          .then(response => response.json())
          .then(data => {
            const templatesDiv = document.getElementById('templates');

            data.forEach(template => {
              const div = document.createElement('div');
              div.id = template.id;
              div.className = 'template';
              div.innerHTML = `
                <h3>${template.name}</h3>
                <img src="preview/template/${template.id}" alt="${template.name}">
                <br/>
                <button onclick="editTemplate('${template.id}')">Start Project</button>
              `;
              templatesDiv.appendChild(div);
            });
          })
          .catch(error => console.error('Error loading templates:', error));
          
          fetch('/user/projects')
          .then(response => response.json())
          .then(data => {
            const projectsDiv = document.getElementById('projects');

            data.forEach(project => {
              const div = document.createElement('div');
              div.id = project.id;
              div.className = 'template';
              div.innerHTML = `
                <h3>${project.name}</h3>
                <img src="preview/project/${project.id}" alt="${project.name}">
                <br/>
                <button onclick="window.location.href = '/editor/${project.id}'">Edit</button>
              `;
              projectsDiv.appendChild(div);
            });
          })
          .catch(error => console.error('Error loading templates:', error));
      };

      async function editTemplate(id) {
          try {
          // Make a POST request to the specified endpoint
          const response = await fetch(`/user/project/${id}`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
              // You may need to include other headers like authorization tokens here
            },
            // If you need to send a body with your POST request, include it here
            // body: JSON.stringify({ someData: 'yourData' })
          });

          if (!response.ok) {
            // If the response is not successful, alert the body of the response
            const errorText = await response.text();
            alert(`Error: ${errorText}`);
            return;
          }

          // If the response is successful, get the JSON data from it
          const data = await response.json();

          // Assuming the server returns an object with an id and name
          // Now redirect to the /editor/${id} page using the id from the response
          window.location.href = `/editor/${data.id}`;
        } catch (error) {
          // If there's an error in the process, alert the error message
          alert(`Error: ${error.message}`);
        }
      }
    </script>
    </body>
    </html>
    ```

The updated page will make a request to the `/templates` endpoint, expecting an array of template objects in return.

## 4. Implementing the Templates Endpoint
Let's set up the `/templates` endpoint in `server.js`, initially with mock data:

```javascript
app.get("/templates", async (context) => {
  const userType = getUserType(context);

  if (userType === "unauth") {
    return context.text("Unauthorized", 403);
  }

  return context.json([{ id: "test", name: "test" }]);
});
```
This endpoint checks the user's type and responds with a 403 status code if the user is unauthorized.

## 5. 🧪Testing the Setup
To verify the implementation:

1. Restart the server:

```shell
node server.js
```

2. Navigate to `http://localhost:3000`.
3. Log in as a user to see the mock template "test" that we added.

## 6. Connecting to the Mock Database
We must link the `/templates` endpoint to the mock database initialized in Section 6. At the beginning of `server.js`, add the following import and initialize the database:

```js
import { initDB } from "./database.js";
```

We need to run this runction `initDB` function. Right below the imports in `server.js`, run the `initDB` function and capture it in the `db` variable.

```js
import { serve } from "@hono/node-server";
import { Hono } from "hono";
import * as fs from "fs";
import { deleteCookie } from "hono/cookie";
import { setUserCookie, getUserType } from "./utility.js";
import { initDB } from "./database.js";

const db = initDB(); // We initalize our database

const app = new Hono();
// ...rest of server.js file
```

Finally, adjust the `/templates` endpoint to fetch templates from the database:

```javascript
app.get("/templates", async (context) => {
  const userType = getUserType(context);

  if (userType === "unauth") {
    return context.text("Unauthorized", 403);
  }

  return context.json(db.getTemplates());
});
```

## 7. 🧪Final Testing

Repeat the testing steps from above. This time, you will notice that the store is empty. This is because no templates have been registered in the database yet.

We will fix this in Section 7.