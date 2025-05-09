# Create Output Settings

[What are output settings?](/GraFx-Studio/concepts/output-settings/)

## Create output settings

In GraFx Studio, go to **Manage > Output settings** to view and configure output settings.

By default, each output format has one preconfigured setting.

![screenshot-full](os00.png)

To add a new setting, click the **+ Create** button.  
Give your setting a relevant name and choose an output file format.

![screenshot](os03.png)

The new setting will appear in the list.

![screenshot-full](os04.png)

To delete a setting, use the **...** menu at the right end of the row.

![screenshot](os06.png)

If all settings are deleted, a placeholder will indicate no output settings exist.

![screenshot-full](os01.png)

---

Output settings vary depending on the file format.

## Generic Settings (all formats)

![screenshot-full](os14.png)

### Name and description

- **Name** (1) appears in the [Studio UI](/GraFx-Studio/guides/create-projects/#customize-your-project)
- **Description** (2) appears as a subtitle in the export UI

![screenshot-full](os15.png)

### Output format

- Select the output format (3) — it can still be changed later.

### Watermark

- Enable this to apply a watermark to your output.
- Renders with watermark **do not** count as billable.
- Enter a non-empty watermark text.

---

## PDF Output Settings

See [Generic Settings](#generic-settings-all-formats)

![screenshot-full](os12.png)

### Bar Width Reduction

Compensates for ink spread during printing (dot gain).  
Use positive values to make bars thinner, negative to make them wider.

### Outline Text

Outputs text as vector shapes instead of embedding fonts.  
This removes font dependencies in the resulting PDF.

![screenshot](os17.png)

### Data Source

When enabled, includes all records from the data source in the output.

![screenshot](output.png)

### Error Handling

Enable **Continue batch output after failure** to skip failed rows.  
A report is available in [Output Tasks](../tasks/).

![screenshot](errorhandling.png)

### Crop Marks

See [Crop Marks](/GraFx-Studio/concepts/crop-marks/).  
Define offset and weight (thickness).

![screenshot](os16.png)

---

## JPG Output Settings

![screenshot-full](os13.png)

### Scaling

Adjusts output resolution.  
Higher resolution assets (if available) are used automatically.

### Quality

Set compression quality (1% to 100%).  
Higher values mean larger file size but better image fidelity.

### Data Source

Exports all data source records as individual JPG files in a ZIP.

![screenshot](output.png)

### Error Handling

Enable **Continue batch output after failure** to skip failed rows.  
A report is available in [Output Tasks](../tasks/).

![screenshot](errorhandling.png)

---

## PNG Output Settings

![screenshot-full](os09.png)

### Scaling

Same behavior as in JPG output.

### Data Source

Exports all records as individual PNG files in a ZIP.

![screenshot](output.png)

### Error Handling

Enable **Continue batch output after failure** to skip failed rows.  
A report is available in [Output Tasks](../tasks/).

![screenshot](errorhandling.png)

---

## GIF Output Settings

![screenshot-full](os11.png)

### Scaling

Same behavior as in JPG and PNG output.

### Frame Rate

Set the number of animation frames per second.

### Data Source

Exports all records as individual GIFs in a ZIP.

![screenshot](output.png)

### Error Handling

Enable **Continue batch output after failure** to skip failed rows.  
A report is available in [Output Tasks](../tasks/).

![screenshot](errorhandling.png)

---

## MP4 Output Settings

![screenshot-full](os10.png)

### Scaling

Same as other image/video formats.

### Frame Rate

Set the number of animation frames per second.

### Data Source

Exports all records as MP4s in a ZIP.

![screenshot](output.png)

### Error Handling

Enable **Continue batch output after failure** to skip failed rows.  
A report is available in [Output Tasks](../tasks/).

![screenshot](errorhandling.png)