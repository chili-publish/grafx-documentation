# Layers

## Z-layers

!!! Info
	Layers are used in digital page layout to separate different elements of a page.
	
	Source: Wikipedia

In GraFx Studio: Layers bring structure in a document. They group frames together. This way multiple frames can be hidden together by hiding the layer and multiple frames can be assigned the same constraints because constraints can be applied to a layer.

Layers are used to bring structure in a template or document. A layer is a group or collection of frames. We refer to them as **z-layers**, because a layer has a z-depth. 

Z-depth refers to the Z-coordinate in the Cartesian coordinate system. 

![XYZ](https://upload.wikimedia.org/wikipedia/commons/6/69/Coord_system_CA_0.svg)

!!! Alert
	There is no actual height difference, but Z-axis is used to refer to the relative position to the other layers.

In GraFx Studio layers are in line with desktop editing tools. All frames need to be assigned to a layer. Each layer has a z-depth. Each frame also has a z-depth, but within scope of it's layer. 

## Layer concepts

When a layer is duplicated, all frames on this layer are duplicated to the copied layer as well. Frame names have to be unique within a document. 

[Shortcuts](/GraFx_studio/concept/shortcuts/) work on layers