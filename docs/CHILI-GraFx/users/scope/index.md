# User management

## Scope of roles

Roles on the Subscription level, have a different impact than a role on the Environment level.

When you are SubScription Admin, you can define who's an Environment Admin, for each Environment.

When you are (only) an Environment Admin, you don't have access to the subscription level.

The schema below shows the relation between the levels in a CHILI GraFx Subscription, to then explain the impact of access on these levels

``` mermaid
erDiagram
  CHILI-GraFx-Client ||--|{ GraFx-Subscription : Has-one-or-more
  GraFx-Subscription ||--|{ GraFx-Environment : Has-one-or-more
```

### A GraFx Subscription

Roles on the subscription level define access for all environments.
These contain operations like managing the lifecycle of users and environments.

### Environment

An environment is the base level, where documents are grouped to serve an application. The minimum restriction you can apply to a set of resources is the environment level.

### Roles

[Roles](../roles/) on the environment level affect only the specific environment.