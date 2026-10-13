# Extensions

An extension adds functionality to GraFx Experience. The portal itself provides the foundation — users, groups, spaces, pages, and navigation — and extensions plug into that foundation to bring in specific capabilities, such as creative automation, media management, translations, or a connection to an external system.

Extensions are built on the **GraFx Extension Framework**. The Extension Framework defines how an extension registers itself, which parts of the platform it can reach, and how it shows up for admins and end users.

## Why extensions

Every organization needs a slightly different portal. Instead of building every capability into the core, GraFx Experience keeps the core lean and lets extensions add what an installation needs:

- A capability that is part of the product, enabled through your license
- An integration with a system you already use
- A custom tool that only makes sense for your own organization

The [CHILI GraFx extension](/GraFx-Experience/concepts/chili-grafx-extension/) is an example: it is the extension that brings Design Systems from GraFx Studio into the portal.

## Shared and local extensions

There are two kinds of extensions.

**Shared extensions** are built once and made available to many installations. They are enabled on your installation as part of your license. The CHILI GraFx extension is a shared extension.

**Local extensions** are bespoke to your own installation. Your admins create and manage them directly in the **Admin Console** to solve a use case that is unique to your organization — for example, a connection to an internal system or a custom internal tool. A local extension applies to your installation only and is never shared with other installations.

See [Create a local extension](/GraFx-Developers/grafx-experience/create-local-extension/) to build your own.

## What an extension can do

What an extension can do is defined by its **capabilities**:

| Capability | What it adds |
|---|---|
| **Experience pages** | Pages that render inside the portal, in a space |
| **Admin Console pages** | Pages for admins in the **Admin Console** |
| **Production output handler** | Handling of production output with the extension's own service |

Next to its capabilities, an extension has **API permissions**. These define which parts of the platform API the extension may reach — for example, reading users or writing assets. Permissions are always scoped: an extension never receives full access to the platform, only the permissions selected for it.

!!! note "Extension permissions are not user permissions"
    API permissions define what the extension itself may do through the API. They are separate from the [roles and group permissions](/GraFx-Experience/overview/roles-permissions/) of the person using it.

## How extensions appear in the portal

An extension with experience pages adds its own page types to the page editor. When you add a page, the list of page types shows whichever types your enabled extensions expose, named **{Extension name} page**. The list differs per installation — it depends on which extensions are installed and active.

Each extension page has two layers of settings:

| Layer | Opened from | Controls |
|---|---|---|
| **Extension settings** | **Configure** in the page editor | What the extension shows on the page and how it behaves |
| **Page settings** | **⋯** next to the page → **Page settings** | Title, navigation name, access, and visibility in the menu |

The extension defines its own settings and stores them per page. Two pages of the same type can therefore use different options — for example, a different entry point or filter. These settings are kept when you export or import page JSON across spaces.

!!! tip "Both layers matter"
    An extension page can be configured correctly and still be hidden from users if the page is disabled in **Page settings**, or if a parent folder restricts access. See [Visibility & access](/GraFx-Experience/admin/page-visibility/).

## Where extensions are managed

Admins manage extensions in the **Admin Console** under **Extensions** > **Installed**. Each installed extension opens on a detail page with the same layout:

| Area | What you find |
|---|---|
| **Header** | Extension name and short description |
| **Side navigation** | Sections for this extension — for example **Authentication** or **Settings** |
| **Main panel** | Forms and tables for the selected section |
| **Save bar** | Appears when you have unsaved changes |

Extensions that connect to an external service usually have two sections:

- **Authentication** — connection details, such as client IDs, secrets, endpoints, and redirect URIs
- **Settings** — how the extension behaves once the connection works

If an extension uses OAuth to sign in to an external platform, its **redirect URIs** must be registered on that platform exactly as shown in GraFx Experience — including `https`, trailing slashes, and path segments. You can add up to three redirect URIs per extension.

If a shared extension does not appear under **Installed**, contact CHILI publish.

## Build your own extension

Developers can build an extension as a web app that GraFx Experience embeds in the portal or the **Admin Console**. The Extension SDK handles the connection to the platform and authenticated API calls.

See [Extend GraFx Experience](/GraFx-Developers/grafx-experience/overview/) in the Developer Center.
