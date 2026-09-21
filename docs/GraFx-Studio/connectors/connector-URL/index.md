# URL Connector

:fontawesome-regular-square-check: Built-in  
:fontawesome-regular-square: Built by CHILI publish  
:fontawesome-regular-square: Third Party

[See Connector types](/GraFx-Studio/concepts/connectors/#types-of-connectors)

## Introduction

The URL Connector is a built-in media connector for accessing public URLs for images.

For example: `https://tcob.space/images/public-image.png`

It is listed here because the URL Connector uses the same **Connector Architecture** as other connectors.

There is no configuration on the connector page and it is turned on by default.

![GraFx Studio Connectors page showing URL connector listed as a Media type](sc01.png){.screenshot-full}

## How to use

It's very simple to implement:

- Create a text variable and an image variable
- Link the text variable to the image variable and select the **URL Connector** type

![GraFx Studio showing a text variable linked to an image variable with URL Connector selected](sc02.png){.screenshot-full}

- Create an image frame and insert the image variable to that frame

In the end user view, when a URL of an image is pasted into the text variable, the image will appear.

![GraFx Studio end user view showing an image appearing after a URL is pasted into the text variable](sc03.png){.screenshot-full}
