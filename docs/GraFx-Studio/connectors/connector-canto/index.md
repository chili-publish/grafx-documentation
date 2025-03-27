# Media Connector for Canto

:fontawesome-regular-square: Built-in  
:fontawesome-regular-square: Built by CHILI publish  
:fontawesome-regular-square-check: Third Party

[See Connector Types](/GraFx-Studio/concepts/connectors/#types-of-connectors)

## Installation

As no "installation" happens, you could also talk about deployment of a connector on your environment.

[See Installation Through Connector Hub](/GraFx-Studio/guides/connector-hub/)

## Canto Configuration 

Consult your [Canto documentation](https://support.canto.com/hc/en-us/articles/23002535539601-Generating-API-Keys) or Canto System Admin to obtain the correct values for the fields.

## CHILI GraFx Connector Configuration 

From the overview of Environments, click on "Settings" on the right to your environment, where you want to install or configure the Connector.

![screenshot-full](sch13.jpg)

Then click the installed Connector to access the configuration.

![screenshot-full](sch12.png)

### Configuration

Your instance of the Connector needs to know which Canto instance it should communicate with and how to authenticate.

![screenshot-full](sch01.png)

**baseURL**

Your Canto System Administrator will provide you with this information.

For example

```html
https://[your-domain].canto.global
```

**Proxy settings**

CHILI GraFx needs to know what domains are allowed to process

For example

```html
*.canto.global
```

### Authentication

![screenshot-full](sch02.png)

Select your type of authentication:

**Server and Browser:** OAuth 2.0 Client Credentials

- **Client ID** and **Client Secret**: These are [customer-specific credentials](https://support.canto.com/hc/en-us/articles/23002535539601-Generating-API-Keys#How-to-generate-API-keys) provided by the Canto Admin.
- **Token Endpoint**:  
```html
https://oauth.canto.global/oauth/api/oauth2/compatible/token
```

- **Scope**: Consult your Canto Admin to determine the appropriate scope.

Consult your Canto System Admin for assistance in configuring these fields.

## Using Assets from Your Canto Dam

### Place Assets in Your Template

- Select the Canto Connector.

![screenshot-full](sch07.png)

![screenshot-full](sch08.png)

![screenshot-full](sch09.png)

Depending on the configuration, you may need to authenticate.

![screenshot-full](sch10.png)

- Once authenticated, Sitecore assets behave like any other asset in GraFx Studio.

### Image Variables

When using [image variables](/GraFx-Studio/guides/template-variables/assign/#assign-template-variable-to-image-frame), you will see the same list of assets when selecting an image.

![screenshot-full](var01.png)

### Configuration Options

#### Introduction

To filter the assets suggested to template users, you can use categories, keywords, or other search parameters.

Canto supports search queries through its query language. Consult the [Sitecore Documentation](https://doc.sitecore.com/ch/en/developers/cloud-dev/generic-properties.html) or your Canto Administrator for guidance.

#### How To

Queries are set at the variable level.

Set the query value in the connector settings.

![screenshot-full](var02.png)

For more dynamic queries, you can use [variables](/GraFx-Studio/concepts/variables/), [actions](/GraFx-Studio/concepts/actions/), and [GraFx Genie](/GraFx-Studio/concepts/grafx-genie/) to automate and refine your queries.

#### Other Configuration Options

- **Show Only Approved Assets**: Displays only assets that have been approved in Canto.
- **Locale**: Filters assets by region or language.