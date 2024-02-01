# User Management

## Introduction

Five basic concepts define user management. Below you can find the details of each concept.

There are four different concepts that make up the user management process in CHILI GraFx:

- Resources
- Access
- Roles
- CHILI GraFx Users
- User Groups

Let's dive into each concept below to see what they do, and how they relate.

### Resources

!!! Definition
    Any item that will be impacted by the user management system.

Resources are items that make up CHILI GraFx. Control and management of these resources require the proper _access_.

An example of resources are collections. You can give access to collections through user groups (soon).

**Example resources:**

GraFx Media assets, GraFx Templates, Users, Environments

### Access

!!! Definition
    The authorization to perform an operation over a resource.

In order to perform an action over a resource, the user must have a role assigned to them that contains the proper permission to do so.

Permissions in CHILI GraFx are not assigned on an individual user basis, but are assigned to a *Role*.

**Examples**

- Create, read, update, delete an asset
- Create, read, update, delete a user
- Create, remove an environment

### Roles

!!! Definition
    A set of permissions that eases the management of permissions for users or groups.
 
Normally users will have more than just a single permission. It is also likely that you may want to update the permissions of multiple users simultaneously. Roles make this possible.

A Role is a container for permissions. Roles should contain all the necessary permissions needed for an intended purpose or workflow.

### CHILI GraFx Users

!!! Definition
    A person or system identified by a username that performs an operation over a resource

We define a CHILI GraFx User as a person or a system. In many cases, you will interact as a human with the CHILI GraFx UI. 

In some cases, you'll also need a system user, which can be used to interact with the CHILI GraFx APIs. It's wise to unlink this system user from a person. In case the human user changes jobs or roles, you don't need to redefine the access or role for the system user.

### User Groups

User Groups in CHILI GraFx represent a collection of users — in the same subscription — who share common access needs and roles. Each user group is defined by the access and roles, which collectively determine the actions members of the group can perform in the system. By categorizing users into groups, you simplify access management, allowing administrators to efficiently assign and modify access rights for multiple users simultaneously, enhancing both security and operational efficiency.

Access to a resource (e.g., Environment) is additive. Meaning if you get End User access through group 1, and Environment Admin access through membership of group 2, you will have both access levels assigned.

### Relation Between Concepts

``` mermaid
erDiagram
  GraFx-Subscription ||--|{ Resources : Has
  GraFx-Subscription ||--|{ GraFx-User : Has
  Access ||--|{ Resources : Impacts
  Role ||--|{ Access : Defines
  GraFx-User ||--|{ Role : Has
  User-Group ||--|{ GraFx-User : Has
  User-Group ||--|{ Role : Has
```
