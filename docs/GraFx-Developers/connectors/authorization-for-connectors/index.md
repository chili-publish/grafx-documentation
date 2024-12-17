# Authorization for Connectors

Connectors support various types of authorization to enable secure integration with external systems. This document outlines the process of adding authorization to a Connector and explains the different authorization types available.

## Understanding Authorization

When developing your Connector's JavaScript logic, you'll often need to make requests to external APIs. While the `runtime.fetch` method makes this process straightforward, handling API endpoints that require authorization or authentication can be challenging.

Hardcoding tokens directly into the Connector code is considered bad practice, as this code may be accessible to other administrators in your environment. To address this security concern, the Connector CLI tool provides four different authorization types:

- Static Header Key
- OAuth2.0 Client Credentials
- OAuth2.0 Authorization Code
- OAuth2.0 Resource Owner Password (Password Grant)

When a user first accesses a Connector and the code makes a `runtime.fetch` call, the GraFx Platform automatically runs the required authentication workflow. The authentication result is then cached and added to subsequent requests automatically.

## Authorization Limitations

While the Connector framework supports the most common authorization schemas, it's important to note that completely customizable authorization is not possible. If your specific authorization requirements don't align with the four provided types, you may need to develop a workaround solution.

For example, services like GraFx Media and GraFx Platform don't meet the requirements of any of the supported authorization types. In such cases, you would need to implement an intermediary service that adapts the authorization workflow to work within the Connector framework.

## Define Supported Authorization Types
Before implementing authorization, you must define the supported authorization types in your `package.json` file. This ensures consistency between your CLI commands and your package configuration.

To do so, add or modify the `supportedAuth` property in your `package.json` file with the types of authentication your Connector supports.

Example of a `package.json` supporting Static Header Key and OAuth2.0 Authorization Code:
```json
{
...
  "config": {
    ...
    "supportedAuth": ["staticKey", "oAuth2AuthorizationCode"]
  }
}
```

## Implement Authorization
To implement authorization in a Connector, you need a published Connector and the [Connector CLI]() tool. Use the following command:

```bash
connector-cli set-auth \
    --connectorId <connector-id> \
    -e <environment> \
    -b <base-url> \
    -au <auth-usage> \
    -at <auth-type> \
    --auth-data-file <path-to-auth-file>
```

<br/>

!!! note "Authorization is Optional"

	  Authorization is optional for Connectors. By default, no authorization is used. However, once authorization is set, there is currently no method to remove it via the Connector CLI.

### Connector ID (`--connectorId`)

This argument is the ID of your connector published in your GraFx environment.

To retrieve all Connectors to get lookup your ID, use the following API endpoint (with proper authorization header):

```bash
GET https://{environment}.chili-publish.online/grafx/api/experimental/environment/{environment}/connectors
```

### Environment (`-e`)

This argument expects the environment name that your Connector is published in.

### Base URL (`-b`)

This argument expects the base URL for GraFx API calls, which will be in either of the following formats:

- Production Environments
```
https://{environment}.chili-publish.online/grafx
```

- Sandbox Environment
```
https://{environment}.chili-publish-sandbox.online/grafx
```

!!! tip "Matching Environment"

    Ensure that the environment in your base URL matches the environment passed via the `-e` argument.


### Authorization Usage (`-au`)

This argument expects one of two values that will specify the usage scenario for the authorization.

Expected values:

- **browser**: Connector authentication to use when Studio is loaded in the browser for Studio editors (e.g., Studio UI) or when using the SDK.
- **server**: Connector authentication to use when Studio is loaded on GraFx servers for generating output (e.g., PDF, PNG, GIF).

Therefore, you can define different authorization types for each usage, allowing your Connector to use separate authorization methods for browser and server interactions. Of course, you can choose the same authorization type for both usage types.

!!! note "Authorization Always Happens on the Server"

	  You can define different authorization types for each usage scenario. However, the actual authorization always occurs on the server to prevent token or credential leakage.

!!! note "Each Usage Can Only Be Set Once"

	  If you run the `set-auth` command twice with the same authorization usage `-au` value but different `-at` authorization types, the authorization type will just be ignored. At this moment there is no way to overwrite or erase authorization once set.

### Authorization Type (`-at`)

This arguments expects one of the four supported types of authorization.

