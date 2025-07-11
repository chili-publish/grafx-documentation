# GraFx Studio Exporter for Adobe® InDesign®

!!! example "Experimental"
	To give you early access to the latest and greatest, we are introducing some features as **"Experimental"**.  
	You’re welcome to explore and use these features, but keep in mind that their functionality may evolve.  
	If you’re working in production workflows, be aware that changes may still occur.
	
	Please let us know through the support channels if you run into issues.

## Introduction

The InDesign Conversion Plugin allows you to export documents from Adobe® InDesign® and import them into **GraFx Studio**. This process lets you automate the creation of design variants by leveraging GraFx Studio’s powerful smart template features. While InDesign® remains a great starting point for creative design, GraFx Studio excels at automation and multi-channel output.

## Elements of the conversion

- GraFx Studio Exporter (Adobe® InDesign® plugin)
- Importer in GraFx Studio

## How to Install the Plugin

### Download the Plugin

Click to download [the latest version of the plugin](https://studio-cdn.chiligrafx.com/plugins/AdobeInDesign/0.3.0/GraFxStudioExporter_InDesign_0.3.0.ccx)

### Install the Plugin

   - Locate the "GraFxStudioExporter_InDesign_x.y.z.ccx" (x.y.z being the version)  
   - Double click the ccx file
   - Follow the steps to install the plugin in Adobe® InDesign®

## How to Convert a Document

### Prepare Your InDesign® Document

   - Open the Adobe® InDesign® document you want to export.
   - Ensure all assets are properly linked.

Example: Blue.png is missing

![screenshot](convert17.png)

All assets are linked correctly

![screenshot](convert18.png)


### Export to GraFx Studio

   - Go to **Plugins > CHILI GraFx plugins > GraFx Studio Exporter**

![screenshot](convert01.png)

   - Run preflight to avoid conversion issues

![screenshot](convert03.png)

![screenshot](convert04.png)

Example of a potential issue: Frame stroke type not supported.  
You can choose to ignore, or to export the object to a PDF asset, and place it as an asset.

![screenshot-full](convert19.png)

   - Choose a destination folder and click **Export**.  
   Required only once, can be changed at any moment
   - Choose the Page to be exported
   - Choose "All pages" to export all the pages

!!! note "Limitations"
    Exported pages must have the same size.
    
    Users can skip differently sized pages or convert them to match the first page.
    
    A maximum of 50 pages can be exported, with any additional pages excluded.

![screenshot](convert20.png)

   - Choose your Layout <a id="alt-layouts"></a>
   
Adobe® InDesign® supports Alternate Layouts (per page).  
The GraFx Studio exporters allows you to choose what page and alternate layout to export.

Choose your Alternate Layout, and this layout will be in the exporter file.

![screenshot](alt2.png)

![screenshot](alt1.png)

   - The plugin creates a `.zip` file containing the document and all necessary assets.
   
![screenshot-full](convert07.png)

!!! info "What's in the zip file?"
    ![screenshot](convert21.png)
    
    - A log file with info about the Plugin version, the Adobe App version, current Date and Plugin Warnings or Errors caught during the Document Preflight or Export
    - The log file is named: GraFx_Studio_Exporter.log
    - The zip file name format: <selected_page>_<document_name>(<optional_duplicate_copy_version>).zip
    
   

### Import into GraFx Studio

   - Open **[GraFx Studio](https://chiligrafx.com/)**
   - Go to **Templates > Import .ZIP** and select the exported `.zip` file.

![screenshot-full](convert06.png)

![screenshot](convert07.png)

   - Name the template and locate the folder for the assets

![screenshot](convert09.png)

   - You can follow the progress in the top right-hand corner

![screenshot](convert10.png)

   - Your InDesign® document is now ready for automation in GraFx Studio.

![screenshot](convert11.png)

## Preflight

**Preflight** is the essential first step in the conversion process. During preflight, the engine checks your document for compatibility with GraFx Studio. This ensures that the content you are converting can be adapted efficiently for automation and variations.

### How Preflight Works

When you initiate a conversion, the preflight engine scans the document for features that may not be fully compatible with GraFx Studio. If any incompatible elements are found, preflight offers two solutions:

1. **Save as PDF Asset**: The element can be saved as a PDF asset and placed into the converted document, preserving its visual integrity.
2. **Ignore**: The preflight engine will change the missing feature to a supported version (e.g. stroke type in the example).
3. **Fix the Issue**: an obvious but not mentioned choice, is you choose to fix it by choosing a different feature in Adobe® InDesign®, and re-run the preflight.

![screenshot-full](convert19.png)

!!! info "Placed Assets: Pros and Cons"

    **Benefits**  
    - **Preserves Quality**: When elements are saved as PDF assets, their original quality and appearance remain intact.
    - **Simplifies Conversion**: For complex designs, converting to a PDF asset can streamline the process by avoiding the need for manual adjustments.  
    
    **Limitations**  
    - **Not Editable**: Placed assets are static. You cannot edit them within GraFx Studio. For example, if text is saved as a PDF asset, you won’t be able to create a text variable to dynamically alter the text content.
  
## Compatibility

The plugin has been tested and is compatible with Adobe® InDesign® versions from 2024 and 2025.

The latest tested version is 20.1 (January 2025).

## Supported Features

As the GraFx Studio Exporter is **Experimental**, the list below will update frequently.

### Feature Support Table

Features marked with a green checkmark ✅ are fully supported. Some unsupported features are listed for clarity where it matters most.
If a feature isn’t mentioned, it’s not supported — for now! Stay tuned, as we’re continually expanding support.

| **Category**           | **Feature**                              | **Support Level** | **Notes**                                           |
|------------------------|------------------------------------------|-------------------|----------------------------------------------------|
| **Plugin UI**          | Selecting a folder for export            | ✅                |                                                    |
|                        | Selecting a page of the document to export | ✅              |                                                    |
|                        | Logging                                   | ✅                |                                                    |
|                        | Appearance color scheme                  | ✅                |                                                    |
| **Document**           | Page size                                | ✅                |                                                    |
|                        | Choose the page to import                | ✅                |                                                    |
|                        | All pages                                | ✅                |  See [Export](/GraFx-Studio/convert/Adobe-InDesign/#export-to-grafx-studio) for limitations |
|                        | Layouts                                  | ✅                | [Choose the Layout](#alt-layouts) you want to export|
|                        | Bleeds                                   | ✅                | Exported from document settings                    |
| **Frames**             | Rotation                                 | ✅                | Includes text, image, ellipse, polygon             |
|                        | Blend modes                              | ⚠️                | Preflight: convert to PDF or ignore                |
|                        | Mirror / Shear                           | ⚠️                | Shear triggers preflight                           |
|                        | Z-index / stacking order                 | ✅                |                                                    |
| **Text Frames**        | Font (name and style)                    | ✅                |                                                    |
|                        | Font size                                | ✅                |                                                    |
|                        | Tracking                                 | ✅                |                                                    |
|                        | Baseline shift                           | ✅                |                                                    |
|                        | Underline                                | ✅                |                                                    |
|                        | Strikethrough                            | ✅                |                                                    |
|                        | Superscript                              | ✅                |                                                    |
|                        | Subscript                                | ✅                |                                                    |
|                        | All caps                                 | ✅                |                                                    |
|                        | Text color                               | ✅                |                                                    |
|                        | Soft return, discretionary line break    | ✅                | Exported as expected                               |
| **Alignment**          | Left                                     | ✅                |                                                    |
|                        | Center                                   | ✅                |                                                    |
|                        | Right                                    | ✅                |                                                    |
|                        | Top                                      | ✅                |                                                    |
|                        | Center (vertical)                        | ✅                |                                                    |
|                        | Bottom                                   | ✅                |                                                    |
| **Styles**             | Paragraph style                          | ✅                | Font must exist on platform                        |
|                        | Character style                          | ✅                | Font must exist on platform                        |
| **Image Frames**       | Arbitrary position                       | ✅                |                                                    |
|                        | Rotated content                          | ✅                |                                                    |
|                        | Stretched content                        | ✅                |                                                    |
|                        | Fill / Fit mappings                      | ✅                | Preflight converts fit modes accordingly           |
|                        | Horizontal / vertical flip               | ✅                |                                                    |
|                        | Shear                                    | ⚠️                | Preflight warning                                  |
|                        | High-resolution image support            | ✅                | Tested with 6000x6000 px                           |
| **Primitives**         | Rectangle, ellipse, triangle             | ✅                |                                                    |
|                        | Polygon                                  | ⚠️                | Stroke weight / size partially supported           |
|                        | Stroke weight                            | ✅                |                                                    |
|                        | Stroke color                             | ✅                | Predefined & custom                                |
|                        | Fill color                               | ✅                | Predefined & custom                                |
|                        | Corner radius                            | ✅                | Rectangle only                                     |
|                        | Triangle corner radius                   | ❌                |                                                    |
| **Colors**             | CMYK, RGB swatches                       | ✅                |                                                    |
|                        | Spot colors                              | ✅                |                                                    |
|                        | Custom RGB/CMYK                          | ✅                |                                                    |
|                        | LAB, HSB                                 | ⚠️                | Preflight: converts to CMYK or black               |
| **Preflight**          | Problem list                             | ✅                |                                                    |
|                        | Details view                             | ✅                |                                                    |
|                        | Centering object                         | ✅                | Clicking warning centers object                    |
|                        | No document open                         | ✅                | Does nothing                                       |
|                        | Switching documents resets preflight     | ✅                |                                                    |
|                        | Frame stroke issues                      | ✅                | Can be ignored or converted                        |
|                        | Tables not supported                     | ✅                | Converted to PDF                                   |
|                        | Text overflow                            | ✅                | Can be ignored or converted to image               |
|                        | Gradient color                           | ✅                | Preflight warning shown                            |
|                        | Text variables converted                 | ✅                | Automatically mapped in Studio                     |
| **Layers**             | Layer names                              | ✅                | Default names in Studio                            |
|                        | Hidden layers                            | ❌                | Not exported                                       |
|                        | Locked layers                            | ✅                | Not exported                                       |
|                        | Hidden/locked objects                    | ✅                | Not exported                                       |
| **Pages**              | Export specific page                     | ✅                | Page dropdown updated in real-time                 |
|                        | Export all pages                         | ✅                | Max 50 pages                                       |
|                        | Mixed page sizes                         | ✅                | Option to skip or unify sizes                      |
|                        | Page numbering in .zip name              | ✅                | Example: 3_Test.zip                                |
|                        | Layout dropdown dynamic refresh          | ✅                |                                                    |


### Legend (not John)

- ✅ **Supported**: Fully supported
- ✴️ **Not yet**: Planned to be released soon
- ❌ **Unsupported**: The team is working hard to add this functionality in the future

## Tips for Successful Conversion

### Simplify Your Design

Ensure your design uses basic text, shapes, and images for best results.

### Check for Unsupported Features

Use the **Preflight** option in InDesign® to identify unsupported features before exporting.

### Use Linked Assets

Make sure all images are properly linked and included in the export.

### Have fonts installed on your environment

Font Files are not included in the .zip and are not exported.
You should have all Fonts installed to the platform.
Fonts will be applied to the template upon Importing, and the match will be made by name of the font.
Otherwise the default font is used.

When you install the fonts after the import, GraFx Studio will try to apply them when you re-open the template.

### Plan for Automation
After importing to GraFx Studio, leverage smart template features to add business logic and automate variant creation.

## Things to consider

- Colors that are not in RGB or CMYK color space (like HSB, LAB) will revert to Black  
- Adobe® Variables (like <document_name> <current_date> etc) will be removed form a text
- Any item Frame in Adobe® InDesign® (text/image) might have properties (background color ,stroke, opacity).  
Frame options are not detected by Preflight and will be missed after export
- ‘Line’ Shapes are always exported as .pdf without Preflight warning
