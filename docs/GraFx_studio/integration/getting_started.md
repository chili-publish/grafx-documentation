# GraFx studio integration

GraFx studio is a client side browser application.
It contains 3 elements

- The Editor SDK
- The workspace
- Your application 

The **Editor SDK** is an open source application with the Canvas to render your document.
This canvas does not have tools.

The **Workspace** is the set of panels and elements pre-built by CHILI publish to interact with your document canvas aka the **Editor SDK**.

**Your application** is the custom code that will make it your application.

## Setting up your local environment

JavaScript could run in the browser, served from a file. Running it from a webserver, will have several advantages, e.g. access to objects in the code you are writing.

### Setting up a webserver

Set up a local webserver of your choice (Apache, Nginx, IIS, ...)

### Folder for you application

create folder on your local machine in the webserver root.

![Properties](https://chilipublishdocs.imgix.net/GraFx_studio/integration/folder.png?w=400&q=80)

### DNS or not?

Up to you, to serve the files from localhost / 127.0.0.1 or from a local DNS.
My preference is to use the .hosts file to setup a local domain.

```
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1       localhost
255.255.255.255 broadcasthost
::1             localhost

127.0.0.1       my.grafxapp.dev

```

!!! note

	Remember to setup a local SSL certificate, to be able to run secure

### Testing the setup

Add an index.html to the root of your folder, and insert "Hello world"

![Properties](https://chilipublishdocs.imgix.net/GraFx_studio/integration/index.png?w=400&q=80)


Browse to the webserver / folder to see

![Properties](https://chilipublishdocs.imgix.net/GraFx_studio/integration/indexpage.png?w=400&q=80)

You now have a working website.

## NPM

We'll use the Node Package Manager to facilitate life.

If you haven't installed NPM yet, you'll need to have it on your dev machine.

[NPM Documentation](https://docs.npmjs.com/){target=_blank}


### Init NPM

You could skipp, if you have this under control

On the command line, go to your Application folder.

```
npm init
```

Answer the questions on the command line

The result of the config are gathered in package.json

```
{
  "name": "grafxapp",
  "version": "1.0.0",
  "description": "Editor SDK test app",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"
  },
  "author": "Bram",
  "license": "MIT",
  "devDependencies": {
    "webpack": "^5.74.0",
    "webpack-cli": "^4.10.0"
  },
  "dependencies": {
    "@chili-publish/editor-sdk": "^0.47.1"
  }
}

```

### Install Webpack

Will bundle your files into browser readable code
E.g. Typescript into JavaScript

```
npm install webpack --save-dev 
npm install webpack-cli --save-dev

# should result into this
added 40 packages, and audited 118 packages in 1s

15 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```

## Add source folder

```
mkdir src
cd src
touch index.js
```

Created the index.js file
For now, we'll only add a console log message, later you can add your logic

```
console.log("Hello world");
```

## Add tis to config in root



```
const path = require('path');
module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
};
```

Also add "mode" to your code (development or production)

```
const path = require('path');
module.exports = {
  entry: './src/index.js',
  mode: "development",
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
};
```

Entry: your basic source files

Mode: defines if you are in dev or prod

Output: will output to 'dist' Folder

Will create "bundle.js" file

[See Webpack documentation](https://webpack.js.org/)


## Get and install latest SDK version from NPM


Mind, we don't do --save-dev but --save, since the SDK will be included in the final build as dependency.

```
npm install --save @chili-publish/editor-sdk
```

See [Editor SDK on Github](https://github.com/chili-publish/editor-sdk){target=_blank} for more information

## First build

Before we do our first build, let's add a build script to the package file "package.json"


```
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"
```

File file looks something like this
```
{
  "name": "grafxstudio",
  "version": "1.0.0",
  "description": "SDK test app",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"
  },
  "author": "Bram",
  "license": "MIT",
  "devDependencies": {
    "webpack": "^5.74.0",
    "webpack-cli": "^4.10.0"
  },
  "dependencies": {
    "@chili-publish/editor-sdk": "^0.47.1"
  }
}
```

## Time to build

Build the output


```
npm run build
```

Result should be like this

```
> grafxstudio@1.0.0 build
> webpack

asset bundle.js 1.21 KiB [compared for emit] (name: main)
./src/index.js 22 bytes [built] [code generated]
webpack 5.74.0 compiled successfully in 38 ms
```

Your built app is in the "dist" folder

All the prep work is done

## Create your custom app

Make index.html, include JS file

!!! note
	
	index.html is not part of the "app", could be hosted elsewere, just need to load the js bundle. 
	For the ease of the demo, we'll host it in the root. That defines how the link is made to the js file in this case
	
```
<!DOCTYPE html>
<html>
<head>
	<title>My First CHILI GraFx app</title>
</head>
<body>

	<script src="./dist/bundje.js"></script>
</body>
</html>

```
## Open the file in your browser

Open index.html to see your work in action!

You are now ready to call the Editor SDK in your application

## Import the Editor SDK

Add this line to your index.js

```
import EditorSDK from "@chili-publish/editor-sdk";
```

## All controllers / classes

Documented here (will move to current documentation site)

[Classes](https://chili-publish.github.io/editor-sdk/)