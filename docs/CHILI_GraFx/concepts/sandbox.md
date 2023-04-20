# Sandbox vs Production

## Sandbox

A sandbox deployment is like a test version of the CHILI GraFx platform or applications that allows you to experiment with new features without affecting the live production data. With each new release, the sandbox deployment will have the latest version of the platform and/or applications, but with separate data. 

This means that any changes made in the sandbox will not affect the production data. The sandbox allows you to test new features to make sure they work properly before they are used in the live version.

## Production

Production is the live version of CHILI GraFx that customers use to access and use the actual platform and applications. It is where all the real work happens, and any changes made in production are immediately reflected to the end-users. 

## Why two versions?

The reason for having a separate sandbox deployment is to allow developers, testers, and customers to test new features without affecting the live production data. This is important because it ensures that any issues or bugs are identified and fixed before they affect the people who are using the live version.

## UI and API

Both the platform and application UI (the way the platform looks) and API (the way the platform works behind the scenes) are subject to the split between sandbox and production. Whenever there are new features added to the platform or applications, they are first deployed in the sandbox before being used in production.

## Testing

We encourage you to setup a strategy to include testing the sandbox deployment as part of your product or platform lifecycle. This will ensure a more stable result.

## Sandbox on multi tenant vs private tenant

Depending on your contract CHILI GraFx is hosted on a multi-tenant or private tenant setup.

The timeframe when a Sandbox is updated is equal for all customers on the same tenant.

With a private tenant, you have more control on the timing when a Sandbox or Production setup is upgraded.