# Mocktopus Data Connector

!!! info "Mocktopus"

	![Mocktopus](Mocktopus.svg){.connector_icon}
	A many-tentacled connector that pretends to connect to everything but actually connects to nothing.

:fontawesome-regular-square: Built-in  
:fontawesome-regular-square: Built by CHILI publish  
:fontawesome-regular-square-check: Third Party

[See Connector types](/GraFx-Studio/concepts/connectors/#types-of-connectors)

Mocktopus is a data connector that generates realistic-looking fake data from a declarative schema. No external service, no credentials, no network required. It is designed for testing and prototyping GraFx Studio templates before a real data source is available.

## Installation

[See installation through Connector Hub](/GraFx-Studio/guides/connector-hub/)

## Supported field types

Mocktopus generates data based on a schema you define. The following field types are available:

| Type | Description |
|---|---|
| `shortText` | Short mock text (1–2 words by default) |
| `longText` | Multiple sentences and paragraphs |
| `number` | Random number within a configurable range |
| `boolean` | Random `true` or `false` |
| `date` | Random date between 2020-01-01 and 2030-01-01 |
| `list` | A single value picked from a pipe-delimited list |
| `image` | A seeded image ID (for use with an image variable) |

## Configuration

Each template can have its own schema and settings, so there is no need to deploy multiple connector instances. In **Resources**, assign Mocktopus as the **Output data source** for the template and set the required configuration options.

### Schema (required)

Defines the fields and types to generate, using a comma-separated DSL.

Each field follows the format `fieldName:type` or `fieldName:type(param1=value1,param2=value2)`.

**Example:**

```
firstName:shortText, age:number(min=18,max=65), active:boolean, joinDate:date, status:list(values=active|inactive|pending)
```

**Field type parameters:**

- `shortText` — `numberOfWords` (default: `2`)
- `longText` — `numberOfParagraphs` (default: `2`)
- `number` — `min` (default: `0`), `max` (default: `1000`)
- `list` — `values`: pipe-delimited list, e.g. `active|inactive|pending`

Any field type also supports the `values` parameter to pick randomly from a fixed set:

```
priority:number(values=1|3|5), status:shortText(values=draft|review|published)
```

### Record count

Number of records to generate. Defaults to `10`.

### Simulate delays

Set to `true` to add random delays between responses, simulating a slower real-world data source. Defaults to `false`.

### Min delay (ms) / Max delay (ms)

When **Simulate delays** is enabled, the connector waits a random duration between these two values before returning data. Defaults are `100` ms and `1000` ms.

## External setup

None required. Mocktopus generates all data locally — there is no external service to configure, no API key, and no authentication.

## Usage in templates

After deploying and configuring Mocktopus, assign it as the data source on a Smart Template variable.

1. Open your template in GraFx Studio.
2. Select a variable and set its **Data source** to your Mocktopus connector instance.
3. Map the variable to the relevant schema field (e.g. `firstName`, `status`).
4. Switch to **Run mode** to preview the template with generated mock data.

### Generating a schema from an existing template

If you have a GraFx template with variables already defined, use the `ConvertTemplateToSchema.ps1` PowerShell script to automatically generate a ready-to-paste schema string. You can find the script in the [connector's repository](https://github.com/chili-publish/studio-connector-framework/blob/main/src/connectors/mocktopus/ConvertTemplateToSchema.ps1).

**Requirements:** PowerShell 7+ (`pwsh`)

```powershell
# Basic usage — prints the schema to the terminal
.\ConvertTemplateToSchema.ps1 -TemplatePath .\template.json

# Save output to a file and include read-only variables
.\ConvertTemplateToSchema.ps1 -TemplatePath .\template.json -OutputPath .\schema.txt -IncludeReadonly
```

The script maps all standard GraFx variable types (`shortText`, `longText`, `number`, `boolean`, `date`, `list`, `image`) directly to their Mocktopus DSL equivalents. Variables with unrecognised types are skipped with a warning.

### Example schema for a product card template

```
productName:shortText(numberOfWords=3), description:longText(numberOfParagraphs=1), price:number(min=5,max=500), inStock:boolean, category:list(values=Electronics|Clothing|Food|Sports), photo:image
```
