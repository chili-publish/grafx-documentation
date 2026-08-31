<!--
  GraFx Genie capability page — follows the GraFx Genie hub pattern:
  1. What it is  2. How GraFx Genie helps  3. Where to find it (links out)
-->

# GraFx Genie Actions

## What it is

In GraFx Studio, **Actions** are the JavaScript scripts that turn a template into a Smart Template. For example: showing an extra asset when a discount drops below a threshold, or adjusting a layout when a value changes. **GraFx Genie for Actions** writes that script for you.

## How GraFx Genie helps

Writing Actions normally means writing JavaScript. With GraFx Genie, you describe the behavior you want in plain language, and GraFx Genie generates the Action script. It knows the template's context, such as your variable and frame names, so the result fits your template. You stay in control: review the suggested script, tweak it, or ask a developer colleague to take a look for the final touches.

## Example

You have a retail template. A template variable field allows the users of the template to enter a discount percentage. When the discount drops below, say, 30%, you (as a template designer) want to show an extra asset to highlight the steep discount.

![Retail template on the canvas: a chill water bottle, a 40% headline and the selected BUY NOW button frame](template.png){.screenshot-full}

A template variable makes sure a user can change the discount.

![Variable settings for the Discount variable: Variable Type Single Line Text, Visible on, default state 30](variable.png){.screenshot-full}

Now, let's make an Action that will be triggered when a template variable value changes.

![The Triggers tab of Edit action, with one If row reading Variable value changed for Any variable](trigger.png){.screenshot-full}

To create the Action, click on the Action tab.

![The Action tab of Create action with an empty script editor at line 1](action.png){.screenshot-full}

You can now ask GraFx Genie to write the script for you. Click on the GraFx Genie icon.

![The round GraFx Genie sparkle icon that sits beside the script editor](genie-icon.png){.screenshot-full}

![The GraFx Genie dialog asking "What action would you like to create?", with the prompt box still empty](genie1.png){.screenshot-full}

Ask GraFx Genie what functionality you need in your Smart Template.

![The same dialog with a typed request to hide or show the buynow frames when the discount is lower than 30](genie2.png){.screenshot-full}

GraFx Genie will now suggest a JavaScript you can use to perform the functionality.

![The generated script in the Action tab, reading the Discount variable and calling setFrameVisible on both frames](action2.png){.screenshot-full}

As you see, GraFx Genie knows about the context. Without specifying that discount is a template variable name, it will understand and use this information to write the script.

If you're not 100% convinced, you can still tweak the script, or ask a developer colleague to take a look for the final touches.

## Where to find it

GraFx Genie for Actions is part of **GraFx Studio**, alongside the Actions that power Smart Templates:

- [Actions](/GraFx-Studio/concepts/actions/): what Actions are and how triggers use them.
- [Create Actions](/GraFx-Studio/guides/actions/create/): the step-by-step guide to building an Action.
