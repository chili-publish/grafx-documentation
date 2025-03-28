# Data Connectors

A **Data Connector** simplifies the creation of graphics and digital assets by automatically pulling information from an external system into GraFx Studio. This allows you to personalize and scale content without manually entering data.

As an end-user, you can access centrally brand-managed data with ease. Data Connectors also enable fully automated content creation, driving content generation at scale.

Connectors can be used in **[self-service](/GraFx-Studio/concepts/self-service/)** or **[headless](/GraFx-Studio/concepts/headless/)** workflows.

## Making Data Available for the End-User

In the **Data Source** panel (under **Resources**) on the left in GraFx Studio, a Template Designer can browse the available Data Connectors. 

Multiple connectors can be deployed. One setup might require a different authentication method. This can be done by deploying multiple instances of the Google Sheets connector, each with different parameters.

![screenshot-full](data01.png)

![screenshot-full](data02.png)

The data of that data source is now available, and will populate the variable values in the document.[^1]

[^1]: See Data Connector specifics on how to setup

## Handling Data Exceptions

In an ideal world, your data would be flawless and work perfectly for every record. However, the Data Connector Framework is designed to help manage situations when the data from your source is less than perfect.

### For Empty and Invalid Values in the Data Source

- The corresponding variable value in GraFx Studio is cleared.
- For different variable types:
    - **Text Variable**: Set to an empty string.
    - **List Variable**: No item is selected.
    - **Image Variable**: No image is shown.
    - **Date Variable**: No date is set.
    - **Number or Boolean Variable**: An error is flagged (invalid variable value).
- When a data source cell is invalid, an error is triggered (invalid variable value).

### For Required Variables in the Template

- If a data source cell for a required variable is empty, the variable value will be cleared, resulting in an error for that record (missing variable value).
- If a required variable is not mapped to any column in the data source, the variable value remains unchanged:
    - **No error** if the variable already has a value.
    - **Error** if the variable value is empty.

A template default value or an action may influence this behavior. Similarly, if a required variable is absent from the API request body, no error occurs if the variable already has a default value in the template.

### Error Handling

See also [Error Report in Output Tasks](/GraFx-Studio/concepts/output-tasks/#accessing-the-output-task-list).

#### Output

- All variables of a record are applied.
- If one or more errors occur, the entire record fails.
- The error report details all errors for each processed record.

### In Studio UI

- All variables of a record are applied.
- For **Text**, **List**, **Image**, and **Date Variables**:
    - If there is no value in the data source, the variable is cleared and an error state is triggered if the variable is required.
    - If an invalid value is detected, the variable is cleared and an error state is triggered (if required), with a toast message stating: “[Variable label] is invalid. The value is cleared.”
- For **Number** and **Boolean Variables**:
    - If no value is provided, the default variable value is used, and a toast message displays: “[Variable label] is invalid. A default value is used.”
    - If an invalid value is detected, the default variable value is used, with a similar toast message.
    - For numbers, the default value "0" is used if it falls within the min/max range; otherwise, the closest limit is used.
    - For booleans, the default value is **False**.

In toast messages, the reference to the variable will use the **label** if it exists; otherwise, it will use the **variable name**.