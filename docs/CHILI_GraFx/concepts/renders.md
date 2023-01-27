# Renders

A render is a measurement for the usage on the CHILI GraFx platform.

## Local vs Server

A lot of calculation is done on the client side, or local.

E.g. movement of frames, showing the animation, etc...

## Output

To generate output, server routines are necessary.

When these routines are called, a render is counted. Depending on the type of output, more or less renders are counted towards the average.

This average is used to size your allowance in your subscription.

## Examples

### Static Digital Output

1 render is counted for each Static Digital Image output generation

### Animated Digital Output

1 render is counted towards each second of output.

### Static PDF output

1 render is counted towards each PDF file.

When variable output is used, this is the formula to count renders.

The first 50 renders are counted individually, then each set of 50 is counted as 1 render.

!!! Formula

	V = Variable Data source size (e.g. 1000 records)
	
	Amount of Renders = 50 + (V-50)/50	
		
	e.g. 50 + (1000-50)/50 = 50 + 19 = 69
	
	The first 50 renders count as 50, then every 50 renders are counted as 1.
	
## Fair use policy

In your subscription, you're entitle to a render quota.

Your dashboard will show the actual status of renders. (with a delay of ±1 day).

![Renders](https://chilipublishdocs.imgix.net/CHILI_GraFx/renders.png)

The light blue line shows the "6 month rolling average".

Render quota are not a hard limit per month. If you generate more output than the render quota, we won’t block or watermark the output.

You are allowed to go over the monthly limit. 

When the 6 month rolling average exceeds the render quota, it's time to add extra render packs to increase your render quota to at least the 6 month average.

!!! Average
	6 month average calculation:

	Total of past 183 days divided by 6