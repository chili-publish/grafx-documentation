# GraFx Studio Overview

GraFx Studio is a smart document editor targeting both digital and print.

GraFx Studio encompasses three distinct parts:

- Editor Engine - the editor that is loaded in a browser, takes a document represented by JSON, and parses that JSON into an interactive experience used by end-users and designers
- Environment API - a REST-like API to generate output and previews from JSON documents, but also to manage Template and Project files which are stored in your environment.
- Connectors - are components that enable the editor engine to link and interact with other software applications or systems. They facilitate communication and data exchange between different software environments.

From an integration standpoint, you will need to determine which of the three you will want to integrate and to what degrees.

For more information see: [Integration Overview](/GraFx-Developers/grafx-studio/integration-overview/01-overview/)

## Editor Engine

Built on-top of Flutter, the Editor Engine is a closed-source application loaded in a browser that provides interactive editing of Studio documents. These documents are defined in JSON.

The Editor Engine has a minimal UI for interacting with frames and frame content loaded. However, to be useful, a UI will need to be added on top of the engine. You can do this by either building your own UI using the [Studio SDK]() to interact with the engine via JavaScript or by using a custom built UI.

### Learning Resources

#### Tutorials

- [Studio SDK Quickstart](/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/01-overview/) - a quick ~15 minute guide that will teach you everything you need to know
- [Integration Project - Building a Custom UI](/GraFx-Developers/grafx-studio/editor-engine/integration-project-building-a-custom-ui/project-overview/) - a step-by-step bootcamp that will guide you in building a complete UI

#### References

- [Studio SDK](https://github.com/chili-publish/studio-sdk) - a SDK library to interface with the Studio Editor Engine
- [Studio SDK Examples](https://github.com/chili-publish/studio-sdk/tree/main/examples/sdk) - a few example projects using the Studio SDK

#### Custom Built UIs

- [Studio UI](https://github.com/chili-publish/studio-ui) - a CHILI publish minimalist end-user UI


## Environment API

CHILI GraFx provides a REST-like API that is used to managed resources on the platform and to output JSON documents or generate previews.

### Learning Resources

#### Tutorials

- [Environment API Quickstart](/GraFx-Developers/grafx-studio/environment-api/environment-api-quickstart/02-managing-integrations/)
- [Integration Project - Building a Template Store](/GraFx-Developers/environment-api/grafx-studio/integration-project-building-a-template-store/project-overview/)

#### References

- [Environment API Swagger](https://sandbox1.chili-publish-sandbox.online/grafx/swagger/index.html)
    - Replace `sandbox1` with your environment and remove `-sandbox` if your environment is on production.

## Connectors

Connectors allow the Editor Engine to link to and interact with other software applications or systems.

!!! warning Experimental

    Connectors are still experimental. Therefore, documentation and examples may be out of date, and APIs may change without notice.

#### References

- [Connector Template](https://github.com/chili-publish/grafx-connector-template) A template for creating connectors to integrate the Editor Engine with other software.

----

## Terms To Know

- Document: A JSON structure that's compatible with the Studio engine.
- Studio Designer UI: An interface tailored for designers, it offers comprehensive tools for creating smart templates and is exclusive to GraFx for licensed designers. Cannot be used in your integration
- Studio UI: A streamlined custom UI interface for end-users.
- Template: Documents that can be edited by designers within the Studio Designer UI. Templates can be placed into collections to be used for creating Projects.
- Project: Templates in collections can be transformed by users into Projects in the Studio UI. Each user's Projects are private, and inaccessible by other users.
- Integration: Special users for API interactions and integrations.
- Studio SDK: A JavaScript library for interacting with the Studio Editor Engine inside an iframe. Also referred to as SDK.
- Environment API: HTTP endpoints offering a CRUD API for GraFx applications.
