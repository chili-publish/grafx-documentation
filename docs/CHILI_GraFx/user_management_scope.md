# User management

## Scope of permissions

The scope of the permissions is the concept that not all permissions have the same impact. Some permissions have impact on a different level.

The schema below shows the relation between the levels in a CHILI GraFx Subscription, to then explain the impact of permissions (roles) on these levels

``` mermaid
erDiagram
  CHILI-GraFx-Client ||--|{ GraFx-Subscription : Has
  GraFx-Subscription ||--|{ GraFx-Environment : Has
```

### A GraFx Subscription

Roles defined on the Subscription level have permission with impact for all environments.
These contain operations like managing the lifecycle of identities and environments.

### Environment

An environment is the smallest level, where documents are grouped to serve an application. The minimum restriction you can apply to a set of resources, is the environment level.

### Roles

[Roles](/CHILI_GraFx/user_management_roles/) (and permissions) on the environment level affect only the specific environment.