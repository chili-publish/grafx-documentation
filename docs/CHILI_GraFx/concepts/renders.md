---
tags:
  - unfinished
---

# Renders

A render is a measurement of the usage of the CHILI GraFx platform.

## Local vs Server

A lot of calculation is done on the client side, or local.

E.g. movement of frames, showing the animation, etc...

## Output

To generate output, server routines are necessary.

When these routines are called, a render is counted. Depending on the type of output, more or less renders are counted towards the average.

This average is used to size your allowance in your contract.

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