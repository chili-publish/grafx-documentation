# Integrate CHILI GraFx apps

Server side, you have access to 2 API's with endpoints.

- [Platform API](/CHILI_GraFx/platform_api/overview/)
- [Environment API](/GraFx_devcenter/environment_api/overview/)

Client side

- [GraFx Studio SDK](/GraFx_studio/sdk/)

## Platform API

A set of classes and endpoints that allows you to manage resources linked to your platform.

## Environment API

Classes and endpoints to interact with your environment, documents, templates, media, fonts, etc.

These endpoints are linked to resources bound to 1 environment.

The API contains functions related to several apps. 

| Ust this API	   	   	    | for this App |
|-------------------|-------------|
| Platform API  	| CHILI GraFx |
| Environment API	| GraFx Studio |
| Environment API	| GraFx Media |
| Environment API	| GraFx Fonts |

### Permissions

Some functions will be restricted. Then the API will provide an error.

- If you don't have the app in your subscription
- If you have the app, but you don't have access to a certail resource

Error codes

| Code	   	   	    | Meaning     |
|-------------------|-------------|
| 200		     	| Ok   |
| 500		     	| Server dead   |
| 404		     	| Function not found   |


# Overview per application

## CHILI GraFx

- [Getting Started](/CHILI_GraFx/integration/getting_started/)
- [Platform API](CHILI_GraFx/platform_api/api_reference.md)

## GraFx Studio

- [SDK Getting Started](/GraFx_studio/integration/getting_started/)		
- [SDK Reference](/GraFx_studio/sdk/)
- [Environment API](/GraFx_devcenter/environment_api/overview)

## GraFx publisher

- [REST API Reference](https://mydocumentation.chili-publish.com/search?text=rest%20api%20endpoints){target="_blank"}
- [Javascript API](https://mydocumentation.chili-publish.com/search?text=Getting%20started%20with%20your%20JavaScript%20integration){target="_blank"}`
- [Getting Started](https://mydocumentation.chili-publish.com/search?text=chili%20api%20guide){target="_blank"}

## GraFx media

- [Environment API](/GraFx_devcenter/environment_api/overview)

## GraFx fonts

- [Environment API](/GraFx_devcenter/environment_api/overview)
