# GraFx Labs

!!! example "Experimental environment"
    GraFx Labs is the area within CHILI GraFx where experimental capabilities are hosted.  
    Features in this environment are released for validation purposes.  
    They can change or be removed at any time and are not covered by SLOs.  
    We welcome your feedback to help shape their evolution.  
      
    GraFx Labs uses advanced AI models.  
    Each render is charged as a production output.  
    Because Sandbox outputs are not billed, GraFx Labs is **not available** on [Sandbox](/CHILI-GraFx/concepts/sandbox/).
    
GraFx Labs helps innovation teams and platform owners experiment with new capabilities in CHILI GraFx before they become part of the production platform.

![GraFx Labs landing page](/release-notes/releasenotesassets/grafx-labs01.png){.screenshot-full}

## What is GraFx Labs?

GraFx Labs is a dedicated area inside CHILI GraFx where experimental features are hosted.

These features:

- Explore new workflows (often AI-driven).
- Validate functional and technical feasibility.
- Collect structured customer feedback.
- Test new value propositions before formal rollout.

GraFx Labs is separated from production-grade capabilities.

!!! warning
    Features in GraFx Labs are experimental.  
    They can change or be removed at any time.  
    They are not covered by SLOs.

## How it fits in the platform

- Design Systems are authored in GraFx Studio.
- Assets are managed in GraFx Media.
- End users interact through GraFx Experience.
- GraFx Labs sits alongside this flow to test new capabilities before they are embedded in Design Systems.

This ensures:

- Production remains stable.
- Innovation remains fast.

## Current experiments

- [GraFx Genie Product Image Creator](/CHILI-GraFx/guides/grafx-labs/grafx-genie-product-image-creator/)
- [GraFx Genie Product Image Composer](/CHILI-GraFx/guides/grafx-labs/grafx-genie-product-image-composer/)

## Turn GraFx Labs off for an environment

GraFx Labs is on by default. Organizations that do not want AI experiments in a given environment can switch it off.

1. Open the environment's **Environment settings**.
2. Go to **AI opt-out**.
3. Under **GraFx Labs**, switch the toggle off.

![The AI opt-out page with two cards: GraFx Labs with its toggle, and GraFx Genie with the Design agent toggle](/GraFx-Genie/design-agent/manage/ai-opt-out.png){.screenshot-full}

When GraFx Labs is off, it is hidden for every user in that environment, end users included: the GraFx Labs entry point and its experiments no longer appear, and their pages can't be opened directly. Switch the toggle back on and GraFx Labs returns as before.

The same page holds the [Design Agent](/GraFx-Genie/design-agent/manage/#opt-out-per-environment) toggle; the two are independent.

Only Subscription Admins and Environment Admins can see and change the AI opt-out, see [roles](/CHILI-GraFx/users/roles/).

!!! info "For integrators"
    The toggle is stored as `applicationsConfig.labs.enabled` in the environment settings, returned by the [environment settings endpoint](/GraFx-Developers/grafx-studio/integration-overview/05-versioning/#reading-the-current-version). It controls what the interface shows; it does not restrict API access.

## Typical use cases

- Retail field marketers generating campaign visuals faster.
- Distributed teams testing AI-assisted image workflows.
- Innovation teams validating new creative production flows.
- Brands exploring AI-generated product imagery before scaling.