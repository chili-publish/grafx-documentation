# Templates vs Projects

Technically, Document, Template, and Project have different means, but generically these words are used interchangeably. This can add confusion when your talking with colleagues or even Client Support as it is very easy to mix up the words.

This guide will go through all the above terms, and help you better understand that these words do have different meanings.

Quick the differences:

- Document - a JSON file that can be loaded in the GraFx Studio Editor Engine or sent to output.
- Template - a Document that can edited by users with a Template Designer seat and can be added to collections for other users to turn into Projects.
- Projects - a Document that is a copy of a Template for editing by users.

!!! question "Why it matters?"

    Depending on your integration level (see [Integraion Overview](GraFx-Developers/grafx-studio/integration-overview/01-overview/index.md)) you may not care about Projects or Templates. For example, if you store everything externally, then Projects have no purpose for your integration.

## Document

GraFx Studio works with JSON files called Documents. You can load these JSON Documents into an instance of the Editor Engine or send them via the Environment API to get an output.

The engine expects a certain format. Below you can find a outline of this formate with notes.

```typescript
{
    "actions": [], // Array of the JavaScript actions used in the Document
    "connectors": [], // Array of connectors, includes the official Media and Fonts connectors by default
    "documentVersion": "0.3.3", // The Document version, the JSON format being used
   "engineVersion": "1.4.1", // The Studio Editor Engine version the Document supports (although it may work with lower)
    "layouts": [], // Array of layouts
    "pages": [ // Array of pages, but only 1 page is supported
        {
            "frames": [], // Array of frames in the document
            "id": "0",
            "number": 0
        }
    ],
    "properties": {
        "type": "template" // Will be changed to "project" for a project
    },
    "sdkVersion": "1.6.2", // The version of the SDK the Document supports (although it may work with lower)
    "selectedLayoutId": "0", // The layout that will be used on load and output
    "stylekit": {}, // All the fonts, colors, etc. used in the Document
    "variables": [] // Array of variables in the Document
}
```

Everything is a Document.

## Template

Templates are just a JSON Document being stored in GraFx Studio with special properties in the user experience.

Users who are assigned with a Template Designer seat can edit Templates in the full Studio UI Workspace. These Template Designers can also assign Templates to collections.

Outside of GraFx Studio context, Templates are just JSON Documents stored on the CHILI servers in a particular environment. You can manage them with them via the [Environment API](GraFx-Developers/grafx-studio/environment-api/environment-api-quickstart/01-overview/index.md) as well as generate output via API.

In a completely external integration, designers with Template Designer seats would create and edit their Documents as Templates inside GraFx Studio and then would register them into the integration application. The integration would take the JSON from GraFx Studio, or the designer would upload the JSON directly.

In the context of GraFx Studio, Templates can be registered in collections. These collections are meant to be used for clients who are utilizing My Projects.

## Project

A Project is a copy of Template that is stored in GraFx Studio. Within chiligrafx.com, an end user would choose a Template from a collection, and the Template would be converted to a Project. Each Project is isolated to the user who created it via the Environment API. That means neither you, the support team, or the integration token can interact with other user's Projects.

From an integration perspective, you can use Projects to copy Templates and basically hide them away from designers.

In the future Projects will be utilized in GraFx Insights for data collecting. However, as an integration if you are not interested in future data analytics, Projects may not be of interest.

Behind the scenes, a Project is just a definition and JSON.

The definition which you can get from the Environment API:

`api/v1/environment/ft-nostress/projects/{project ID}`

Is just the ID of the Project, name, and related Template.

```json
{
    "id": "1e4bb3a5-34fb-43dc-b047-c8044f7f0a07",
    "name": "New 2024 1",
    "template": {
        "id": "0532b935-6438-4174-be78-1b4910d8ff11"
    }
}
```

The JSON can get from the Environment API too:

`/api/v1/environment/{environment}/projects/{projectId}/document`

From a JSON standpoint, the only difference between a Template and Project is the `properties` property:

```json
"properties": {
    "templateId": "0532b935-6438-4174-be78-1b4910d8ff11",
    "type": "project"
  },
```
