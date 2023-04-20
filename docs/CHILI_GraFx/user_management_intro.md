# User management

## Introduction

4 basic concepts define the user management. Below you can find the details of each concept.

There are 4 different concepts that make up the user management process in CHILI GraFx.

	- Resources
	- Permissions
	- Roles
	- CHILI GraFx Users
 
Let's dive in to each concept below to see what they do, and how they relate.

### Resources

!!! Definition
	Any item that will be impacted by the user management system.
	
Resources are items that make up CHILI GraFx. Control and management of these resources require the proper _permissions_

**Example resources:**

GraFx Media assets, GraFx Templates, Users, Environments

!!! Definition 
	A Person or system identified by a username that performs an operation over the resource
	
We defined a CHILI GraFx User as a person or a system. In many cases you will interact as a human with the CHILI GraFx UI. 

In some cases, you'll also need a system user, that can be used to interact with the CHILI GraFx API's. It's wise to unlink this system user from a person. In case the human user changes jobs or roles, you don't need to redefine the access or role for the system user.

### Permissions

!!! Definition
	The authorization to perform an operation over a resource. 

In order to be able to perform an action over a resource, the user must have a role assigned to them that contains the proper permission to do so.

Permissions in CHILI GraFx not assigned on an individual user, but are assigned to a *Role*.

**Examples**

create, read, update, delete an asset

create, read, update, delete a user

create, remove an environment

### Roles

!!! Definition
	A set of permissions that eases the management of permissions to users or groups.
  
Normally users are going to have more than just a single permission. It is also likely that you may want to be able to update the permissions of multiple users simultaneously. Roles make this possible.

A Role is a container for permissions. Roles should contain all the necessary permissions needed for an intended purpose or workflow. 


### CHILI GraFx Users

!!! Definition 
	An individual with access to GraFx.
	
A user is someone that has credentials to GraFx. A user can have 1 or more roles assigned to them. These roles will dictate the permissions that the user have which in turn controls their ability to view, create, update, and destroy resources in GraFx


 
### Relation between concepts

``` mermaid
erDiagram
  GraFx-Subscription ||--|{ Resources : Has
  GraFx-Subscription ||--|{ GraFx-User : Has
  Permission ||--|{ Resources : Impacts
  Role ||--|{ Permission : Has
  GraFx-User ||--|{ Role : Has-one-or-more
```
