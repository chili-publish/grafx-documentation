# GraFx Studio Overview

This is a quick start guide to get you started with the [Studio SDK](https://github.com/chili-publish/studio-sdk), using[Bun](https://bun.sh) as our JavaScript runtime & toolkit, because it is more user-friendliness. Our end goal is to familiarize you with the basics of setting up a project using the Studio SDK to load and interact with the editor engine.

## What You'll Need for Production

To deploy your project in a live environment, ensure you have:

- **JavaScript Engine:** [Node.js](https://nodejs.org/en) recommended. For simplicity, this guide uses Bun.
- **Bundler:** Bundlers package your code into a single file, essential for StudioSDK which is an exteranl project. Common choices include [webpack](), [esbuild](), and [parcel]().
- **Web Server:** Required to deliver your files over HTTP to avoid errors.

However, for production purposes, we currently suggest using [node](https://nodejs.org/en).

## Guide Requirements

However, for this guide, you need only two things:

- `bun` a JavaScript engine which you can install [here](https://bun.sh/docs/installation). Bun comes with easy API for serving files over HTTP and a bundler built in.
- An integration token, which you need to generate here: [integration](/GraFx-Developers/grafx-studio/integration-overview/04-managing-integrations-and-authentication/)
