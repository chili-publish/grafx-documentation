# User management

## Overview of Role Access

| Roles | End User | SA | EA | TD | CA |
|:---:|:---:|:---:|:---:|:---:|:---:|
|![smallapplogo](/assets/CHILI_publisher_RGB.svg)| 🚫 | ✅ | ✅ | ✅ | ✅ |
|![smallapplogo](/assets/CHILI_LOGOS_OK-09.svg)<br/>TD Workspace| 🚫 | 🚫 | 🚫 | ✅ | ✅(1)|
|![smallapplogo](/assets/CHILI_LOGOS_OK-09.svg)| ✅ | ✅ | ✅ | ✅ | ✅ |
|![smallapplogo](/assets/CHILI_LOGOS_OK-07.svg)| 🚫 | ✅ | ✅ | ✅ | ✅ |
|![smallapplogo](/assets/CHILI_LOGOS_OK-11.svg)| 🚫 | ✅ | ✅ | ✅ | ✅ |


Subscription Admins and Environment Admins can function as Template Designers when they are allocated a Template Designer Seat.

(1) Content Admins will be able to create Templates, but the output will be watermarked.

!!! Info "Legend"
	**Roles**

	- *End User*: [End User](#end-user)
	- *CA*: [Content Admin](#content-administrator)
	- *EA*: [Environment Admin](#environment-admin)
	- *TD*: [Template Designer](#template-designer)
	- *CA*: [Content Admin](#content-administrator)

	**Specific application**

	- *TD Workspace*: The workspace where Template Designers can edit Smart Templates in GraFx Studio
	
## Roles

### Subscription Admin

**Definition**: A Subscription Admin manages the subscription(s) they are assigned to

Permissions

- View all subscription(s) assigned to
- View usage reporting
- View subscription details
- View overview of all the environments in a subscription
- Request add-ons (eg. extra storage)
- Directly contact to Client Success Manager
- User management for all users in the subscription (CRUD)
- Invite users to all available environments in the subscription

In the API, this role is labeled as "SA".

!!! info "CRUD?"
	CRUD is an acronym for
	- Create (users in this case, i.e. Invite users)
	- Retrieve (see the user list)
	- Update (change details of a user)
	- Delete (remove them from the list)

!!! Tip "Subscription Admin"
	**Important**: a Subscription Admin can assign the role 'Subscription Admin' to other users on 'User Detail page'.
	A Subscription Admin can take away the role of another **Subscription Admin**.

### Environment Admin

**Definition**: An Environment Admin manages the CHILI GraFx environment(s) where they are assigned to by their Subscription Admin

Permissions

- Access to environments where you are Environment Admin
- View overview of all the environments where you are Environment Admin
- Manage the CHILI GraFx environment where you are Environment Admin
	- Environment Settings (eg. branding)
	- User management (CRUD actions) for the users of environments where you are Environment Admin
- Invite users to the Environment

In the API, this is labeled as "EA".

### End User

**Definition**: An "End User" works as an end user in the CHILI GraFx environment(s) where they are assigned to. This is the default role, and cannot be removed.

Permissions

- Access to the environments the End User is assigned to
- View overview of all the environments where the End User has access
- Limited in what applications they can access (see table)
- Create "[My projects](/GraFx-Studio/guides/create-projects/)" based on Collections (using fonts & media that are made available in the template)

In the API, this is labeled as "EU". (End User)

!!! Warning "Template Designer"
	- If an End User wants to create templates in the CHILI GraFx environment this user needs to have an additional role: [Template Designer](#template-designer).
	See also [Phased approach in roles](#overview-of-role-access)

### Template Designer

See the [Template Designer Seat](/CHILI-GraFx/users/template-designer-seat/) page

### Content Administrator

**Definition**: A content Administrator is a legacy role, available to users that have been converted from CHILI publisher Online.

A content Administrator can create and use GraFx Publisher templates. There is no limit to Content Administrators for converted CHILI publisher Online customers.

This role will not be visible to Subscriptions without a prior CHILI publisher Online subscription.

Content Administrators will be able to create templates in GraFx Studio, but the output will be watermarked in [phase 2](#phase-2-2024).

## User creation and invitation

### First user

The first user will be the subscription admin, and is created by CHILI publish, as a result of a signed contract.

### Subsequent Users

All End Users (except the first (subscription admin) user) can be invited to CHILI GraFx by

- A Subscription Admin
- An Environment Admin

Only the Subscription Admin & the Environment Admin can access the User Management page on CHILI GraFx where they can:

- view an overview of the users
- view an overview of the roles on CHILI GraFx
- invite users to CHILI GraFx

## Changing roles

Click here to see how to [change roles & Environment access](/CHILI-GraFx/users/update/).