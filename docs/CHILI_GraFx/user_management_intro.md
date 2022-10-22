# User management

## Introduction

5 Basic concepts define the user management. Below you can find the details of each concept.

### Relation between concepts

``` mermaid
erDiagram
  GraFx-Subscription ||--|{ Resources : Has
  Permission ||--|{ Resources : Impacts
  Role ||--|{ Permission : Groups
  GraFx-UserGroup ||--|{ Role : Has-one-or-more
  GraFx-User ||--|{ Role : Has-one-or-more
  GraFx-UserGroup ||--|{ GraFx-User : Contains
```

### Resources

!!! Definition
	Any item that will be impacted by the user management system.
	
Let's start with resources, since they are the items undergoing the effect of permissions. All levels of over management will have an effect on resources in the Platform.

Sample resources: GraFx Media assets, GraFx Documents, Users, Environments

### GraFx Users

!!! Definition 
	A Person or system identified by a username that performs an operation over the resource
	
We defined a GraFx User as a person or a system. In many cases you will interact as a human with the GraFx UI. 

In some cases, you'll also need a system user, that can be used to interact with the GraFx API's. It's wise to unlink this system user from a person. In case the human user changes jobs or roles, you don't need to redefine the access or role for the system user.

### GraFx UserGroup

!!! Definition
	A list of 1 or more users, sharing the same role(s)

A group of users allows you to easily give the same role(s) to all the users in that group. 

All roles associated with a group of users will be associated with all members of the group

### permissions

!!! Definition
	The authorization to perform an operation over a resource. 
	
Sample permissions: 

create, read, update, delete an asset

create, read, update, delete a user

create, remove an environment

In order to be able to perform an action over a resource, the user needs to have the permission to do so.

Permissions in CHILI GraFx will never be assigned on an individual level, but allways be combined in a role.

### Roles

!!! Definition
	A set of permissions that eases the management of permissions to users or groups. Allows assigning multiple permissions to a user or a group of users without making individual assignments