| Auth Type | Reference | Usage Support | Expected Argument Value |
|-----------|-----------|---------------|---------------------|
| Static Header Key | [MDN - Authorization Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) | browser and server | staticKey |
| OAuth2.0 Client Credentials | [OAuth2.0 - Client Credentials](https://oauth.net/2/grant-types/client-credentials/) | browser and server | oAuth2ClientCredentials |
| OAuth2.0 Authorization Code | [OAuth2.0 - Authorization Code](https://oauth.net/2/grant-types/authorization-code/) | browser | oAuth2AuthorizationCode |
| OAuth2.0 Resource Owner Password | [OAuth2.0 - Password Grant](https://oauth.net/2/grant-types/password/) | browser and server | oAuth2ResourceOwnerPassword |
| OAuth2.0 JWT Bearer Token | [OAuth2.0 - JWT Bearer Token Flow](https://datatracker.ietf.org/doc/html/rfc7523) | browser and server | oAuth2JwtBearer |

In addition to specifying the authorization type using the `-at` argument, you must also define the supported authorization types in your `package.json` file. See [Define Supported Authorization Types](#define-supported-authorization-types)

!!! warning "Each Usage Can Only Be Set Once"

    OAuth2.0 Authorization Code is only supported with browser usage.

<br/>

#### OAuth2.0 Considerations

1. OAuth2.0 responses must comply with the [Access Token Response](https://www.oauth.com/oauth2-servers/access-tokens/access-token-response/) format, with the exception `expires_in` being mandatory.
2. The `grant_type` for OAuth2.0 types is automatically set as per the specification and cannot be configured.
3. `access_token` and `refresh_token` are cached internally for OAuth2.0 types. There's currently no way to reset them without deleting the Connector.
4. OAuth2.0 Authorization Code is user-specific and not useful with an Integration User (used outside the GraFx Platform).
5. OAuth2.0 Authorization Code is limited to "browser" usage, which may restrict its applicability in certain scenarios.

### Authorization Data File Requirements (`--auth-data-file`)

Each authorization type requires a specific JSON schema. The `grant_type` for OAuth2.0 types is predefined by the specifications.

#### Static Header Key
```typescript
{
  "name": string, // An arbitrary string value
  "key": string,  // HTTP header name
  "value": string // HTTP header value
}
```

#### OAuth2.0 Client Credentials
```typescript
{
  "name": string,         // An arbitrary string value
  "clientId": string,     // OAuth2.0 app client id
  "clientSecret": string, // OAuth2.0 app client secret
  "scope": string,        // OAuth2.0 app scope. Optional
  "tokenEndpoint": string // OAuth2.0 app token endpoint URL
}
```

#### OAuth2.0 Authorization Code
```typescript
{
  "name": string, // An arbitrary string value
  "clientId": string, // OAuth2.0 app client id
  "clientSecret": string, // OAuth2.0 app client secret
  "scope": string, // OAuth2.0 app scope. Optional
  "authorizationServerMetadata": {
    "authorization_endpoint": string, // OAuth2.0 app authorization endpoint URL
    "token_endpoint": string, // OAuth2.0 app token endpoint URL
    "token_endpoint_auth_methods_supported": ["client_secret_basic", "client_secret_post"] // Describe the way of how "clientId" and "clientSecrets" are sending in HTTP requests
  },
  "specCustomization": {
    "codeParameterName": string, // Name of the "code" parameter that send in HTTP requests. Optional, default "code"
    "requestContentType": "applicationJson" | "formUrlEncoded" // Defines which HTTP Content-Type will be used for HTTP request. Optional, default "formUrlEncoded"
  }
}
```

#### OAuth2.0 Resource Owner Password
```typescript
{
  "name": string, // An arbitrary string value
  "clientId": string, // OAuth2.0 app client id
  "clientSecret": string, // OAuth2.0 app client secret
  "scope": string, // OAuth2.0 app scope. Optional
  "username": string, // User that has an access to the OAuth2.0 app
  "password": string, // Password of the username
  "bodyFormat": "applicationJson" | "formUrlEncoded", // Defines which HTTP Content-Type will be used for token request. Optional, default "formUrlEncoded"
  "tokenEndpoint": string // OAuth2.0 app token endpoint URL
}
```

#### OAuth2.0 JWT Bearer Token
```typescript
{
  "name": string, // An arbitrary string value
  "issuer": string, // OAuth2.0 issuer
  "scope": string, // OAuth2.0 app scope. Optional
  "tokenEndpoint": string // OAuth2.0 app token endpoint URL
  "expirationTimeSeconds": number, // Expiration time for JWT token. Optional
  "signatureConfig": {
    "algorithm": "RS256", // Algorithm to sign JWT token
    "privateKey": string // Private key to sign JWT token
  }
}
```

## Example: Setting Multiple Authorization Types

This example demonstrates how to set up a Connector with different authorization types for server and browser interactions. In this scenario, we'll use OAuth2.0 Client Credentials for server interactions and OAuth Authorization Code for browser interactions.

### Step 1: Prepare Authorization Data Files

First, create two JSON files with the necessary authorization data:

#### OAuth2.0 Client Credentials JSON
```json title="oauth-client-credentials.json"
{
  "name": "MyClientCredentials",
  "clientId": "abc123xyz789",
  "clientSecret": "s3cr3tk3y",
  "scope": "read write",
  "tokenEndpoint": "https://oauth.example.com/token"
}
```

#### OAuth2.0 Authorization Code JSON
```json title="oauth-authorization-code.json"
{
  "name": "MyAuthorizationCode",
  "clientId": "client123id",
  "clientSecret": "client123secret",
  "scope": "openid profile",
  "authorizationServerMetadata": {
    "authorization_endpoint": "https://oauth.example.com/authorize",
    "token_endpoint": "https://oauth.example.com/token",
    "token_endpoint_auth_methods_supported": ["client_secret_basic", "client_secret_post"]
  },
  "specCustomization": {
    "codeParameterName": "authCode",
    "requestContentType": "formUrlEncoded"
  }
}
```

### Step 2: Update package.json

Ensure that your `package.json` file includes both authorization types in the `supportedAuth` array:

```json
{
  "config": {
    "supportedAuth": ["oAuth2ClientCredentials", "oAuth2AuthorizationCode"]
  }
}
```

### Step 3: Set Authorization for Server Interactions

Use the following command to set OAuth2.0 Client Credentials for server interactions:

```bash
connector-cli set-auth \
    --connectorId your-connector-id \
    -e example \
    -b https://example.chili-publish.online/grafx \
    -au server \
    -at oAuth2ClientCredentials \
    --auth-data-file path/to/oauth-client-credentials.json
```

### Step 4: Set Authorization for Browser Interactions

Use the following command to set OAuth2.0 Authorization Code for browser interactions:

```bash
connector-cli set-auth \
    --connectorId your-connector-id \
    -e example \
    -b https://example.chili-publish.online/grafx \
    -au browser \
    -at oAuth2AuthorizationCode \
    --auth-data-file path/to/oauth-authorization-code.json
```

By following these steps, we've configured our Connector to use OAuth2.0 Client Credentials for server-side interactions and OAuth2.0 Authorization Code for browser-based interactions. This setup allows for secure communication with external APIs in both scenarios.
