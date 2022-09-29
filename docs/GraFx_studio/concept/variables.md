---
tags:
  - unfinished
---

# Variables

!!! Info
	
	A variable is a named container for a particular set of data (text, image reference, date, etc...).
	
	Source: [Wikipedia](https://en.wikipedia.org/wiki/Variable_(computer_science)){target="_blank"}
	
	In the context of GraFx Studio, that variable is used in a frame as placeholder to be replaced with the content of the variable or datasource.
	
## Definition

In the headerbar, choose [Automate](/GraFx_studio/headerbar/)

A Variable panel will appear, where you can define your variables.

A list of all variables that are available in the document shows

- Variable name
- Variable type
- Visibility of the variable
- Number of occurrences of the variable in the document

## Selecting

You can click to select / unselect a variable.

With several variables selected, you can [group](#group-variables) variables.


## Options for a variable

Each variable has a pencil icon, and three dots.
The pancil icon will bring up the "Settings" panel.

The three dots will provide you below options:

### Settings 

Opens the settings panel of the variable

### Rename 

The variable name goes into inline rename modus.
You can also double click/tap on the variable name.

### Duplicate 

Creates a copy of the variable and all its properties. 
Since the name of a variable must be unique, the name of the new variable is appended with an incrementing number.

### Delete 

A confirmation dialog is shown before the variable is deleted.

### Move to Top 

Will move the variable to the top of the list

### Move to Bottom 

Will moves the variable to the bottom of the list


## Variable Types

### Single Line of Text

A placeholder for text.

### Image

A placeholder for a reference to an image in the (GraFx) Media pool.

## Default state

The default value your variable with have.

## Basic properties:

- Name: Cannot be empty, must be unique
- Type: See [types](/#variable-types) above
- [Visible](/#visibility-conditions): Enabled by default
- [Required](/#required-variables): Disabled by default
- Read-only: Disabled by default

### Required variables

When checked, the Studio Editor will ask the user to provide a value.

!!! Info
	When a variable is required and it doesn’t have a default value it doesn’t show an error upon opening the document.
	
An error is triggered upon these conditions:

- When the input is in focus and left empty.
- When the user enters a value for the first time, deletes it again (so the input is empty again) the error message will be shown below the input until the error is resolved. 
- When trying to save the document or generate output. A dialog is shown to inform the user that the document can’t be saved or exported.

To indicate that a variable is required an asterisk ( * ) is shown next to the variable label.

### Visibility conditions

When the “Visible” setting is enabled (is enable by default), there is an option to add one or more visibility conditions. Only if ALL conditions are met the variable is visible for the end-user.

The visibility conditions:

- Variable … has value …
- Selected frame name contains …
- Selected frame is of type …
- Selected frame has private data … with value …
- Selected layout name contains …

!!! Note
	We limit the options to keep it simple. 
	If you want more advanced action, you can create a hidden variable that is set by an action and use that variable as a visibility condition.

### Appearance settings

These setting define how the variable is presented:

- Label: Can be empty, must not be unique, by default it has the same value as the variable name (When the variable name is changed, the label is updated, unless if the label already has a different value)
- Label position

## Group variables

You can put variables into variable groups. 

These groups can be used as a filter in the variable input form for the end-user. E.g. the variables can be presented as different steps the end-user needs to go through, with different input panels, each showing the variables from a specific variable group.

It is possible to drag and drop one or more variables in and out of groups and from one group to another.

## Sort variables

You can drag and drop variables in the variable list to change the order of the variables.

This is also the order in which they will be presented to the end-user.

It is possible to select multiple variables and move them together in a group.

## Search variables

This will search on variable name and label.

Doing a search does not impact the list of variables that is presented to the end-user. It’s just a tool to make it easier to find variables.

## Delete variables

When a variable is removed from the list all occurrences of this variable in the document are also removed. This means that an image frame using that variable will become an empty image frame (showing the placeholder again). In a text frame all occurrences of the variable will be removed.

