# GraFx studio integration

CHILI studio is a client side application.
It contains 3 elements

- The Editor SDK
- The workspace
- Your application

The **Editor SDK** is an open source application with the Canvas to render your document.

The **Workspace** is the set of panels and elements prebuilt by CHILI publish to interact with your document canvas.

**Your application** is the custom code that will make it your application.

## Getting the JavaScript

To load the logic into your page you'll need to point to the Editor SDK files.

=== "NPM"

	Use npm to download and install the source files into your application.
	Go to your local repository directory
	```
	npm install --save @chili-publish/editor-sdk
	```
	If you don't have npm installed, have a look at the [npm Docs](https://docs.npmjs.com){target="_blank"}.
	This will add node module to your app

	
=== "NPM served"
	
	Point to the .js file, served by NPM
	```
	<script src="https://storageeditor2.blob.core.windows.net/stable/early-access/sdk/v0.0.4/main.js"></script>

	```

## Custom integration

index.js

## Allways run in webserver

(e.g. )

## Load your document

