# Federated Single Sign On: SAML

This document lists the steps required for setting up Federated Single Sign On from your SAML Identity Provider ("IDP") to CHILI GraFx.

## 1. Configure your IDP

Create a SAML application in your IDP.

To do this, you will need a few details:

- Redirect URI: `https://login.chiligrafx.com/login/callback`
- Service Provider ID
  - The name GraFx will identify itself as on your IDP
  - This will be provided by our Client Success team

Please configure your IDP to provide at least following required attributes in SAML responses:

| **Attribute name**                        | **Description**                                           |
| ------------------------------------- | --------------------------------------------------------- |
| `email`                               | The email address of the user                             |
| `given_name`                          | The given name of the user                                |
| `family_name`                         | The family name of the user                               |
| `https://chili-publish.com/CGXGroups` | A list of UUIDs of the GraFx groups the user should be in |

Also, please configure the application to use the **email address** as the `NameID` in SAML responses.

## 2. GraFx Configuration

Next we need to configure a few things on our side, so your users get redirected to your IDP when logging into GraFx.

Please provide us following metadata:

- Sign In URL
- X509 Signing Certificate

Alternatively, you can provide the **SAML metadata URL**.  
Above values can be derived from it.

Also, please let us know which **email domain(s)** to enable the FSSO for.
After specifying an email address in one of these domains, users will be redirected to your IDP.

!!! Tip "Test domain"
    Ideally we first test the FSSO using a different domain.  
    This avoids breaking authentication for your users already using GraFx, if the FSSO configuration needs more tweaking.

## Get in touch!

If you want to setup Federated Single sign on, [click here](/CHILI-GraFx/guides/setup-fsso/)

## Examples

### Attributes in the SAML response

Here's an excerpt from a SAML response showing a valid format for the required attributes:

```XML
...
<saml:AttributeStatement>
    <saml:Attribute Name="family_name" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
        <saml:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Smith</saml:AttributeValue>
    </saml:Attribute>
    <saml:Attribute Name="given_name" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
        <saml:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">John</saml:AttributeValue>
    </saml:Attribute>
    <saml:Attribute Name="email" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
        <saml:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">john.smith@company.com</saml:AttributeValue>
    </saml:Attribute>
    <saml:Attribute Name="https://chili-publish.com/CGXGroups" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
        <saml:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">2a01aa2d-8f8a-427b-ba9e-ecc02fa74179</saml:AttributeValue>
        <saml:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">e68dc58a-324f-468b-a0ab-32494699d61c</saml:AttributeValue>
    </saml:Attribute>
</saml:AttributeStatement>
...
```