# Create Output Settings

[What are output settings?](/GraFx-Studio/concepts/output-settings/)

<iframe width="690" height="388" src="https://www.youtube.com/embed/OmQYHIwrqwE?controls=1&mute=0&showinfo=0&rel=0&autoplay=0&loop=0" title="Create output settings in GraFx Studio" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Getting Started with GraFx Studio — full course](https://www.youtube.com/playlist?list=PLOzpLl2aXHcM)

## Create output settings

In GraFx Studio, go to **Manage > Output settings** to view and configure output settings.

By default, each output format has one preconfigured setting.

![Output settings list with one preconfigured setting per format, and the + Create button](os00.png){.screenshot-full}

To add a new setting, click the **+ Create** button.  
Give your setting a relevant name and choose an output file format.

![Create output setting dialog named Print Quality PDF, with the Output format list open on JPG, PNG, MP4, GIF and PDF](os03.png){.screenshot}

The new setting will appear in the list.

![The list with the new Print Quality PDF setting added below the default MP4, PDF and PNG rows](os04.png){.screenshot-full}

To delete a setting, use the **...** menu at the right end of the row.

![The row menu open, offering Edit output settings and Delete](os06.png){.screenshot}

If all settings are deleted, a placeholder will indicate no output settings exist.

![The empty state reading No output settings created, with a single Create button](os01.png){.screenshot-full}

---

Output settings vary depending on the file format.

## Generic Settings (all formats)

![Name, Description and Output format numbered 1 to 3, with the Download preview numbered 4](os14.png){.screenshot-full}

### Name and description

- **Name** (1) appears in the [Studio UI](/GraFx-Studio/guides/create-projects/#customize-your-project)
- **Description** (2) appears as a subtitle in the export UI

![A description typed as PDF settings for high quality print, repeated as the subtitle in the Download preview](os15.png){.screenshot-full}

### Output format

- Select the output format (3) — it can still be changed later.

### Watermark

- Enable this to apply a watermark to your output.
- Renders with watermark **do not** count as billable.
- Enter a non-empty watermark text.

---

## PDF Output Settings

See [Generic Settings](#generic-settings-all-formats)

![The whole PDF panel: Bar width reduction, Outline text, Data source, Crop marks, Error handling and Watermark](os12.png){.screenshot-full}

### Bar Width Reduction

Compensates for ink spread during printing (dot gain).  
Use positive values to make bars thinner, negative to make them wider.

### Outline Text

Outputs text as vector shapes instead of embedding fonts.  
This removes font dependencies in the resulting PDF.

![The Outline text switch, shown off, above the note that it removes font dependencies](os17.png){.screenshot}

### Data Source

When enabled, includes all records from the data source in the output.

![Data source section of the PDF settings, with Use data source switched on](output.png){.screenshot}

### Error Handling

Enable **Continue batch output after failure** to skip failed rows.  
A report is available in [Output Tasks](../tasks/).

![Error handling section of the PDF settings, with Continue batch output after failure switched on](errorhandling.png){.screenshot}

### Crop Marks

See [Crop Marks](/GraFx-Studio/concepts/crop-marks/).  
Define offset and weight (thickness).

![Crop marks switched on, with Offset set to 3 Millimeters and Weight to 0.25 Points](os16.png){.screenshot}

### PDF Output Conversion

![PDF Output version](os20.png){.screenshot}

In **Convert to version**, choose the required PDF version.

Example:
- PDF 1.4, 1.5, 1.6 or 1.7 (default)

Select the version required by your production partner.

### Color Management

![Convert CMYK colors](os21.png){.screenshot}

Enable **Convert CMYK colors** to activate color transformation during export.

When enabled, you must define:

- **Intended CMYK profile** (required)  
- **Target CMYK profile** (required)

#### Intended CMYK profile (required, if "Convert CMYK colors" is checked)

Defines the original print condition the document is assumed to be prepared for.

This setting tells the system how existing CMYK values should be interpreted.

#### Target CMYK profile (required, if "Convert CMYK colors" is checked)

Defines the destination print condition to which colors are converted.

!!! warning
    If the intended and target profiles do not reflect the actual production workflow, visible color shifts may occur.

#### Convert RGB colors to CMYK colors

Enable **Convert RGB colors to CMYK colors** to also convert RGB content — such as photos and colors defined in RGB — to the target CMYK profile during export.

RGB conversion is a complementary step to CMYK conversion:

- The switch becomes available once both the **Intended CMYK profile** and **Target CMYK profile** are set. Until then, it is visible but disabled, with a tooltip explaining why.
- RGB colors with an embedded profile are converted using that embedded profile.
- For unmanaged RGB colors (no embedded profile), select the assumed source profile in the **RGB source profile** dropdown that appears when the switch is on.

Available RGB source profiles:

- Adobe RGB (1998)
- Apple RGB
- Color Match RGB
- HDTV (Rec. 709)
- PAL/SECAM
- SDTV NTSC
- SDTV PAL
- SMPTE-C
- sRGB IEC61966-2.1

For a deeper explanation of color management concepts, see:

- [Color Management in CHILI GraFx](/GraFx-Studio/concepts/color-management/)

---

## HTML Output Settings

See [Generic Settings](#generic-settings-all-formats)

![HTML output settings, the format tagged Experimental, with no scaling or quality controls](os-18.png){.screenshot-full}

### Data Source

When enabled, includes all records from the data source in the output.

![Data source section of the HTML settings, with Use data source switched on](output.png){.screenshot}

### Error Handling

Enable **Continue batch output after failure** to skip failed rows.  
A report is available in [Output Tasks](../tasks/).

![Error handling section of the HTML settings, with Continue batch output after failure switched on](errorhandling.png){.screenshot}

---

## JPG Output Settings

![JPG output settings, with Scaling on 1x and Quality on 90%](os13.png){.screenshot-full}

### Scaling

Adjusts output resolution.  
Higher resolution assets (if available) are used automatically.

### Quality

Set compression quality (1% to 100%).  
Higher values mean larger file size but better image fidelity.

### Data Source

Exports all data source records as individual JPG files in a ZIP.

![Data source section of the JPG settings, with Use data source switched on](output.png){.screenshot}

### Error Handling

Enable **Continue batch output after failure** to skip failed rows.  
A report is available in [Output Tasks](../tasks/).

![Error handling section of the JPG settings, with Continue batch output after failure switched on](errorhandling.png){.screenshot}

---

## PNG Output Settings

![PNG output settings, with a Scaling dropdown on 1x and no quality slider](os09.png){.screenshot-full}

### Scaling

Same behavior as in JPG output.

### Data Source

Exports all records as individual PNG files in a ZIP.

![Data source section of the PNG settings, with Use data source switched on](output.png){.screenshot}

### Error Handling

Enable **Continue batch output after failure** to skip failed rows.  
A report is available in [Output Tasks](../tasks/).

![Error handling section of the PNG settings, with Continue batch output after failure switched on](errorhandling.png){.screenshot}

---

## GIF Output Settings

![GIF output settings, with Scaling on 1x and Frame rate on 5 fps](os11.png){.screenshot-full}

### Scaling

Same behavior as in JPG and PNG output.

### Frame Rate

Set the number of animation frames per second.

### Data Source

Exports all records as individual GIFs in a ZIP.

![Data source section of the GIF settings, with Use data source switched on](output.png){.screenshot}

### Error Handling

Enable **Continue batch output after failure** to skip failed rows.  
A report is available in [Output Tasks](../tasks/).

![Error handling section of the GIF settings, with Continue batch output after failure switched on](errorhandling.png){.screenshot}

---

## MP4 Output Settings

![MP4 output settings, with Scaling on 1x and Frame rate on 30 fps](os10.png){.screenshot-full}

### Scaling

Same as other image/video formats.

### Frame Rate

Set the number of animation frames per second.

### Data Source

Exports all records as MP4s in a ZIP.

![Data source section of the MP4 settings, with Use data source switched on](output.png){.screenshot}

### Error Handling

Enable **Continue batch output after failure** to skip failed rows.  
A report is available in [Output Tasks](../tasks/).

![Error handling section of the MP4 settings, with Continue batch output after failure switched on](errorhandling.png){.screenshot}