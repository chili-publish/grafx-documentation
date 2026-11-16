# Extensions

An extension adds functionality to GraFx Experience. The portal provides the basics: users, groups, spaces, pages, and navigation. Extensions add specific capabilities on top, such as creative automation, media management, translations, or a connection to an external system.

Extensions are built on the **GraFx Extension Framework**. The Extension Framework defines how an extension registers itself, what it can access, and where it shows up for admins and end users.

## Why extensions

Every organization needs a slightly different portal. GraFx Experience keeps the core lean, and extensions add what you need:

- A capability that is part of the product, enabled through your license
- An integration with a system you already use
- A custom tool for your own organization

For example, the [CHILI GraFx extension](/GraFx-Experience/concepts/chili-grafx-extension/) brings Design Systems from GraFx Studio into the portal.

## Shared and local extensions

**Shared extensions** are built once and used by many installations. They are enabled on your installation through your license. The CHILI GraFx extension is a shared extension.

**Local extensions** are built for your installation only. Your admins create them in the **Admin Console** for needs that are specific to your organization, such as a link to an internal system or a custom internal tool. A local extension is never shared with other installations.

To build one, see [Create a local extension](/GraFx-Developers/grafx-experience/create-local-extension/).

## What an extension can do

An extension's **capabilities** define what it adds:

| Capability | What it adds |
|---|---|
| **Experience pages** | Pages in a space in the portal |
| **Admin Console pages** | Pages in the **Admin Console** |
| **Production output handler** | Production output handled by the extension's own service |

An extension also has **API permissions**. They define which parts of the platform API it can use, such as reading users or writing assets. An extension only gets the permissions selected for it, never full access.

!!! note "Extension permissions are not user permissions"
    API permissions control what the extension can do. A user's [roles and group permissions](/GraFx-Experience/overview/roles-permissions/) are set separately.

## How extensions appear in the portal

An extension with experience pages adds its own page type to the page editor, named **{Extension name} page**. Which page types you see depends on the extensions installed and active on your installation.

Each extension page has two sets of settings:

| Settings | Opened from | Controls |
|---|---|---|
| **Extension settings** | **Configure** in the page editor | What the extension shows and how it behaves |
| **Page settings** | **⋯** next to the page, then **Page settings** | Title, navigation name, access, and menu visibility |

Extension settings are stored per page, so two pages of the same type can use different options, such as a different filter. The settings are kept when you export or import page JSON.

!!! tip "Check both"
    A page can be configured correctly and still be hidden if it is disabled in **Page settings** or if a parent folder restricts access. See [Visibility & access](/GraFx-Experience/admin/page-visibility/).

## Where extensions are managed

Admins manage extensions in the **Admin Console** under **Extensions** > **Installed**. Every extension opens on a detail page with the same layout:

| Area | What you find |
|---|---|
| **Header** | Extension name and short description |
| **Side navigation** | Sections such as **Authentication** and **Settings** |
| **Main panel** | Forms and tables for the selected section |
| **Save bar** | Appears when you have unsaved changes |

Extensions that connect to an external service usually have:

- **Authentication**: client IDs, secrets, endpoints, and redirect URIs
- **Settings**: how the extension behaves once connected

If an extension signs in to an external platform with OAuth, register its **redirect URIs** on that platform exactly as GraFx Experience shows them, including `https`, trailing slashes, and paths. You can add up to three redirect URIs per extension.

If a shared extension is missing under **Installed**, contact CHILI publish.

## Build your own extension

An extension is a web app that GraFx Experience embeds in the portal or the **Admin Console**. The Extension SDK takes care of the connection and authenticated API calls.

!!! info "You choose where your extension runs"
    You host the extension app yourself, or your customer or a third party hosts it. For now, CHILI GraFx does not host extension apps. See [Hosting your extension](/GraFx-Developers/grafx-experience/overview/#hosting-your-extension).

Get started in the Developer Center: [Extend GraFx Experience](/GraFx-Developers/grafx-experience/overview/).
