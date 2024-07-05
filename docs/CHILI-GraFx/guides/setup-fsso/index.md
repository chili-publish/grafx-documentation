# Setup Federated Single Sign-On

## Configuring FSSO

To setup Federated Single Sign-On (FSSO), CHILI publish will need certain information.

This information depends on the [preferred protocol](/CHILI-GraFx/concepts/federated-single-sign-on/#supported-protocols).

Consult the supported protocols, and initiate a support ticket with the Client Success team to assist you with the setup.

!!! info "Configuring your Identity Provider"
	During the setup of Federated Single Sign-On, CHILI publish can not configure your Identity Provider (IdP) on your behalf.  
    The reason is that there are numerous IDP systems, each with its own unique configuration methods.

## Testing FSSO connection

Once the CHILI Publish team configures the connection, regardless of the preferred protocol selected, your users will be able to authenticate using your company's identities.

To verify this, please follow this process:

1. Open a fresh browser via Private or Incognito browsing
2. Go to [GraFx](https://chiligrafx.com)
3. Enter an email address in the domain provided to our team
4. Verify the browser redirects you to your company's login screen
5. Authenticate normally following the authentication process of your company
6. Confirm you can successfully access the GraFx platform

## Migrate existing GraFx users

The migration of the users happens in a transparent way based on the user's email address.

The users change their authentication process from username and password to the process in your company, but the platform behaves the same for them.

The user migration process does not affect the user management processes. You will continue inviting and managing users the same way you did before configuring Federated SSO.