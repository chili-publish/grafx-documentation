# User management

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
- User management for all users in the subscription (CRUD actions)
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

### Environment Admin

**Definition**: An Environment Admin manages the CHILI GraFx environment(s) where he is assigned to by his Subscription Admin

Permissions

- Access to environments where you are Environment Admin
- View overview of all the environments where you are Environment Admin
- Access to GraFx Publisher
- Manage the CHILI GraFx environment where you are Environment Admin
	- Environment Settings (eg. branding)
	- User management (CRUD actions) for the users of environments where you are Environment Admin
- Invite users to the Environment

In the API, this is labeled as "EA".

### User

**Definition**: A **User** works as an end user in the CHILI GraFx environment(s) where they are assigned to. This is the default role, and cannot be removed.

Permissions

- Access to the environments the user is assigned to
- View overview of all the environments where the user is Environment User
- Limited in what applications they can access (see table below)

In the API, this is labeled as "EU".

!!! Warning "Template Designer"
	- If an Environment user wants to create templates in the CHILI GraFx environment this user needs to have an additional role: [Template Designer](#template-designer).
	See also [Phased approach in roles](#overview-of-role-access)

### Template Designer

See the [Template Designer Seat](/CHILI-GraFx/users/template-designer-seat/) page

### Content Administrator

**Definition**: A content Administrator is a legacy role, available to users that have been converted from CHILI publisher Online.

A content Administrator can create and use GraFx Publisher templates. There is no limit to Content Administrators for converted CHILI publisher Online customers.

This role will not be visible to Subscriptions without a prior CHILI publisher Online subscription.

Content Administrators will be able to create templates in GraFx Studio, but the output will be watermarked in [phase 2](#phase-2-2024).

## Overview of Role Access

We're enhancing our SaaS platform's user management through a phased approach. 

Currently, Subscription Admins and Environment Admins can create templates to familiarize themselves with the system. 

However, these shouldn't be part of your main workflow, as permissions will change in upcoming phases. We're working towards an optimized platform, and we appreciate your adaptability during this transition.

### Phase 1 (today)

| Roles | User | SA | EA | TD | CA |
|:---:|:---:|:---:|:---:|:---:|:---:|
|![smallapplogo](/assets/CHILI_publisher_RGB.svg)| 🚫 | ✅ | ✅ | ✅ | ✅ |
|![smallapplogo](/assets/CHILI_LOGOS_OK-09.svg)<br/>TD Workspace| 🚫 | ✅ | ✅ | ✅ | ✅|
|![smallapplogo](/assets/CHILI_LOGOS_OK-09.svg)| ✅ | ✅ | ✅ | ✅ | ✅ |
|![smallapplogo](/assets/CHILI_LOGOS_OK-07.svg)| 🚫 | ✅ | ✅ | ✅ | ✅ |
|![smallapplogo](/assets/CHILI_LOGOS_OK-11.svg)| 🚫 | ✅ | ✅ | ✅ | ✅ |

### Phase 2 (End of 2023)

| Roles | User | SA | EA | TD | CA |
|:---:|:---:|:---:|:---:|:---:|:---:|
|![smallapplogo](/assets/CHILI_publisher_RGB.svg)| 🚫 | ✅ | ✅ | ✅ | ✅ |
|![smallapplogo](/assets/CHILI_LOGOS_OK-09.svg)<br/>TD Workspace| 🚫 | 🚫 | 🚫 | ✅ | ✅(1)|
|![smallapplogo](/assets/CHILI_LOGOS_OK-09.svg)| ✅ | ✅ | ✅ | ✅ | ✅ |
|![smallapplogo](/assets/CHILI_LOGOS_OK-07.svg)| 🚫 | ✅ | ✅ | ✅ | ✅ |
|![smallapplogo](/assets/CHILI_LOGOS_OK-11.svg)| 🚫 | ✅ | ✅ | ✅ | ✅ |


In phase 2, Subscription Admins and Environment Admins will have the opportunity to function as Template Designers when they are allocated a Template Designer Seat.

(1) Content Admins will be able to create Templates, but the output will be watermarked.

!!! Info "Legend"
	**Roles**

	- *SA*: Subscription Admin
	- *EA*: Environment Admin
	- *TD*: Template Designer
	- *CA*: Content Admin

	**Specific application**

	- *TD Workspace*: The workspace where Template Designers can edit Smart Templates

## User creation and invitation

### First user

The first user will be the subscription admin, and is created by CHILI GraFx, as a result of a signed contract.

### Subsequent Users

All users (except the first (subscription admin) user) can be invited to CHILI GraFx by

- A Subscription Admin
- An Environment Admin

Only the Subscription Admin & the Environment Admin can access the User Management page on CHILI GraFx where they can:

- view an overview of the users
- view an overview of the roles on CHILI GraFx
- invite users to CHILI GraFx

## Changing roles

Click here to see how to [change roles & Environment access](/CHILI-GraFx/users/update/).
