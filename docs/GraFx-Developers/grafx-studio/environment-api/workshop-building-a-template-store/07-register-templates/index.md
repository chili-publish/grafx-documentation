# Section 7: Register Templates

In this section, we aim to enhance the functionality of our web application by enabling administrators to register new templates. We will achieve this through the following objectives:

**Objectives:**

- **Update Base Routing**: Refine the base routing to direct administrators to a dedicated admin page (`store-admin.html`) for template management.
- **Modify Admin Page**: Revise `store-admin.html` to include a new form that allows template registration.
- **Create Registration Endpoint**: Implement a new endpoint (`/templates/:id`) to handle the registration of templates via POST requests.

## 1. Configuring the Base Path for Admin Access

To facilitate administrators in registering new templates, the base path (`/`) needs to be updated to redirect to the `store-admin.html` page.

We can update our base path `/` with
```js
app.get("/", async (context) => {
  const type = getUserType(context);

  if (type == "unauth") {
    const loginPage = await fs.promises.readFile("public/login.html", "utf8");
    return context.html(loginPage);
  }

  if (type == "admin") {
    const storeadminPage = await fs.promises.readFile("public/store-admin.html", "utf8");
    return context.html(storeadminPage);
  }
  else {
    const storefrontPage = await fs.promises.readFile("public/store-front.html", "utf8");
    return context.html(storefrontPage);
  }
});
```

This modification checks the user type and serves the appropriate page.

## 2. Updating the Admin Page

To allow template registration, the `store-admin.html` must be updated to include a template registration form. Refer to the provided HTML snippet below and update it `store-admin.html`. 

??? abstract "store-admin.html cotent"

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
        gap: 10px;
      }
      .template {
        border: 1px solid #ccc;
        padding: 10px;
        width: 200px;
      }
      .template img {
        width: 200px;
        height: auto;
      }
      .template h3 {
        margin: 0;
        font-size: 1.2em;
        color: #333;
      }
      .template button {
        margin-top: 10px;
        margin-right: 5px; /* Add space between buttons */
      }
      .error-message {
        color: red;
        margin-top: 10px;
      }
    </style>
    </head>
    <body>
    <div>
      <form id="register-form">
        <label for="template-id">Register Template:</label>
        <input type="text" id="template-id" name="template-id" required>
        <button type="submit">Submit</button>
      </form>
      <div id="error-message" class="error-message"></div>
    </div>
    <h2>Templates</h2>
    <div id="templates" class="template-container">
      <!-- Templates will be loaded here -->
    </div>
    <h2>User Projects</h2>
    <div id="projects" class="template-container">
      <!-- Templates will be loaded here -->
    </div>

    <script>
      document.getElementById('register-form').onsubmit = function(event) {
        event.preventDefault();
        const templateId = document.getElementById('template-id').value;
        registerTemplate(templateId);
      };

      function registerTemplate(id) {
        fetch(`/templates/${id}`, { method: 'POST' })
          .then(response => {
            if (!response.ok) {
                return response.text().then(text => {
                  throw new Error(`Registration failed: ${text}`);
                });
            }
            return response.json();
          })
          .then(data => {
            loadTemplates(); // Reload all templates
          })
          .catch(error => {
            document.getElementById('error-message').textContent = error.message;
          });
      }
      
      function loadTemplates() {
        fetch('/templates')
          .then(response => response.json())
          .then(data => {
            const templatesDiv = document.getElementById('templates');
            templatesDiv.innerHTML = '';
            data.forEach(template => {
              const div = document.createElement('div');
              div.id = template.id;
              div.className = 'template';
              div.innerHTML = `
                <h3>${template.name}</h3>
                <img src="preview/template/${template.id}" alt="${template.name}">
                <br/>
                <button onclick="removeTemplate('${template.id}')">Remove</button>
              `;
              templatesDiv.appendChild(div);
            });
          })
          .catch(error => console.error('Error loading templates:', error));
      }

      function editTemplate(id) {
        // Replace with the actual logic to edit the template
        console.log('Editing template', id);
      }

      function removeTemplate(id) {
        fetch(`/templates/${id}`, { method: 'DELETE' })
          .then(response => {
            if (!response.ok) {
              throw new Error('Deletion failed');
            }
            loadTemplates(); // Reload all templates after deletion
          })
          .catch(error => {
            document.getElementById('error-message').textContent = error.message;
          });
      }

      window.onload = function() {
          // Initial load of templates
          loadTemplates();
          
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
      
    </script>
    </body>
    </html>
    ```

This form will send a POST request to `/templates/:id` to register a new template.

## 3. Adding the Template Registration Endpoint

A new endpoint needs to be added to handle template registration. Update your `server.js` with the following route:

```js
app.post("/templates/:id", async (context) => {
  const type = getUserType(context);

  if (type != "admin") {
    return context.text("Unauthorized", 403);
  }

  const {id} = context.req.param();
});
```

In the Hono framework, the `param` function simplifies the extraction of the `id` from the URL path.

Next, we need to integrate logic to add a template to the database using the `addTemplate` method. 
```js
app.post("/templates/:id", async (context) => {
  const type = getUserType(context);

  if (type != "admin") {
    return context.text("Unauthorized", 403);
  }

  const {id} = context.req.param();

  // db.addTemplate(???); - we only have id no name
});
```

However, the template's name is required and is not provided by the current implementation. Additionally, we must verify the template's existence in GraFx Studio to prevent registering non-existent templates.

To resolve these issues, we will interface with the Environment API, which will be covered in the next section, where we will also obtain the necessary token.
