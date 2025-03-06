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
sheets.googleapis.com
```


### Authentication

To authenticate with Google Sheets, you need to provide [credentials](google-setup/).

You can configure **Server Authentication** and **Browser Authentication** separately or use a single setup for both.

![screenshot](separate.png)

- **Server Authentication** Always required: defines the method on how the CHILI GraFx Server will talk to the Google Sheets server
- **Browser Authentication** Optionally, you can define how the browser needs to talk to Google Sheets, to pull data in

### 1. Server Authentication

Server authentication is Always required.

For the server authentication, you will need to setup a [service account on Google Cloud](google-setup/#service-account).

After confirmation, a JSON file will be downloaded to your computer. (see example below)

Below is an example (where **actual credentials have been removed** for security). Below, we'll refer to parts of that JSON to use in the setup.

``` json
{
  "type": "service_account",
  "project_id": "your-project-name",
  "private_key_id": "2d7f5c97ccae8465e708bc...",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADqsdfkjqmsdlkfjmsqdkfjtyTXDMR\n42AQ7VJsIxnPM5FUZx8xzRNMVDQakle5Ksi6zFeZr3/Nrh20yXp0iYXtkLqNTvAD\n...\nXwbYE9GufVHVtvXz573fQcQzrPJ5ifjoZ+hDpfpT9ZOfMO1zA/HzOlxfUN9XF2Kc\njfFdOCixWLT6HuKeOb0GH1eo\n-----END PRIVATE KEY-----\n",
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
If you come back to change settings, you will not see the private key, for obvious reasons.  
New changes: re-enter the private key again before you save.

### Try it out

To try out your setup, open a test Google Sheets document with public access.

!!! warning "Public data"
    Beware to not share data you would like to keep private, as the sheet will be public to anyone with the link.

![screenshot](google22.png)

![screenshot-full](google23.png)

Now, [add 1 variable to a Smart Template](in-smart-template/#create-variables-in-grafx-studio), and preview in Run Mode.

If that works, the connector works fine.

Later you can tweak the security and permissions on the google side, together with your system admin.

!!! warning "Stop here"
    No need to setup **Browser authentication**, if the system can use the service account for both Server and Browser authentication.
    Only if you need a different way to authenticate in the Browser, then continue on 2.

### 2. Browser Authentication or Impersonation

Create Client ID credentials on [Google Cloud Console](google-setup/#oauth-20-client-id-credentials)

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