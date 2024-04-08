# Section 1: Setting Up The Project

This section outlines the initial steps for setting up a JavaScript project that uses Node.js and the Hono server library to create a template store. 

**Objectives**

- **Install Node.js**: Ensure [Node.js](https://nodejs.org/) version 18.x or higher is installed on your system.
- **Set up the Project Directory**: Create and navigate into the project directory.
- **Initialize Node.js Project**: Use `npm init -y` to create the necessary Node.js files.
- **Install Hono**: Add [Hono]](https://hono.dev) and its Node server package to the project.
- **Configure ES6 Modules**: Modify `package.json` to support ES6 modules.
- **Test the Setup**: Create a simple server file and run it to verify the setup is functional.

## 1. Prerequisites: Node.js Installation

### Install Node.js
Ensure you have Node.js version 18.x or greater.

- Download [Node.js](https://nodejs.org/)
- Or use a package manager specific to your OS:

| OS           | Command                                     |
|--------------|---------------------------------------------|
| Arch Linux   | `sudo pacman -S nodejs npm`                 |
| macOS (brew) | `brew install node`                         |
| Windows      | `winget install OpenJS.Nodejs`              |

!!! warning

    Becareful as some package mangers only install `node` and not the node package manager `npm`.

### Verify Installations
You can test if the installs were successiful by running the following commands in your terminal:

```
node --version
```

and 
```
npm --version
```

If you see versions for both, especially node version ≥18, you're set. Need help? Consider reaching out to your IT department or chatting with [chatGPT](http://chat.openai.com) to help you with installing Node.js.

## 2. Initilizing Our Project

Create a project folder:
```
mkdir building-a-template-store-with-studio
cd building-a-template-store-with-studio
```

!!! note

    From here on, all terminal commands are assumed to be within this directory.

Initialize a Node.js project:

```
npm init -y
```

This will create the require files for Node.js. Learn more about `npm init` in the (NPM documentation)[https://docs.npmjs.com/cli/v10/commands/npm-init].

## 3. Installing Hono

To add Hono to your project, simply run:

```
npm i hono @hono/node-server
```

## 4. Modifying package.json

Final thing we must do is enable ES6 modules, update your package.json by adding `"type": "module"`

Before:
```json
{
  ...
  "main": "index.js",
  ...
}
```

After:
```json
{
  ...
  "type": "module",
  "main": "index.js",
  ...
}
```

## 5.🧪 Testing the Setup

Alright, great job. Let's now test our setup to make sure things are working.

**Create a Server File**

1. Make a server.js file
2. Add the following code (to that file):

```js
import { serve } from '@hono/node-server';
import { Hono } from 'hono';

const app = new Hono();
app.get('/', (c) => c.text('Hello Node.js!'));

serve(app);
```

```
node server.js
```

**Check Your Setup**

1. Visit `http://localhost:3000` in your browser
2. You should see 'Hello Node.js!'.

??? failure "Troublshooting"

    If you do not get 'Hello Node.js!', here are some things to investigate:

    **Server is Running**
    - Ensure the server is actively running in the terminal.
    - You should see a message or log indicating the server has started and is listening on a specific port (usually `3000` in this case).

    **Correct URL**
    - Double-check the URL in the browser. It should be [http://localhost:3000](http://localhost:3000).
    - Make sure there are no typos or extra characters in the URL.

    **Check Console for Errors**
    - Look for error messages in the terminal where the server is running.
    - Common errors might include port conflicts, missing dependencies, or syntax errors in your code.

    **Check Network**
    - Ensure your computer's network settings aren't preventing the server from binding to the port or responding to requests.

    **Correct Node.js Version**
    - Ensure you're running Node.js version 18.x or greater.

        ```bash
        node --version
        ```

    **Dependencies Installed**
    - Confirm that both `hono` and `@hono/node-server` are installed in your `node_modules` folder.
    - If uncertain, reinstall with:

        ```bash
        npm i hono @hono/node-server
        ```

    **package.json Configuration**
    - Ensure the `package.json` has the `"type": "module"` setting.
    - Verify that there are no syntax errors or typos in the `package.json` file.

    **Code in server.js**
    - Double-check the code in `server.js` for typos or omissions.
    - Confirm the file is saved after any edits.

    **Port Conflict**
    - Another service or application might be using port 3000.
    - You can change the port in your code or stop the conflicting service.

    **Firewall or Security Software**
    - Sometimes, local firewall or security software might block certain ports or actions. Temporarily disable them and try accessing the server again.

    **Browser Cache**
    - Clear your browser cache or try accessing the server in a private/incognito browser window.

    **Console Log Errors**
    - Check your browser's developer console for any client-side errors or warnings.

