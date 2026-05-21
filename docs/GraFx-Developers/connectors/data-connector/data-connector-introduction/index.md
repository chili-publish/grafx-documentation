# Data Connector Introduction

GraFx Studio provides Data Connectors as a powerful way to integrate external data sources into your templates. Data Connectors enable you to dynamically populate your templates with data from various sources such as databases, APIs, or other data services.

Data Connectors are particularly valuable for creating dynamic templates that can be populated with real-time or frequently updated data. This integration allows for the creation of personalized and data-driven documents while maintaining a consistent design.

## Examples of Data Connectors

CHILI publish and our community have developed several Data Connectors to enhance the functionality of GraFx Studio. Some common use cases include:

- [Google Sheets Connector](/GraFx-Studio/connectors/connector-google-sheets-data/): Import data from spreadsheet files

## Tutorial Sequence

For those new to building Data Connectors, we recommend following this structured learning path.

### Output Data Source

For batch and variable-data-printing workflows where Studio iterates forward through every row of the source.

1. [Data Connector Fundamentals](/GraFx-Developers/connectors/data-connector/data-connector-fundamentals/): Learn the basic concepts and architecture of Data Connectors.
2. [Build a Simple Data Connector](/GraFx-Developers/connectors/data-connector/build-a-simple-data-connector/): Create your first Data Connector with step-by-step guidance.

### Data Source Variable

For templates where an end user (or API caller) picks a single row to populate the document, with forward/backward navigation and lookup by row ID.

1. [Data Connector Fundamentals — Data Source Variable use case](/GraFx-Developers/connectors/data-connector/data-source-variable/data-source-variable-fundamentals/): Bidirectional paging, `getPageItemById`, and `DataSourceVariableDataModel`.
2. [Build a Data Connector — Data Source Variable use case](/GraFx-Developers/connectors/data-connector/data-source-variable/build-a-data-source-variable-connector/): Implement the `dataSourceVariable` capability on an existing connector.

## Reference Documentation

To deepen your understanding and for quick access to specific information, refer to these resources:

- [Authorization for Connectors](/GraFx-Developers/connectors/authorization-for-connectors/): Understand the authentication and authorization processes for secure connector integration.
- [Connector CLI](/GraFx-Developers/connectors/connector-cli/): Learn about the Command Line Interface tools available for connector development and management.