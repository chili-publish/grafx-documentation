# Create a local extension

A local extension is built for your own GraFx Experience installation. You create it in the **Admin Console** for needs that are specific to your organization, such as a custom integration or an internal tool. It is never shared with other installations.

Every extension you build starts here. The local extension tells GraFx Experience what your app is, what it can access, and where it appears.

See also: [The concept of extensions](/GraFx-Experience/concepts/extensions/#shared-and-local-extensions)

## When to use a local extension

Use one when the shared extensions don't cover what you need, for example to:

- Connect GraFx Experience to an internal system
- Add your own pages to the portal or the **Admin Console**
- Handle production output with your own service

## Before you start

- You need admin access to the **Admin Console**.
- Choose the **Extension key** carefully. You can't change it later.

## Create the extension

1. In the **Admin Console**, go to **Extensions** > **Installed**.
2. Select **Create local extension**.
3. Fill in the [Basic information](#basic-information), [CMS content](#cms-content), [Authentication](#authentication), and [Capabilities](#capabilities) sections.
4. Save.

You can save before your app is deployed, and set the **Base URL** and **Active** later.

## Basic information

| Field | Description |
|---|---|
| **Extension key** *(required)* | Unique identifier. Lowercase letters and hyphens only, for example `my-extension`. Can't be changed later. |
| **Name** *(required)* | Display name of the extension. |
| **Active** | Turns the extension on. Leave it off while you set it up. |

## CMS content

What admins see in the list of installed extensions.

| Field | Description |
|---|---|
| **Icon** | Image for the extension. Select **Choose File** to upload one. |
| **Provider name** | The organization that provides the extension. |
| **Short description** | A short summary. |

## Authentication

| Field | Description |
|---|---|
| **Permissions** | The API permissions the extension needs. Search for and select each one. See [API permissions](#api-permissions). |
| **Auth type** | How the extension signs in to an external service. Set to **None** if it doesn't use one. |
| **SDK authentication** | Lets the extension's pages receive a token through the Extension SDK. Turn this on if the pages call the API. |

!!! note "About the token"
    The token is a JWT (JSON Web Token): a short-lived key that lets the extension act for the signed-in user. It only grants the permissions you selected. See [Authentication](/GraFx-Developers/grafx-experience/authentication/#extension-sdk-jwt-claims) for what it contains.

### API permissions

Extensions use the platform API to read and change data in GraFx Experience, such as users, projects, and assets. The **Permissions** field decides which parts of the API the extension can use.

Each permission combines a resource and an action:

| Permission | Allows |
|---|---|
| Read users | View users and groups |
| Read projects | View projects and their layouts |
| Read assets | View media in the library |
| Write assets | Add or update media in the library |

Keep in mind:

- **Grant only what's needed.** An extension that only shows media doesn't need write access.
- **Access is always limited.** The extension can only do what its permissions allow.
- **They apply to the extension, not the user.** A user's own [roles and group permissions](/GraFx-Experience/overview/roles-permissions/) are set separately.

!!! info "More permissions are coming"
    The Extension Framework is growing, so the list of permissions will too. Search the **Permissions** field to see what's available.

## Capabilities

| Capability | Description |
|---|---|
| **Experience pages** | Show pages in a space in the portal. |
| **Admin Console pages** | Add pages to the **Admin Console**. |
| **Production output handler** | Create production output with your own service. |

If you turn on **Experience pages** or **Admin Console pages**:

- Set **Base URL** to the HTTPS address where your app is hosted. See [Hosting your extension](/GraFx-Developers/grafx-experience/overview/#hosting-your-extension).
- Add at least one page, with a title and a path your app serves.

Experience pages then show up as a page type in the page editor, named after your extension. See [How extensions appear in the portal](/GraFx-Experience/concepts/extensions/#how-extensions-appear-in-the-portal).

## Next step

Build the app: [Build with the Extension SDK](/GraFx-Developers/grafx-experience/extension-sdk/).
