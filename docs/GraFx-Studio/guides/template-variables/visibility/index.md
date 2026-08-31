# Variable Visibility Conditions

A variable is always visible in [Design mode](../../../concepts/design-run/#design-mode). However, in [Run mode](../../../concepts/design-run/#run-mode) or the [Studio UI](../../../../GraFx-Studio/concepts/template-management/#studio-ui) (end-user interface), variables can be hidden from the end user.

In some cases, you may want to show or hide a variable dynamically based on the document state or the values of other variables. This helps create a cleaner user experience by ensuring users only see relevant information.

This is where **Visibility Conditions** come into play.

In the **User Interface** tab of a variable, you can define its visibility settings.

![The Variable settings panel, User Interface tab, with Visibility set to Conditional at the bottom](var08.png){.screenshot-full}

Three options are available:

![The Visibility dropdown open on Always, Never and Conditional, with Conditional ticked](var13.png){.screenshot}

- **Always** (default)
- **Never**
- **Conditional**

### Conditional Visibility

If you select **Conditional**, you can define the conditions under which the variable will be shown in the end-user interface.

You can add one or more conditions. **All conditions must be met** for the variable to be displayed.

![The Visibility section reading "2 visibility conditions added" above the Visibility conditions button](var09.png){.screenshot}

Click **Visibility Conditions**.

![The empty Visibility conditions dialog, offering only Add condition](var10.png){.screenshot-full}

Click **+ Add Condition** and define the criteria that must be met for the variable to be visible.

![A first condition, Selected layout Equal to A4, with the layout list open on A4 and A5](var11.png){.screenshot-full}

![A second condition on the variable Show text, its value list open on True and False](var12.png){.screenshot-full}

## Deprecated in Actions

!!! warning "Deprecated Action"
    Visibility can also be controlled via Actions (with or without GraFx Genie).  
    However, **visibility conditions are not compatible with Actions**.

    If you use **SetVisible** in an Action, it will ❌ override and remove ❌ the visibility conditions.

    Before making the document available to end users, ensure that:
    
    - **You do not use `SetVisible` in Actions** if you want to maintain visibility conditions.
    - **You only use Actions or Visibility Conditions**, but not both.

![The Edit action dialog, where setVariableVisible is struck through in the code and in autocomplete](var14.png){.screenshot-full}

The Action Editor will display **SetVisible** as ~~strikethrough~~ to indicate that it is deprecated. Hovering over the function will also display a **deprecated** warning.