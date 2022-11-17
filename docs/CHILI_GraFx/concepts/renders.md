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

!!! Alert
	V = Variable Data source size (e.g. 1000 recors)
	R = Renders
	
	R = 1 + (V-50)*1
	
	The first 50 renders count as 1, then 1 render is counted towards each record.
	
## Fair use policy

In your subscription, you're entitle to a render quota.

Your dashboard will show the actual status of renders. (with a delay of ±1 day).

![Renders](https://chilipublishdocs.imgix.net/CHILI_GraFx/renders.png)

The light blue line shows the "6 month average".

Render quota are not a hard limit per month. If you generate more output than the render quota, we won’t block or watermark the output. 

You are allowed to go over the monthly limit. 

When the 6 month rolling average exceeds the render quota, it's time to add extra render packs to increase your render quota to at least the 6 month average.

!!! Info
	6 months average calculation	

	Total of past 183 days divided by 6