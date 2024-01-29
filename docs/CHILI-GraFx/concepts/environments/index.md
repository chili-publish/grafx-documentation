# Environments in CHILI GraFx

## Introduction

In CHILI GraFx, an environment is a foundational concept that shapes how users interact with and manage their creative assets. Environments act as segregated, secure spaces where documents, templates, and other creative elements are stored and managed.

## Key Characteristics of Environments

### Isolation

One of the crucial features of an environment is its isolation from others. No data interchange or interaction is possible between different environments[^1]. This isolation ensures security and integrity of data, where each environment functions independently.

### Sandbox vs. Production Environments

CHILI GraFx offers two primary types of environments – the Sandbox and the Production environment. See [here](/CHILI-GraFx/concepts/sandbox/) for more info.

### Testing and Deployment

The existence of separate Sandbox and Production environments allows for thorough testing of new features. This process is crucial to identify and fix any issues before they impact the live version used by customers.

### User Interface and API

Both the user interface (UI) and the application programming interface (API) of CHILI GraFx are subject to this environmental split.

### Hosting and Control

CHILI GraFx environments can be hosted on multi-tenant or private tenant setups, depending on the contract. This aspect determines the control you have over the timing of updates in both Sandbox and Production environments.

[^1]: Using the API you could build a workflow, interacting with several environments, considering you have access to all environments. Through API calls, could access assets on different environments.
