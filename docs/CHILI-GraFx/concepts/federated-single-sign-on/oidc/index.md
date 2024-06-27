# Federated Single Sign On: OIDC

This document lists the steps required for setting up Federated Single Sign On from your OIDC Identity Provider ("IDP") to CHILI GraFx.

## 1. Configure your IDP
Create an OIDC application in your IDP

Redirect URI: `https://login.chiligrafx.com/login/callback`

Please configure your IDP to provide at least following claims:

| **Claim name**                        | **Description**                                    |
|---------------------------------------|----------------------------------------------------|
| `email`                               | The email address of the user                      |
| `given_name`                          | The given name of the user                         |
| `family_name`                         | The family name of the user                        |
| `https://chili-publish.com/CGXGroups` | The IDs of the GraFx groups the user should be in  |

## 2. GraFx Configuration

Please provide us:

- Issuer URL 
- Client ID 
- Client Secret
- Domain of the email addresses of your corporate users

## Get in touch!

If you want to setup Federated Single sign on, [click here](/CHILI-GraFx/guides/setup-fsso/)