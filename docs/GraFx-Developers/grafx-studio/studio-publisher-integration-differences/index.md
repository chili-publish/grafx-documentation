# Moving From Existing GraFx Publisher Integrations

If you're moving an existing GraFx Publisher workflow to use GraFx Studio, an important factor to consider is the integration layer. This page will lay out key integration differences between the two products, and provide general guidance for replicating existing GraFx Publisher integrations in GraFx Studio.

## Editor vs. API Integrations

This guide is split into two broad sections:

1. **Editor Integrations** - Embedding the GraFx Studio (or Publisher) editor in your frontend site
2. **API Integrations** - Using our REST libraries to directly access resources and functionalities on the GraFx environment level

In frontend integrations, these two layers often work in tandem. For the purposes of organizing this guide, though, they will be treated as separate.

---

## Editor Integrations

Integrating the GraFx Publisher editor is done by directly embedding an authenticated editor URL in an `iframe` element on your own site, which delivers the full editor UI experience in a single package. While this makes for a very simple integration process, there is a fundamental drawback to having the entire experience delivered by one URL inside an `iframe`. GraFx Studio, by contrast, was built from the ground up around a clear split between the **engine** and the **editor** — two experiences that live separately. So instead of a single URL that packages the whole UI into an `iframe`, we provide open-source libraries that let you build the editor elements directly in your own sites.

The simple answer for how to integrate the GraFx Studio editor is to use [Studio UI](https://github.com/chili-publish/studio-ui), an open-source, pre-built end-user workspace. **If you are looking for a direct alternative to plug-and-play GraFx Publisher `iframe` integrations, this is what you should use.**

### Can I Integrate GraFx Studio via `iframe`?

The short answer is "no". GraFx Publisher used pre-authenticated URLs that came with the full editor workspace packaged in. GraFx Studio does not provide such a URL, so placing a Template or Project URL directly in an `iframe` will simply redirect users to log in via GraFx rather than open the editor experience directly.

GraFx Studio instead provides a rendering engine you plug directly into. Using the [Studio SDK](https://chili-publish.github.io/studio-sdk/), you pass it the parent element for the engine to load, a Studio document JSON, an integration token, and a GraFx Environment API base URL, and behind the scenes it sets up and renders the Studio document. For the full end-user experience, we instead recommend [Studio UI](https://github.com/chili-publish/studio-ui), which comes with a complete end-user UX along with a `studioUILoaderConfig` function — you supply similar information through one simple build function, together with the project ID.

### How are Workspaces and View Preferences Handled in GraFx Studio?

Many existing GraFx Publisher integrations attach customized Workspaces and View Preferences to their editor URLs, in order to control what UI elements end users actually see on their own site. A common question, then, might be how to get that same functionality with GraFx Studio editor integrations.

[Studio UI](https://github.com/chili-publish/studio-ui) provides a number of customization options when building it (see [Studio UI Advanced Integrations](https://github.com/chili-publish/studio-ui/blob/main/documentation/advanced-integration.md#javascript)). You can think of these build options as the equivalent of GraFx Publisher's Workspaces. View Preferences, then, would be covered by GraFx Studio's [User Interfaces](/GraFx-Studio/concepts/user-interface/).

### How are End-User vs. Administrator Template Workspace Views Handled in GraFx Studio?

This is an area where GraFx Studio is a bit simpler than GraFx Publisher. When you use [Studio UI](https://github.com/chili-publish/studio-ui) to integrate the GraFx Studio editor, that is *always* loading the end-user workspace. The GraFx Studio equivalent of GraFx Publisher's "Workspace Administrator" view would be the Design Mode view on Templates. This workspace is only available to GraFx users with a Template Designer seat assigned; you **cannot** integrate this view in your own site.

### Can I Use JavaScript to Interact with the GraFx Studio Editor?

Yes! You can use the [Studio SDK](https://chili-publish.github.io/studio-sdk/) library to directly interact with the editor in your own site. In [Studio UI](https://github.com/chili-publish/studio-ui), you can access the SDK via the `StudioUISDK` window object. This is the GraFx Studio version of using `editorObject`/`editor` with GraFx Publisher. One important structural difference is that the [Studio SDK](https://chili-publish.github.io/studio-sdk/) is promise based. If your existing GraFx Publisher integration is using PublisherInterface, then you've already handled this as that library is also promise based.

GraFx Studio integrations have the added bonus of not needing any extra steps to comply with the [Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy); with no `iframe` embedding involved, you don't have to worry about the host differing between the edtior and your own site.

### Is Studio UI My Only Integration Option?

No, [Studio UI](https://github.com/chili-publish/studio-ui) is just the easiest direct alternative to existing GraFx Publisher `iframe` integrations. You can check out the [Studio SDK Quickstart Guide](/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/01-overview/) for more details on working directly with the SDK. That said, we would generally recommend working with [Studio UI](https://github.com/chili-publish/studio-ui) rather than trying to build out your own UI wrapper.

---

## API Integrations

Like GraFx Publisher, GraFx Studio exposes a comprehensive set of REST API endpoints to interact with resources on the GraFx environment. There are a few key differences when moving from a GraFx Publisher API workflow to a GraFx Studio one.

### Swagger Documentation

You can access Swagger documentation for the GraFx Environment API via:

```
https://{yourEnvironmentName}.chili-publish.online/grafx/swagger
```

### Authentication

The Environment API uses Bearer Token authorization, and a standard oAuth2 Client Credentials flow to generate tokens. This means that instead of environment-specific `/apikey` endpoints to generate authentication headers, you would use our generic oAuth server endpoint to generate tokens (see [Generating a Token](/GraFx-Developers/environment-api/03-generating-a-token/)).

### Content Type

The Environment API deals exclusively with `JSON` content types, as opposed to `XML` like GraFx Publisher's API deals in. This applies to request and response bodies.

### Templates vs. Projects

GraFx Publisher defines a single `resourceType` for document content as simply `documents`. It makes no delineation between the master template documents and customer/order copies that may have been generated from it.

In contrast, GraFx Studio splits documents into `templates` and `projects`, which each have their own set of REST endpoints. A `project` is always generated from a `template`, you can think of this as simply codifying the relationship between GraFx Publisher "master documents" and "user/customer/order copies", if this is a workflow you already use.

!!! warning "Projects Exist per-User"

    Projects in GraFx Studio are saved on the user level. This means projects are only accessible by the GraFx user that originally created them.