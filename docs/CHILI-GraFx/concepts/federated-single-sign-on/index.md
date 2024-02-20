# CHILI GraFx Federated Single sign-on

This document contains general concepts that apply to the federation with third-party IDPs as well as details for the configuration depending on the protocol to be used.

See [Glossary](glossary/) for abbreviations used in this document.

## What is an Identity federation?

Identity federation is a mechanism that allows two or more organizations to share user identity and access information securely and seamlessly.

In a federation, each organization maintains its own identity provider (IdP), which is responsible for authenticating users and issuing identity and access tokens.

When a user tries to access a resource in a different organization, their browser is redirected to their own IDP for authentication. If the authentication is successful, the IdP issues a token that contains the user's identity and access information and redirects the user back to the resource with the token.

The resource then verifies the token with the user's IdP, and grants access if the token is valid and the user is authorized to access the resource.

Federation allows organizations to leverage each other's authentication and authorization capabilities, without the need for users to create and manage multiple accounts across different systems.

Federation can also improve security and compliance, by enabling organizations to enforce consistent identity and access policies across multiple systems and reducing the risk of credential theft or unauthorized access.

## Architecture

Depending on the use of the SSO federation, the components and their responsibilities may change.

This section explains the relationship between the components and how those responsibilities change.

### Without federation

Those customers who use the CHILI GraFx platform without SSO federation host their users and the permissions of those in the platform itself.

Within the components of the platform, there is an identity hub that manages both the **Authentication** of the users and the **permissions** they have on each platform component. These permissions include Individual access, Groups, and Group memberships.

``` mermaid
erDiagram
  CHILI-GraFx ||--|| CHILI-GraFx-Identity-Hub : A-P
  GraFx-Studio ||--|| CHILI-GraFx-Identity-Hub : A-P
  GraFx-Publisher ||--|| CHILI-GraFx-Identity-Hub : A-P
  GraFx-Fonts ||--|| CHILI-GraFx-Identity-Hub : A-P
  GraFx-Media ||--|| CHILI-GraFx-Identity-Hub : A-P
  CHILI-GraFx-Identity-Hub {
  	handles Authentication
  	handles Individual-Access
    handles Groups-Definition
    handles Group-Membership
  }
```

### With federation

Those customers who use the SSO Federation host their own users and take care of the authentication process. This enables the use of multiple factors for the authentication, and those mechanisms to be shared with other systems of the company.

In this case, the CHILI GraFx Identity Hub only takes care of the **Individual access** of the users and the definition of the permissions of the **User groups**. Plus, of course, the management of the trust relationship between CGX and the customer’s IDP.

``` mermaid
erDiagram
  CHILI-GraFx ||--|| CHILI-GraFx-Identity-Hub : A-P
  GraFx-Studio ||--|| CHILI-GraFx-Identity-Hub : A-P
  GraFx-Publisher ||--|| CHILI-GraFx-Identity-Hub : A-P
  GraFx-Fonts ||--|| CHILI-GraFx-Identity-Hub : A-P
  GraFx-Media ||--|| CHILI-GraFx-Identity-Hub : A-P
  CHILI-GraFx-Identity-Hub ||--|| Customer-Identity-Provider : A
  CHILI-GraFx-Identity-Hub {
  	handles Individual-Access
    handles Groups-Definition
  }
  Customer-Identity-Provider {
  	handles Authentication
    handles Group-Membership
  }
```

### Trust relationship

Regardless of the federation protocol to be used, it is necessary to establish a trust relationship between the CHILI GraFx Identity Hub and the Customer Identity Provider.

The CGX Identity Hub needs to trust the Customer IDP to verify the authentication tokens and claims signed by it. Without this trust in place, CGX could not know which authentications to trust.

At the same time, the customer’s IDP must trust CGX Identity Hub to make sure the authentications of the users are legit, avoiding the authentication process for unknown applications.

A Client Success colleague can assist you in the setup process.

!!! warning "Important: Invitation Only"
	Expected behaviour of **Federated Single Sign On** would be to have user groups in place. 
	Today, allowing access to CHILI GraFx, happens through **invitation via email**. As soon as the invitee has accepted the invitation, the invited user will be able to login through the Enterprise Identity Provider.


## Federated SSO via the OIDC protocol

[Details for the OIDC protocol](oidc/)

## Federated SSO via the SAML protocol

[Details for the SAML protocol](saml/)
