# Install and config NPM & WebPack

We'll use the [NPM](https://docs.npmjs.com/getting-started) to facilitate life.

## Initialize NPM

You could skip, if you have this under control

On the command line, go to your [Application folder](local_environment.md).

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

## Install Webpack

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

To store your source JS files, that will be compiled into the final bundle.

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

**Add this to config in root** (webpack.config.js)

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

Also add "mode" to your code (development or production) (webpack.config.js)

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

Entry: source files
Mode: defines if you are in dev or prod
Output: will output to 'dist’ Folder (change to your preference)

Output will create "bundle.js" file

[See Webpack documentation](https://webpack.js.org/)