# Google Sheets Data Connector

|  | Connector type |
| --- | --- |
|  | Built-in |
| :fontawesome-regular-square-check: | Built by CHILI publish |
|  | Third party |

[See Connector types](/GraFx-Studio/concepts/connectors/#types-of-connectors)

## Installation

[See installation through Connector Hub](/GraFx-Studio/guides/connector-hub/)

You can deploy multiple instances of the connector, each with different settings.

## Configuration

### Base Configuration

Once installed, navigate to the **Connector overview**, and select your deployed **Google Sheets** connector. Start with **Configuration**.

![screenshot-full](config.png)

Consult your IT Admin who manages your Google Workspace to obtain the correct values for the fields.

### Authentication

To authenticate with Google Sheets, you need to provide credentials.

You can configure **Server Authentication** and **Browser Authentication** separately or use a single setup for both.

![screenshot](separate.png)

- **Server Authentication** allows the system to act as a service account, so the end-user does not need to authenticate when using the Smart Template.
- **Browser Authentication** requires users to authenticate and log in with their credentials.

### 1. Server Authentication

![screenshot-full](auth_1.png)

- **Authorization method**: Select the required authentication method.
- **Separate or same method**: Enable to configure different methods for Server and Browser authentication.

![screenshot](separate.png)

- **Token endpoint**: https://oauth2.googleapis.com/token
- **Issuer**: Provide the email address of the service account.
- **Signing algorithm**: Specify the algorithm to sign the JWT token.
- **Private Key**: If applicable, provide the PEM-formatted private key.

### 2. Browser Authentication or Impersonation

![screenshot-full](auth_2.png)

- **Authorization method**: Select the required authentication method.
- **Client ID** and **Client Secret**: In your Google API console, create an application and use the provided Client ID and Secret.
- **Authorization endpoint**: Provide the Google Authorization URL.
- **Token endpoint**: Provide the Google token endpoint.
- **Scope**: Enter one or more scopes required for authentication.

For more details, refer to [Google Developers](https://developers.google.com/identity/protocols/oauth2).

## Using Data from Your Google Sheet in a Smart Template

### Different Sheet per Template

Each Smart Template can link to a different Google Sheet. You can even make the link dynamic using variables.

![screenshot](datasource.png)

![screenshot](sheetsetup.png)

This setup allows you to configure authentication at the instance level while linking to different sheets per template.

### How to Use Google Sheets Data

!!! important
  Your Google Sheet column names must match the Smart Template variable names.

For this example, we'll use a [publicly available document](https://docs.google.com/spreadsheets/d/1cJDWEjmP76YVEA31Ir4n8usVDc1ytYBav6w4a9p4TBM/edit?usp=sharing).

![screenshot-full](sheet.png)

1. **Create Variables**  
 - In your template, create variables corresponding to the column names in Google Sheets.
 - As long as the names match and a data source is connected, the values will be populated automatically.

![screenshot](variables.png)

2. **Link the Google Sheet**  
 - Copy the link of the [public document](https://docs.google.com/spreadsheets/d/1cJDWEjmP76YVEA31Ir4n8usVDc1ytYBav6w4a9p4TBM/edit?usp=sharing).
 - Paste it into the data source field.

![screenshot](sheetsetup.png)

3. **Preview in Run Mode or Studio UI**  
 - In [Run mode](/GraFx-Studio/concepts/design-run/#run-mode) or the [Studio UI](/GraFx-Studio/concepts/template-management/#studio-ui), you can browse records to preview how content changes.

#### Run Mode (in Studio Workspace)

![screenshot-full](runmode.png)

#### Studio UI

![screenshot-full](studioui.png)

## Output

To generate output with dynamic data, create an [output setting](/GraFx-Studio/concepts/output-settings/).

Ensure the **data source is enabled** for processing.

!!! info
  The exact name of this setting is to be confirmed.

To process the Google Sheets data via the [API](https://sandbox1.chili-publish-sandbox.online/grafx/swagger/index.html#/Output/post_api_v1_environment__environment__output_settings_pdf), set `"dataSourceEnabled": true`.

## Supported Variable Types

Currently, the Google Sheets connector supports:

- **Text variables**[^1]

[^1]: Using a simple action, you can assign the text variable (containing an image name) to an image variable. **GraFx Genie** can assist in automating this.  
![screenshot](action.png)