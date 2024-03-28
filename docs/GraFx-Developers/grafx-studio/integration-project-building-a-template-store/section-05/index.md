# Section 5: Constructing a Mock Database

This section guides you through setting up a mock database, which utilizes your local file system to store data as JSON. This approach is designed to streamline the initial development phase by providing a clear and editable data structure.

!!! note
    
    Keep in mind that while this mock file system database is great for learning and prototyping, it is not intended for use in production environments.

## 1: Defining the Database Structure

We'll need our database to manage several types of data:

- Backend and frontend tokens
- Template registrations
- Template visibility states
- User-uploaded media
- User projects
- Project order statuses
- Tasks (referred to as orders) processed by GraFx

The database will be represented as a JSON file, structured according to the following TypeScript interface:

### TypeScript Definition

??? abstract "TypeScript Defintion"

    ```typescript
        type Token = {
            value: string,
            expires: number
        }

        type Template = {
            id: string,
            name: string,
        }

        type Project = {
            id: string,
            name: string,
        }

        type User = {
            id: string,
            admin: boolean,
            projects: Map<string, Project>,
            media: string[]
        }

        type Order = {
            projectID: string,
            taskID:string,
            downloadURL?:string,
            error?:boolean,
            age?: number
        }

        type Database = {
            tokens: {
                readonlyToken: Token,
                dangerousToken: Token
            },
            storeTemplates: Map<string,Template>,
            users: Map<string,User>,
            orders: Map<string,Order>
        }
    ```

## 2: Creating the Database Code

Start by creating a new file named `database.js` in your project directory.

=== "Linux/macOS"

    ```sh
    touch database.js
    ```

=== "Windows (PowerShell)"

    ```powershell
    ni database.js
    ```

Instead of building the code incrementally, you'll find the complete code snippet below. Copy this code and paste it into your newly created `database.js` file. Utilize the "Copy to clipboard" feature available at the top of each code block for convenience.

