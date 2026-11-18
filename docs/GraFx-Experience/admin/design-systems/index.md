# Design Systems in GraFx Experience

GraFx Experience exposes **Design Systems** created in **GraFx Studio** through the GraFx Experience extension.

This is where admins decide **which Design Systems are available**, how they are identified, and how they can be used in pages.

## Where this is configured

Admins manage Design Systems from the **GraFx Experience admin**, under the **GraFx extension**.

This section acts as the bridge between:
- Design Systems authored in GraFx Studio
- Pages and workflows built in GraFx Experience

Only Design Systems configured here can be used in the Experience portal.

## Templates list

The **Templates** view shows all Design Systems that are known to the Experience layer.

Each row represents one Design System and includes:

- **Name**  
  A landscape thumbnail of the main visual, the human-readable name shown to admins and, depending on configuration, to end users, and the internal reference used to identify the Design System in Experience.

- **Status**  
  **Active**, **Inactive** or **Expired**.

- **Version**  
  The published version that new projects use, with a chip when there is a draft or a failed sync.

- **Last updated**  
  When the template was last changed.

The **⋯** menu on each row offers **Open**, **Edit in GraFx Studio**, and **Set active** or **Set inactive**.

To add a Design System, click **Add template** and pick it from the templates in your CHILI GraFx environment. See [Configure a Design System](/GraFx-Experience/guides/configure-design-system/).

This overview helps admins verify which Design Systems are connected and ready for use.

## Making Design Systems available

A Design System becomes usable in Experience when:

- It exists and is published in **GraFx Studio**
- It is registered and active in the **GraFx Experience extension**
- Access is granted through groups and page visibility

Registering a Design System here does not automatically expose it to users.  
Availability is controlled through **pages, navigation, and access rules**.

## Relationship with pages

Pages in GraFx Experience reference Design Systems from this list.

This means:
- Pages can only use Design Systems that are registered here
- Removing or disabling a Design System makes it unavailable in pages
- Access to a Design System is further restricted by page and group settings

The extension defines *what is possible*; pages define *where it appears*.

## Admin responsibilities

In this section, admins typically:

- Verify that Design Systems from GraFx Studio are correctly linked
- Check version and draft status
- Keep references and names consistent
- Disable Design Systems that should no longer be used
- Coordinate changes with designers working in GraFx Studio

This ensures end users only work with approved and supported Design Systems.

## Key principle

- **GraFx Studio** defines *how a Design System works*
- **GraFx Experience (extension)** defines *which Design Systems are available*
- **Pages and access rules** define *who can use them and where*

This separation keeps design, governance, and execution clearly scoped.