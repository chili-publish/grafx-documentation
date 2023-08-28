# CHILI GraFx Federated Single sign-on

## SSO Glossary

- **SAML**: Security Assertion Markup Language, an XML-based standard for exchanging authentication and authorization data between parties.
- **OIDC**: OpenID Connect, an authentication protocol that allows users to authenticate with a web application or service using a third-party identity provider (IdP). OIDC builds on top of the OAuth 2.0 protocol and adds an authentication layer on top of it.
- **Authentication**: The process of verifying the identity of a user, device, or application.
- **Delegation**: The act of transferring authentication responsibilities from one entity to another.
- **Identity Provider (IdP)**: A system or service that authenticates users and provides identity information in the form of SAML assertions. In our case, the Identity Provider will be the third-party IDP. Auth0 will work as a Service Provider in this case.
- **Service Provider (SP)**: A system or service that relies on an IdP to authenticate users and grant access to protected resources. In our case, Auth0 will work as a Service Provider. The Identity Provider will be the third-party IDP.
- **SSO**: Single Sign-On, a mechanism that enables users to authenticate once and access multiple applications or services without having to re-enter their credentials.
- **Assertion/Claim**: A statement of fact, such as a statement about a user's identity or attributes. The most common term in a SAML context is Assertion. The most common term in an OIDC context is Claim
- **Metadata**: A collection of information about a SAML entity, including its endpoints, keys, and certificates. In our case, we will work with the metadata elements of information one by one, and not in the form of a metadata file.
- **EntityID**: A unique identifier for a SAML entity, typically a URL or URN.
- **Token**: A token (in this context) is like a digital ticket that proves you've been authenticated by the Identity Provider (IdP). It's a small piece of information that contains details about your identity and permissions. When you log in with SSO, the IdP issues a token to your browser or device. This token is then used to vouch for your identity when you access other services (Service Providers or SPs). Instead of sharing your username and password with each SP, you simply show them this token, which says, "I'm authenticated; you can trust me." Tokens are typically short-lived and encrypted to enhance security. They help streamline the process of accessing multiple services without repeatedly entering your credentials.