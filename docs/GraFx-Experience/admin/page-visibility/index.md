# Visibility & access

Admins control who can see pages and content in GraFx Experience by combining **visibility settings** with **group-based access rules**. This determines what each user sees in navigation and what they can reach via links.

## Access control

Each page can restrict access so only certain users see it.

- By default, a page inherits permissions from its parent folder or space.
- You can choose specific groups that are allowed to access the page.
- Users only see pages they have permission to access.

Access control works at the group level. If a user is not in any of the selected groups, the page will be hidden from them.

## Visibility settings

### Enable page

- When **enabled**, the page is active and accessible to users who have permission.
- When **disabled**, the page is hidden in navigation and cannot be reached even via direct link.

Disabled pages do not show up anywhere for end users.

### Hide from navigation

- The page still exists and is accessible if a user has permission and the direct link.
- The page is **not shown in navigation menus**.

Use this when you want a page reachable only from specific links or workflows but not listed in menus.

## Navigation & visibility interaction

Navigation is automatically built from the enabled pages that a user can access:

- Only pages that are both **enabled** and **permitted for the user’s group(s)** appear in menus.
- A page can be available via direct link even if hidden from menus.

This lets admins create targeted entry points or landing pages without cluttering the navigation.

## Best practices for visibility

- Use page visibility to simplify menus for different audiences.
- Restrict access at the folder level when possible to reduce repeated settings.
- For pages used in deep links or campaigns, use hidden visibility instead of disabling.
- Test visibility by logging in as a user with different group combinations.

## Summary

Visibility and access settings work together:

- **Access** defines who can retrieve the page.
- **Enable/disable** controls whether the page is live at all.
- **Hide from navigation** controls whether it appears in menus.

Combined with group permissions, admins shape what each user experiences without changing the underlying content.