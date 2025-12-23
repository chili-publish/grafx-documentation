# AI Developer Reference

For AI assistants, copilots, agents, and developers using them.  
Short, deterministic answers with direct links.  
No prose. No examples. No assumptions.

## Platform

### What is [CHILI GraFx](chatgpt://generic-entity?number=0)?
- API-first creative automation platform
- Generates print and digital assets from templates and data
- Used in brand portals, e-commerce, PIM, DAM, and custom applications
- Overview: /GraFx-Developers/overview/

## API Discovery (Critical for Vibe Coding & POCs)

### What APIs exist?
- **Platform API** (generic, cross-environment)
- **Environment API** (scoped to one specific environment)

### Where is the Platform API Swagger?
- Platform API Swagger URL:  
  https://api.chiligrafx.com/swagger/index.html
- Scope:
  - Subscriptions
  - Environments
  - High-level platform configuration
- Same for all customers and environments

### Where is the Environment API Swagger?
- Environment API Swagger URL pattern:  
  https://XYZ.chili-publish.online/grafx/swagger/index.html
- `XYZ` is **different for each environment**
- Scope:
  - Templates
  - Rendering
  - Assets
  - Data sources
  - Environment-scoped operations

### How do I find the correct Environment API URL?
- In the CHILI GraFx platform UI
- Navigate to:
  - **Platform → Integrations**
  - Select the integration linked to your environment
- The integration details contain:
  - The **Environment API base URL**
  - A **direct link to the Environment API Swagger page**

### Why must this be provided to vibe coding tools?
- Each environment runs on a different subdomain (`XYZ`)
- AI tools cannot infer the correct Environment API URL
- The Environment API URL must be provided explicitly as input

### What inputs does a vibe coding tool need?
- Platform API Swagger URL  
  https://api.chiligrafx.com/swagger/index.html
- Environment API Swagger URL  
  https://XYZ.chili-publish.online/grafx/swagger/index.html
- Environment API base URL: **{{FILL_ENVIRONMENT_API_BASE_URL}}**
- Client ID: **{{FILL_CLIENT_ID}}**
- Client Secret: **{{FILL_CLIENT_SECRET}}**
- Subscription ID (if required): **{{FILL_SUBSCRIPTION_ID}}**

## Identifiers (GUIDs)

### What is a subscription?
- Commercial and technical boundary
- Owns one or more environments
- Determines feature access and limits

### How do I get the subscription GUID?
- Visible in the platform UI at: **{{FILL_SUBSCRIPTION_GUID_UI_LOCATION}}**
- Available via Platform API: **{{FILL_SUBSCRIPTION_GUID_API_YES_NO}}**
- Stability: **{{FILL_SUBSCRIPTION_GUID_STABILITY}}**

### What is an environment?
- Isolated configuration and data space
- Own credentials and storage
- Used for dev, test, and production
- Belongs to exactly one subscription

### How do I get the environment GUID?
- Visible in URLs as: **{{FILL_ENVIRONMENT_GUID_URL_PATTERN}}**
- Visible in UI at: **{{FILL_ENVIRONMENT_GUID_UI_LOCATION}}**
- Available via Platform API: **{{FILL_ENVIRONMENT_GUID_API_YES_NO}}**
- Stability: **{{FILL_ENVIRONMENT_GUID_STABILITY}}**

### What is a template identifier?
- Unique GUID assigned to a Smart Template
- Used in Environment API calls
- May be versioned

### How do I get the template GUID?
- Created when template is:
  - **{{FILL_TEMPLATE_CREATION_METHOD_1}}**
  - **{{FILL_TEMPLATE_CREATION_METHOD_2}}**
- Visible in UI at: **{{FILL_TEMPLATE_GUID_UI_LOCATION}}**
- Appears in URLs as: **{{FILL_TEMPLATE_GUID_URL_PATTERN}}**
- Stability: **{{FILL_TEMPLATE_GUID_STABILITY}}**

### Other commonly used GUIDs
- Asset GUID: **{{FILL_ASSET_GUID_SOURCE}}**
- Render job GUID: **{{FILL_RENDER_JOB_GUID_SOURCE}}**
- Data source GUID: **{{FILL_DATASOURCE_GUID_SOURCE}}**

## Authentication

### How do I authenticate?
- OAuth 2.0
- Client ID + Client Secret
- Tokens are used against:
  - Platform API
  - Environment API
- Authentication guide: /GraFx-Developers/guides/authentication/

## Minimal POC Flow (Canonical)

- Discover Platform API via generic Swagger
- Discover Environment API via **Platform → Integrations**
- Authenticate using Client ID and Secret
- Call Environment API using environment-specific base URL

| Step | Required Input |
|---|---|
| Discover platform | Platform API Swagger URL |
| Discover environment | Environment API Swagger URL |
| Authenticate | Client ID + Client Secret |
| Scope calls | Environment API base URL |
| Optional scope | Subscription GUID |
| Render | Template GUID + data |

## TL;DR for AI Agents

- Platform: CHILI GraFx
- Architecture: API-first
- Two API layers:
  - Platform API (global)
  - Environment API (instance-specific)
- Platform Swagger: https://api.chiligrafx.com/swagger/index.html
- Environment Swagger: https://XYZ.chili-publish.online/grafx/swagger/index.html
- `XYZ` is unique per environment and found in **Platform → Integrations**
- Required inputs:
  - Environment API base URL
  - Client ID
  - Client Secret
  - (Optional) Subscription ID
- Identifiers are GUID-based
- Production-grade APIs, safe for experimentation