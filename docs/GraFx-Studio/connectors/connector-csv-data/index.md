# CSV Data Connector

:fontawesome-regular-square: Built-in  
:fontawesome-regular-square-check: Built by CHILI publish  
:fontawesome-regular-square: Third Party

[See Connector types](/GraFx-Studio/concepts/connectors/#types-of-connectors)

The CSV Data Connector lets you use any publicly accessible CSV file as a data source in GraFx Studio. Each row in the file becomes a record, and each column becomes a variable you can bind to your template.

No authentication is required. If your CSV file is publicly reachable, the connector can use it.

## Installation

[See installation through Connector Hub](/GraFx-Studio/guides/connector-hub/)

You can deploy multiple instances of the connector, each pointing to a different file.

## Configuration

Once installed, open the connector in your **Connector overview** and go to **Configuration**.

The only setting is:

- **CSV File URL** — the full public URL of your CSV file.

Paste in your URL and save. The connector will fetch and parse the file on every use.

## Hosting requirement

!!! warning "Serve your CSV with Content-Type: application/json"
    The connector runtime can only read the contents of a response when the server sends a `Content-Type` header that contains `"json"`. For any other content type, the response is returned in a format the connector cannot read.

    This means your CSV file must be hosted on a server where you can set the response `Content-Type` to `application/json` — even though the file itself contains CSV text. The content of the file is not affected; only the header matters.

    Most static hosting services (AWS S3, Azure Blob Storage, CDNs, GitHub raw with a proxy) allow you to override the content type per file or per bucket.

## Supported CSV formats

The connector handles a wide range of real-world CSV files without any manual configuration:

- **Delimiters**: comma (`,`) and semicolon (`;`) — detected automatically based on the first line.
- **Quoted fields**: fields can contain commas, semicolons, newlines, and escaped double quotes — fully supported.
- **Excel exports**: UTF-8 BOM (added by Excel's "Save as CSV UTF-8") is stripped automatically.
- **Line endings**: both Windows (CRLF) and Unix (LF) are supported.
- **Blank rows**: empty rows, including trailing newlines, are ignored.
- **Missing headers**: if a column header cell is empty, the column is named `Column1`, `Column2`, and so on.

## Using the connector in a template

### Set up your CSV file

Your CSV file must have a **header row** followed by **at least one data row**. The column headers become the variable names in GraFx Studio.

| product_name | price | available |
|---|---|---|
| Summer T-Shirt | 19.99 | true |
| Denim Jacket | 59.99 | true |

### Link the connector in your template

In your template, open the **Data source** panel, select your CSV connector instance, and paste in the URL of your CSV file if it differs from what was set during configuration.

GraFx Studio will read the column headers and create the corresponding variables automatically.

### Browse records in Run Mode

In [Run Mode](/GraFx-Studio/concepts/design-run/#run-mode) or the [Studio UI](/GraFx-Studio/concepts/template-management/#studio-ui), you can page through the records to preview how your template looks with each row of data.

### Output

To generate output across all records, create an [output setting](/GraFx-Studio/guides/output/settings/#data-source) and enable the **Data source** option. Your output will include one page per record in the CSV file.

## Column types

Column types are inferred automatically by sampling all values in the column. You don't need to configure anything — the connector figures it out.

| CSV values | Variable type |
|---|---|
| `true` / `false` (any case) | Boolean |
| Numeric values (not starting with `0` or `+`) | Number |
| Dates in `YYYY-MM-DD` or ISO 8601 format | Date |
| Everything else, or mixed columns | Single-line text |

Leading zeros are preserved as text — a value like `007` will not be converted to a number.

If a column contains mixed types (for example, mostly numbers but with `"N/A"` in some cells), the entire column is treated as single-line text. No data is lost.

## CSV file guidelines

- The first row must be the **header row** — column names must match your template variable names.
- Every column should have a header. Empty header cells are auto-named but harder to work with.
- Avoid columns with mixed types if you need a specific type (number, date, boolean) — a single inconsistent value causes the whole column to fall back to text.
- Leading-zero values (product codes, postal codes) should stay as text — the connector will not convert them to numbers.
- The file must be reachable without authentication, and served with `Content-Type: application/json`.
