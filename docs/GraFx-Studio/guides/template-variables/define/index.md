# Defining template variables

!!! info "Template Variables"
	When referring to **variables** we can mean **[Template variables](/GraFx-Studio/concepts/variables/#template-variables)** or **[JavaScript variables](/GraFx-Studio/concepts/variables/#javascript-variables)**.
	In the context of this page, we are talking about Template variables, unless stated differently.

In the properties panel (right), choose the wrench & screwdriver tool.

![screenshot](var01.png)

Then choose **Variables**

![screenshot](var02.png)

A panel will appear, where you can define your template variables.

A list of all template variables that are available in the document shows

- Variable type
- Variable name
- Pencil icon (when hovering over the variable)
- "..." menu (when hovering over the variable)

![screenshot](var03.png)

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

### Group

You can group variables in a group or folder. This allows you to stay organised in more complex templates.

Shift-select multiple variables, and group them. After grouping, you can rename the group.

![screenshot](group01.png)

![screenshot](group02.png)

## Types

Create a variable. Then, in the properties panel, choose the variable type. Different use cases demand different variable types.

![screenshot](vartypes.png)

### Single-line Text

A placeholder for text.

<iframe width="690" height="388" src="https://www.youtube.com/embed/nLqE_XGqSyE?si=19bArigpUEZeRa5t&controls=1&mute=1&showinfo=0&rel=0&autoplay=0&loop=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[All feature videos](https://www.youtube.com/playlist?list=PLLHtQ1R6R-B_m7XAVySM9OjbbUscsgBOH)

See also: [Text Direction](/GraFx-Studio/concepts/text-direction/)

### Multi-line Text

A placeholder for multi-line text.

### Image

A placeholder for a reference to an image in the (GraFx) Media pool, or other sources through **Connectors**

<iframe width="690" height="388" src="https://www.youtube.com/embed/pP6_3Ej6x-U?si=HqEr0xf11Ka1oVN7&controls=1&mute=1&showinfo=0&rel=0&autoplay=0&loop=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[All feature videos](https://www.youtube.com/playlist?list=PLLHtQ1R6R-B_m7XAVySM9OjbbUscsgBOH)

### Single-select list

A placeholder with a predefined list of values.

A potential use case: define a list of colors to choose from.

<iframe width="690" height="388" src="https://www.youtube.com/embed/iahktXHDu6k?si=UBn6AysRLhP15ylV&controls=1&mute=1&showinfo=0&rel=0&autoplay=0&loop=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[All feature videos](https://www.youtube.com/playlist?list=PLLHtQ1R6R-B_m7XAVySM9OjbbUscsgBOH)


### Boolean

A placeholder that can hold "True" or "False".

<iframe width="690" height="388" src="https://www.youtube.com/embed/l418kpravX0?si=DqSxbg2LhsUy12CM&controls=1&mute=1&showinfo=0&rel=0&autoplay=0&loop=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[All feature videos](https://www.youtube.com/playlist?list=PLLHtQ1R6R-B_m7XAVySM9OjbbUscsgBOH)


### Number

A Placeholder to hold a numeric value. Different than a text variable, you can set specific elements related to numbers.

### Date

A Placeholder to hold a date value. Different than a text variable, you can [set specific elements](../date/) related to dates.

## Variable settings

### Variable name

![screenshot](var07.png)

In the list of variables, you can double click or "Rename" the variable Name.

!!! important "Variable name vs Display Label"

    The variable name is the technical name, that will be used for further automation.
    In the appearance tab you can set the (display) label, that will be shown in the [Studio UI interface](/GraFx-Studio/concepts/template-management/?h=studio#studio-ui).

### Default state

![screenshot](var04.png)

The default value your template variable will have.

### General properties

![screenshot](var05.png)

- Type: See [types](#types) above
- Required: Disabled by default
- Remove paragraph if empty: Disabled by default  
Check to remove the full paragraph this variable is used on.  
Available on (Single-line text, Multi-line text, Single-select list, Date)
![screenshot-full](removeparagraph.gif)
- [Private data](/GraFx-Studio/concepts/private-data/?h=private)  
A set of key-value pairs to assist you with automation.

### User Interface

![screenshot](var14.png)

![screenshot](var08.png)

These settings define how the template variable is presented:

- Label: Can be empty, must not be unique, by default it has the same value as the name (When the name is changed, the label is updated, unless if the label already has a different value)
- Placeholder: Default text, to help nudge the end user to fill in something
- Help text: Text that will appear below the variable to add more info what to do with the variable.

#### Visibility

Choose how visibility is set

![screenshot](var13.png)

- Always (default)
- Never
- Conditional

Conditional: See [Visibility Conditions](../visibility/)