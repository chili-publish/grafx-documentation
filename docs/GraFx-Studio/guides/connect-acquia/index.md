# Media Connector for Acquia DAM

|  | Connector type |
| --- | --- |
|  | Built-in |
| :fontawesome-regular-square-check: | Built by CHILI publish |
|  | Third party |

## Installation

Ask CHILI publish to activate on your environment

## Configuration

- Endpoint configuration
- Authentication for impersonation
- Authentication for machine-machine

Ask CHILI publish to setup configuration

## Governance

### Impersonation

GraFx Studio is a consumer of the assets available in the DAM. Therefore, the user that is used to impersonate the access to the DAM system, will dictate what assets are available in the template.

### Machine to machine

The credentials used to setup machine 2 machine, will dictate the governance on the assets in the automation setup. 

This means if the credentials only allow access to part of the assets, only these assets will be available when batch processing requests access to place assets in the output.

## Place assets in your template

- Select the right Connector
- Assign the asset to an image frame

## DAM Queries

DAM queries happen on the level of the connector, for a specific frame.

How to restrict what assets are shown to a template user.

### Variable DAM Queries

With the use of variables and/or GraFx Genie, you can set a text variable to hold a DAM query. This variable can be influenced, and used to serve as the DAM query.