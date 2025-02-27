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

### Authentication

To authenticate with Google Sheets, you need to provide credentials.

You can configure **Server Authentication** and **Browser Authentication** separately or use a single setup for both.

![screenshot](separate.png)

- **Server Authentication** Always required: defines the method on how the CHILI GraFx Server will talk to the Google Sheets server
- **Browser Authentication** Optionally, you can define how the browser needs to talk to Google Sheets, to pull data in

### 1. Server Authentication

Server authentication is Always required.

![screenshot-full](auth_1.png)

- **Authorization method**: Select the required authentication method.
- **Separate or same method**: Enable to configure different methods for Server and Browser authentication.

![screenshot](separate.png)

- **Token endpoint**: https://oauth2.googleapis.com/token
- **Issuer**: Provide the email address of the service account. (Created via [Google Cloud Console](https://cloud.google.com/iam/docs/service-accounts-create))
- **Signing algorithm**: JWT Bearer token requires RS256 algorithm.
- **Private Key**: Provide the PEM-formatted private key.  
Once provided, we will never show the private key again.

### 2. Browser Authentication or Impersonation

![screenshot-full](auth_2.png)

**OAuth 2.0 Authorization Code**

- **Client ID** and **Client Secret**: In your Google API console, create an application and use the provided Client ID and Secret.
- **Authorization endpoint**: Set the endpoint to:
``` html
https://accounts.google.com/o/oauth2/v2/auth?access_type=offline&include_granted_scopes=true
```
- **Token endpoint**: Set the endpoint to:
```html
https://oauth2.googleapis.com/token
```
- **Scope**: Provide the scope: 
``` html
https://www.googleapis.com/auth/spreadsheets.readonly
```

For more details, refer to [Google Developers](https://developers.google.com/identity/protocols/oauth2).

## Google Sheet data in a Smart Template

### Different Sheet per Template

Each Smart Template can link to a different Google Sheet. You can even make the link dynamic using variables.

![screenshot](datasource.png)

![screenshot](sheetsetup.png)

This setup allows you to configure authentication at the instance level while linking to different sheets per template.

![screenshot-full](instance.png)

### Google Sheet Setup guidelines

- **Column Range**: Only columns from A to Z are used.
- **Header**: Your Google Sheet column names must match the Smart Template variable names
- **Column Data Type**
    - All values are considered: "Single Line Text"
    - Format Numbers as Numbers  
    ![screenshot](format_number.png)
    - Format Date as Date or Data Time  
    ![screenshot](format_date.png)
    - Booleans: Boolean columns must always have a value (cells cannot be empty)
    - Booleans: Define boolean columns using checkboxes  
    ![screenshot](format_boolean.png)
- **Row Structure**: The sheet must **NOT** contain empty rows between rows with data  
![screenshot](format_empty.png)
- **Sharing**  
**OAuth2.0 JWT Bearer authentication**: Share it with the service account setup during configuration of the Connector.  
**OAuth2.0 Authorisation Code**: share with the user who is authorising.  
**Public**: All people with the link can access your document. You can set it to read-only or editable.  

## How to Use Google Sheets Data

For this example, we'll use a [publicly available document](https://docs.google.com/spreadsheets/d/1ApwDcYH6CK5pXjKEbTe5Ie-Y2wVsrHxJoKKN8x4Xd_w/edit?usp=sharing).

![screenshot-full](sheet.png)

#### Create Variables

- In your template, create variables corresponding to the column names in Google Sheets.
- As long as the names match and a data source is connected, the values will be populated automatically.

![screenshot](variables.png)

#### Link the Google Sheet

- Select the Connector Instance (for the right Authentication method)

![screenshot](datasource.png)

![screenshot](connector.png)

- Copy the link of the [public document](https://docs.google.com/spreadsheets/d/1ApwDcYH6CK5pXjKEbTe5Ie-Y2wVsrHxJoKKN8x4Xd_w/edit?usp=sharing).
- Paste it into the data source field.

![screenshot](sheetsetup.png)

#### Preview in Run Mode or Studio UI

- In [Run mode](/GraFx-Studio/concepts/design-run/#run-mode) or the [Studio UI](/GraFx-Studio/concepts/template-management/#studio-ui), you can browse records to preview how content changes.

#### Run Mode (in Studio Workspace)

![screenshot-full](runmode.png)

#### Studio UI

![screenshot-full](studioui.png)

## Output

To generate output with dynamic data, create an [output setting](../../guides/output/settings/#data-source).

Ensure the **Data source** is enable for batch processing.

![screenshot](output.png)

When set to "Use data source", your output will have a page for each record in the data source.

![screenshot-full](output2.png)