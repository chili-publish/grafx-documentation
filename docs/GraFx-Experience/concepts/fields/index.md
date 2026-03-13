# Fields

Fields are reusable metadata elements that allow admins to enrich templates, projects, and production entities with structured information.

A field is defined once and can then be assigned to templates, projects, production channels, or outputs. The same field can be used across multiple templates.

Fields are managed in the **general settings** of GraFx Experience — not inside the CHILI GraFx extension. This separation allows fields to be used beyond GraFx content, for example in other editors and tools in the platform, making it possible to define permissions and metadata consistently across content types.

## What fields are used for

Fields serve two distinct purposes:

**Categorization and filtering**
Fields can hold values that describe a template — for example, its type, intended output, or target region. End users can filter the campaigns page by these values to find the right template faster.

**Access control**
User group fields define which groups of users can see and work with a specific template. When a user group field is assigned to a template, only users belonging to one of the selected groups will see that template in the portal.

## Field types

More field types are being added over time. Currently supported:

**Select**
A list of predefined options. When assigned to a template, an admin picks one or more of those options as the field's value. Examples: Template Type (Employer Branding, Campaign, Social Media), Output Intent (Print, Digital), Region (Europe, North America).

Select fields can be used as filters on the campaigns page, and as display information on project cards.

**User Group**
Links a field to user groups defined in GraFx Experience. Used to control access — a template with a User Group field will only be visible to users who belong to one of the selected groups. When no User Group field is assigned to a template, the template is visible to all users.

![The Fields list in GraFx Experience general settings showing Select and User Group type fields](fields-list.png){.screenshot-full}

## Where fields are used

A field can be applied to one or more of the following:

| Applied to | Effect |
|---|---|
| Template | Controls visibility and filtering on the campaigns page |
| Project | Controls visibility in the projects overview and enables project-level filtering |
| Production channel | Controls which user groups can access a production channel |
| Production output | Controls which user groups can view specific production outputs |

## Relationship to templates

Fields are defined centrally and then assigned to individual templates. When a field is assigned to a template, an admin sets its value for that template. The same field (e.g. "Template Type") can have different values on different templates.

See [Manage fields](../../guides/manage-fields/) for step-by-step instructions on creating and assigning fields.
