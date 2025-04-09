# Credentials for Google Sheets on Google Cloud

## Before you Start

Enable the API!

Find the Settings for Google Sheets, in the [API library](https://console.cloud.google.com/apis/library/browse?inv=1&invt=AbrOXg&q=sheets)

![screenshot](../google20.png)

If the API is enabled, we're all set, if not, **Enable** the API

In the screenshot below, it is already enabled.

![screenshot](../google21.png)

## Service Account

!!! warning "Disclaimer"
    How to setup the **Service Account** on Google Cloud might change over time.

Go to [Google Cloud Console](https://console.cloud.google.com/welcome).

Go to API and Services

![screenshot](../google07.png)

Go to Credentials, and create a new Service account. Go through all steps.

![screenshot-full](../google08.png)

You now have the Service Account credentials.

![screenshot-full](../google02.png)

If you have not done during the initial creation, go to the created credentials, and add a private KEY.

Create a private key, in the **Keys** section.

![screenshot-full](../google04.png)

Choose JSON format

![screenshot](../google05.png)

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

## OAuth 2.0 Client ID Credentials

Go to [Google Cloud Console](https://console.cloud.google.com/welcome)

Choose API and services > Credentials

Start creation of OAuth client ID

![screenshot-full](../google13.png)

Important to set an **Authorised redirect URI**

![screenshot-full](../google03.png)

It should be set to this URI

``` json
https://{ENVIRONMENT}.chili-publish.online/grafx/api/v1/environment/{ENVIRONMENT}/connectors/{CONNECTOR_ID}/auth/oauth-authorization-code/redirect
```

Where: {ENVIRONMENT} = Environment Key

Where is the Environment Key?

Open GraFx Publisher (on CHILI GraFx), and take the Key from the URI, it's the first element.

![screenshot](../google10.png) 

Below is an example, your Environment Key will be unique to your setup.

![screenshot-full](../google11.png) 

Set the {CONNECTOR_ID} to the ID of your Connector Instance

You can grab the connector ID from the URI, if you are in the Connector setup (in CHILI GraFx)

![screenshot](../google12.png)

![screenshot-full](../google09.png)

At the end, you'll get a JSON file. We'll refer to elements in the setup below.

A **secured** example to use as reference: [^1]

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