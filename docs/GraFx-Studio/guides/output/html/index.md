# Output to HTML

!!! example "HTML output is Experimental"
	To give you early access to the latest and greatest, we will release some features as "**Experimental**".
	
	This feature and related endpoints (for the API) are not yet final: syntax might change, response could be different, etc. Don't base your production code on experimental features. See [Feature maturity](/release-notes/feature-maturity/).

## Create an output setting

[How to create an export setting?](/GraFx-Studio/guides/output/settings/)

![Create HTML Output a setting](html-02.png){.screenshot-full}

## In GraFx Studio

### Select the right Layout

In [run mode](/GraFx-Studio/concepts/design-run/) select the right layout.

![Choose a layout in Run-mode](html-01.png){.screenshot}

### Choose Export (to HTML)

Click "Export as" and choose your output setting in the dropdown.

![The Export panel in run mode with HTML output chosen under Output](html-03.png){.screenshot}

When the export is ready, your browser will download the zip file into your downloads folder.

## In Studio UI

Very similar in [Studio UI](/GraFx-Studio/concepts/template-management/?h=studio#studio-ui).

### Select the right Layout

![Choose a layout in Studio UI](html-04.png){.screenshot}

### Choose Download (to HTML)

Click "Download" and choose your output setting in the dropdown.

![Download in Studio UI](html-05.png){.screenshot}

If you don't see the correct output settings, check the [User interface](/GraFx-Studio/guides/manage-user-interfaces/), and if it's assigned to the Collection before you create a project.

More on the [workflow](/GraFx-Studio/concepts/template-management/#process) on how to make templates available in My projects with the right output settings.

## Components and images in HTML output

- **Component frames** are rendered in HTML output, including their [resize mode](/GraFx-Studio/guides/use-components/#resize-mode) (Scale, Resize, or Scale and resize) and background color.
- **Image frames** are clipped to the shape of the frame. When the frame has a stroke, the stroke is drawn on top of the clipped image.
- Every asset in the exported zip file gets a unique file name, for example `logo.png` and `logo_2.png`.
