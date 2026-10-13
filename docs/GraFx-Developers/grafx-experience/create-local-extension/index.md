# Create a local extension

A local extension is an extension that is bespoke to your own GraFx Experience installation. You create and manage it directly in the **Admin Console** to solve a use case that is unique to your organization — a custom integration or an internal tool that is never shared with other installations.

Every extension you build starts as a local extension: it is the registration that tells GraFx Experience what your app is, what it may access, and where it appears.

See also: [The concept of extensions](/GraFx-Experience/concepts/extensions/#shared-and-local-extensions)

## When to use a local extension

Use a local extension when you need something the shared extensions do not cover, for example to:

- Connect GraFx Experience to an internal system or a custom integration
- Add your own pages to the portal or the **Admin Console**
- Handle production output with your own service

## Before you start

- You need admin access to the **Admin Console**.
- Decide on the **Extension key** before you save. It cannot be changed after the extension is created.

## Create the extension

1. In the **Admin Console**, go to **Extensions** > **Installed**.
2. Select **Create local extension**.
3. Fill in the [Basic information](#basic-information), [CMS content](#cms-content), [Authentication](#authentication), and [Capabilities](#capabilities) sections described below.
4. Save the extension.

You can save the extension before your app is deployed, and come back later to set the **Base URL** and switch it to **Active**.

## Basic information

General details about the extension.

| Field | Description |
|---|---|
| **Extension key** *(required)* | A unique identifier for the extension. Use lowercase letters and hyphens only, for example `my-extension`. This cannot be changed after creation. |
| **Name** *(required)* | The display name of the extension. |
| **Active** | Enables the extension on your installation. Leave it off while you are still setting it up. |

## CMS content

Content shown for the extension in **Installed** extensions.

| Field | Description |
|---|---|
| **Icon** | The image shown for the extension. Select **Choose File** to upload one. |
| **Provider name** | The name of the organization that provides the extension. |
| **Short description** | A brief summary shown in the list of installed extensions. |

## Authentication

Authentication methods and API permissions for the extension.

| Field | Description |
|---|---|
| **Permissions** | The API permissions the extension requires. Search for and select each permission the extension needs. See [API permissions](#api-permissions) below. |
| **Auth type** | The authentication method the extension uses. Set to **None** if the extension does not authenticate against an external service. |
| **SDK authentication** | Allows the extension's iframes to receive a scoped JWT through the Extension SDK. Enable this when the extension makes authenticated API calls from its embedded pages. |

!!! note "What a scoped JWT is"
    A JWT (JSON Web Token) is a secure, short-lived token that proves the extension may act on behalf of the current user. *Scoped* means the token only grants the permissions you selected for the extension — nothing more. See [Authentication](/GraFx-Developers/grafx-experience/authentication/#extension-sdk-jwt-claims) for the claims it contains.

### API permissions

The platform API is how an extension reads and changes data in GraFx Experience — users, projects, assets, and more. The **Permissions** field controls which parts of that API the extension may reach.

Each permission covers a **resource** and an **action**. For example:

| Permission | What it allows |
|---|---|
| Read users | View user and group details |
| Read projects | View projects and their layouts |
| Read assets | View media in the library |
| Write assets | Add or update media in the library |

Keep these principles in mind:

- **Grant only what the extension needs.** Select the smallest set of permissions required. An extension that only displays media does not need write access.
- **Permissions are scoped, never unlimited.** The extension can only act within the permissions you select.
- **They apply to the extension, not the person.** These permissions define what the extension itself may do through the API. They are separate from a user's own [roles and group permissions](/GraFx-Experience/overview/roles-permissions/).

!!! info "Available permissions grow over time"
    The Extension Framework is being expanded in phases, so the list of selectable permissions may grow. Search the **Permissions** field to see what is available for your installation.

## Capabilities

Capabilities define what the extension can do on the platform.

| Capability | Description |
|---|---|
| **Experience pages** | Render iframe-based pages in a space in the portal. |
| **Admin Console pages** | Add pages to the **Admin Console**. |
| **Production output handler** | Handle the creation of production output. |

When you enable **Experience pages** or **Admin Console pages**:

- Set **Base URL** to the HTTPS origin where your app is hosted. See [Hosting your extension](/GraFx-Developers/grafx-experience/overview/#hosting-your-extension).
- Add at least one page, with a title and a path that your app serves.

Experience pages then appear as a page type in the page editor, named after your extension. See [How extensions appear in the portal](/GraFx-Experience/concepts/extensions/#how-extensions-appear-in-the-portal).

## Next step

Build the app that runs inside the extension: [Build with the Extension SDK](/GraFx-Developers/grafx-experience/extension-sdk/).
