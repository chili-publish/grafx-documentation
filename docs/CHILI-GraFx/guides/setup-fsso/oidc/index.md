# Setup Federated Single Sign-On using OpenID Connect

This document lists the steps required for setting up Federated Single Sign-On from your OIDC Identity Provider ("IDP") to CHILI GraFx.

## 1. Gather necessary info

CHILI publish recommends testing FSSO on a separate 'test' domain initially. Given the variability in protocols and differences among various Identity Provider (IDP) services, there’s a risk of incompatible configurations. By enabling FSSO for the test domain first, you can verify the correctness of the configuration without impacting your users.

## 2. Configure your IDP

Create an OIDC application in your IDP

| **Configuration** | **Value**                                     |
| ----------------- | --------------------------------------------- |
| Redirect URI      | `https://login.chiligrafx.com/login/callback` |
| Enabled flows     | `Standard` (auth code) and `Implicit`         |

Please configure your IDP to provide at least following claims in the **ID token**:

| **Claim name**                        | **Description**                                           |
| ------------------------------------- | --------------------------------------------------------- |
| `sub`                                 | The user ID. Should be set to the email address           |
| `email`                               | The email address of the user                             |
| `given_name`                          | The given name of the user                                |
| `family_name`                         | The family name of the user                               |
| `https://chili-publish.com/CGXGroups` | A list of UUIDs of the GraFx groups the user should be in |

## 3. GraFx Configuration

Next CHILI publish needs to configure a few things on the GraFx side, so your users get redirected to your IDP when logging into GraFx.

Please provide us following details of the application you created on your IDP:

- URL to your IDP's OpenID Configuration document
- Client ID 
- Client Secret

Please inform us of the **domain** you’d like to use for testing FSSO.

## 4. Testing

Once CHILI publish has enabled FSSO for the test domain, please verify that users with an email address in that domain are able to log on and get the expected permissions.

## 5. Enable FSSO

We will coordinate with you to enable FSSO for your main domain(s) at a mutually agreed-upon time.

## Examples

### Claims in the ID token

Here's an excerpt from the ID token returned by the IDP, showing a valid format for the required claims:

```json
...
  "sub": "oidc-user@my-oidc-realm.com",
  "https://chili-publish.com/CGXGroups": [
    "e68dc58a-324f-468b-a0ab-32494699d61c",
    "2a01aa2d-8f8a-427b-ba9e-ecc02fa74179"
  ],
  "given_name": "Oidc",
  "family_name": "User",
  "email": "oidc-user@my-oidc-realm.com"
...
```