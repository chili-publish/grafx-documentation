# Smart Crop

![rn_icon](/assets/icon-Grafx-Genie.svg){.rn_icon}

Smart Crop is the GraFx Genie capability that positions an image inside a frame automatically, keeping the most important part of the picture in view whatever the frame's size or aspect ratio. One source image can become a social post, a banner, and a print ad, each correctly framed, without manual cropping for every variant.

Smart Crop works across GraFx Media, GraFx Studio, and the platform settings. The step-by-step guide for each is linked below.

> **TODO (build session):** add a short hero image or the feature video here, matching the existing Smart Crop pages.

## The Full Picture

From upload to output, this is how Smart Crop works:

1. An image is uploaded to GraFx Media.
2. GraFx Genie analyzes it and stores two pieces of metadata on the asset: a **Subject Area** and a **Point of Interest**.
3. The asset is placed into an image frame in a GraFx Studio Smart Template.
4. The frame's Fill mode is set to **Smart Crop**.
5. GraFx Genie positions the image so the subject stays in view, respecting the frame's size and aspect ratio.
6. Optionally, a **Subject Position** (where the subject should sit inside the frame) and a **Subject type** are chosen on the frame.
7. The stored metadata is used wherever the template is rendered: on screen, in output, and through the API.

## Where to manage Smart Crop

| You want to… | Do it in | Page |
|---|---|---|
| Review or adjust an image's Subject Area and Point of Interest | GraFx Media | [Set the Subject Area & POI](/GraFx-Media/guides/smart-crop-subject-area/) |
| Turn on Smart Crop for a frame, set the Subject Position, pick a subject type | GraFx Studio | [Use Smart Crop on an image frame](/GraFx-Studio/guides/smart-crop/) |
| Define the list of subject types for the environment | Platform settings | [Manage subject types](/CHILI-GraFx/guides/manage-subject-types/) |

## Key terms

| Term | What it means |
|---|---|
| **Subject Area** | The boundary around the most important element in an image. Stored on the asset. |
| **Point of Interest (POI)** | The exact focus point inside the Subject Area (for example, a person's eyes). Stored on the asset. |
| **Subject Position** | The area *inside the frame* where the subject should appear. Set on the frame in GraFx Studio. Not the same as the Subject Area. |
| **Subject type** | A category (such as *person* or *product*) that lets one asset store a different Subject Area and POI per intent. |
| **Default** | The Subject Area and POI detected automatically on upload. Always present; used when no subject type is selected. |
| **Fill mode** | How an image fills its frame: Fit, Fill, Smart Crop, or Manual. See [Crop modes](/GraFx-Studio/concepts/crop/). |

## How GraFx Genie detects the subject

When an image is uploaded (or reprocessed), GraFx Genie Vision examines it and sets the Default Subject Area and Point of Interest. GraFx Genie recognizes people and a range of contextual objects, and places the Point of Interest on the most relevant feature. For a person, that means detecting the eyes.

!!! info "Applies to new or reprocessed assets"
    Improvements to GraFx Genie's detection apply to newly uploaded assets, or to assets that are reprocessed. Existing assets keep their stored Subject Area and POI until they are reprocessed.

> **TODO / [CONFIRM] (build session):**
>
> - List what GraFx Genie currently detects (people, contextual objects such as buildings) and confirm that logo detection is no longer performed, so examples here must not imply automatic logo detection. Source: GraFx Genie Vision release note, Jul 2025; confirm current state with `chili-docs`.
> - Explain Smart Crop algorithm **versioning**: how versions work and how an asset/template picks up a newer version. **[CONFIRM]**

## Subject types

A single image can hold more than one Subject Area and Point of Interest, grouped under a **subject type**, for example *person* or *product*. The same photo can then crop to the person for a social ad and to the product for a catalog page, without duplicating the asset or rebuilding the frame.

The **Default** subject type is detected automatically and is always available. Additional subject types are defined per environment by an admin. See [Manage subject types](/CHILI-GraFx/guides/manage-subject-types/).

## Best practices

- Leave some space around the main subject in the original image, so GraFx Genie has room to reposition without creating whitespace or scaling the image up.
- Place the Point of Interest precisely on the feature that matters most (for a person, the eyes).
- Remember that the Subject Area and POI are stored on the asset: changing them affects **every** template that uses the image.

## When automatic cropping isn't enough

Smart Crop handles most cases, but some images, such as lifestyle photos, need manual fine-tuning:

- **Subject Position** lets you control where the subject lands in a specific frame (for example, to the left when text sits on the right). See [Use Smart Crop on an image frame](/GraFx-Studio/guides/smart-crop/).
- **Manual Crop Override** lets you lock a hand-tuned crop for one image in one frame and layout, while every other image keeps using Smart Crop. See [Manual Crop Override](/GraFx-Studio/concepts/manual-crop-override/).

## Prerequisites & limits

> **TODO / [CONFIRM] (build session):** supported file types, minimum resolution, where GraFx Genie runs, and any credit/billing implications of GraFx Genie processing. Confirm with `chili-docs` / an SME before publishing.
