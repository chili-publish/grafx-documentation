# Sandbox vs Production

## Sandbox

A sandbox environment is like a test version of the CHILI GraFx platform or applications, with its own separate data. It is a safe place to experiment with new features, explore connectors and extensions, and try out integrations without affecting the live production data.

This means that any changes made in the sandbox will not affect the production data.

Output generated in a sandbox environment has a watermark and does not count as a [render](/CHILI-GraFx/concepts/renders/).

![Sandbox output of a "Citytrip to Paris" poster, with a diagonal SAMPLE watermark across it](sample.jpeg){.screenshot}

### What you can use it for

- **Explore connectors.** Set up and try [media and data connectors](/GraFx-Studio/concepts/connectors/), or build and debug your own, without affecting production.
- **Try extensions and integrations.** Connect extensions such as the [CHILI GraFx extension](/GraFx-Experience/concepts/chili-grafx-extension/), or integrations that call the API, and see how they work end-to-end.
- **Try new versions.** Check new features and your existing setup on a newer GraFx Studio version before you move production to it. See [Testing](#testing).

### Templates

Build and maintain templates in a production environment. Designers need a [Template Designer Seat](/CHILI-GraFx/concepts/subscriptions/#template-designer-seats) there.

A sandbox is for trying things out, not for building or keeping your template library. Sandbox data stays in the sandbox. Templates saved there do not move to production.

## Production

Production is the live version of CHILI GraFx that customers use to access and use the actual platform and applications. It is where all the real work happens, including building and maintaining templates, and any changes you make in production immediately reach end users.

## Why two environments?

The reason for having a separate sandbox is to allow developers, testers, and customers to try things out, such as new features, connectors, extensions, and integrations, without affecting the live production data. This lets you identify and fix any issues before they affect the people who use the live version.

## UI and API

Both the platform and application UI (the way the platform looks) and API (the way the platform works behind the scenes) are subject to the split between sandbox and production.

## Testing

We encourage you to set up a strategy to include testing the sandbox as part of your product or platform lifecycle.

Releases are available to all environments at the same time. If you pin the GraFx Studio version on production, you can move the sandbox to a newer version first, try it with your own setup, and update production when you are confident. See [Manage Environment Version](/CHILI-GraFx/guides/manage-environment-version/).

## Sandbox on multitenant vs private tenant

Depending on your contract, CHILI GraFx is hosted on a multitenant or private-tenant setup.

CHILI GraFx updates the sandbox at the same time for all customers on the same tenant.

With a private tenant, you have more control over when your sandbox and production environments are upgraded.
