# Smart Crop

See the concept [Smart Crop](../../concepts/genie-smart-crop/).

## How to use Smart Crop?

In your Smart Template, place an Image Frame and select a source image asset.

![screenshot-full](sc6.png)

By default, the Fill property of an Image Frame is set to **Fill**.  
Change this to **Smart Crop** to enable the AI-driven cropping feature.

> **Note**:  
> Smart Crop requires the Subject Area to be defined in advance. See [how to set a Subject Area in GraFx Media](../../../GraFx-Media/guides/smart-crop-subject-area/).

After setting the Subject Area (e.g., the runner on the right side of the image below), GraFx Genie will automatically focus on this subject. (because it's defined in GraFx Media)

## Define Subject Position

If another object or text overlaps your image frame, define a specific area (Subject Position) within the frame for the subject to appear clearly.

![screenshot-full](sc7.png)

To define the Subject Position, click the **Subject Position** button in the properties panel:

![screenshot-full](sc8.png)

A box appears over your image frame. Adjust its size and position to specify exactly where your subject should appear. Click **Apply** to confirm.

![screenshot-full](sc10.png)

Your subject will now fit within the defined Subject Position box.

![screenshot-full](sc11.png)

!!! warning "Important rules for Smart Crop"

    The appearance of your subject depends heavily on the defined Subject Area, the available space around the subject, and the frame’s dimensions. Experiment with different positions and sizes to achieve optimal results.
    
    For best results, ensure the subject has sufficient surrounding area to allow repositioning without causing whitespace or unwanted scaling.