# Example configuration: Entra ID (formerly Azure ID)

!!! Warning "Disclaimer"
	The objective of this sample is not the definition of a canonical implementation, but to serve as an illustrative example of one possible way to implement the integration on the customer side.

## Introduction

The federation with CHILI GraFx is based on standard protocols (SAML and OIDC) and the requirements made by CHILI GraFx for a successful integration are based on those protocols.

At the same time, we want to help our customers with a sample configuration to be done in Microsoft Entra ID (Former Azure AD).

In this example, we assume the federation configuration is working correctly. For that reason, this example is focused on the management of groups and memberships.

## Concepts

We will be using the following concepts from **Entra ID**

### Application role

Permissions are defined at the application level. In our case, the application is the one used to define the federation. An Application role can be linked to a user or a group

### User group

This is defined beyond the application. A User group can be assigned one or many Application Roles. All user members of that User group get all of the Application roles of the group.

### Group membership

Associating a user to a User group

## Procedure

Once the Federated SSO connection is configured as an application in Entra ID, follow these steps to make a user of your company member of a CGX group:

- Create the User in Entra ID following your procedures. We’ll call the user “Mike”
- Create a User group in Entra ID. We’ll call the group “marketing_group”
- Create a User group in CGX and copy the Group ID (follow the CGX documentation if needed)
- Create an Application role with the ID of the CGX Group ID. We’ll use the value “CGX-marketing-ID”
- Add the group “marketing_group” to the Application Role “CGX-marketing-ID”
- Add user “Mike” as a member of the group “marketing_group”

The next time the user “Mike” logs into CGX, he will have all of the permissions of group “CGX-marketing-ID”