??? abstract "database.js content"
    ```js linenums="1"
    // Import the filesystem module to interact with the file system
    import * as fs from "fs";

    // Define the path to the database file
    const databasePath = "./database.json";

    // Export the `initDB` function, which initializes the database
    export function initDB() {
      // Check if the database file does not exist
      if (!fs.existsSync(databasePath)) {
        // If it does not exist, create a new file with initial database structure in JSON format
        fs.writeFileSync(
          databasePath,
          JSON.stringify(
            {
              // Tokens to be used for authentication 
              tokens: {
                readonlyToken: {
                  value: "",
                  expires: new Date().getTime(),
                },
                dangerousToken: {
                  value: "",
                  expires: new Date().getTime(),
                },
              },
              // Templates for store items
              storeTemplates: {
                dataType: "Map",
                value: [],
              },
              // User information
              users: {
                dataType: "Map",
                value: [
                  [
                    "admin",
                    {
                      id: "admin",
                      admin: true,
                      projects: {
                        dataType: "Map",
                        value: [],
                      },
                      media: [],
                    },
                  ],
                  [
                    "user",
                    {
                      id: "user",
                      admin: false,
                      projects: {
                        dataType: "Map",
                        value: [],
                      },
                      media: [],
                    },
                  ],
                ],
              },
              // Orders placed in the system
              orders: {
                dataType: "Map",
                value: [],
              },
            },
            null,
            4, // Pretty-print with 4 spaces for readability
          ),
        );
      }

      // Read the existing database file and parse it into a JavaScript object
      // Custom reviver function transforms values with dataType 'Map' into JavaScript Map objects
      const db = JSON.parse(fs.readFileSync(databasePath, "utf8"), (_, value) => {
        if (typeof value === "object" && value !== null) {
          if (value.dataType === "Map") {
            return new Map(value.value);
          }
        }
        return value;
      });

      // Function to update the database file by writing the current state of the `db` object to the file
      const updateDB = () => {
        fs.writeFileSync(
          databasePath,
          JSON.stringify(
            db,
            (_, value) => {
              // Custom replacer function to transform Map objects back into the storable object format
              if (value instanceof Map) {
                return {
                  dataType: "Map",
                  value: [...value],
                };
              } else {
                return value;
              }
            },
            4, // Pretty-print with 4 spaces for readability
          ),
        );
      };

      // Helper function for turning seconds into timestamp
      const expiresAt = (expiresInSeconds) => {
              // Get the current date and time
          const now = new Date();

          // Calculate the future expiration time
          const expiresAt = new Date(now.getTime() + expiresInSeconds * 1000); // getTime() returns milliseconds, so multiply seconds by 1000

          return expiresAt.getTime();
      }

      // Return an object containing methods for manipulating the database
      return {
        // Method to get tokens
        getTokens: () => {
          return {
            readonly: {...db.tokens.readonly},
            dangerous: {...db.tokens.dangerous}
          }
        },

        // Methods to set tokens
        setReadonlyToken: (tokenValue, expiresInSeconds) => {
          db.tokens.readonly.value = tokenValue;
          db.tokens.readonly.expires = expiresAt(expiresInSeconds);
        },

        setDangerousToken: (tokenValue, expiresInSeconds) => {
          db.tokens.dangerous.value = tokenValue;
          db.tokens.dangerous.expires = expiresAt(expiresInSeconds);
        },

        // Method to add a new template to the storeTemplates
        addTemplate: ({ id, name}) => {
          db.storeTemplates.set(id, { id, name});
          updateDB(); // Update the database file after the change
        },

        // Method to remove a template from the storeTemplates
        removeTemplate: (id) => {
          if (db.storeTemplates.delete(id)) {
            updateDB(); // Update the database file after the change
          }
        },

        // Method to retrieve all templates
        getTemplates: () => {
          return Array.from(db.storeTemplates.values()).map((obj) => ({ ...obj }));
        },

        // Method to add a project to a user's list of projects
        addProjectToUser: ({userID, projectID, projectName}) => {
          const user = db.users.get(userID);

          if (user == null) throw new Error(`User ${userID} not found`);

          if (!user.projects.has(projectID)) {
            user.projects.set(projectID, { id: projectID, name: projectName});
            updateDB(); // Update the database file after the change
          }
        },

        // Method to remove a project from a user's list of projects
        deleteProjectFromUser: (userID, projectID) => {
          const user = db.users.get(userID);

          if (user == null) throw new Error(`User ${userID} not found`);

          if (user.projects.delete(projectID)) {
            updateDB(); // Update the database file after the change
          }
        },

        // Method to get all projects for a user
        getUserProjects: (userID) => {
          const user = db.users.get(userID);

          // Throw an error if the user is not found
          if (user == null) throw new Error(`User ${userID} not found`);

          // Convert the user's projects Map into an array of project objects and return it
          return Array.from(user.projects.values()).map((obj) => ({ ...obj }));
        },

        // Method to add a new order to the database
        addOrder: ({ taskID, projectID }) => {
          // Set the new order in the orders map with the taskID as the key
          db.orders.set(taskID, { taskID, projectID });

          // Update the database file after adding the new order
          updateDB();
        },

        // Method to get orders from the database
        getOrders: () => {
          return Array.from(db.orders.values()).map(obj => ({...obj}));
        },

        // Method to remove an order from the database
        removeOrder: (taskID) => {
          // Delete the order by taskID from the orders map
          if (db.orders.delete(taskID)) {
            // Update the database file after removing the order
            updateDB();
          }
        },
      };
    }
    ```

The supplied JavaScript sets up a mock database, storing data in a file named `database.json`. This technique reduces the complexity associated with database management, allowing you to focus on handling API interactions.

This file exports a single function, `initDB()`, which initializes the database if it doesn't exist and provides helper functions for data manipulation.

As mentioned previous, the database is actually a JSOB file. Every time a change is made to the data, the internal `updateDB()` function is called. This function writes the current state of the database back to `database.json`. This ensures that changes are not lost when the server is restarted.

Reading from and writing to the filesystem is handled by Node.js's `fs` module.

- Reading: When the database file is read, a custom reviver function transforms certain objects into JavaScript Map objects. This function checks if an object has a dataType property set to "Map" and, if so, converts it to an actual Map object.
- Writing: Conversely, when updating the database, a replacer function transforms Map objects back into a storable format that includes the dataType property, allowing for a reversible transformation.
Database Operations

### Database Operations

The mock database allows you to:

- Add or remove templates
- Retrieve all templates
- Update template visibility
- Manage user projects
- Handle orders

For instance, to add a project to a user's account:

```javascript
db.addProjectToUser({userID:"userId", projectID:"projectId", projectName:"projectName"});
```

To modify the order count for a user's project:

```javascript
db.updateUserProjectOrderCount("userId", "projectId", 10);
```
