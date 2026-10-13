# Authentication

Extensions authenticate in two ways, depending on where the code runs:

| Where your code runs | How it authenticates |
|---|---|
| **Embedded in the portal or Admin Console** | The Extension SDK delivers a scoped JWT during the handshake. See [Extension SDK JWT claims](#extension-sdk-jwt-claims). |
| **On a server, connected to an external service** | The extension's OAuth application issues access and refresh tokens. See [OAuth refresh tokens](#oauth-refresh-tokens). |

## Extension OAuth applications

Extensions that connect to external services, or host embedded widgets, authenticate through an **OAuth application** registered for that extension.

Typical flow:

1. An admin installs and configures the extension in the **Admin Console**.
2. The integrator completes the interactive OAuth authorization flow once.
3. GraFx Experience issues an **access token** and a **refresh token**.
4. The integration uses the refresh token to get new access tokens when needed.

This applies to server-side integrations built on the Extension Framework — not to regular end-user sign-in.

## OAuth refresh tokens

Extension OAuth applications use **rolling refresh tokens**, so integrations stay connected without repeating the sign-in flow.

| Rule | Detail |
|---|---|
| **Initial validity** | A refresh token is valid for **30 days** from issuance. |
| **Renewal on use** | Each time the integration exchanges the refresh token for a new access token, validity extends for another **30 days** from that moment. |
| **Indefinite connection** | An integration that refreshes at least once every 30 days keeps working without repeating the OAuth flow. |
| **Idle expiry** | A refresh token that is not used for **30 consecutive days** is rejected. Complete the OAuth authorization flow again to get a new one. |
| **Reusability** | Refresh tokens stay usable within their validity window — using one does not immediately invalidate it. |
| **Scope** | Applies only to **extension OAuth applications**. Regular user sign-in and web sessions are unchanged. |
| **Revocation** | Disabling or uninstalling an extension revokes its refresh tokens. |

!!! tip "Keep integrations alive"
    Schedule your integration to refresh its access token regularly — at least once every 30 days — so the refresh token never reaches idle expiry.

## Extension SDK JWT claims

When an embedded extension connects through the Extension SDK, GraFx Experience issues a JWT with `token_type` set to `extension_sdk`. The token is delivered in the handshake (`connect()`). Use these claims to validate the token and to identify the user, installation, and extension.

### Standard claims

| Claim | Description |
|---|---|
| **`iss`** | Issuer — the identity provider URL for your environment. Use it to verify the token source and to find the JWK set for signature validation. |
| **`aud`** | Audience — the extension identifier, for example `ext:grafx-vdp`. |
| **`sub`** | Subject — the GraFx Experience user ID. |
| **`exp`** | Expiration time (Unix timestamp). |
| **`iat`** | Issued-at time (Unix timestamp). |
| **`jti`** | Unique token identifier. |

### Platform claims

| Claim | Description |
|---|---|
| **`email`** | Email address of the signed-in user. |
| **`tenant_id`** | UUID of the installation (tenant). |
| **`ext_id`** | UUID of the extension instance on this installation. |
| **`ext_key`** | Extension key, for example `assets` or `grafx-vdp`. |
| **`token_type`** | Always `extension_sdk` for SDK tokens. |
| **`scope`** | OAuth scopes granted to this token. |
| **`roles`** | Array of role identifiers for the signed-in user. |
| **`amr`** | Authentication methods reference. |

### Role values

The **`roles`** claim lists the platform roles of the user. See [Roles & permissions](/GraFx-Experience/overview/roles-permissions/) for what each role means.

| Role value | Role |
|---|---|
| **`ROLE_USER`** | User — access to spaces and content based on group permissions. |
| **`ROLE_TENANT_ADMIN`** | Admin — access to the page editor and the **Admin Console**. |
| **`ROLE_TENANT_OWNER`** | Account Owner — same platform access as Admin; one per installation. |

Use **`roles`** to gate features in your extension — for example, show admin-only actions only when `ROLE_TENANT_ADMIN` or `ROLE_TENANT_OWNER` is present.

!!! warning "Validate with `iss`"
    Always verify the JWT signature against the JWK set published by the issuer in **`iss`**. Do not trust tokens from an unexpected issuer URL.

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

Issuer URLs differ per environment. Contact CHILI publish to confirm the correct **`iss`** value for development, UAT, and production.
