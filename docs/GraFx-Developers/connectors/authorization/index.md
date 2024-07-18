# Connector Authorization

When building a custom connector that interacts with an external system (which is typically protected by some form of authorization), we often need to include specific credentials or tokens in our requests. However, hardcoding these sensitive details directly into the connector’s code poses a security risk. Anyone with access to the code could potentially extract these credentials. Fortunately, there’s a safer approach.

## Setup

To enable authorization for your connector you need to do it in two places:

- Connector project
- Deployed connector instance in the environment

### Connector project

Within the `package.json` file of your connector project, locate the `config` section. Here, you’ll specify the valid authorization methods. This step ensures that only supported authorization types can be configured and provides an overview of the connector’s authorization capabilities

```json
...
"config": {
	...
	"supportedAuth": ["staticKey", "oAuth2AuthorizationCode"]
}
...
```

!!! tip
	Once you specify `supportedAuth` on connector's project level, you might execute `connector-cli info` to see the information about them

To see list of all available authorization types supported by our Framework see [Supported authorization types](#authorization-types) section below in this page

### Deployed connector instance

!!! Important
	To configure authorization you need first deploy your connector to the environment via `connector-cli publish ...` command

Once we specified `supportedAuth` on the connector's project level we can procceed with configuration of deployed connector instance. It can be achieved by following CLI command:

```bash
connector-cli set-auth \
 	--connectorId <connector-id> \
 	-e <environment> \
	-b <base-url> \
	-au <auth-usage> \
	-at <auth-type> \
	--auth-data-file <path-to-auth-file>
```

!!! tip
	To get more information about command's parameter, you can always refer to the help command, `connector-cli set-auth -h`

## Authorization types

Our Framework supports following authorization types:

- CHILI token
- Static key
- OAuth2.0 client credentials flow
- OAuth2.0 resource owner flow
- OAuth2.0 authorization code

### "-au" and "-at"

Below is a table of CLI parameters per authorization type

| Type                             | "-au"                 | "-at"                         |
| -------------------------------- | --------------------- | ----------------------------- |
| CHILI token                      | "browser" or "server" | "chili"                       |
| Static key                       | "browser" or "server" | "staticKey"                   |
| OAuth2.0 client credentials flow | "browser" or "server" | "oAuth2ClientCredentials"     |
| OAuth2.0 resource owner flow     | "browser" or "server" | "oAuth2ResourceOwnerPassword" |
| OAuth2.0 authorization code      | "browser"             | "oAuth2AuthorizationCode"     |

!!! Important
	When configuring authentication for your connector, remember to configure it twice: once for `browser` and once for `server` authentication usages (`-au`). The `browser` authentication applies when using the connector via the Studio interface in your browser, while the `server` authentication is specifically for output generation.

### "--auth-data-file" file

For each authorization type, you’ll need to provide a file (in JSON or YAML format) containing the relevant authorization information.

#### Chili token

```typescript title="format"
interface ChiliToken {
	/**
	 * An arbitary string value
	 */
	name: string;
}
```

Example:

```json title="auth-chili.json"
{
	"name": "chili-token-auth"
}
```

or

```yaml title="auth-chili.yaml"
name: "chili-token-auth"
```

#### Static key

```typescript title="format"
interface StaticKey {
	/**
	 * An arbitary string value
	 */
	name: string;

	/**
	 * HTTP header name
	 */
	key: string;

	/**
	 * HTTP header value
	 */
	value: string;
}
```

Example:

```json title="auth-static-key.json"
{
	"name": "static-key-auth",
	"key": "Authorization",
	"value": "Api-Key"
}
```

or

```yaml title="auth-static-key.yaml"
name: "static-key-auth"
key: Authorization
value: Api-Key
```

#### OAuth2.0 client credentials

```typescript title="format"
interface OAuth2ClientCredentials {
	/**
	 * An arbitary string value
	 */
	name: string;

	/**
	 * OAuth 2.0 app client id
	 */
	clientId: string;

	/**
	 * OAuth 2.0 app client secret
	 */
	clientSecret: string;

	/**
	 * OAuth 2.0 app scope.
	 * @optional
	 */
	scope?: string;

	/**
	 * OAuth 2.0 app token endpoint URL
	 */
	tokenEndpoint: string;
}
```

Example:

```json title="auth-oauth-2-client-credentials.json"
{
	"name": "oauth-2-client-credentials-auth",
	"clientId": "clientId",
	"clientSecret": "secretKeyValue",
	"tokenEndpoint": "http://oauth-app.com/token"
}
```

or

```yaml title="auth-oauth-2-client-credentials.yaml"
name: "oauth-2-client-credentials-auth"
clientId: clientId
clientSecret: secretKeyValue
scope: offline
tokenEndpoint: http://oauth-app.com/token
```

#### OAuth2.0 resource owner

```typescript title="format"
interface OAuth2ResourceOwnerPassword {
	/**
	 * An arbitary string value
	 */
	name: string;
	/**
	 * OAuth 2.0 app client id
	 */
	clientId: string;

	/**
	 * OAuth 2.0 app client secret
	 */
	clientSecret: string;

	/**
	 * OAuth 2.0 app scope.
	 * @optional
	 */
	scope?: string;

	/**
	 * User that has an access to the OAuth 2.0 app
	 */
	username: string;

	/**
	 * Password of the username
	 */
	password: string;

	/**
	 * Defines which HTTP Content-Type will be used for token request.
	 * @optional
	 * @default "formUrlEncoded"
	 */
	bodyFormat?: "applicationJson" | "formUrlEncoded";
	/**
	 * OAuth 2.0 app token endpoint URL
	 */
	tokenEndpoint: string;
}
```

Example:

```json title="auth-oauth2-resource-owner.json"
{
	"name": "oauth2-resource-owner-password-auth",
	"clientId": "clientId",
	"clientSecret": "secretKeyValue",
	"tokenEndpoint": "http://oauth-app.com/token",
	"username": "demo@google.com",
	"password": "superSecretPassword",
	"bodyFormat": "applicationJson"
}
```

or

```yaml title="auth-oauth2-resource-owner.yaml"
name: "oauth2-resource-owner-password-auth"
clientId: clientId
clientSecret: secretKeyValue
tokenEndpoint: http://oauth-app.com/token
scope: offline
username: demo@google.com
password: superSecretPassword
```

#### OAuth2.0 authorization code

```typescript title="format"
interface Oauth2AuthorizationCode {
	/**
	 * An arbitary string value
	 */
	name: string;
	/**
	 * OAuth 2.0 app client id
	 */
	clientId: string;

	/**
	 * OAuth 2.0 app client secret
	 */
	clientSecret: string;

	/**
	 * OAuth 2.0 app scope.
	 * @optional
	 */
	scope?: string;

	/**
	 * OAuth 2.0 authorization server config
	 */
	authorizationServerMetadata: AuthorizationServerMetadata;

	/**
	 * Possible customization of the OAuth 2.0 specifications
	 * @optional
	 */
	specCustomization?: SpecCustomization;
}
```

```typescript
interface AuthorizationServerMetadata {
	/**
	 * OAuth 2.0 app authorization endpoint URL
	 */
	authorization_endpoint: string;

	/**
	 * OAuth 2.0 app token endpoint URL
	 */
	token_endpoint: string;

	/**
	 * Describe the way of how "clientId" and "clientSerects" are sending in HTTP requests
	 * More info:
	 * - https://developer.okta.com/docs/reference/api/oidc/#client-authentication-methods
	 */
	token_endpoint_auth_methods_supported: Array<
		"client_secret_basic" | "client_secret_post"
	>;
}
```

```typescript
interface SpecCustomization {
	/**
	 * Name of the "code" parameter that send in HTTP requests.
	 * @optional
	 * @default "code"
	 */
	codeParameterName?: string;

	/**
	 * Defines which HTTP Content-Type will be used for HTTP request.
	 * @optional
	 * @default "formUrlEncoded"
	 */
	requestContentType?: "applicationJson" | "formUrlEncoded";
}
```

Example:

```json title="auth-oauth2-authorization-code.json"
{
	"name": "oauth2-authorization-code-auth",
	"clientId": "clientId",
	"clientSecret": "secretKeyValue",
	"authorizationServerMetadata": {
		"authorization_endpoint": "http://oauth-app.com/authorization",
		"token_endpoint": "http://oauth-app.com/token",
		"token_endpoint_auth_methods_supported": ["client_secret_post"]
	}
}
```

or

```yaml title="auth-oauth2-authorization-code.yaml"
name: "oauth2-authorization-code-auth"
clientId: clientId
clientSecret: secretKeyValue
scope: offline
authorizationServerMetadata:
  authorization_endpoint: http://oauth-app.com/authorization
  token_endpoint: http://oauth-app.com/token
  token_endpoint_auth_methods_supported:
	- client_secret_basic
specCustomization:
  requestContentType: applicationJson
  codeParameterName: authorization_code
```
