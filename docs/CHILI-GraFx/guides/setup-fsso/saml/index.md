# Setup Federated Single Sign on using SAML

This document lists the steps required for setting up Federated Single Sign On from your SAML Identity Provider ("IDP") to CHILI GraFx.

## 1. Gather necessary info

Our Client Success team will provide you following details:

| **Name**            | **Description**                                    |
| ------------------- | -------------------------------------------------- |
| Redirect URI        | `https://login.chiligrafx.com/login/callback`      |
| Service Provider ID | The name GraFx will identify itself as on your IDP |

CHILI publish recommends testing FSSO on a separate 'test' domain initially. Given the variability in protocols and differences among various Identity Provider (IDP) services, there’s a risk of incompatible configurations. By enabling FSSO for the test domain first, you can verify the correctness of the configuration without impacting your users.

## 2. Configure your IDP

Create a SAML application in your IDP, using the gathered information.
The **email address** should be used as the subject's `NameID` in SAML responses.

Please configure your IDP to provide at least following required attributes in SAML responses:

| **Attribute name**                    | **Description**                                           |
| ------------------------------------- | --------------------------------------------------------- |
| `email`                               | The email address of the user                             |
| `given_name`                          | The given name of the user                                |
| `family_name`                         | The family name of the user                               |
| `https://chili-publish.com/CGXGroups` | A list of UUIDs of the GraFx groups the user should be in |

## 3. GraFx Configuration

Next CHILI publish needs to configure a few things on the GraFx side, so your users get redirected to your IDP when logging into GraFx.

Please provide us following metadata:

| **Name**                 | **Description**                                    |
| ------------------------ | -------------------------------------------------- |
| Sign In URL              | `https://login.chiligrafx.com/login/callback`      |
| X509 Signing Certificate | The name GraFx will identify itself as on your IDP |

Alternatively, you can provide the **SAML metadata URL**.  
Above values can be derived from it.

Please inform us of the **domain** you’d like to use for testing FSSO.

## 4. Testing

Once CHILI publish has enabled FSSO for the test domain, please verify that users with an email address in that domain are able to log on and get the expected permissions.

## 5. Enable FSSO

We will coordinate with you to enable FSSO for your main domain(s) at a mutually agreed-upon time.

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