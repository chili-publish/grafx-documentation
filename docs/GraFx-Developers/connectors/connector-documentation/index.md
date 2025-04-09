# Connector Documentation

## Introduction

You have build a great connector. Good job.

Next to the bits and the bytes, a customer will also need documentation.

An example of Connector Documentation, is the "[Google Sheets Data Connector](/GraFx-Studio/connectors/connector-google-sheets-data/)".

This documentation gives your users the insights to

- How to deploy your connector from the Connector HUB
- How to setup your connector (authentication, credentials, ...)
- How to use your connector in a template

## How do I start documenting?

First read the [Read me](https://github.com/chili-publish/grafx-documentation/blob/main/README.md) file.

ANd don't forget the [Contributing guide](https://github.com/chili-publish/grafx-documentation/blob/main/CONTRIBUTING.md). The basis to contribute to the CHILI GraFx Documentation.

1. Download this [zip](connector_base_.zip) file.  
It contains a sample structure, where you can start from, but feel free to extend.

2. Make a Fork of this Documentation repository

3. Add your folder (and subfolders) and assets to the file structure

4. Add a link to the mkdocs.yml navigation

5. Commit, and make a Pull Request, to validate your contribution

4. Soon your Connector Documentation will be live

## Naming convention

The example zip file contains a folder "connector-serrano".

!!! info "Serrano"
    Serrano is the fictitious name for the Connector we are going to document.
    
Change the name "serrano" to your connector name. If you need spaces, add a dash "**-**"

E.g. If you connector will be named "Infinity", rename the folder to "connector-infinity"

## Files in the folder

- index.md will be the main file  
Using markdown to describe the functionality. We use "[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/)" so you can use all the markdown in this reference.

- example.png add images or screenshots to the same folder

## Subfolders

If your documentation is extensive, and having it all in 1 page is too much, feel free to add subfolders to your folders.

Follow the same structure and guidelines as in the Contributing guide.

## What needs to be in documentation?

### Type of connector

In the zip file, you'll find the three options. If you document your connector, your connector will be a "**Third Party**" connector.

Add a link to your company, as the vendor of the connector.

### Installation

Explain how a user can choose your connector from the [Connector Hub](/GraFx-Studio/guides/connector-hub/).

### Configuration

Each connector will have configuration options.

Depending on your setup, more or less fields will be available.

Add a screenshot of all configuration screens, and explain each field.

### Configuration on your side

Explain how a user need to setup credentials or authentication on your end. If your DAM, PIM or other source needs a setup, explain how this is done.

### How to use the connector

Explain how your connector can be used in a GraFx Studio template

As each setup is different, explain all possible use cases.