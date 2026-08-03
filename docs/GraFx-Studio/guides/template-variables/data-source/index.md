# Data source variables

A **Data source variable** holds a reference to a single record — one row of data — coming from outside the template. The end user picks that record, and every variable mapped to one of its columns updates at once.

!!! info "Data source variable vs. Output data source"
    GraFx Studio has two ways of connecting a template to external data, and they solve different problems.

    | | **Output data source** | **Data source variable** |
    |---|---|---|
    | Purpose | Generate many outputs, one per row | Fill one document from one row |
    | Who selects the row | Nobody — Studio iterates through all of them | The end user, or an integration |
    | Typical use | Variable data printing, batch runs | Self-service: pick a product, a store, a colleague |
    | Where it lives | Output settings and the Data source panel | The variable list, like any other variable |

    Both can be used in the same template. Only the naming changed: what used to be called *Data source* in output settings, Run mode, and Studio UI is now consistently called **Output data source**.

## Create a Data source variable

Under the Automate icon, click **Variables**, and add a variable with the "+" sign. Choose **Data source** as the variable type.

Two decisions follow: where the records come from, and how the end user picks one.

## Choose where the records come from

In the **General** tab, the **Data Source** dropdown offers two options.

### Data Connector

The records are read live from a [data connector](/GraFx-Studio/concepts/connectors-data/) — a Google Sheet, a product API, a CRM.

Select **Data Connector**, then use **Configure your connector** (or the connector tab that appears) to pick the connector instance. Authorization works exactly as it does when an image variable browses a media connector.

!!! warning "Not every data connector qualifies"
    The dropdown only lists connectors that explicitly support the Data source variable use case. A connector built for Output data source alone will not appear, because single-record selection needs capabilities that batch iteration does not: paging backwards as well as forwards, and looking up a row by its ID.

    If a connector you expect is missing, it needs the `dataSourceVariable` capability added. See [Data Connector Fundamentals — Data Source Variable use case](/GraFx-Developers/connectors/data-connector/data-source-variable/data-source-variable-fundamentals/) and [Build a Data Connector — Data Source Variable use case](/GraFx-Developers/connectors/data-connector/data-source-variable/build-a-data-source-variable-connector/) in the Developer Center.

### Data Injection

The records are supplied by an integration at runtime rather than fetched by Studio. Use this when the surrounding application already holds the data and there is no reason to make Studio fetch it again.

Because no connector describes the shape of the data in this case, you describe it yourself. Click **Manage fields** to open the schema editor, add a field per column with its name and type, and click **Done**. The schema is what the rest of the template maps against — mapping dropdowns, the **Display Column** list, and the columns shown in Table mode all read from it.

!!! note "Records arrive at runtime"
    In the Template Designer Workspace no data is injected, so the variable shows **No data available** once a schema is defined, and **No preview available** while it is not. This is expected: the records appear when the integration provides them.

## Choose how the end user picks a record

The **User Interface** tab has a **Show variable as** setting with two options.

### Table

The end user clicks the variable's input and a modal opens showing every column, one row per record, with **previous** and **next** navigation. This is the same experience as an Output data source, with the addition of backwards navigation. Nothing else needs configuring.

Use Table when the end user needs several columns side by side to recognise the right record.

### List

The variable renders as an ordinary dropdown. The end user sees one column — the one you choose in **Display Column** — and more records load as they scroll.

Use List when a single field, such as a product name, identifies the record unambiguously.

!!! tip "Display Column needs a source first"
    **Display Column** stays disabled until the variable knows its columns: a connector must be selected, or a schema defined. Set the data source first, then pick the display column.

The remaining **User Interface** settings — **Label**, **Placeholder**, **Help text**, and **Visibility** — work as described in [User Interface](../define/#user-interface).

## Required

**Required** works as it does for other variables, with one dependency: a Data source variable can only be required once it can actually resolve records. It cannot be switched on while no connector is selected, and if you remove every field from a Data Injection schema, **Required** is switched back off and disabled.

## What the end user sees

In Studio UI and Run mode, the variable renders according to **Show variable as** — a browsable table, or a dropdown that pages as you scroll.

When the template opens, GraFx Studio restores the record that was previously selected. If there is no stored selection, or the record can no longer be found — deleted from the source, or renumbered — the **first available record is selected** instead, so the document is never left in an empty state.

If the variable is configured in a way that cannot resolve any records — no connector selected, or no schema defined — its input is not rendered at all rather than shown broken.

## Use a record to fill a component

The most direct payoff of a Data source variable is filling a [component](/GraFx-Studio/guides/use-components/) from one record. Instead of mapping each component variable to a template variable and then populating those individually, map them straight to the record's columns.

Select the component frame, then click **Manage mapping** in the **Component** section of the properties panel. The button is disabled — with the tooltip *"Select a component to enable mapping."* — until a component is selected.

The **Map component to variables** modal has two tabs, **Not mapped** and **Mapped**. For each component variable, choose what it maps to:

- **Data source column** — pick a Data source variable, then one of its columns
- **Variable** — an existing template variable
- **New variable** — a template variable created for you

Select the checkbox on the rows you want to change, then click **Apply**. **Reset** clears the mappings.

Type compatibility is enforced: a number variable maps only to a numeric column, a date variable only to a date column, and so on. Component **image** variables can be mapped to a text column, which is how imagery is driven from a record — the column holds the image reference.

!!! note "Components cannot own a Data source variable"
    **Data source** is not offered as a variable type inside the component editor. A component receives record data through mapping from the template that places it, which keeps the component reusable across templates with different data sources.

## Keep internal component variables out of the mapping list

Not every variable in a component is meant to be mapped. Intermediate values assembled by an action, or flags driving a visibility condition, only add noise to the parent template's mapping list.

In a component variable's general settings, the **Available for mapping** toggle controls whether the variable is offered to the parent template. It is on by default. Switch it off and the variable becomes internal to the component: it disappears from the mapping list, and any mapping configured earlier is no longer applied.

## Read more

- [Defining template variables](../define/)
- [Use components in a template](/GraFx-Studio/guides/use-components/)
- [Data Connectors](/GraFx-Studio/concepts/connectors-data/)
- [Data Connector Fundamentals — Data Source Variable use case](/GraFx-Developers/connectors/data-connector/data-source-variable/data-source-variable-fundamentals/)
