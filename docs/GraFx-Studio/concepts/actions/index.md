# Actions

## Introduction

"Hi Jane. The customer asked if we can make this price pop out, when it's a promo?"

![](ad1.png)

Jane: "Like this?"

![](ad2.png)

"Yes, perfect! And now make this happen automatically, for all 76500 items."

Jane: "I will add a trigger on the variable 'Promo'. If says 'promo', then I will show the shape behind the price to make the price pop"

## Concept

The concept of Action in GraFx Studio is simple: What should the GraFx Smart Template do, and when should it do it.

### When: Triggers

When is covered in Triggers.

Imagine the Triggers as a system that monitors what is happening in the Template. When a predefined change is detected (triggered), an Action will be performed.

### What: Actions

Actions are the scripts that will be executed, when this change is detected.

## Triggers

What can be detected?

- Select layout changed
- Frame moved
- Page size changed
- Document loaded
- Variable value changed

If any of the above situations occur, a trigger is called.

Important to know that a trigger can be called through the manipulation of the template by an end-user. A trigger can also be called if a condition is met through the execution of batch output.

## Actions

The second tab in the Trigger popup screen shows the Action editor.

Enter you JavaScript code that should be executed.

![screenshot](actioncode.png)