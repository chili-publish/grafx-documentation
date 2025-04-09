# CHILI GraFx Federated Single Sign-On

This document contains general concepts that apply to the federation with third-party IDPs as well as details for the configuration depending on the protocol to be used.

See [Glossary](#sso-glossary) for abbreviations used in this document.

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
	Expected behaviour of **Federated Single Sign-On** would be to have user groups in place. 
	Today, allowing access to CHILI GraFx, happens through **invitation via email**. As soon as the invitee has accepted the invitation, the invited user will be able to login through the Enterprise Identity Provider.

## Supported protocols

CHILI GraFx supports federation using following protocols:

- [OpenID Connect (OIDC)](/CHILI-GraFx/guides/setup-fsso/oidc/)
- [Security Assertion Markup Language (SAML)](/CHILI-GraFx/guides/setup-fsso/saml/)

## Configuring FSSO
See [the FSSO setup guide](/CHILI-GraFx/guides/setup-fsso/intro/)

## SSO Glossary

- **Authentication**: The process of verifying the identity of a user, device, or application.
- **Assertion/Claim**: A statement of fact, such as a statement about a user's identity or attributes. The most common term in a SAML context is Assertion. The most common term in an OIDC context is Claim
- **Delegation**: The act of transferring authentication responsibilities from one entity to another.
- **EntityID**: A unique identifier for a SAML entity, typically a URL or URN.
- **Identity Provider (IdP)**: A system or service that authenticates users and provides identity information in the form of SAML assertions. In our case, the Identity Provider will be the third-party IDP. Auth0 will work as a Service Provider in this case.
- **Metadata**: A collection of information about a SAML entity, including its endpoints, keys, and certificates. In our case, we will work with the metadata elements of information one by one, and not in the form of a metadata file.
- **OIDC**: OpenID Connect, an authentication protocol that allows users to authenticate with a web application or service using a third-party identity provider (IdP). OIDC builds on top of the OAuth 2.0 protocol and adds an authentication layer on top of it.
- **SAML**: Security Assertion Markup Language, an XML-based standard for exchanging authentication and authorization data between parties.
- **Service Provider (SP)**: A system or service that relies on an IdP to authenticate users and grant access to protected resources. In our case, Auth0 will work as a Service Provider. The Identity Provider will be the third-party IDP.
- **SSO**: Single Sign-On, a mechanism that enables users to authenticate once and access multiple applications or services without having to re-enter their credentials.
- **Token**: A token (in this context) is like a digital ticket that proves you've been authenticated by the Identity Provider (IdP). It's a small piece of information that contains details about your identity and permissions. When you log in with SSO, the IdP issues a token to your browser or device. This token is then used to vouch for your identity when you access other services (Service Providers or SPs). Instead of sharing your username and password with each SP, you simply show them this token, which says, "I'm authenticated; you can trust me." Tokens are typically short-lived and encrypted to enhance security. They help streamline the process of accessing multiple services without repeatedly entering your credentials.