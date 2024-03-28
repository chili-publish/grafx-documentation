# Section 3: Setting The Login Page As Default

This section of the documentation focuses on configuring the login page to be the default landing page of a web application. It walks through the steps to set up a simple login interface and includes the necessary changes in the server configuration to serve the login page as the default.

**Objectives**

- **Configure Login Page**: Modify `public/login.html` with the provided HTML to set up the login interface.
- **Set Default Page**: Adjust `server.js` to direct the root path ("/") to serve the login page by default.
- **Test Login Page**: Verify that the server correctly displays the login page when accessed through the browser at `http://localhost:3000`.

## 1. Configuring the Login Page

1. Open up `public/login.html`. 
2. Replace its contents with the HTML below (open the tab):

??? abstract "login.html contents"
    ``` html
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Login Page</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    height: 100vh;
                    margin: 0;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                }
                header {
                    position: absolute;
                    top: 0;
                    left: 50%;
                    transform: translateX(-50%);
                    font-size: 24px;
                    margin-top: 20px;
                }
                button {
                    margin: 10px;
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                }
                .button-container {
                    display: flex;
                    justify-content: center;
                }
            </style>
        </head>
        <body>
            <header>Login</header>
            <div class="button-container">
                <button onClick="login('admin')">Admin</button>
                <button onClick="login('user')">User</button>
            </div>
            <script>
                async function login(role) {
                    try {
                        const response = await fetch(`login/${role}`, {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json",
                            },
                        });
                        const data = await response.json();
                        console.log(data);

                        if (data.success == true) {
                            // Reload the page after processing the response
                            setTimeout(() => window.location.reload(), 200);
                        }
                    } catch (error) {
                        console.error("Error:", error);
                    }
                }
            </script>
        </body>
    </html>
    ```

This page presents a simple login interface with the title "Login" displayed at the top. Below the title, centered in the middle of the screen, are two buttons labeled "Admin" and "User".

When either button is clicked:

1. The login function is invoked, with the role ("admin" or "user") passed as an argument.
2. This function initiates an asynchronous GET request to an endpoint specific to the role (login/admin or login/user).
3. Upon receiving a response, the response status is logged to the console for verification or debugging purposes.
4. After processing the response status, the page is reloaded using window.location.reload() after 200 ms. 

!!! note

    This example omits usernames and passwords for brevity. A real-world scenario would involve diverse user roles and authentication mechanisms.

## 2. Update the Default Page to Login
Assuming you have a `server.js`, modify its contents as follows:

1. Import the necessary modules.
2. Update the root path ("/") route handler to load the login page by default.

`server.js` now looks like:
```js linenums="1" hl_lines="3 7"
import { serve } from "@hono/node-server";
import { Hono } from "hono";
import * as fs from "fs";

const app = new Hono();
app.get("/", async (context) => {
  const loginPage = await fs.promises.readFile("public/login.html", "utf8")
  return context.html(loginPage);
});

serve(app);
```

Here is what we changed:

1. On line 3, the `fs` module was imported to allow interaction with the file system.
2. The route handler for the root path ("/") on line 7 was changed:
    * It now uses an asynchronous function.
    * Inside the handler, the `public/login.html` file is read using `fs.promises.readFile`
    * The contents of the read file are returned as HTML using `c.html()`.

??? question "Need help understanding this code?"

    Imagine you're setting up a lemonade stand on your street, but instead of a street, it's the internet, and instead of lemonade, you're handing out web pages. Let's look at what each part of this code is doing using that analogy:

    **Getting the tools and ingredients**
    Just like you need pitchers and cups for lemonade, for a website, you need some tools to handle requests from people who visit it (that's what the import lines are for).

    ```javascript
    import { serve } from "@hono/node-server";
    import { Hono } from "hono";
    import * as fs from "fs";
    ```
    
    - `import { serve } from "@hono/node-server";` this line is importing the serve function from the "@hono/node-server" module, you use `serve` as your stand to serve the lemonade
    - `import { Hono } from "hono";` this line imports the Hono class from the "hono" module. `Hono` is a web framework for building server applications. In many ways it is the recipe book to know how to make lemonade.
    - `import * as fs from "fs";` this line imports the built-in `fs` (file system) module in Node.js. `fs` is like having access to a fridge where your lemonade (web pages) are stored.

    **Setting up your stand**

    ```javascript
    const app = new Hono();
    ```
    
    - This line creates a new Hono instance representing the web application. Is like saying, "Okay, I have my recipe book (Hono), now let's open up the stand (app) and get ready to serve!"

    **Telling people what you have to sell (Route setup)**

    ```javascript
    app.get("/", async (context) => {
      const loginPage = await fs.promises.readFile("public/login.html", "utf8")
      return context.html(loginPage);
    });
    ```

    - `app.get("/", async (c) => { ... })` is like putting up a sign that says, "Here's where you can get lemonade!" When someone comes to your stand and asks for lemonade, you know to give them lemonade from your fridge.
    - Inside the curly braces `{ ... }` is the instruction for what to do when someone asks for that lemonade. You look in the fridge `(fs.promises.readFile("public/login.html", "utf8"))`, which has your lemonade already made (a web page file called "login.html").   
    
    **Opening you stand (start server)**
    
    ```javascript
    serve(app);
    ```
    
    - This line is like saying, "We're open for business!" Now people can come to your stand, and when they ask for the lemonade menu ("/"), you give them a cup of lemonade (the "login.html" page).

    **Summary**

    That's pretty much what the code is doing. It's setting up a stand on the internet where people can ask for a specific thing (in this case, a web page), and you know how to give them exactly what they're asking for!;
    ```

## 3. 🧪Testing the Login Page

**Restart the Server**

1. If the server is running, stop it using Ctrl + C.
2. Start or restart the server with:

```SH
node server.js
```

!!! warning

    You must restart the server with the `node` command everytime after modifying `server.js` or imported files.

**Verify your Setup**

1. Visit `http://localhost:3000` in your browser.
2. Confirm the presence of the "Admin" and "User" buttons on the login page.

??? failure "Troublshooting"

    If you do not get the login page, here are some things to investigate:
    
    **Check Server Status**:
    - Ensure the server is running, run `node server.js`.

    **Verify File Changes**:
    - Ensure all changes in `server.js` and `public/login.html` are saved.
    - Check that files are in the correct directories.

    **Port Issues**:
    - Make sure no other services are using the default port 3000.
    - If you see an "Address already in use" error, the port is occupied. Stop the service using that port or choose a different one.

    **Browser Cache**:
    - Refresh with `Ctrl + F5` (or `Cmd + Shift + R` on macOS) to bypass cache.
    - Clear browser's cache, then retry.

    **Check Console for Errors**:
    - Open browser's developer tools (`F12` or `Ctrl + Shift + I`) and check the 'Console' tab for errors.
    - Check the terminal running your server for error logs.

    **Network Issues**:
    - Ensure server access is from the correct network. Local servers can't be accessed externally without configurations.
    - Ensure firewall or antivirus isn't blocking the server or port.

    **URL Check**:
    - Visit the correct URL: `http://localhost:3000`. Adjust if you changed the default port.

    **Dependencies & Libraries**:
    - Confirm required libraries (like `@hono/node-server` and `hono`) are installed. Reinstall them using `npm install`.

    **File Permissions**:
    - Ensure server has permissions to read `public/login.html` and the other HTML files.

    **Review Code for Typos**:
    - Double-check code against the guide for any mistakes.
