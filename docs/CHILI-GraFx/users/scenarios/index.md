# User management

## Scenarios

### Brand Owner

As the owner of the access to CHILI platform, you will have the Subscription Admin access.

How you organize the other levels will depend on your organization.

The main thought process is: who needs access to one or more resources, and how do I combine or separate these resources?

**Example 1**: Brand-owner with 1 brand.

All resources for your brand can be stored into 1 Environment.

Environment Admin is the Brand Manager, or whoever is responsible for managing the brand assets and smart templates.

End-users are the consumers of the templates, able to make publications. These end-users could be local marketing responsibles.

**Example 2**: Brand-owner with multiple brands, available worldwide

Each brand has its own Environment.

Subscription Admin: IT responsible, Global Brand manager, CMO

Environment Admin is the brand manager, responsible for the group of smart templates, related to his/her group of brands.

End-users are the consumers of the templates, able to make publications. They can be the local marketing users.

### Solution Provider

You build a software solution, and part of the features is the interaction with a smart template.

E.g. A Brand management portal to allow people to create publications based on Smart Templates.

In this scenario, you - The solution Provider - is the CHILI publish customer.

How you setup the access to Environments, depends on you. Below 2 examples, with only a slight difference, but a huge impact when done right.

### Solution Provider (End-users have CHILI GraFx access)

Imagine, a Brand "B" using the Brand management Portal of Solution provider "SP".

It might be a scenario where "B" has direct access to the CHILI GraFx Environments and other resources used in this context.

"SP" consumes the Smart Templates and other resources in their Brand Management Portal, and might augment the functionality with their solution.

The solution provider is the Subscription Admin.

The Brand "B" can be: (choice of the Solution Provider)

- Environment Admin
- Environment User

### Solution Provider (End-users have NO CHILI GraFx access)

Similar scenario as above, but the Brand "B" has no access to the templates directly in CHILI GraFx.

The Solution Provider has build a full management shell, where also the managent of Smart Templates and resources is handled by "SP"'s portal.

"SP" can still choose to have 1 environment, or even a full Private Tenant for each of their customers. That choice will be driven by the level of data separation needed.
Another driver could be the storage region required by the Brand.

Subscription Admin: "SP"

Environment Admin: "SP"

Environment User: "SP" (or a service account consuming the API)

The users at the Brand would be fully handled in the "SP"'s portal.