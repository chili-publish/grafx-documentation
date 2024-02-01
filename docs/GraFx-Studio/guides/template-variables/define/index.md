# Defining template variables

!!! info "Template Variables"
	When referring to **variables** we can mean **[Template variables](/GraFx-Studio/concepts/variables/#template-variables)** or **[JavaScript variables](/GraFx-Studio/concepts/variables/#javascript-variables)**.
	In the context of this page, we are talking about Template variables, unless stated differently.

In the headerbar, choose [Automate](/GraFx-Studio/overview/headerbar/)

A panel will appear, where you can define your template variables.

A list of all template variables that are available in the document shows

- Variable name
- Variable type
- Visibility of the variable
- Number of occurrences of the variable in the document

## Options

Each template variable has a pencil icon, and three dots.
The pencil icon will bring up the "Settings" panel.

The three dots will provide you below options:

### Settings

Opens the settings panel

### Rename

The template variable name goes into inline rename modus.
You can also double click/tap on the name.

### Duplicate

Creates a copy of the template variable and all its properties.
Since the name must be unique, the name is appended with an incrementing number.

### Delete

A confirmation dialog is shown before it's deleted.

### Move to Top

Will move the template variable to the top of the list

You can also drag the template variable in the list to where you want to position it.

This location does not have any effect on the working of your document. It will only help to guide the end-user to see them in a logical order.

### Move to Bottom

Will move the template variable to the bottom of the list

You can also drag it in the list to where you want to position it.

This location does not have any effect on the working of your document. It will only help to guide the end-user to see them in a logical order.


## Types

### Single Line of Text

A placeholder for text.

### Image

A placeholder for a reference to an image in the (GraFx) Media pool, or other sources through **Connectors**

## Default state

The default value your template variable will have.

## Basic properties:

- Name: Cannot be empty, must be unique
- Type: See [types](#types) above
- [Visible](#visibility-conditions): Enabled by default
- Read-only: Disabled by default

### Appearance settings

These setting define how the template variable is presented:

- Label: Can be empty, must not be unique, by default it has the same value as the name (When the name is changed, the label is updated, unless if the label already has a different value)
- Label position
