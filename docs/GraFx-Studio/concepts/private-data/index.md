# Private Data

## Overview

Most of what you configure in a Design System is meant to be seen: variables become input fields, layouts become the format options an end user can pick. **Private Data** is the opposite. It is information you store on an item that never appears in GraFx Studio or in the end-user interface, but that a custom integration can read.

It exists for the cases where your integration needs to know something extra about an item, and GraFx Studio has no built-in property to hold it.

## What is Private Data?

Private Data is a set of key-value pairs attached to an item in the template. Keys and values are both plain text. Neither is shown in the Studio UI or to the end user, and both are available to custom integrations through the [Studio SDK](/GraFx-Developers/grafx-studio/overview/).

## Where you can set it

Private Data can be set on two levels.

| Level | Where you set it | Studio SDK |
|---|---|---|
| Variable | The **Private data** section of the variable settings | `SDK.variable.setPrivateData()` and `SDK.variable.getPrivateData()` |
| Layout | The **Private data** section of the layout properties panel | `SDK.layout.setPrivateData()` and `SDK.layout.getPrivateData()` |

The editor is the same in both places — a dialog where you add, edit and delete key-value pairs. What differs is what the data is attached to, and therefore what your integration can conclude from it.

- **On a variable**, it says something about an input. A custom end-user interface can use it to decide how to render or group a field, or to tie the field back to a record in your own system.
- **On a layout**, it says something about a format. An integration can use it to decide where the output of that layout is meant to go: a channel, a placement code, an ad platform, an identifier your ordering system expects.

## Key characteristics

- **Non-disruptive:** it does not change how the variable or layout behaves in GraFx Studio or in the end-user interface.
- **Integration-specific:** GraFx Studio never interprets the data. Only your integration gives it meaning.
- **Text only:** keys and values are strings. Anything structured has to be encoded by your integration.

!!! warning "Private, not secret"
    "Private" means hidden from the interface — not encrypted and not access-controlled. Private Data travels with the document and is readable by anything that can read the document, so never store credentials, tokens or personal data in it.

<!-- TODO Bram / Product review: confirm whether Private Data on a parent layout is inherited by its sub-layouts, and whether it is copied when a layout is duplicated. The SDK exposes privateData as a plain value with no reset method, which suggests it is set per layout with no inheritance — but this should be confirmed before we state it. -->

## Guides

- [Private data on variables](/GraFx-Studio/guides/template-variables-private-data/)
- [Private data on layouts](/GraFx-Studio/guides/layouts/#private-data)
