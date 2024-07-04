# Project Setup

## 1. Initialize Your Project

Start by creating a new directory for your project. Open your terminal (PowerShell for Windows, Terminal for macOS/Linux) and run:

=== "Linux or macOS"

    ```bash
    mkdir studio-sdk-quickstart && cd studio-sdk-quickstart
    ```

=== "Windows PowerShell"

    ```powershell
    mkdir studio-sdk-quickstart; cd studio-sdk-quickstart
    ```

The rest of this guide will assume you are inside this new directory.

Next, initialize your project with default settings using Bun:

```bash
bun init -y
```

Test to ensure your setup works by executing `bun run index.ts` in your terminal.

## 2. Setting Up a Server

Create a `server.ts` file, and fill it with the following code to set up a basic HTTP server. This server will respond to file requests and serve the appropriate content:

```typescript
const server = Bun.serve({
  port: 3000,
  fetch: async (req) => {
    const fileName = new URL(req.url).pathname.split("/").filter(Boolean).pop()
    const fileResp = Bun.file(`./${fileName ?? "index.html"}`);
    if (!(await fileResp.exists())) {
      return new Response(`${fileName} not found`, { status: 404, statusText: `${fileName} not found` });
    }
    return new Response(fileResp);
  },
});

console.log(`Listening on http://localhost:${server.port} ...`);
```
??? question "What does this code block do?"

    This code block is setting up a basic HTTP server using Bun. Let's break down what each part does for a clearer understanding:

    **Overview**
    The `Bun.serve` method is used to create a new HTTP server. The configuration object passed to `Bun.serve` specifies how the server should behave, particularly on which port to listen and how to handle incoming requests with the `fetch` function.
    
    Let's break it down:

    **Server Configuration
    ```javascript
    const server = Bun.serve({
      port: 3000,
      fetch: async (req) => {
        ...
      },
    });
    ```
    - `Bun.serve` method creates a new HTTP server. The configuration object specifies the server's behavior, particularly the port to listen on and how to handle incoming requests with the `fetch` function.
    - `port: 3000` tells the server to listen on port 3000. You can access it by navigating to `http://localhost:3000` in a web browser.

    **Handling Requests with `fetch`
    ```javascript
    fetch: async (req) => {
      ...
    }
    ```
    - This asynchronous function handles incoming HTTP requests. `req` contains details about the request.

    **Extracting the Requested File Name
    ```javascript
    const fileName = new URL(req.url).pathname.split("/").filter(Boolean).pop();
    ```
    - Breaks down the request URL to extract the file name. It uses several methods to process the pathname and isolate the file name.

    **Serving the File
    ```javascript
    const fileResp = Bun.file(`./${fileName ?? "index.html"}`);
    ```
    - Attempts to read the requested file from the file system, defaulting to `"index.html"` if no file name is provided.

    **Handling File Not Found
    ```javascript
    if (!(await fileResp.exists())) {
      return new Response(`${fileName} not found`, { status: 404, statusText: `${fileName} not found` });
    }
    ```
    - Checks if the file exists. If not, responds with a 404 status code and a message indicating the file was not found.

    **Returning the File
    ```javascript
    return new Response(fileResp);
    ```
    - If the file exists, it's returned to the client in the response.

    **Starting the Server
    ```javascript
    const server = Bun.serve({
      ...
    });

    console.log(`Listening on http://localhost:${server.port} ...`);
    ```
    - `Bun.serve` function starts the server when the script is ran.
    - `console.log` logs a message indicating the server is running and listening on the specified port.

    This script demonstrates setting up a static file server using Bun, which serves files from its directory. If a file is requested, it tries to serve that file; otherwise, it either serves `index.html` or returns a 404 error if the file does not exist.

## 3. Serving an HTML File

Create an `index.html` in your project directory with the following content. This HTML file will be served by your server:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title></title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <div id="studio" style="width:90vw; height:90vh">GraFx Studio</div>
    <script type="module">
    import "./index.js";
    </script>
  </body>
</html>
```
## 4. 🧪 Test the Server

Run your server using `bun server.ts` and visit `http://localhost:3000` to see your setup in action. You should see a page with the words "GraFx Studio". 

Stop the server afterward with `Ctrl + C`.
