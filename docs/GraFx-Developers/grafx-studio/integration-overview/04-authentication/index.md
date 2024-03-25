# Authentication

As we progress with [Custom Connectors], the vision of a future where authentication is with GraFx Studio is no longer need. However, for the time being, utilizing default connectors and interacting with the Environment API necessitates the creation of integrations. An integration functions as a specialized user within your environment, facilitating the association of all user projects under a single set of credentials. This guide outlines the essential steps and considerations for setting up integrations, ensuring secure authentication processes.

## Importance of Secure Credential Handling

When setting up an integration, you're provided with a client ID and secret. These credentials are the keys to your digital kingdom and must be guarded with utmost diligence. Exposure of these details can lead to unauthorized access to your environment. It is paramount to store these credentials securely, preferably in a key store or as environment variables, to mitigate the risk of leaks.

## Project Association and Access

Integrations are special users, but it's critical to understand that projects are inherently bound to a single user. This binding implies that projects cannot be accessed by other integration users. Each integration is isolated, ensuring that one integration user cannot access the projects of another.

!!! warning

    It's important to note the exclusivity of project access. Projects are linked to a single user, and thus, cannot be accessed by other GraFx users. This exclusivity underscores the need for careful planning and setup of integrations to ensure appropriate access rights are assigned.

## Setting Up an Integration

To establish an integration, you must navigate to your preferred environment. During this process, it's crucial to assign all necessary permissions to the integration, tailoring its capabilities to your specific needs. Detailed instructions on creating an integration can be found in our comprehensive [integration guide](#).

## Understanding Different Tokens

Integrations necessitate two distinct types of users, each requiring different permissions:

1. **Read-only Permissions Integration**: Essential for use in the Studio Editor Engine within your custom UI. This integration type ensures that users can only view and not modify content.
2. **All Permissions Integration**: Required for full interaction with the Environment API. Tokens generated with all permissions should be handled with care and never exposed to the front-end.

!!! danger

    Tokens, especially those with comprehensive permissions, pose a significant security risk if mishandled. Tokens cannot be invalidated and will have their permissions until they expire. It's imperative to manage these tokens with extreme caution to prevent unauthorized access.

!!! note

    The authentication endpoint caches tokens. A new token is usually generated around 1 hour before the current token expires.
