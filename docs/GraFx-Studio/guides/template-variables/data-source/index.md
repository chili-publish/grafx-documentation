# Data source variables

A **data source variable** holds a table of records and remembers which one is selected. Instead of typing a product name, price and description into three separate variables, the end user picks one row — "Apple, 0.60 euro" — and everything mapped to that data source updates at once.

The records come from an external system, and the variable keeps only a reference to the selected row. That makes it the right tool for self-service work: pick your store, pick your product, get your poster.

!!! info "Template Variables"
    When referring to **variables** we can mean **[Template variables](/GraFx-Studio/concepts/variables/#template-variables)** or **[JavaScript variables](/GraFx-Studio/concepts/variables/#javascript-variables)**. On this page we are talking about Template variables.

## Not the same as an output data source

A template can also have an **output data source**, which looks similar but does a different job. The distinction matters, because picking the wrong one leads to a template that produces one output when you wanted five hundred, or the reverse.

| | Output data source | Data source variable |
|---|---|---|
| **What it does** | Iterates over every row to drive a batch of outputs | Holds one selected row, used inside a single document |
| **Drives output** | Yes — one output per row | No |
| **Navigation** | Forward through all rows | Browse, and one row stays selected |
| **Typical use** | Variable data printing: 500 personalised mailers | Self-service: pick a product, get a poster |

A template can use both together. See [Data connectors](/GraFx-Studio/concepts/connectors-data/) for the output data source.

## Where the data comes from

A data source variable is populated in one of two ways, chosen per variable:

- **Connector** (default) — GraFx Studio *pulls* the data through a [data connector](/GraFx-Developers/connectors/data-connector/data-connector-introduction/). Use this when the data lives in a system you can reach: a PIM, a CRM, a spreadsheet, an API.
- **Data injection** — an integration *pushes* the data in via the SDK. Use this when the surrounding application already has the data in hand and routing it through a connector would be a detour.

Both end up in the same place: a table of rows with a selected row. Only the plumbing differs.

## Create a data source variable

Open the variables panel from the properties panel on the right (the wrench & screwdriver tool), then choose **Variables** — the same starting point as [defining any template variable](/GraFx-Studio/guides/template-variables/define/).

Add a variable and set its **Type** to **Data source**. The General tab then shows:

- **Required** — optional toggle. It can only be switched on once the variable actually has a source: either a connector is selected (not `[None]`), or the source is set to Data injection.
- **Data source** — **Connector** or **Data injection**.

The action button below changes with that choice.

<!-- TODO Bram: screenshots needed for the General tab in both modes. Zeplin refs are on PRODUCT-769. -->

### Connector

Choosing **Connector** shows a **Configure connector** button, which takes you to the **Connector** tab. There you:

1. Pick the connector from the **Select connector** dropdown.
2. Fill in the **configuration options**. These are dynamic — the connector declares them, so what you see depends on the connector. Commonly a search or query parameter, an endpoint, or a record type.

Each configuration field can be set to a **static value** or **linked to another variable** — the same pattern used for media connectors. Linking a field to a variable is what makes cascading selection possible: when the linked variable changes, the query re-runs and this variable's rows change with it.

!!! info "The connector must support this use case"
    Support for data source variables is an **opt-in extension** a data connector has to implement explicitly. A connector built only for batch output will not appear in the dropdown. If one is missing, check that it declares the capability and that it is enabled on your environment — see [Data Connector Fundamentals — Data Source Variable use case](/GraFx-Developers/connectors/data-connector/data-source-variable/data-source-variable-fundamentals/).

### Data injection

Choosing **Data injection** hides the Connector tab entirely and shows a **Manage fields** button instead.

Because nothing is pulling data, GraFx Studio cannot discover the shape of it. You have to declare it. In the **Manage fields** modal, add one field per column with a **Name** and a **Type**:

- Single-line text
- Multi-line text
- Number
- Boolean
- Date

At least one field is needed before List mode can be configured.

Two rules govern what happens when the pushed data doesn't match the schema:

- Extra fields in the incoming data are **ignored**.
- A declared field that is missing from the incoming data is left **empty** for every row.

!!! tip "Testing an injection variable"
    There is no data to pull, so a template using data injection will look empty in the designer workspace until an integration pushes rows in. Plan for how you will test — the values only appear once the surrounding application supplies them.

## Choose how the end user sees it

On the **User interface** tab, **Show variable as** controls the end-user presentation:

- **Table** (default) — the end user opens a table of all rows and clicks one, much like the output data source table. Nothing else to configure.
- **List** — the end user picks from a simple list. Because a list shows one line per row, you must choose which column supplies that line.

When you select **List**, a **Display column** dropdown appears. Pick the column to use as the visible label.

If the data source is not configured yet, that dropdown is **disabled**, with the message *"Configure your data source to enable display column selection."* Configure the connector or declare your injection fields first, then come back.

!!! note "If the data model changes"
    Change the source and GraFx Studio tries to keep your choice. If the new data model still contains the column you picked, the selection is preserved. If it doesn't, the display column is *not* silently reassigned — the dropdown returns to its placeholder state and you choose again.

The tab also carries the usual presentation fields, which work as they do for every other variable type: **Label**, **Placeholder**, **Help text**, and **Visibility** (default **Always**). See [Variable settings](/GraFx-Studio/guides/template-variables/define/#variable-settings).

<!-- TODO Bram: screenshots for Table mode, List mode, and the disabled Display column tooltip. -->

## Default state

The **Default state** section is where you set which row is selected when someone opens the template.

In the designer workspace, GraFx Studio does **not** fetch data automatically. You trigger the fetch, browse the rows with the **previous** and **next** controls, and the row you land on becomes the default row stored in the template.

From then on:

- Opening a project **with** a default row selects that row.
- Opening a project **without** one fetches and selects the first row.

<!-- TODO Bram: confirm the exact fetch trigger in Default state — is it a button, or does opening the table modal fetch? -->

## How it behaves

### The data is live, not a snapshot

This is the behaviour most likely to surprise people, so it's worth being explicit about.

!!! warning "Data refreshes on every open"
    A data source variable stores a reference to the selected **row**, not a copy of its values. The data is refreshed **every time the template or project is opened**, and again whenever a query parameter or a variable linked to one changes.

    So if a price is 0.56 when a project is saved and 0.60 in the source system two days later, reopening that project shows **0.60**. There is no snapshot mode. If you need values frozen at a point in time, that has to be handled on the data supply side — by publishing a stable, versioned dataset rather than a live one.

### The selected row survives a refresh

Refreshing the data would be disruptive if it reset the user's choice, so GraFx Studio tries to hold onto it. This happens per project as well as in the template, so two projects from the same template keep their own selections.

Behaviour on refresh:

- The selected row is looked up again and stays selected — even if it has moved to a different position in the table.
- If it can no longer be found, the selection falls back to the **first row**.
- If the source returns no data at all, there is **no** selected row.

How the row is identified depends on the source. Connectors that expose a stable row ID are matched on that ID. Sources without one — a plain spreadsheet, for instance — fall back to position, which means a refresh that reorders rows can land the user on different data.

<!-- TODO Bram: worth naming Google Sheets explicitly here as a position-based example, or is that too implementation-specific for public docs? -->

### Using the selected row in the design

The data source variable itself only holds the table and the selection — it does not place values on the canvas. The selected row is read by whatever is configured to consume it, and changing the selection refreshes those consumers automatically, in the designer workspace and in My Projects alike.

If no row is selected, the first row is used. If the source is empty, consumers render empty values.

<!-- TODO Bram: this section is deliberately vague because PRODUCT-770 (mapping component variables to data source columns) was still In Progress and is not publicly available yet. Once it ships, expand this with the mapping workflow, the runtime read of [selected row, mapped column], and the error cases (mapped column removed, fetch failed, data source variable deleted while mapped). Likely the REL note's job. -->

<!-- TODO Bram: Preview mode (a third "Show variable as" option rendering each row with a component) is also left out — postponed on performance grounds per PRODUCT-769. Re-add when it ships. -->

### When the data fetch fails

The variable shows an error and offers a retry. It does not silently fall back to previously loaded values — an error state is better than a design that looks correct but is showing yesterday's prices.

### Empty and invalid values

Values that arrive empty or invalid follow the standard data exception rules, the same ones that apply to an output data source: text, list, image and date variables are cleared, while number and boolean variables fall back to their default with a toast message. See [Handling data exceptions](/GraFx-Studio/concepts/connectors-data/#handling-data-exceptions).

### In output

A data source variable does **not** turn one document into a batch. One selected row produces one output, rendering exactly what was on screen. For batch production across many rows, use an output data source.

If a required data source variable has no selection at output time, the output fails and the reason appears in the error report on the output task page. See [Output tasks](/GraFx-Studio/concepts/output-tasks/).

## Example: cascading selection

Three dropdowns, each backed by its own data source variable in List mode.

The first lists regions. Its selected row feeds a query parameter on the second variable, which lists the stores in that region. The second feeds the third, which lists the products stocked by that store. Each selection narrows the next, because the query parameter on each variable is linked to the one before it rather than set statically.

This works precisely because data refreshes when a linked variable changes — the second and third lists re-query themselves rather than going stale.

## Related

- [Data connectors](/GraFx-Studio/concepts/connectors-data/) — how data reaches a template, and the output data source
- [Defining template variables](/GraFx-Studio/guides/template-variables/define/) — all variable types and their settings
- [Use components in a template](/GraFx-Studio/guides/use-components/) — placing components and mapping their variables
- [Data Connector Fundamentals — Data Source Variable use case](/GraFx-Developers/connectors/data-connector/data-source-variable/data-source-variable-fundamentals/) — the developer side
- [Build a Data Connector — Data Source Variable use case](/GraFx-Developers/connectors/data-connector/data-source-variable/build-a-data-source-variable-connector/) — adding the capability to an existing connector
