# Branding & login

Tenant admins control how the portal looks before and after users log in: the logo in the main navigation, the icon in the browser tab, the images on the login page, and the visuals of each space.

## Where branding images are set

| Image | Where to set it | Where it appears |
|---|---|---|
| Tenant logo | **Admin Console → General settings** | Main navigation, when the active space has no logo of its own |
| Tenant favicon | **Admin Console → General settings** | Browser tab |
| Login page background images | **Admin Console → Login appearance** | Login page — several images can be added and are rotated |
| Space logo | **Admin Console → Spaces → create / edit** | Main navigation, spaces list, and launchpad cards for that space |
| Space favicon | **Admin Console → Spaces → create / edit** | Browser tab while the user is in that space. Enable **Use logo as favicon** to reuse the space logo |
| Layouts page image | Page settings of the Layouts page | Cover image of the Layouts page |

The main navigation has no separate logo upload: it shows the space logo if one is set, and the tenant logo otherwise.

During onboarding of a new tenant, the logo entered in the branding step is applied to every space, so the portal is branded from the first login.

## Where the images are stored

All branding images are selected from your local device. Where they are stored depends on how your tenant was set up:

- **Tenants with the Assets extension** keep working as before: space images, Layouts page images and file settings are stored in the Assets extension; tenant logo, favicon and login images are stored in GraFx Experience.
- **New GraFx tenants without the Assets extension** upload every branding image to **GraFx Media** in the connected CHILI GraFx environment, through the environment's default media connector. GraFx Experience keeps a copy for display, so the portal does not depend on the connector at render time.

Replacing or removing a branding image only clears the reference in GraFx Experience. The original file in GraFx Media is never deleted, so it stays available to other pages or templates that use it.

## Image requirements

- Images only. Videos and other file types are not accepted for branding.
- Favicons uploaded to GraFx Media must be **PNG** and no larger than **250 KB**. A file that does not meet these rules is rejected before upload, and the previous favicon stays in place.
- Favicons stored in the Assets extension accept `.ico`, `.svg` and `.png`, with the same 250 KB limit.
- Logos, favicons and login images are displayed at their stored resolution. Upload them at the size you want them shown.

## Images in CMS pages

Images placed in pages — inline images, card images, banner and slider backgrounds — are picked through the CMS image picker. On tenants without the Assets extension, the picker browses the default media connector of your CHILI GraFx environment and can upload new images to GraFx Media. Images on pages are automatically resized for the container they appear in and delivered as WebP, so pages stay fast; SVG and GIF files are served as-is.

The resized copies are only used for pages. GraFx Studio and output generation always use the original, high-resolution asset.
