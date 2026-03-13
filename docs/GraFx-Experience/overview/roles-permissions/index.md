# Roles & Permissions in GraFx Experience

This page explains how roles and permissions work in **GraFx Experience**, who can do what, and how user authentication works including support for federated identity.

## Core concepts

Permissions are *not* assigned to individual users. They are determined by:

- A user’s **global role**

- The **groups** the user belongs to

A user’s effective permissions are the *sum* of the permissions granted to those groups.

## Global user roles

Global roles control broad access to the platform:

- **User** — Can log in and access Experience features based on group permissions.
- **Admin** — Can configure platform settings, manage groups, environments, and permissions.
- **Account Owner** — Has full control, including billing and subscription management.

Being an Admin or Account Owner does not automatically grant access to specific assets or workflows — group permissions determine visibility and actions.

## Permission groups

Groups define which specific features and content a user can access:

- A user must be a member of at least one group.
- Groups encapsulate permissions such as:
  - Access to specific Design Systems
  - Ability to create or edit documents
  - Ability to export or publish assets
  - Access to media or upload capabilities
- Users can be in *multiple groups*; permissions are additive.

## What users see and do

Permissions determine:
- Which Design Systems and templates a user can see
- Whether they can create, edit, or export assets
- What categories of media or brand resources they can access
- Which workflows are available to them

A user with no group membership cannot perform any actions.

## Authentication and identity

### Local user accounts

- Managed within the platform.
- Admins invite users and assign roles and groups.
- Users sign in with a platform password.

### Single Sign-On (SSO)

- Supported via federated identity providers.
- When enabled, the identity provider passes group information at login.
- Group membership from the identity provider determines access and permissions.
- This method centralizes identity and simplifies user provisioning.

## Assigning roles & groups

- Only Admins and Account Owners can assign roles and groups.
- Users are added to environments and groups in a controlled fashion.
- A user’s effective permissions result from their group memberships.

## Summary

Roles give *broad platform access*:
- **User** can sign in and use the Experience app.
- **Admin** can configure system and manage access.
- **Account Owner** adds subscription control.

Groups give *specific operational permissions*:
- Groups determine what users can see and do on a detailed level.
- Users may belong to multiple groups.
- With SSO, group membership can come from your identity provider.