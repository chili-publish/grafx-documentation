# Roles and permissions

CHILI GraFx uses role-based access control. Every user has one or more **roles** that determine what they can see and do across the platform. Roles can be combined — a single user can be both a Subscription Admin and an Environment Admin, for example.

In addition to roles, **Template Designer Seats** grant extra permissions. Seats are a paid add-on with a limited number per subscription. Any role can be combined with a Template Designer Seat.

## Access matrix

The table below shows what each role can access. A Template Designer Seat (TDS) can be added to any role.

### Application access

|  | EU | SA | EA | TDS | CA[^1] |
|:---|:---:|:---:|:---:|:---:|:---:|
| ![smallapplogo](/assets/CHILI_LOGOS_OK-09.svg) GraFx Studio | ✅ | ✅ | ✅ | ✅ | ✅ |
| ![smallapplogo](/assets/CHILI_LOGOS_OK-09.svg) GraFx Studio — TD Workspace | 🚫 | 🚫 | 🚫 | ✅ | ✅[^1] |
| ![smallapplogo](/assets/CHILI_publisher_RGB.svg) GraFx Publisher | 🚫 | ✅ | ✅ | ✅ | ✅ |
| ![smallapplogo](/assets/CHILI_LOGOS_OK-11.svg) GraFx Media | 🚫 | ✅ | ✅ | ✅ | ✅ |
| ![smallapplogo](/assets/CHILI_LOGOS_OK-07.svg) GraFx Fonts | 🚫 | ✅ | ✅ | ✅ | ✅ |

### Feature access

|  | EU | SA | EA | TDS | CA[^1] |
|:---|:---:|:---:|:---:|:---:|:---:|
| Templates — view and use | ✅ | ✅ | ✅ | ✅ | ✅ |
| Templates — create and edit | 🚫 | 🚫 | 🚫 | ✅ | ✅[^1] |
| [Components](/GraFx-Studio/concepts/components/) — view and use | 🚫 | Read only | Read only | ✅ | ✅[^2] |
| [Components](/GraFx-Studio/concepts/components/) — create and edit | 🚫 | 🚫 | 🚫 | ✅ | ✅[^2] |
| User management | 🚫 | ✅ (subscription) | ✅ (environment) | 🚫 | 🚫 |

Users without component edit rights can open a component in read-only mode — the Template Designer Workspace opens, but no changes can be saved. Users without creation rights will not see the **Create component** button.

[^1]: [Content Administrator](#content-administrator-ca) is a legacy role for converted CHILI publisher Online customers. On a CPO pricebook, CA can create templates and access the TD Workspace. On a GraFx pricebook, a Template Designer Seat is required instead.
[^2]: CA on a CPO pricebook has read + write access to components. CA on a GraFx pricebook has no access to the components page.

## Roles

### Subscription Admin (SA)

A Subscription Admin manages the subscription(s) they are assigned to. This is the highest-level administrative role.

Permissions include viewing subscription details and usage reporting, managing users across all environments in the subscription (invite, update, remove), requesting add-ons, and contacting the Client Success Manager directly.

!!! tip
    A Subscription Admin can assign or remove the Subscription Admin role for other users.

### Environment Admin (EA)

An Environment Admin manages one or more CHILI GraFx environments, as assigned by a Subscription Admin.

Permissions include managing environment settings (e.g. branding), managing users within their environment(s) (invite, update, remove), and accessing all applications available to SA-level users within those environments.

### End User (EU)

An End User works within the CHILI GraFx environments they are assigned to. This is the default role and cannot be removed.

End Users can access GraFx Studio to create [My Projects](/GraFx-Studio/guides/create-projects/) based on Collections, using the fonts and media made available in the template. Access to other applications requires an additional role.

!!! info "Need to create templates?"
    If an End User needs to create or edit templates, they must be assigned a [Template Designer Seat](#template-designer-seat).

### Content Administrator (CA)

!!! warning "Legacy role"
    Content Administrator is only available to subscriptions converted from CHILI publisher Online. It is not visible on new subscriptions.

A Content Administrator can create and use GraFx Publisher templates with no seat limit for converted CHILI publisher Online customers.

For GraFx Studio, the impact depends on the pricebook: on a CPO pricebook, Content Administrators can create templates (output may be watermarked). On a GraFx pricebook, a [Template Designer Seat](#template-designer-seat) is required to create or edit templates.

## Template Designer Seat

A Template Designer Seat (TDS) is a paid add-on that grants template creation and editing permissions. The number of available seats is defined by your contract — if you have 100 users and 5 seats, only 5 users can hold this role at any time.

A Template Designer Seat can be assigned to any role: End User, Subscription Admin, or Environment Admin. Once assigned, the user gains access to the TD Workspace and can create, edit, and delete templates and components.

See [Template Designer Seat](/CHILI-GraFx/users/template-designer/) for how to assign and manage seats.

## Next steps

- [Invite users](/CHILI-GraFx/users/creation/) — create and invite users to your subscription or environment
- [Change roles](/CHILI-GraFx/users/update/) — update a user's role or environment access
- [Deactivate users](/CHILI-GraFx/users/deactivate/) — temporarily disable a user account
- [Delete users](/CHILI-GraFx/users/delete/) — permanently remove a user
