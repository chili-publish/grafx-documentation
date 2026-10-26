## Login & access

Your ability to access GraFx Experience depends on how your organization has set up authentication.

### How login can vary

- The **login page** presented to users may be customized by your organization.  
  Customizations can include branding, messages, images, and social login options.

- The **look and behavior of the login page** may differ between environments depending on how it was configured in the admin settings.

- Because the login page may be customized, it may include:
  - Custom text or message
  - Company logo and colors
  - Background or supporting images
  - Optional social login buttons

These visual or content customizations do not change your underlying access rights.

### Single Sign-On (SSO)

GraFx Experience supports federated login via an identity provider (IdP).  
When SSO is enabled:

- You log in through your organization’s identity provider (examples include Azure AD, Okta, or other third-party systems).
- Your identity provider handles authentication and then lets the platform know who you are.
- Group membership and permissions may be passed from the identity provider at login.
- Once authenticated, you land directly into GraFx Experience without a separate platform password.

SSO integration requires setup by your organization’s technical team or platform admin.

### What you need before logging in

- A **valid user account** — either local or federated via SSO.
- If SSO is used, your identity provider must be configured and linked to the platform’s identity system.
- You must be assigned to one or more **groups** that grant permission to access GraFx Experience.

### Checking which version you are on

Once logged in, open the user menu (your avatar in the navigation). Below **Log out**, it lists the deployed frontend and backend versions with the time of their last deployment. Clicking a version copies its full identifier — useful to include when you contact support.

### Summary

- The login page may look different depending on your organization’s configuration.  
- GraFx Experience supports both local accounts and federated SSO.  
- SSO may streamline sign-in and automatically apply group permissions from your identity provider.