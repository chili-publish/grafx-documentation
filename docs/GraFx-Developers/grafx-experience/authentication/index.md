# Authentication

How an extension authenticates depends on where its code runs:

| Where the code runs | How it authenticates |
|---|---|
| **In the portal or Admin Console** | The Extension SDK receives a token during the handshake. See [Extension SDK JWT claims](#extension-sdk-jwt-claims). |
| **On a server, connected to an external service** | The extension's OAuth application issues access and refresh tokens. See [OAuth refresh tokens](#oauth-refresh-tokens). |

## Extension OAuth applications

Extensions that connect to external services use an **OAuth application** registered for that extension.

1. An admin installs and configures the extension in the **Admin Console**.
2. The integrator signs in through the OAuth flow once.
3. GraFx Experience issues an **access token** and a **refresh token**.
4. The integration uses the refresh token to get new access tokens.

This only applies to server-side integrations, not to end users signing in.

## OAuth refresh tokens

Refresh tokens roll over, so integrations stay connected without signing in again.

| Rule | Detail |
|---|---|
| **Validity** | A refresh token is valid for **30 days**. |
| **Renewal** | Each time you use it to get a new access token, it's valid for another **30 days**. |
| **Staying connected** | Refresh at least once every 30 days and the integration keeps working. |
| **Expiry** | A refresh token unused for **30 days** stops working. Go through the OAuth flow again to get a new one. |
| **Reuse** | Using a refresh token doesn't invalidate it. |
| **Scope** | Only for **extension OAuth applications**. User sign-in is not affected. |
| **Revocation** | Disabling or uninstalling the extension revokes its refresh tokens. |

!!! tip "Stay connected"
    Schedule your integration to refresh at least once every 30 days.

## Extension SDK JWT claims

When your app connects through the Extension SDK, GraFx Experience issues a JWT with `token_type` set to `extension_sdk`. Your app receives it from `connect()`. Use its claims to validate the token and to see who the user is and which installation and extension it's for.

### Standard claims

| Claim | Description |
|---|---|
| **`iss`** | Issuer: the identity provider URL. Use it to verify the token and find the keys (JWK set) to check the signature. |
| **`aud`** | Audience: the extension, for example `ext:grafx-vdp`. |
| **`sub`** | Subject: the user ID. |
| **`exp`** | Expiry time (Unix timestamp). |
| **`iat`** | Issue time (Unix timestamp). |
| **`jti`** | Unique token ID. |

### Platform claims

| Claim | Description |
|---|---|
| **`email`** | Email address of the signed-in user. |
| **`tenant_id`** | ID of the installation (tenant). |
| **`ext_id`** | ID of the extension on this installation. |
| **`ext_key`** | Extension key, for example `assets` or `grafx-vdp`. |
| **`token_type`** | Always `extension_sdk`. |
| **`scope`** | OAuth scopes granted to the token. |
| **`roles`** | The user's roles. |
| **`amr`** | How the user authenticated. |

### Role values

For what each role means, see [Roles & permissions](/GraFx-Experience/overview/roles-permissions/).

| Value | Role |
|---|---|
| **`ROLE_USER`** | User. Access to spaces and content through group permissions. |
| **`ROLE_TENANT_ADMIN`** | Admin. Access to the page editor and the **Admin Console**. |
| **`ROLE_TENANT_OWNER`** | Account Owner. Same access as Admin; one per installation. |

Use **`roles`** to show admin-only features only to `ROLE_TENANT_ADMIN` or `ROLE_TENANT_OWNER`.

!!! warning "Always check the issuer"
    Verify the signature against the JWK set of the issuer in **`iss`**. Reject tokens from any other issuer.

### Example payload

```json
{
  "iss": "https://idp.kadanza.app",
  "aud": "ext:assets",
  "sub": "336ce6b4-ec7b-11ec-8179-7e7497b0126b",
  "email": "user@example.com",
  "tenant_id": "6c58d5a8-60f0-11f1-b6c7-2eaf6dc1d365",
  "ext_id": "f3322f0e-6a21-11f1-8f7f-beee13e1b806",
  "ext_key": "assets",
  "token_type": "extension_sdk",
  "roles": ["ROLE_USER"],
  "exp": 1781689458,
  "iat": 1781685858,
  "jti": "626baa89-204e-4c74-8690-30544d7272cb"
}
```

The issuer URL differs per environment. Contact CHILI publish for the right **`iss`** value for development, UAT, and production.
