# Upload fonts

<iframe width="690" height="388" src="https://www.youtube.com/embed/9okRyIPa3RQ?controls=1&mute=0&showinfo=0&rel=0&autoplay=0&loop=0" title="Upload and manage custom fonts in GraFx Fonts" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Getting Started with GraFx Studio — full course](https://www.youtube.com/playlist?list=PLOzpLl2aXHcM)

## License

Adding fonts to CHILI GraFx requires a valid license. Before uploading, check your font supplier (foundry) if you have a valid license to use your fonts for your application.

## Adding font to GraFx Fonts

Click the upload button

![appscreen](uploadbutton.png){.screenshot-full}

Select 1 or more files to upload

![appscreen](selectfiles.png){.screenshot-full}

Confirm you have the license.

![appscreen](confirmlicense.png){.screenshot}

Listen carefully while uploading.

![appscreen](elevator.png){.screenshot-full}

GraFx Fonts will read the metadata from the font files and suggest the categorization of the fonts according the family and [style](https://en.wikipedia.org/wiki/Font#Characteristics).

![appscreen](confirmstyles.png){.screenshot-full}

At this moment in the upload process, you can still choose to NOT upload a specific font to the GraFx Fonts application.

Click the waste bin next to the font (style) you wish NOT to upload.

![appscreen](wastebin.png){.screenshot-full}

## Upload ready

After you confirmed the upload, your font family will appear in the list.

![appscreen](result2.png){.screenshot}

Click the font family to see its contents (the font styles).

![appscreen](harry.png){.screenshot-full}


## Warnings

### Duplicates

When GraFx Fonts detects a duplicate, you'll see a warning icon.

![appscreen](error.png){.screenshot-full}

You can choose to delete (not to upload) the font, or categorize it differently.

Two criteria are used to check if a font style is unique

	- Font family (eg. Satoshi)
	- Style (eg. Regular Italique)
	
When the combination of the family and style is already available, GraFx Fonts will mark the upload as duplicate.

### Metadata wrong

When uploading a font, GraFx Fonts will read the metadata. When the information in the metadata is not correct, this might be confusing.

E.g. Uploading a font with the name "SatoshiRegularItalic.otf" you would imagine the font to look "regular" and "_Italic_". However, CHILI GraFx might suggest to use a regular style, because the _Italic_ meta data was not present.

You can choose to follow the suggestion (if not duplicate) or you can change the style based on your information.

Once uploaded, the new metadata will be used in GraFx Studio to categorize the font.

In the example below, the _italic_ was not encoded correctly for 2 out of 3 fonts. And therefore also marked as duplicates, since the non-italic version was available in the repository.

![appscreen](wrontmetadata.png){.screenshot-full}