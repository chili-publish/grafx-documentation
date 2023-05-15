# Integrate CHILI GraFx apps

To communitcate with GraFx server side, please use these two APIs. You can learn more about the role of each API below.

- [Platform API](https://api.chiligrafx.com/swagger/index.html)
- [Environment API](https://sandbox1.chili-publish-sandbox.online/grafx/swagger/index.html)

Client side

- [GraFx Studio SDK](https://chili-publish.github.io/studio-sdk/index.html)

## Platform API

The **GraFx Platform API** allows you to manage GraFx Platform resources.

Some exmaple use cases are:

- User management
- Environment creation
- Buy (Render pack) add-ons


## Environment API

Through the **GraFx Environment API** you can manage your CHILI GraFx environment.

Some exmaple use cases are:

- Adding Smart Templates
- Adding Template Designer seats (later)
- Generating Output

The Environment API contains endpoints related to several apps.

| Ust this API	   	   	    | for this App |
|-------------------|-------------|
| Platform API  	| CHILI GraFx (platform)|
| Environment API	| GraFx Studio |
| Environment API	| GraFx Media |
| Environment API	| GraFx Fonts |

### Authorization

Certain endpoints require authentication and authorization to access. If you have not properly authorized, the API will respond with an error.

- If you don't have the app in your subscription
- If you have the app, but you don't have access to a certain resource

Error codes

| Code	   	   	    | Meaning     |
|-------------------|-------------|
| 200		     	| Ok   |
| 500		     	| Server dead   |
| 404		     	| Function not found   |

# Overview per application

## CHILI GraFx

- [Getting Started](/CHILI-GraFx/integration/getting_started/)
- [Platform API Swagger](https://api.chiligrafx.com/swagger/index.html)

## GraFx Studio

- [SDK Getting Started](/GraFx-Studio/integration/getting-started/)
- [SDK Reference](https://chili-publish.github.io/studio-sdk/index.html)
- [Environment API Swagger](https://sandbox1.chili-publish-sandbox.online/grafx/swagger/index.html)

## GraFx Publisher

- [REST API Reference](https://mydocumentation.chili-publish.com/search?text=rest%20api%20endpoints){target="_blank"}
- [Javascript API](https://mydocumentation.chili-publish.com/search?text=Getting%20started%20with%20your%20JavaScript%20integration){target="_blank"}
- [Getting Started](https://mydocumentation.chili-publish.com/search?text=chili%20api%20guide){target="_blank"}

## GraFx Media

- [Environment API Swagger](https://sandbox1.chili-publish-sandbox.online/grafx/swagger/index.html)

## GraFx Fonts

- [Environment API Swagger](https://sandbox1.chili-publish-sandbox.online/grafx/swagger/index.html)
