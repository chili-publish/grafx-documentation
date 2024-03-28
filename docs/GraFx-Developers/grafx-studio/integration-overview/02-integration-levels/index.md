# GraFx Studio Integration Levels Guide

Integrating with GraFx Studio offers a spectrum of possibilities, ranging from minimal integration to a fully custom solution. This guide explores the various levels of integration with GraFx Studio and the GraFx Platform, helping you decide how closely you want to integrate your systems with GraFx Studio. Each level has its unique set of advantages and challenges, and your choice should align with your project requirements and strategic goals.

## Integration Options Overview

The integration levels with GraFx Studio vary from using GraFx Studio solely within the GraFx Platform to creating a completely custom front-end and managing all aspects of your projects and files externally. Here's a breakdown of each integration level, along with their pros and cons.

### 1. No Integration: Only GraFx Studio on the GraFx Platform

This approach means your end-users will directly use GraFx Studio via the GraFx Platform without any custom integration.

**Pros:**
- Immediate startup with no setup required.
- Supports Single Sign-On (SSO) for streamlined access.

**Cons:**
- Bound by the limitations of the GraFx Platform.
- GraFx Studio’s file management and sharing capabilities are still evolving.
- Does not serve as a full Digital Asset Management (DAM) system replacement.
- Users are limited to the Studio UI provided by GraFx.

### 2. Partial Integration: GraFx Studio and Platform with Custom Connectors

End-users still access GraFx Studio via the platform, but custom connectors are used to integrate with external asset systems.

**Pros:**
- Quick to start with minimal setup.
- Supports SSO.
- Enables the use of assets from external systems.

**Cons:**
- Some platform limitations remain, except for asset management.
- Developing custom connectors may be necessary if none exist for your asset managent.

### 3. Custom Front-End for End-Users, Files on GraFx

Documents are stored on GraFx, but end-users interact with them through a custom application interface.

**Pros:**
- Offers a tailored user experience and workflow.
- Frees you from the constraints of the Studio UI.

**Cons:**
- Requires additional development effort to integrate custom UI with GraFx.
- GraFx’s file management and sharing features may still be limited.

### 4. Advanced Custom Integration: End-User and Document Management Externally

Similar to the previous level, but document management is handled entirely through your application, with GraFx serving as storage.

**Pros:**
- Full control over document management and user experience.
- Not limited by Studio UI constraints.

**Cons:**
- Requires a management system or database for files.
- Increased development complexity.

### 5. Full Custom Integration: External Management for All Aspects

This level eliminates the need for GraFx.com for both end-users and designers, with external management of assets and documents.

**Pros:**
- GraFx Studio is solely used as a rendering engine.
- Complete control over both user and designer experiences.

**Cons:**
- Represents the highest development demand.

## Common Integration Challenges

Regardless of the chosen integration level, there are some common challenges due to the platform's evolving nature. These include:

- **API Versioning:** The Environment API currently lacks proper versioning, potentially leading to unexpected changes. This is targeted for improvement by summer 2024.
- **Project Sharing Limitations:** Currently, it's not possible to share projects with other users, including template designers and support staff. Solutions are planned, but until then integrations should provide support access.
- **Custom Connectors in Development:** As custom connectors are still being refined, availability and stability may vary.
- **User Isolation:** Tokens used for front-end integration cannot access projects managed by a different back-end token. Plans are in place to unify user access by end of 2024.

