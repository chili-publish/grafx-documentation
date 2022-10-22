# Variables

!!! Info
	
	A variable is a named container for a particular set of data (text, image reference, date, etc...).
	
	Source: [Wikipedia](https://en.wikipedia.org/wiki/Variable_(computer_science)){target="_blank"}
	
	In the context of **GraFx Studio**, that variable is used in a frame as placeholder to be replaced with the content of the variable or datasource.
	
## Example

!!! Text
	"Hello <!firstname!>,
	
	How is life?"


This text contains a placeholder for a **firstname**.

We assume it's supposed to be a firstname, because of the name.

But the name of the variable **firstname** is not related to the content.

It could also have been:

!!! Text
	"Hello <!V1!>,
	
	How is life?"

Variables are placeholders, that will be replaced with variable content.

## Types of content

The type of content for the variable will differ with the context. In the previous example, this most likely will be a piece of text.

In other cases, it could be a reference to an image (or other digital asset).

!!! Info	
	https://upload.wikimedia.org/wikipedia/commons/6/68/Raffael_058.jpg
	
	![Image](https://upload.wikimedia.org/wikipedia/commons/6/68/Raffael_058.jpg)
	
When the frame has a source reference **$ImageRef** then you can replace the variable **$ImageRef** with the source that is relevant at any moment.