# Smart(er) templates are less complex

## BATS, the formula to simplicity
In times of Covid-19, bats got a bad name (no pun intended). But they are special animals, equipped with Sonar to navigate. A very effective yet simple tool. Some people are scared of bats, due to the appearance in horror movies. And they sleep upside down…

We will use “Bats” to help you simplify your templates.

CHILI publisher is a template building engine to enable one smart template to output multiple variants of the same document. How to get the most out of the smart template, without overdoing it?

The Formula: 
!!! Formula
    B(ATS){*}

Translated to people who have less affection with regex:
Build template - (Add 1 type of logic - Test - Simplify) {repeat until happy}

## Desktop
Probably, your smart template journey starts on your desktop. If not, you can skip this step to "Build your template".
## Conversion
The conversion itself is not the challenge. But it’s “What” you convert. 

Reducing the complexity before conversion will greatly benefit the quest to simplicity.

Imagine a design with a few thousand vector elements, used as a background for a design. When converting, these elements will be converted to vector elements, to be calculated individually to show in your browser window.

If these elements will remain background items, and will not change with any variant, you can increase simplicity by combining all these elements into 1 vector layer and place this layer as an asset.


!!! Tip
    Simplify: Combine background elements into 1 placed asset

![alt text](https://chilipublishdocs.imgix.net/GraFx_publisher/articles/4cffdb11-bfa0-40c9-8bfe-902aedaea502.png?w=840&q=80)
 
## Build your template
Your document is now ready to be made smart(er).
At this stage, you have a blank document in CHILI publisher, or you have converted a document form your desktop application. Either way, it’s time to start adding Logic to the document, to make it smart.
## B(ATS){*}

We have arrived at the recurring theme of the formula (ATS){*}.

- Add 1 type of Logic
- Test the result
- Simplify
- {*} Repeat

## Add Logic

The art of adding logic to your document is the core of CHILI publisher. Enabling 1 smart template to create several types of output.

This means, that the logic added to your template has the power to change the output, depending on the circumstances.

Imagine a campaign for CHILL water, for several sport types. A database feeds

To make a document smarter, several tools are at your disposal.

!!! Tip
	Add one logic layer and test

Unlike the basic human rights, not all logic is created equal. Some types of logic will have more impact on the cost of processing the variant.

Adding a single variable, to a one page document (like a Business Card) is less “expensive” than let’s say an anchored frame, that holds several variable in itself, combined with auto-grow.

### Example

Frame1 will auto-grow, according to more content added

![alt text](https://chilipublishdocs.imgix.net/GraFx_publisher/articles/74a8bb05-ebf7-4c4f-b995-1550a7bb09dc.png?w=300&q=80)
 
Frame2 is anchored, to Frame1, and will refer to its bottom coordinates.

![alt text](https://chilipublishdocs.imgix.net/GraFx_publisher/articles/41009b87-3147-4d67-8ff5-1df9b5980857.png?w=300&q=80)
 
So, when more content is added, Frame1 grows, and Frame2 will move down.

![alt text](https://chilipublishdocs.imgix.net/GraFx_publisher/articles/f00bbd10-e3b4-402e-b445-6d0f392dd519.gif)
 
These are 3 calculations to be coordinated.

- Variables
- Auto-grow
- Anchoring

Each layer of logic will add complexity, and make the document “heavier” to calculate the output.

!!! Tip
	Add 1 layer at a time

### Test

When you added 1 layer of automation logic, test the output.

How can you test? That will differ according to your setup. If you setup allow the interaction with an end-user to fill in the variable, look for challenging variable content. What is the shortest word, what is the longest variant?

Maybe your setup containts a datasource, that will auto populate the variables. Best to check the shortest and longest variable. Does the datasource contain special characters?

!!! Tip
	check variable input with a pre-set of test content (long, short, special characters)

### What is your output?

Check digital output, with or without variable

Check print / pdf output, with and without variables

Check output with datasources

### Simplify

When you test is successful, now is a good time to think about simplification, before adding more automation logic.

E.g. You can add a frame anchor to the left and bottom of another frame. 

![alt text](https://chilipublishdocs.imgix.net/GraFx_publisher/articles/8e547f1f-1c38-467c-9087-a031e0c46a39.png?w=300&q=80)
 
In the picture, you see Frame2 is anchored to 2 targets.

Frame2 is anchored to the bottom, where the top of Frame2 is anchored to the bottom of Frame1, with an offset of 5mm.

Frame2 is anchored to the left side of Frame1, without offset.

Nothing wrong with this setup, but the left of Frame 1 is never changing. So, the second anchor of Frame2 is unnecessary. And it would mean a 4th calculation, where only 3 are necessary.

This is a easy simplification, than can save processing time. 

Even when it only saves a few microseconds, this would be multiplied by 

- Amount of outputs (1 digital / 2 print)
- Amount of records in a Data Source (e.g. 1M)

This add up to: 5 microseconds x 2 million = 10 million microseconds = 166 minutes.

!!! Tip
	think volume when you create your template. Bigger variant runs, bigger savings

### Repeat {*}

You created your document (manually or through conversion), you Added logic, you tested and you simplified.

Time to repeat, add more logic, test and simplify.

{*} is a reference to Regular Expressions. Where the asterisk refers to “infinite” times. You can always improve!

!!! Tip
	never stop improving, keep repeating to find better solutions

### Template building is not an exact science
Since template logic is calculated by a computer, the outcome should be very predictable.

But, templates are created by humans. Humans are creative architects of solutions. Every outcome has several ways to get there. Ask 2 colleagues to make the same smart template, they will both find different approaches.

That’s why template building is not an exact science. Add to that the several possible layers of complexity, and amount of data being output through datasources, and you might run into unexpected behaviour.

That’s why follow the BATS approach gives you the best possible outcome. Document your steps, so you can always return one step to re-test.

If the outcome is not what is supposed to happen, then it’s time to call in the troops, and inform us you may have found an exceptions.

You could submit a support ticket with the Client Success team, or you could ask for specialist help.

Our service partners have trained staff to help you with the template building journey.

!!! Tip
	document every step of your building process, so you can back-trace

### Cost weight

Below is an attempt to list features that will make your template smarter. Some features have more impact on complexity than other. This table gives you an insight in less and more taxing features.

The more taxing features you use, the more complex your document will be, and the more testing will be required.

!!! Warning
	There is no exact weight nor cost, since it will always depend on the context and your specific situation.
	
|Low Tax|Medium Tax|Heavier Tax|
|---|---|---|
|Swatches|Text in shapes|Snippets|
|Image frames|Complex variables|Alternate Layouts|
|(low amount) Simple vector Objects|Actions|Complex Actions|
|Text Frames||Anchors|
|Simple variables||Dynamic Layouts|
|||Logic / Actions triggering other logic|
|||Transparancy effects|

!!! Warning
	Combining several “Low Tax” features will also add up to complexity