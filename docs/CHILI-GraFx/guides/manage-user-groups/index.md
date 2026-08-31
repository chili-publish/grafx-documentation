# User Group Management

## Create User Group

Go to User Management, and click "Groups"

![Arrows pointing at the User Management icon in the side rail and at the Groups tab](ug000.png){.screenshot}

Start with "+ Create group".

![Empty Groups tab reading "No groups created", with a Create group button](ug001.png){.screenshot-full}

Give the user group a name. (Step 1/3)

![Create group dialog with the group name typed in, and a Next 1/3 button](ug002.png){.screenshot}

Give an (optional) description (Step 2/3)

![Description step of the wizard with a description typed in, showing Previous and Next 2/3](ug003.png){.screenshot}

Assign Access, similar to [Individual Access assignment](/CHILI-GraFx/guides/manage-individual-access/).

- Select the Environments the group has access to
- Select the Role everybody in this group will have, for this Environment

![Assign access step with the Select environments list open, offering one environment](ug004.png){.screenshot}

![Assign access step with an environment chosen and the Role list open on Environment Admin and End User](ug005.png){.screenshot}

The group will appear in the list, showing "0" members.

![Groups list with the new group listed under Name and Description, showing 0 members](ug006.png){.screenshot-full}

## Delete a User Group

To delete a group, select the group, en "Delete Group" under the Actions drop down menu

![Open Actions menu offering "Edit name and description" and, in red, "Delete group"](ug008.png){.screenshot}

Upon deletion, all members are removed from the group, and the related access is revoked.

Unless if the person still has access through [Individual Access](/CHILI-GraFx/guides/manage-individual-access/), or through membership of another group.

## Manage User Group Membership

See [Manage Group Membership](/CHILI-GraFx/guides/manage-group-membership/)

## Special group: [All users]

This group is available by default, and cannot be renamed.

The group contains all users from the current subscription.

This group can be used, to provide specific access for all users (current and new).

![The default All users row in the groups list, with its member count and subscription-wide description](allusers.png){.screenshot-full}