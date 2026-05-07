# How to use Supabase data

Once the [connector is configured and authenticated](../#configuration) and your [Supabase project is ready](../supabase-setup/), you can bind the connector to a Smart Template. Each binding picks **what** to read from Supabase and **how**.

## Bind the connector in your template

In your template, open the **Data source** panel and select your Supabase connector instance. The binding accepts a small set of options:

| Option | When to set it | What it does |
|---|---|---|
| `queryMode` | always | `rpc` (default) or `view`. Picking `view` requires an admin to have set `ALLOW_TABLE_VIEW` to `true` on the connector. |
| `targetName` | always | The function name (rpc) or the table/view name (view). |
| `idColumn` | view mode | The primary key column. Defaults to `id`. The connector uses it to look up single rows. |
| `rpcParams` | rpc mode | A JSON object passed as the function arguments, e.g. `{"campaign_slug":"spring-fresh"}`. |
| `columnsOverride` | optional | A JSON array of column definitions, e.g. `[{"name":"foo","type":"singleLine"}]`. Use this when auto-discovery can't infer the schema — typically when an rpc function returns no rows for the default parameters. |

## Example: binding to an rpc function

Using the `get_campaign_products` function from [Prepare your Supabase project](../supabase-setup/#for-rpc-mode-create-a-postgres-function):

- **`queryMode`**: `rpc`
- **`targetName`**: `get_campaign_products`
- **`rpcParams`**: `{"campaign_slug":"spring-fresh"}`

The connector calls the function with those arguments and exposes the resulting columns as variables in your template.

## Example: binding to a table

For a `products` table:

- **`queryMode`**: `view`
- **`targetName`**: `products`
- **`idColumn`**: `id`

(plus an admin must have set `ALLOW_TABLE_VIEW` to `true` on the connector — see [Runtime options](../#runtime-options).)

## Preview in Run Mode or Studio UI

In [Run Mode](/GraFx-Studio/concepts/design-run/#run-mode) or the [Studio UI](/GraFx-Studio/concepts/template-management/#studio-ui), you can browse records to preview how your template looks with each row of data.

## Output

To generate output across all records, create an [output setting](/GraFx-Studio/guides/output/settings/#data-source) and enable the **Data source** option. Your output will include one page per record returned by Supabase.

## How column types are detected

The connector tries to figure out column types by itself so designers don't have to spell them out:

- **In `view` mode**, it first reads the auto-generated OpenAPI document from PostgREST and pulls column definitions from there. This is the most accurate path — Postgres types map cleanly to GraFx Studio types.
- **If OpenAPI isn't accessible** (Supabase can lock the OpenAPI doc to the `service_role` in some configurations), the connector falls back to fetching one row of data and inferring types from the values: numbers, booleans, ISO date strings, and everything else as text.
- **In `rpc` mode**, the connector calls the function once with `limit=1` and the supplied `rpcParams`, then samples the first row.

If your rpc function returns no rows for the default `rpcParams`, auto-discovery has nothing to learn from — supply a `columnsOverride` in that case.

### Type mapping

| Postgres type | GraFx Studio type |
|---|---|
| `integer`, `bigint`, `numeric`, `real`, `double precision` | `number` |
| `boolean` | `boolean` |
| `date`, `timestamp`, `timestamptz`, `timestamp with time zone` | `date` |
| everything else (text, varchar, uuid, jsonb, arrays, …) | `singleLine` |

JSON and array values are stringified into a single line of text. Override the type with `columnsOverride` if you want something different.
