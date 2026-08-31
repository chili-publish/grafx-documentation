# How to Use Google Sheets Data

In the example below, we'll use a [publicly available read-only Google sheet](https://docs.google.com/spreadsheets/d/1ApwDcYH6CK5pXjKEbTe5Ie-Y2wVsrHxJoKKN8x4Xd_w/edit?usp=sharing).

![The example Google Sheet "RealEstate DS", with Headline and Property Image columns and three data rows](../sheet.png){.screenshot-full}

## Create Variables in GraFx Studio

- In your template, create variables corresponding to the column names in Google Sheets.
- As long as the names match and a data source is connected, the values will be populated automatically.

![The Variables panel, with Headline plus the Property info and Agent info groups matching the sheet columns](../variables.png){.screenshot}

## Link the Google Sheet

- Select the Connector Instance (for the right Authentication method)

![The Resources panel opened from the bottom quick tools, pointing at the Data source entry](../datasource.png){.screenshot}

![The Select connector dropdown open, with the Google Sheets connector instance ticked](../connector.png){.screenshot}

- Copy the link of the [public document](https://docs.google.com/spreadsheets/d/1ApwDcYH6CK5pXjKEbTe5Ie-Y2wVsrHxJoKKN8x4Xd_w/edit?usp=sharing).
- Paste it into the data source field.

![Configuration options for the data source, with the spreadsheet URL pasted under Set value](../sheetsetup.png){.screenshot}

## Preview in Run Mode or Studio UI

- In [Run mode](/GraFx-Studio/concepts/design-run/#run-mode) or the [Studio UI](/GraFx-Studio/concepts/template-management/#studio-ui), you can browse records to preview how content changes.

## Run Mode (in Studio Workspace)

![Run mode in the dark Studio workspace, with the Data row picker on Row 1 and the record table open](../runmode.png){.screenshot-full}

## Studio UI

![The light Studio UI with the same record table, the row's values in the form and the New Listing design beside it](../studioui.png){.screenshot-full}

## Output

To generate output with dynamic data, create an [output setting](../../../guides/output/settings/#data-source).

Ensure the **Data source** is enabled for batch processing.

![The Data source section of an output setting, with the Use data source toggle switched on](../output.png){.screenshot}

!!! note "PDF only"
    Only PDF output will use the data source. Soon the other formats will support batch output too.

When set to "Use data source", your output will have a page for each record in the data source.

![Output preview with a page per record: New Listing on the canvas, New Price and Hello in the Pages panel](../output2.png){.screenshot-full}

## Google Sheet Setup guidelines

- **Column Range**: Values from all columns will be read[^1].
[^1]: Although all columns from the Google Sheet will be read, relying on too many variables may significantly slow down performance.
- **Header**: Your Google Sheet column names must match the Smart Template variable names
- **Column Data Type**
    - All values are considered: "Single Line Text"
    - Format Numbers as Numbers  
    ![The Format > Number submenu in Google Sheets, pointing at the Number option](../format_number.png){.screenshot}
    - Format Date as "Date" or "Date Time"  
    ![The same Format > Number submenu, expanded further and pointing at both Date and Date time](../format_date.png){.screenshot}
    - Booleans: Boolean columns must always have a value (cells cannot be empty)
    - Booleans: Define boolean columns using checkboxes  
    ![The Insert menu in Google Sheets, pointing at "Tick box", with a ticked cell in the Reduction column](../format_boolean.png){.screenshot}
- **Row Structure**: The sheet must **NOT** contain empty rows between rows with data  
![A Reduction, Price and Date sheet where blank row 6 sits between filled rows, boxed in red](../format_empty.png){.screenshot}
- **Sharing**  
**OAuth2.0 JWT Bearer authentication**: Share it with the service account setup during configuration of the Connector.  
**OAuth2.0 Authorisation Code**: share with the user who is authorising.  
**Public**: All people with the link can access your document. You can set it to read-only or editable. 