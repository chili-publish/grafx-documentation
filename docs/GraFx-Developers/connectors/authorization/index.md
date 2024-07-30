# Authorization for Connectors

Connectors support various types of authorization to enable secure integration with external systems. This document outlines the process of adding authorization to a Connector and explains the different authorization types available.

## Adding Authorization to a Connector

To implement authorization in a Connector, follow these steps:

1. Define the authorization usage (browser or server)
2. Specify the authorization type

## Authorization Usage

Connectors are used in two different scenarios:

1. **browser**: Used when Studio is loaded in the browser for Studio editors (e.g., Studio UI) or when using the SDK.
2. **server**: Employed when Studio is loaded on GraFx servers for generating output (e.g., PDF, PNG, GIF).

Therefore, you can define different authorization types for each usage, allowing your Connector to use separate authorization methods for browser and server interactions.

!!! note "Authorization Always Happens on the Server"

	In both cases, the actual request and authorization occurs on the server to prevent token or credential leakage to the frontend. All requests in the browser are proxied through our servers, where the authorization is added.

## Supported Authorization Types

Connectors support four types of authorization:

| Auth Type | Reference | Usage Support | CLI Argument (-at) |
|-----------|-----------|---------------|---------------------|
| Static Header Key | [MDN - Authorization Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) | browser and server | staticKey |
| OAuth Client Credentials | [OAuth - Client Credentials](https://oauth.net/2/grant-types/client-credentials/) | browser and server | oAuth2ClientCredentials |
| OAuth Authorization Code | [OAuth - Authorization Code](https://oauth.net/2/grant-types/authorization-code/) | browser | oAuth2AuthorizationCode |
| OAuth Resource Owner Password | [OAuth - Password Grant](https://oauth.net/2/grant-types/password/) | browser and server | oAuth2ResourceOwnerPassword |

!!! note "Authorization is Optional"

	Authorization is optional for Connectors, and by default no authorization is used. However, please be aware that once authorization is set, there is currently no method to remove it via the CLI.

### OAuth Considerations

1. OAuth responses must comply with the [Access Token Response](https://www.oauth.com/oauth2-servers/access-tokens/access-token-response/) format, with the exception that `expires_in` being mandatory.
2. The `grant_type` for OAuth types is automatically set as per the specification and cannot be configured.
3. `access_token` and `refresh_token` are cached internally for OAuth types. Currently, there's no way to reset them without deleting the Connector.
4. OAuth Authorization Code is user-specific and thus is not useful with an Integration User (which is used outside the GraFx Platform).
5. OAuth Authorization Code is limited to "browser" usage, which may restrict its applicability in certain scenarios. or example, if you wanted to build a connector where unknown users can use their Google Photos, the OAuth Authorization Code will work in the "browser" usage, but there is no way to access the user's photos on the "server" usage during output because Goolge does not support any other authentication types into unknown accounts.

## Setting Up Authorization

You must use the the CLI tool to set up authorization on a Connector. This guide assumes you have a published Connector project and its ID.

### Step 1: Add Supported Authorization Types to package.json

In your Connector project's `package.json` file, add the supported authorization types to the `supportedAuth` property:

```json
{
  "config": {
    "supportedAuth": ["staticKey", "oAuth2AuthorizationCode"]
  }
}
```

The values accepted are the same as the ones in the `-at` agurment in the `set-auth` command. See [Supported Authorization Types](#supported-authorization-types)

!!! note "For Future Use"

	The package config is required by the CLI tool, and in the future is meant to signify to other parties what types of authenitcation your Connector supports.

### Step 2: Add Authorization via CLI

Use the `set-auth` command in the CLI tool:

```bash
connector-cli set-auth \
    --connectorId <connector-id> \
    -e <environment> \
    -b <base-url> \
    -au <auth-usage> \
    -at <auth-type> \
    --auth-data-file <path-to-auth-file>
```

Parameters:
- `--connectorId`: ID of your Connector
- `-e`: Name of your environment
- `-b`: Base URL of your API (including environment name)
- `-au`: Authorization usage (browser or server)
- `-at`: Authorization type (see table in [Supported Authorization Types](#supported-authorization-types))
- `--auth-data-file`: Path to a JSON file with authorization-specific data

!!! tip "Each Usage Can Only Have One Authorization Type"

	In most cases, if you are setting authorization for one usage, you will do so for all usages. You can set the same authorization type for both "server" and "browser." You can also make them different. 
	
	However, you cannot set multiple authorization types for the same usage. Attempting to set, for example, "browser" twice will result in the authorization type for "browser" being overwritten.

### Authorization Data File Requirements

Each authorization type requires specific JSON schema for the `--auth-data-file`:

#### Static Header Key
```json
{
  "name": "string",
  "key": "string",
  "value": "string"
}
```

#### OAuth Client Credentials
```json
{
  "name": "string",
  "clientId": "string",
  "clientSecret": "string",
  "scope": "string",
  "tokenEndpoint": "string"
}
```

#### OAuth Authorization Code
```json
{
  "name": "string",
  "clientId": "string",
  "clientSecret": "string",
  "scope": "string",
  "authorizationServerMetadata": {
    "authorization_endpoint": "string",
    "token_endpoint": "string",
    "token_endpoint_auth_methods_supported": ["client_secret_basic", "client_secret_post"]
  },
  "specCustomization": {
    "codeParameterName": "string",
    "requestContentType": "applicationJson" | "formUrlEncoded"
  }
}
```

#### OAuth Resource Owner Password
```json
{
  "name": "string",
  "clientId": "string",
  "clientSecret": "string",
  "scope": "string",
  "username": "string",
  "password": "string",
  "bodyFormat": "applicationJson" | "formUrlEncoded",
  "tokenEndpoint": "string"
}
```
