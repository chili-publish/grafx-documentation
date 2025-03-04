# Google Sheets Data Connector

:fontawesome-regular-square: Built-in  
:fontawesome-regular-square-check: Built by CHILI publish  
:fontawesome-regular-square: Third Party

[See Connector types](/GraFx-Studio/concepts/connectors/#types-of-connectors)

## Installation

[See installation through Connector Hub](/GraFx-Studio/guides/connector-hub/)

You can deploy multiple instances of the connector, each with different settings.

## Configuration

### Base Configuration

Once installed, navigate to the **Connector overview**, and select your deployed **Google Sheets** connector. Start with **Configuration**.

![screenshot-full](config.png)

- **Name**: Choose a name to distinguish your connector setup.
- **Description**: Give more context what this connector does, what is specific about it.
- **Version**: If available, choose the version you want to use.
- **Proxy settings**

```html
https://sheets.googleapis.com
```


### Authentication

To authenticate with Google Sheets, you need to provide credentials.

You can configure **Server Authentication** and **Browser Authentication** separately or use a single setup for both.

![screenshot](separate.png)

- **Server Authentication** Always required: defines the method on how the CHILI GraFx Server will talk to the Google Sheets server
- **Browser Authentication** Optionally, you can define how the browser needs to talk to Google Sheets, to pull data in

### 1. Server Authentication

Server authentication is Always required.

For the server authentication, you will need to setup a service account.

#### Google setup

!!! warning "Disclaimer"
    How to setup the **Service Account** on Google Cloud might change over time.

Go to [Google Cloud Console](https://cloud.google.com/iam/docs/service-accounts-create).

Go to API and Services

![screenshot](google07.png)

Go to Credentials, and create a new Service account. Go through all steps.

![screenshot-full](google08.png)

You now have the Service Account credentials.

![screenshot-full](google02.png)

If you have not done during the initial creation, go to the created credentials, and add a private KEY.

Create a private key, in the **Keys** section.

![screenshot-full](google04.png)

Choose JSON format

![screenshot](google05.png)

After confirmation, a JSON file will be downloaded to your computer. (see example below)

![screenshot-full](google06.png)

#### JSON

Below is an example (where **actual credentials have been removed** for security). Below, we'll refer to parts of that JSON to use in the setup.

``` json
{
  "type": "service_account",
  "project_id": "your-project-name",
  "private_key_id": "2d7f5c97ccae8465e708bc...",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADqsdfkjqmsdlkfjmsqdkfjtyTXDMR\n42AQ7VJsIxnPM5FUZx8xzRNMVDQakle5Ksi6zFeZr3/Nrh20yXp0iYXtkLqNTvAD\n5Q5L2zATHx2nvlRxJcCwehxdWW58KubHvdyaN2uQMdxj8idr964LhW53bpgKK6vg\nygdMnY8i+X6++9eaqlyf+MXsckN5Qrk15AigEcJlCStLHE7D9xD+ivXMgUwFpXU+\n...\nXwbYE9GufVHVtvXz573fQcQzrPJ5ifjoZ+hDpfpT9ZOfMO1zA/HzOlxfUN9XF2Kc\njfFdOCixWLT6HuKeOb0GH1eo\n-----END PRIVATE KEY-----\n",
  "client_email": "google-generated-address@your-project-name.iam.gserviceaccount.com",
  "client_id": "123456789123456798",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/yourname%40yourproject-grafx.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

```


![screenshot-full](auth_1.png)

- **Authorization method**: Select the required authentication method.
- **Separate or same method**: Enable to configure different methods for Server and Browser authentication.

![screenshot](separate.png)

- **Token endpoint**:  
see [JSON](#1-server-authentication): **token_uri**  
```html
https://oauth2.googleapis.com/token
```
- **Issuer**: Provide the email address of the service account.  
see [JSON](#1-server-authentication): **client_email**
- **Signing algorithm**: JWT Bearer token requires RS256 algorithm.
- **Private Key**: Provide the PEM-formatted private key.  
see [JSON](#1-server-authentication): **private_key**
You can copy-past the full contents, leaving in the "\n". They will be replaced when you save your settings.  
Once provided, we will never show the private key again.  
PS: With each change, you will have to re-enter the private key.

!!! warning "Stop here"
    No need to setup **Browser authentication**, if the system can use the service account for both Server and Browser authentication.
    Only if you need a different way to authenticate in the Browser, then continue on 2.

### 2. Browser Authentication or Impersonation

Create Client ID credentials on [Google Cloud Console](https://cloud.google.com/iam/docs/service-accounts-create)

Important to set an **Authorised redirect URI**

![screenshot-full](google03.png)

It should be set to this URI

``` json
https://{ENVIRONMENT}.chili-publish.online/grafx/api/v1/environment/{ENVIRONMENT}/connectors/{CONNECTOR_ID}/auth/oauth-authorization-code/redirect
```

Set the {ENVIRONMENT} to your Environment Key.

Where is the Environment Key?

Open Publisher, and take the Key from the URI, it's the first element.

![screenshot](google10.png) 

Below is an example, your Environment Key will be unique to your setup.

![screenshot](google11.png) 

Set the {CONNECTOR_ID} to the ID of your Connector Instance

You can grab the connector ID from the URI, if you are in the Connector setup (in CHILI GraFx)

![screenshot](google12.png)

![screenshot-full](google09.png)

At the end, you'll get a JSON file. We'll refer to elements in the setup below.

A **modified** example to use as reference: [^1]

[^1]: Goes without saying, these settings will NOT work, you need to make your own.

``` json
{
"web":
    {
    "client_id":"123456789.apps.googleusercontent.com",
    "project_id":"your-project-id",
    "auth_uri":"https://accounts.google.com/o/oauth2/auth",
    "token_uri":"https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
    "client_secret":"ABCDEF-_DEF123456HIJKLM"
    }
}
```


![screenshot-full](auth_2.png)

**OAuth 2.0 Authorization Code**

- **Client ID**:  
see [JSON](#2-browser-authentication-or-impersonation): **client_id**  

- **Client Secret**:  
see [JSON](#2-browser-authentication-or-impersonation): **client_secret**  

- **Authorization endpoint**:  
see [JSON](#2-browser-authentication-or-impersonation): **auth_uri**  
Set the endpoint to:  
The below endpoint includes 2 extra parameters  
``` html
https://accounts.google.com/o/oauth2/v2/auth?access_type=offline&include_granted_scopes=true
```  
!!! info "Extra URL parameters"
	**access_type**=offline
	This ensures that the application can continue to access the Google API even when the user is not actively using it. It allows the system to receive a refresh token, which can be used to get a new access token without requiring the user to log in again.
	
	**include_granted_scopes**=true
	If the user has already granted permission for certain scopes in a previous authentication, this setting ensures that those permissions are retained. This way, the user doesn’t have to approve the same access every time they log in.

- **Token endpoint**:  
see [JSON](#2-browser-authentication-or-impersonation): **token_uri**  
``` html
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
    - Format Date as "Date" or "Date Time"  
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

Ensure the **Data source** is enabled for batch processing.

![screenshot](output.png)

!!! note "PDF only"
    Only PDF output will use the data source. Soon the other formats will support batch output too.

When set to "Use data source", your output will have a page for each record in the data source.

![screenshot-full](output2.png)