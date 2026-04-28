# CSV Data Connector

:fontawesome-regular-square: Built-in
:fontawesome-regular-square: Built by CHILI publish
:fontawesome-regular-square-check: Third Party

[See Connector types](/GraFx-Studio/concepts/connectors/#types-of-connectors)

The CSV Data Connector lets you use any publicly accessible CSV file as a data source in GraFx Studio. Each row in the file becomes a record, and each column becomes a variable you can bind to your template.

No authentication is required. If your CSV file is publicly reachable, the connector can use it.

## Installation

[See installation through Connector Hub](/GraFx-Studio/guides/connector-hub/)

You can deploy multiple instances of the connector, each pointing to a different file.

## Configuration

Once installed, open the connector in your **Connector overview** and go to **Configuration**.

- **CSV File URL** — the full public URL of your CSV file.
- **Allowed Domains** — a list of domains the connector is permitted to fetch from.

Paste in your URL and save. The connector will fetch and parse the file on every use.

### Allowed Domains

Because the connector fetches files from public URLs, it's good practice to restrict which domains it can reach. The **Allowed Domains** setting lets you define an explicit list — the connector will only fetch CSV files hosted on those domains and refuse any other URL.

For example, if your CSV files are always hosted on `cdn.example.com`, add that domain to the list. Any request to a different domain will be blocked, even if a valid URL is provided.

This protects against a template or integration accidentally — or intentionally — pointing the connector at an untrusted source.

Wildcards are supported. Use `*.example.com` to allow all subdomains of a domain — for example, if your files are spread across multiple subdomains like `cdn.example.com` and `assets.example.com`, a single wildcard entry covers all of them.

!!! tip
    Keep the list as specific as possible. Use an exact hostname (e.g. `cdn.example.com`) when your files always come from one place. Use a wildcard (e.g. `*.example.com`) only when you genuinely need to cover multiple subdomains.

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
- **Empty headers**: columns with an empty header cell are silently ignored — they will not appear in the data model or as variables in your template.

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

Column types are inferred automatically by scanning all non-empty values in the column. You don't need to configure anything — the connector figures it out.

If any value in a column contradicts the detected type, the entire column falls back to **Single-line text** so no data is lost.

### Boolean

**GraFx Studio type:** `boolean`

Detected when every non-empty value in the column is exactly `true` or `false` (case-insensitive).

| ✅ Accepted | ❌ Not accepted |
|---|---|
| `true` | `yes` |
| `false` | `no` |
| `TRUE` | `1` / `0` |
| `False` | `on` / `off` |

### Number

**GraFx Studio type:** `number`

Detected when every non-empty value is a valid finite number. Values starting with `0` (except `0` itself) or `+` are intentionally excluded — this protects things like product codes, postal codes, and phone numbers from being mis-detected as numbers.

| ✅ Accepted | ❌ Not accepted |
|---|---|
| `42` | `007` (leading zero) |
| `3.14` | `+44` (leading plus) |
| `-100` | `Infinity` |
| `0` | `NaN` |
| `1000000` | `1,000` (comma formatting) |
| | `N/A` |

### Date

**GraFx Studio type:** `date`

Detected when every non-empty value matches ISO 8601 format (`YYYY-MM-DD` or a full datetime) **and** represents a valid calendar date.

| ✅ Accepted | ❌ Not accepted |
|---|---|
| `1973-01-01` | `1/01/1973` (D/MM/YYYY) |
| `2024-12-31` | `01/01/1973` (DD/MM/YYYY) |
| `2024-06-15T14:30:00Z` | `01-01-1973` |
| `2024-06-15T14:30:00+02:00` | `January 1, 1973` |
| | `2024-13-45` (invalid calendar date) |

!!! warning "Spreadsheet exports often use regional date formats"
    Most spreadsheet applications export dates in a regional format such as `1/01/1973`. These will **not** be detected as `date` — they will fall back to Single-line text. To use the `date` type, make sure your CSV exports dates in `YYYY-MM-DD` format.

### Single-line text (fallback)

**GraFx Studio type:** `singleLine`

Applied to any column that does not match the rules above, or any column where values are mixed types. No data is lost — the original text is kept exactly as it appears in the file.

| Examples |
|---|
| `Hello world` |
| `Product-001` |
| `007` (leading zero) |
| `1/01/1973` (non-ISO date) |
| A column mixing numbers and text |
| An empty column (header present, no values underneath) |

## CSV file guidelines

- The first row must be the **header row** — column names must match your template variable names.
- Every column should have a header. Columns with empty headers are silently dropped, so any data underneath them is ignored.
- Avoid columns with mixed types if you need a specific type (number, date, boolean) — a single inconsistent value causes the whole column to fall back to text.
- Leading-zero values (product codes, postal codes) should stay as text — the connector will not convert them to numbers.
- The file must be reachable without authentication, and served with `Content-Type: application/json`.
