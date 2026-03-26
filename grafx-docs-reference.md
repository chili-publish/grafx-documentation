# KNOWLEDGE.md — CHILI GraFx Documentation Reference

> **Purpose:** This file is a structured reference for a documentation author AI assistant working with the CHILI GraFx documentation site at [docs.chiligrafx.com](https://docs.chiligrafx.com/). It covers terminology, branding, site structure, feature details, and cross-linking guidance — all derived from the live documentation as of March 2026.

---

## 1. Correct terminology and branding

### 1.1 Product names and casing

Every product name below must be written **exactly** as shown. Casing, spacing, and the "GraFx" prefix are intentional brand conventions.

| Product | Correct Name | Notes |
|---------|-------------|-------|
| Platform | **CHILI GraFx** | Always uppercase "CHILI", camelCase "GraFx". This is the overarching cloud platform. |
| Template editor | **GraFx Studio** | The multichannel Smart Template editor for digital and print output. |
| Self-service layer | **GraFx Experience** | The end-user experience/self-service layer. Not a separate doc section — its features are documented under GraFx Studio and the Developer Center. |
| Asset repository | **GraFx Media** | Central repository for assets used in Smart Templates. Explicitly **not** a DAM. |
| Brand management | **GraFx Brand Kits** | Manages brand identity elements (colors, fonts, media, styles). |
| Font management | **GraFx Fonts** | Font storage and serving exclusively for GraFx Studio. |
| Legacy editor | **GraFx Publisher** | Formerly "CHILI publisher Online (CPO)". Print-focused Smart Template editor. |
| AI features | **GraFx Genie** | AI assistant brand for Smart Crop, template creation assist, code generation. |
| Experimental features | **GraFx Labs** | Dedicated space for experimental/pre-production features. |
| Company | **CHILI publish** | The company name. Lowercase "publish". Full legal: CHILI publish NV. |

### 1.2 Key terminology

| Term | Definition |
|------|-----------|
| **Smart Template** | A document with variables, actions, brand guardrails, and business logic — the core design artifact in both GraFx Studio and GraFx Publisher. |
| **Design System** | A Smart Template that can generate endless asset variants across channels (up to 250 Smart Layouts). Marketing-level concept used especially with GraFx Experience. |
| **Frame** | Basic design element container in GraFx Studio. Four types: Text Frame, Image Frame, Shape Frame, Barcode Frame. |
| **Layout** | A size/proportion variant of a document. Uses an inheritance model (base layout → sub-layouts with overridable properties). |
| **Sub-layout** | A layout derived from the base layout; inherits all properties but allows per-layout overrides. |
| **Layout Intent** | Classification of a layout's output purpose: **Print**, **Digital Static**, or **Digital Animated**. Determines available output formats. |
| **Layout Size Constraints** | Rules governing allowed size and aspect ratio ranges for resizable layouts. |
| **Variable (Template Variable)** | Dynamic placeholder in a template. Types: Text (single-line, multi-line), Image, List, Boolean, Number, Date. |
| **JavaScript Variable** | Variable scoped to Action scripts (distinct from Template Variables). |
| **Action** | JavaScript-based business logic executed when a Trigger fires. |
| **Trigger** | Event that activates an Action. Events: Variable value changed, Select layout changed, Frame moved, Page size changed, Document loaded. |
| **Action Helper Functions** | Pre-built get/set functions for use in Actions (e.g., `getVariableValue`, `setFrameVisible`, `setFrameX`, `setFrameY`, `setFrameWidth`, `setFrameHeight`, `setBooleanVariableValue`, `setImageVariableValue`, `setListVariableValue`, `setTextVariableValue`, `setVariableValue`, `setVariableVisible`, `setPageSize`). |
| **Design Mode** | Editing mode where actions are inactive; for layout and styling work. |
| **Run Mode** | Testing mode simulating the end-user experience with live actions and conditional visibility. |
| **Brand Kit** | Collection of brand elements (colors, fonts, media, paragraph/character styles) defining visual identity. Replaces the legacy term "Stylekit". |
| **Stylekit** | **Legacy/alternative term** for Brand Kit. Still referenced on some older pages. |
| **Swatch** | A named color saved inside a Brand Kit. |
| **Paragraph Style** | Reusable text paragraph formatting preset in a Brand Kit. |
| **Character Style** | Reusable character-level text formatting preset in a Brand Kit. |
| **Template Collection** | A group of templates made available to end users. |
| **My Projects** | End-user workspace for creating and customizing copies of templates. |
| **Studio UI** | Streamlined end-user interface for project customization. This is the GraFx Experience editor. |
| **Studio Designer UI** | Full-featured interface for template designers. Cannot be used in custom integrations. |
| **User Interface** | Configurable UI profile per Layout Intent — controls visible panels, output settings, and form layout for end users. |
| **Form Builder** | Tool for controlling the form layout shown to end users in My Projects / Studio UI. |
| **Connector** | Component enabling the Editor Engine to link with external systems. Two types: Media Connectors and Data Connectors. |
| **Connector Hub** | Platform UI for managing and activating connectors per environment. |
| **Media Connector** | Connector linking to external DAM/media repositories (Acquia DAM, Canto DAM, GraFx Media, Keepeek Media, Sitecore Content Hub). |
| **Data Connector** | Connector linking to external data sources (Google Sheets, custom APIs). |
| **Output Settings** | Pre-configured output format settings assigned per Layout Intent. |
| **Output Task** | A generation job that produces output files (PDF, JPG, PNG, GIF, MP4, HTML). |
| **Render** | Output unit. 1 render = each started second of output. Watermarked output does not count. |
| **Environment** | An isolated, secure workspace where documents, templates, and creative elements are stored. Two types: Sandbox and Production. |
| **Sandbox** | Testing environment. Platform changes are applied to Sandbox before Production. |
| **Production** | Live environment for real work and output. |
| **Subscription** | Container for environments. Tracks storage usage, render quota, sandbox/production environment counts. |
| **Integration** | A special API user with Client ID + Client Secret credentials for machine-to-machine API access. |
| **Editor Engine** | Flutter-based, closed-source browser application that renders and edits GraFx Studio documents (JSON format). |
| **Studio SDK** | JavaScript library (`@chili-publish/studio-sdk`) for programmatic interaction with the Editor Engine inside an iframe. |
| **Environment API** | REST-like HTTP API for managing environment-level resources (templates, projects, output, media, fonts). |
| **Platform API** | API for managing platform-level resources (subscriptions, environments, users). |
| **Document** | A JSON file compatible with the Studio engine. Can be loaded in Editor Engine or sent to API for output generation. |
| **Template** | A Document stored in GraFx Studio, editable by Template Designer seat holders, placeable into Collections. |
| **Project** | An end-user's private copy of a Template for customization. Isolated to the user who created it. |
| **Template Designer** | User role that creates and manages Smart Templates. Requires a licensed Template Designer Seat. |
| **End User** | User who customizes templates via Studio UI / GraFx Experience but does not design them. |
| **Subscription Admin** | Top-level admin role managing users and environments across a subscription. |
| **Environment Admin** | Admin role scoped to specific environment(s). |
| **Smart Crop** | AI-powered subject-aware image cropping (GraFx Genie feature). Requires a Subject Area defined on the asset. |
| **Subject Area** | A defined region on a GraFx Media asset identifying the main subject for Smart Crop. |
| **Point of Interest (POI)** | Specific focal point within an asset for intelligent cropping. |
| **Private Data** | Non-visible data attached to variables; not shown to end users. |
| **Headless** | API-driven batch output generation without any UI. |
| **VDP (Variable Data Printing)** | Output with variable substitution via API. Limit: 10,000 rows or 10 MB per request. |
| **Anchoring** | Positioning system for consistent frame positioning across layout sizes. |
| **Bleed** | Extra area beyond trim for print output. |
| **Crop Marks** | Print alignment marks. |
| **FSSO (Federated Single Sign-On)** | Enterprise authentication via OpenID Connect (OIDC) or SAML. |
| **Connector CLI** | Command-line tool for building, testing, and deploying custom connectors. |
| **BackOffice** | GraFx Publisher management interface for templates, assets, and settings. Authentication now requires a CHILI GraFx account (as of Nov 2025). |
| **PublisherInterface** | JavaScript package for cross-origin integration with the GraFx Publisher editor iframe. |
| **editorObject** | JavaScript object on the Publisher editor window for same-origin Document Event Actions. |

### 1.3 Terms to avoid / legacy names

| Avoid | Use Instead | Reason |
|-------|------------|--------|
| CHILI publisher (standalone) | GraFx Publisher | Legacy on-premise product is end-of-life. The cloud version is "GraFx Publisher". |
| CPO | GraFx Publisher | "CHILI publisher Online" is the former name. |
| MyCP / My CHILI publish | CHILI GraFx | Legacy web portal replaced by the CHILI GraFx platform. |
| Stylekit | Brand Kit | "Stylekit" is the legacy term; "Brand Kit" is the current name. Some older doc pages still use "Stylekit". |
| DAM (for GraFx Media) | Asset repository / GraFx Media | GraFx Media is explicitly **not** a DAM. It is a focused asset repository. |
| CHILI Editor | GraFx Publisher / GraFx Studio | Context-dependent; use the specific product name. |

---

## 2. Site structure and navigation

### 2.1 Top-level sections

The documentation site at `docs.chiligrafx.com` has **eight** top-level navigation tabs:

| Tab Label | URL Path | Purpose |
|-----------|----------|---------|
| **CHILI GraFx** | `/CHILI-GraFx/` | Platform-level documentation: environments, subscriptions, user management, administration, trust/security, onboarding, FSSO, GraFx Labs. |
| **GraFx Studio** | `/GraFx-Studio/` | Smart Template editor: workspace UI, concepts, how-to guides, connectors, conversion plugins. Largest section (~105 pages). |
| **GraFx Publisher** | `/GraFx-Publisher/` | Legacy editor documentation: introduction, conversion tools, JavaScript integration. Smaller section (~5–10 pages). |
| **GraFx Media** | `/GraFx-Media/` | Asset repository: browsing, uploading, folder management, Smart Crop. ~10 pages. |
| **GraFx Fonts** | `/GraFx-Fonts/` | Font management: supported types, upload/manage fonts, fonts vs families. ~7 pages. |
| **GraFx Brand Kits** | `/GraFx-Brand-Kits/` | Brand identity management: creating/editing Brand Kits, elements. ~7 pages. |
| **Platform Updates** | `/release-notes/` | Release notes blog: chronological, filterable by category (Releases, Operational Updates), yearly archives. |
| **Developer Center** | `/GraFx-Developers/overview/` | Integration documentation: Studio SDK, Editor Engine, Environment API, Connectors, workshops. ~30+ pages. |

**Important:** There is **no dedicated `/GraFx-Experience/` section**. GraFx Experience documentation is distributed across GraFx Studio (concepts: Self-service, Template Management, User Interfaces, Design & Run) and the Developer Center (Studio UI, SDK, Environment API).

### 2.2 Organization pattern

Each product section follows a consistent pattern:

```
{Product}/
├── Introduction (landing page)
├── Application Overview (UI elements and workspace documentation)
├── Concepts (theoretical/conceptual explanations — "what and why")
└── How to / Guides (step-by-step procedural guides — "how to do it")
```

GraFx Studio is additionally subdivided:
- **How to: Design** — Frame creation, styling, fonts, colors
- **How to: Connectors** — Connector Hub setup
- **How to: Animate** — Animation guides
- **How to: Automate** — Variables and Actions (with code examples)
- **How to: Output** — Output format guides (PDF, JPG, PNG, GIF, MP4, HTML)
- **Connectors: Media** — Individual DAM connector setup pages
- **Connectors: Data** — Data connector setup pages (Google Sheets)
- **Plugins / Conversion** — Adobe InDesign and Photoshop import

### 2.3 URL patterns

| Pattern | Example |
|---------|---------|
| Product landing | `/GraFx-Studio/` |
| Application overview | `/GraFx-Studio/overview/{topic}/` |
| Concept page | `/GraFx-Studio/concepts/{topic}/` |
| How-to guide | `/GraFx-Studio/guides/{topic}/` |
| Nested guide | `/GraFx-Studio/guides/actions/example-hideframe/` |
| Connector page | `/GraFx-Studio/connectors/connector-{name}/` |
| Conversion plugin | `/GraFx-Studio/convert/Adobe-InDesign/` |
| Platform concept | `/CHILI-GraFx/concepts/{topic}/` |
| User management | `/CHILI-GraFx/users/{topic}/` |
| Platform admin | `/CHILI-GraFx/admin/` |
| Trust pages | `/CHILI-GraFx/trust/{topic}/` |
| Onboarding | `/CHILI-GraFx/guides/onboarding/{step}/` |
| FSSO setup | `/CHILI-GraFx/guides/setup-fsso/{protocol}/` |
| Developer overview | `/GraFx-Developers/overview/` |
| SDK/Engine | `/GraFx-Developers/grafx-studio/editor-engine/...` |
| Environment API | `/GraFx-Developers/environment-api/{topic}/` |
| API Reference | `/GraFx-Developers/environment-api/reference/` |
| Connectors (dev) | `/GraFx-Developers/connectors/{type}/{topic}/` |
| Release note | `/release-notes/{YYYY}/{MM}/{DD}/{slug}` |
| Release archive | `/release-notes/archive/{YYYY}/` |
| Release category | `/release-notes/releases/` or `/release-notes/operational-updates/` |

---

## 3. Feature details per product

### 3.1 GraFx Studio

**What it does:** GraFx Studio is the multichannel Smart Template editor for (animated) digital and print output. It is the primary design tool in the CHILI GraFx platform, used by template designers to create Smart Templates that end users then customize.

**Key features and concepts:**

**Design system:**
- **Frames** — Core building blocks (Text, Image, Shape, Barcode). Properties: position (X, Y), width, height, rotation, opacity, blend mode, drop shadow, Z-index.
- **Layers** — Reorderable via drag-and-drop; controls Z-index rendering order.
- **Pages** — Multi-page document support.
- **Layouts** — Multiple size/proportion variants from same document via inheritance model (base layout → sub-layouts). Properties can be overridden per layout.
- **Layout Intent** — Categorizes layouts as Print, Digital Static, or Digital Animated. Determines output options.
- **Layout Size Constraints** — Define allowed size/aspect ratio ranges for end-user resizing.
- **Anchoring** — Fixed or relative positioning for consistent layout across sizes.
- **Snapping** — Alignment assistance during frame positioning.

**Styling:**
- **Brand Kits** — Named colors (swatches), font families, paragraph styles, character styles.
- **Paragraph Styles and Character Styles** — Reusable text formatting presets.
- **Bulleted Lists and Numbered Lists** — Multi-level list support.
- **Gradients** — Linear gradient fills.
- **Blend Modes** — Visual blending between frames.
- **Drop Shadow** — Frame shadow effects.
- **Color Management** — RGB, Hex, CMYK color spaces.
- **Text Direction** — RTL/LTR support.
- **Text Stroke** — Outline effect on text.

**Automation:**
- **Variables (Template Variables)** — Dynamic placeholders: Text (single-line, multi-line), Image, List, Boolean, Number, Date.
- **Variable Visibility Conditions** — Control when variables appear to end users.
- **Private Data** — Hidden metadata attached to variables.
- **Actions** — JavaScript code triggered by events (Variable value changed, Layout changed, Frame moved, Page size changed, Document loaded). Scope can target specific frames, variables, "Any variable", or "Any frame".
- **Action Helper Functions** — `getVariableValue`, `setFrameVisible`, `setFrameX/Y/Width/Height/Rotation`, `setBooleanVariableValue`, `setImageVariableValue`, `setListVariableValue`, `setTextVariableValue`, `setVariableValue`, `setVariableVisible`, `setPageSize`, `setSelectedItemFromListVariable`, etc.
- **Design Mode & Run Mode** — Design Mode for layout/styling (actions inactive); Run Mode simulates end-user experience with live actions and conditional visibility.

**Output:**
- Supported formats: **PDF, JPG, PNG, GIF, MP4, HTML** (HTML is experimental).
- **Output Settings** — Pre-configured per Layout Intent.
- **Output Tasks** — Generation jobs.
- **Bleed** and **Crop Marks** — Print-specific settings.
- **Headless** — API-driven batch output without UI.

**Template management and self-service:**
- **Smart Template** → **Template Collection** → **My Projects** → **Studio UI** workflow.
- **User Interfaces** — Configurable UI per Layout Intent with Form Builder.
- **Studio UI** — Streamlined end-user interface (the GraFx Experience editor).
- **Studio Designer UI** — Full-featured designer interface.
- **Self-service** — End-user driven template customization workflow.

**Connectors:**
- Media: Acquia DAM, Canto DAM, GraFx Media, Keepeek Media, Sitecore Content Hub.
- Data: Google Sheets.
- Metadata mapping to template variables; digital rights management.

**AI features (GraFx Genie):**
- Smart Crop — AI-powered subject-aware image cropping.
- Template creation assist — Reduces creation time up to 80%.
- Code generation for Actions.
- GraFx Labs: Product Image Creator, Product Image Composer (experimental).

**Conversion/Plugins:**
- Import from Adobe InDesign and Adobe Photoshop via exporter plugins.
- Export to `.zip` containing assets, document structure, settings; import into GraFx Studio.

**Sub-pages (complete inventory — ~105 pages):**

| Section | Page Count | Key URLs |
|---------|-----------|----------|
| Introduction | 1 | `/GraFx-Studio/` |
| Application Overview | 12 | `/GraFx-Studio/overview/animation/`, `/overview/bottom-quicktools/`, `/overview/brandkits/`, `/overview/document-canvas/`, `/overview/timeline/`, `/overview/hamburger-menu/`, `/overview/layouts/`, `/overview/movement/`, `/overview/document/`, `/overview/properties/`, `/overview/sidebar/`, `/overview/workspace-elements/` |
| Concepts | 35+ | `/GraFx-Studio/concepts/actions/`, `/concepts/helper-functions/`, `/concepts/anchoring/`, `/concepts/animation/`, `/concepts/barcodes/`, `/concepts/brandkits/`, `/concepts/bleed/`, `/concepts/blendmodes/`, `/concepts/color-management/`, `/concepts/connectors/`, `/concepts/connectors-data/`, `/concepts/connectors-media/`, `/concepts/constraints/`, `/concepts/crop/`, `/concepts/crop-marks/`, `/concepts/design-run/`, `/concepts/drop-shadow/`, `/concepts/frames/`, `/concepts/gradients/`, `/concepts/grafx-genie/`, `/concepts/headless/`, `/concepts/shortcuts/`, `/concepts/layers/`, `/concepts/layouts/`, `/concepts/layout-size-constraints/`, `/concepts/layout-intent/`, `/concepts/manual-crop-override/`, `/concepts/output-settings/`, `/concepts/output-tasks/`, `/concepts/pages/`, `/concepts/private-data/`, `/concepts/shapes/`, `/concepts/snapping/`, `/concepts/genie-smart-crop/`, `/concepts/self-service/`, `/concepts/template-management/`, `/concepts/text-direction/`, `/concepts/user-interface/`, `/concepts/variables/`, `/concepts/stylekits/` |
| How to: Design | 20+ | `/guides/hello-world/`, `/guides/anchoring/`, `/guides/barcodes/overview/`, `/guides/barcodes/add/`, `/guides/barcodes/available/`, `/guides/brandkits/`, `/guides/blendmodes/`, `/guides/bulleted-lists/`, `/guides/characterstyles/`, `/guides/colors/`, `/guides/layouts/`, `/guides/cropping/`, `/guides/drop-shadow/`, `/guides/add-fonts/`, `/guides/gradients/`, `/guides/image-frame/`, `/guides/layout-size-constraints/`, `/guides/numbered-lists/`, `/guides/pages/`, `/guides/paragraphstyles/`, `/guides/shape-frame/`, `/guides/smart-crop/`, `/guides/text-frame/` |
| How to: Connectors | 1 | `/guides/connector-hub/` |
| How to: Animate | 1 | `/guides/animate-frame/` |
| How to: Automate | 14 | `/guides/template-variables/define/`, `/guides/template-variables/visibility/`, `/guides/template-variables/assign/`, `/guides/template-variables/date/`, `/guides/template-variables/image/`, `/guides/template-variables/multi-line-text/`, `/guides/template-variables/single-line-text/`, `/guides/template-variables/number/`, `/guides/template-variables-private-data/`, `/guides/actions/create/`, `/guides/actions/javascript/`, `/guides/actions/example-changelayout/`, `/guides/actions/example-hideframe/`, `/guides/actions/example-multipleframes/`, `/guides/actions/example-currency/` |
| How to: Output | 7 | `/guides/output/settings/`, `/guides/output/tasks/`, `/guides/output/gif/`, `/guides/output/html/`, `/guides/output/image/`, `/guides/output/mp4/`, `/guides/output/pdf/` |
| How to: General | 3 | `/guides/create-projects/`, `/guides/manage-collections/`, `/guides/manage-user-interfaces/` |
| Connectors: Media | 5 | `/connectors/connector-acquia-dam/`, `/connectors/connector-canto/`, `/connectors/connector-grafx-media/`, `/connectors/connector-keepeek-media/`, `/connectors/connector-sitecore-content-hub/` |
| Connectors: Data | 3 | `/connectors/connector-google-sheets-data/`, `/connectors/connector-google-sheets-data/google-setup/`, `/connectors/connector-google-sheets-data/in-smart-template/` |
| Plugins / Conversion | 3 | `/convert/intro/`, `/convert/Adobe-InDesign/`, `/convert/Adobe-Photoshop/` |

### 3.2 GraFx Experience

**What it does:** GraFx Experience is the experience/self-service layer on top of CHILI GraFx. It allows central teams to provide master artwork with guidelines and restrictions baked in, while local teams generate campaign variations tailored to their audiences, stores, and channels.

**Documentation status:** GraFx Experience does **not** have its own section at `/GraFx-Experience/`. Its technical documentation is embedded in existing sections:

| Feature | Documented At |
|---------|--------------|
| Template management workflow | `/GraFx-Studio/concepts/template-management/` |
| Self-service concept | `/GraFx-Studio/concepts/self-service/` |
| User Interfaces / Form Builder | `/GraFx-Studio/concepts/user-interface/` |
| Design & Run Mode | `/GraFx-Studio/concepts/design-run/` |
| Project creation | `/GraFx-Studio/guides/create-projects/` |
| Collection management | `/GraFx-Studio/guides/manage-collections/` |
| User Interface management | `/GraFx-Studio/guides/manage-user-interfaces/` |
| Studio UI (end-user editor) | `/GraFx-Developers/grafx-studio/overview/` |
| Studio SDK integration | `/GraFx-Developers/grafx-studio/editor-engine/...` |
| Browser support (mentions GraFx Experience) | `/CHILI-GraFx/browser-support/` |

**Key concept:** Designers create Smart Templates in GraFx Studio → add them to Template Collections → configure User Interfaces → end users access collections under "My Projects" and open projects in the Studio UI.

### 3.3 GraFx Media

**What it does:** Central repository to store digital assets used in Smart Templates. Serves both GraFx Studio and GraFx Publisher. **Explicitly not a DAM** — it is a focused asset repository that leverages the Connector Framework to integrate with external DAMs.

**Key features:**
- Folder-based organization for assets.
- Upload/browse/search functionality.
- Supported file types are enforced at upload.
- **Smart Crop (GraFx Genie)** — AI-powered cropping based on Subject Area and Point of Interest.
- Default media connector built into GraFx Studio; external DAMs connected via Media Connectors.
- Upload folder: files stored in "Upload/" by default with configurable custom paths.

**Sub-pages (~10 pages):**

| URL | Title |
|-----|-------|
| `/GraFx-Media/` | Introduction |
| `/GraFx-Media/overview/elements/` | Application elements |
| `/GraFx-Media/overview/filetypes/` | Supported File Types |
| `/GraFx-Media/concepts/media-vs-dam/` | Media vs DAM |
| `/GraFx-Media/concepts/genie-smart-crop/` | GraFx Genie: Smart Crop |
| `/GraFx-Media/guides/browse/` | Browse media |
| `/GraFx-Media/guides/browse/search/` | Search media |
| `/GraFx-Media/guides/manage-folders/` | Manage folders |
| `/GraFx-Media/guides/upload-media/` | Upload media |
| `/GraFx-Media/guides/smart-crop-subject-area/` | Set Subject Area |

### 3.4 GraFx Brand Kits

**What it does:** Defines and manages an organization's visual identity in one place. Provides a "source of truth" for brand visual DNA that template designers and end users access directly in GraFx Studio.

**Brand Kit elements:**
- **Colors** — Named swatches in RGB, CMYK, and SPOT color spaces.
- **Fonts** — Full font families from GraFx Fonts.
- **Media** — Logos, artwork, image assets from GraFx Media.
- **Paragraph Styles** — Standardized paragraph formatting (supports text stroke, bulleted/numbered lists).
- **Character Styles** — Character-level text styling.

**Key capability:** Import existing Brand Kits for faster onboarding.

**Sub-pages (~7 pages):**

| URL | Title |
|-----|-------|
| `/GraFx-Brand-Kits/` | Introduction |
| `/GraFx-Brand-Kits/overview/` | Application overview |
| `/GraFx-Brand-Kits/concepts/brandkit/` | Brand Kit (concept) |
| `/GraFx-Brand-Kits/concepts/elements/` | Elements (concept) |
| `/GraFx-Brand-Kits/guides/create/` | Create a Brand Kit |
| `/GraFx-Brand-Kits/guides/edit/` | Edit a Brand Kit |
| `/GraFx-Brand-Kits/guides/import/` | Import a Brand Kit |

### 3.5 GraFx Fonts

**What it does:** Stores and serves Fonts and Font Families exclusively for GraFx Studio. GraFx Publisher has its own separate font system (GraFx Publisher Fonts) — fonts uploaded to GraFx Fonts are NOT available in GraFx Publisher.

**Key details:**
- **Supported formats:** OTF (OpenType) and TTF (TrueType) only.
- **Not supported:** WOFF/WOFF2, Variable Fonts, PostScript Type 1, EOT, SVG Fonts, COLR/CPAL color fonts.
- **OpenType support:** GSUB (ligatures, joining forms) and GPOS (diacritics, marks) tables supported.
- **Arabic/RTL support:** Complex script rendering supported.
- **Duplicate detection:** Based on font family + style combination.
- **License requirement:** Users must confirm a valid font license before uploading.

**Sub-pages (~7 pages):**

| URL | Title |
|-----|-------|
| `/GraFx-Fonts/` | Introduction |
| `/GraFx-Fonts/overview/elements/` | Application elements |
| `/GraFx-Fonts/overview/supported-font-types/` | Supported Font Types |
| `/GraFx-Fonts/concepts/fonts-vs-families/` | Fonts vs Families |
| `/GraFx-Fonts/concepts/fonts-in-publisher/` | Fonts in GraFx Publisher |
| `/GraFx-Fonts/guides/upload-fonts/` | Upload fonts |
| `/GraFx-Fonts/guides/manage-fonts/` | Manage fonts |

### 3.6 GraFx Publisher

**What it does:** The evolution of CHILI publisher Online (CPO) into the CHILI GraFx platform. Print-focused Smart Template editor for end-user interaction with documents in a controlled, on-brand way.

**Legacy status:** "CHILI publisher (legacy) is end-of-life. To benefit from continued support and maintenance, switch to CHILI GraFx." The on-premise version is no longer supported.

**Current status (as of March 2026):**
- Authentication now requires a CHILI GraFx account (centralized login, enforced Nov 16, 2025).
- Direct login to Publisher BackOffice is discontinued; API integrations continue to function without changes.
- BackOffice itself still exists — only the authentication method changed.
- GraFx Publisher has its own separate font system (GraFx Publisher Fonts).

**Key relationships:**
- My CHILI publish (MyCP) → replaced by CHILI GraFx.
- BackOffice → holds documents, assets, configurations; functionality transferring to CHILI GraFx.
- CHILI Editor → lives on in GraFx Publisher.
- Assets → evolve into GraFx Media.
- Fonts → evolve into GraFx Fonts.

**JavaScript integration:**
- **PublisherInterface** — JS package for cross-origin communication with Publisher editor iframe (for integrations).
- **editorObject** — JS object for same-origin Document Event Actions.

**Sub-pages (~5–10 pages):**

| URL | Title |
|-----|-------|
| `/GraFx-Publisher/` | Introduction |
| `/GraFx-Publisher/convert/Adobe-InDesign/` | Converter for Adobe InDesign |
| `/GraFx-Publisher/guides/javascript/` | Intro to JavaScript |
| `/GraFx-Publisher/guides/javascript/document/` | Document (JavaScript) |
| `/GraFx-Publisher/guides/hello-world/` | Hello World |

### 3.7 CHILI GraFx platform

**What it does:** Cloud-based platform centralizing account information, users, resources, and documents. Hosts all GraFx applications.

**Platform hierarchy:**
```
CHILI GraFx Client
  └── Subscription(s) [storage, render quota, environment counts]
       └── Environment(s) [isolated; Sandbox or Production]
            ├── GraFx Studio
            ├── GraFx Publisher
            ├── GraFx Media
            ├── GraFx Fonts
            └── GraFx Brand Kits
```

**Key concepts:**
- **Environments** — Isolated, secure spaces. Two types: Sandbox (testing, changes applied first) and Production. No data interchange between environments.
- **Subscriptions** — Track storage, render quota, environment counts.
- **Renders** — 1 render = each started second of output. VDP formula: first 50 counted individually, then each set of 10 adds 1.
- **Integrations** — Client ID + Client Secret for API access. Two tiers: Platform API and Environment API.
- **FSSO** — Federated Single Sign-On via OIDC or SAML.
- **GraFx Labs** — Experimental feature space.

**User management:**
- **Roles:** Subscription Admin, Environment Admin, Template Designer (licensed seat), End User, User (default).
- **User Groups** — Collection of users sharing common access needs.
- **Resources** — Items impacted by user management (e.g., collections).
- **Scope hierarchy:** Client → Subscription(s) → Environment(s).

**Trust and security:**
- Security policy, compliance, data centers, GDPR, user-generated content, AI policy, definitions.

**Authentication:**
- Users: CHILI GraFx account login.
- API: OAuth2 client_credentials flow via `https://integration-login.chiligrafx.com/oauth/token`.
- FSSO: OIDC and SAML supported.

**URL patterns:**
- Production: `https://{environment-name}.chili-publish.online/grafx`
- Sandbox: `https://{environment-name}.chili-publish-sandbox.online/grafx`

**Sub-pages (~40+ pages):**

| Section | Key URLs |
|---------|----------|
| Introduction | `/CHILI-GraFx/` |
| Applications | `/CHILI-GraFx/applications/overview/`, `/CHILI-GraFx/applications/editor-comparison/` |
| Concepts (8) | `/CHILI-GraFx/concepts/environments/`, `/concepts/federated-single-sign-on/`, `/concepts/grafx-labs/`, `/concepts/integrations/`, `/concepts/renders/`, `/concepts/sandbox/`, `/concepts/storage/`, `/concepts/subscriptions/` |
| Administration | `/CHILI-GraFx/admin/` |
| User Management (8) | `/CHILI-GraFx/users/intro/`, `/users/scope/`, `/users/roles/`, `/users/template-designer/`, `/users/creation/`, `/users/deactivate/`, `/users/delete/`, `/users/transition/` |
| How-to Guides (11) | `/CHILI-GraFx/guides/role-access-update/`, `/guides/manage-individual-access/`, `/guides/manage-user-groups/`, `/guides/manage-group-membership/`, `/guides/manage-group-access/`, `/guides/create-studio-template/`, `/guides/create-publisher-template/`, `/guides/setup-fsso/intro/`, `/guides/setup-fsso/oidc/`, `/guides/setup-fsso/saml/`, `/guides/setup-fsso/example-federated-groups-entraid/` |
| GraFx Labs (2) | `/CHILI-GraFx/guides/grafx-labs/grafx-genie-product-image-creator/`, `/guides/grafx-labs/graFx-genie-product-image-composer/` |
| Onboarding (7) | `/CHILI-GraFx/guides/onboarding/intro/`, `/onboarding/migration/`, `/onboarding/logging-in/`, `/onboarding/navigation/`, `/onboarding/applications/`, `/onboarding/upgrade/` |
| Trust (8) | `/CHILI-GraFx/trust/introduction/`, `/trust/security-policy/`, `/trust/compliance/`, `/trust/data-centers/`, `/trust/gdpr/`, `/trust/user-generated-content/`, `/trust/AI/`, `/trust/definitions/` |
| Other | `/CHILI-GraFx/support/`, `/CHILI-GraFx/browser-support/` |

### 3.8 Developer Center

**What it does:** Integration documentation for developers who want to embed CHILI GraFx into their applications. Covers three integration pillars: Editor Engine + Studio SDK, Environment API, and Connectors.

**Three integration pillars:**

1. **Editor Engine + Studio SDK**
   - Editor Engine: Flutter-based, closed-source, loaded in browser, processes JSON documents.
   - Studio SDK: JavaScript library (`@chili-publish/studio-sdk` on npm) for interacting with Editor Engine in an iframe.
   - Key controllers: `FrameController`, `ConnectorController`, `document.load()`.
   - Configuration via `WellKnownConfigurationKeys`: `GraFxStudioEnvironmentApiUrl`, `GraFxStudioAuthToken`.

2. **Environment API**
   - REST-like API for managing resources.
   - Base URL: `https://{ENVIRONMENT}.chili-publish.online/grafx/api/v1/environment/{ENVIRONMENT}/`
   - Swagger: `{ENVIRONMENT}.chili-publish.online/grafx/swagger/index.html`
   - Authentication: OAuth2 client_credentials → `https://integration-login.chiligrafx.com/oauth/token` (audience: `https://chiligrafx.com`).
   - Common endpoints: templates, projects, collections, connectors, output tasks, media, fonts.
   - Two token types: "dangerous" (full write, server-side only) and "readonly" (safe for front-end).

3. **Connectors**
   - Still marked **experimental** — APIs may change without notice.
   - Run in isolated sandboxed environment (no browser or Node.js APIs).
   - Use `ConnectorRuntimeContext` for `fetch()` and `logError()`.
   - Published via `connector-cli` tool.
   - Types: Media Connectors and Data Connectors.

**GitHub repositories:**

| Repository | Description |
|-----------|-------------|
| `chili-publish/studio-sdk` | Studio SDK — JS library for Editor Engine interaction |
| `chili-publish/studio-ui` | Studio UI — open-source minimalist end-user UI |
| `chili-publish/grafx-documentation` | Documentation source (MkDocs-based) |
| Connector Template | Template for creating custom connectors |

**Sub-pages (~30+ pages):**

| Section | Key URLs |
|---------|----------|
| Overview | `/GraFx-Developers/overview/` |
| GraFx Studio Integration | `/GraFx-Developers/grafx-studio/overview/`, `/grafx-studio/references/` |
| SDK Quickstart | `/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/01-overview/`, `.../03-loading-studio-sdk/` |
| Workshop: Custom UI | `/GraFx-Developers/grafx-studio/editor-engine/workshop-building-a-custom-ui/01-setting-up-the-project`, `.../05-working-with-the-media-connector/` |
| Workshop: Template Store | `/GraFx-Developers/grafx-studio/workshop-building-a-template-store/05-constructing-a-mock-database/`, `.../09-api-&-template-management/`, `.../11-authentication-data-management/` |
| Supplementary Materials | `/GraFx-Developers/grafx-studio/supplementary-materials/templates-vs-projects/`, `.../variable-data-printing-with-output-api/` |
| Environment API | `/GraFx-Developers/environment-api/02-managing-integrations/`, `.../04-making-api-calls/`, `.../reference/` |
| Connectors General | `/GraFx-Developers/connectors/connectors-introduction/`, `.../connector-cli/`, `.../connector-documentation/` |
| Data Connectors | `/GraFx-Developers/connectors/data-connector/data-connector-introduction/`, `.../build-a-simple-data-connector/` |
| Media Connectors | `/GraFx-Developers/connectors/media-connector/media-connector-introduction/`, `.../media-connector-fundamentals/` |

---

## 4. Cross-linking guidance

### 4.1 Concept → guide linking pattern

The documentation consistently pairs **concept pages** (explaining "what and why") with **guide pages** (explaining "how to"). When linking, follow this pattern:

| Concept Page | Corresponding Guide(s) |
|-------------|----------------------|
| `/GraFx-Studio/concepts/variables/` | `/GraFx-Studio/guides/template-variables/define/`, `/guides/template-variables/assign/` |
| `/GraFx-Studio/concepts/actions/` | `/GraFx-Studio/guides/actions/create/`, `/guides/actions/javascript/` |
| `/GraFx-Studio/concepts/layouts/` | `/GraFx-Studio/guides/layouts/` |
| `/GraFx-Studio/concepts/layout-intent/` | `/GraFx-Studio/guides/output/settings/` |
| `/GraFx-Studio/concepts/frames/` | `/GraFx-Studio/guides/text-frame/`, `/guides/image-frame/`, `/guides/shape-frame/` |
| `/GraFx-Studio/concepts/brandkits/` | `/GraFx-Studio/guides/brandkits/` |
| `/GraFx-Studio/concepts/connectors/` | `/GraFx-Studio/guides/connector-hub/` |
| `/GraFx-Studio/concepts/animation/` | `/GraFx-Studio/guides/animate-frame/` |
| `/GraFx-Studio/concepts/output-settings/` | `/GraFx-Studio/guides/output/settings/` |
| `/GraFx-Studio/concepts/template-management/` | `/GraFx-Studio/guides/create-projects/`, `/guides/manage-collections/`, `/guides/manage-user-interfaces/` |
| `/GraFx-Studio/concepts/genie-smart-crop/` | `/GraFx-Studio/guides/smart-crop/` |
| `/GraFx-Media/concepts/genie-smart-crop/` | `/GraFx-Media/guides/smart-crop-subject-area/` |
| `/CHILI-GraFx/concepts/environments/` | `/CHILI-GraFx/admin/` |
| `/CHILI-GraFx/concepts/federated-single-sign-on/` | `/CHILI-GraFx/guides/setup-fsso/intro/` |
| `/CHILI-GraFx/concepts/integrations/` | `/GraFx-Developers/environment-api/02-managing-integrations/` |

### 4.2 Cross-product linking relationships

```
GraFx Studio ←→ GraFx Fonts         (font selection in editor)
GraFx Studio ←→ GraFx Media         (asset browsing via GraFx Media connector)
GraFx Studio ←→ GraFx Brand Kits    (Brand Kit panel in editor)
GraFx Brand Kits → GraFx Fonts      (fonts sourced from GraFx Fonts)
GraFx Brand Kits → GraFx Media      (media assets sourced from GraFx Media)
GraFx Studio → Developer Center     (SDK, API, integration docs)
CHILI GraFx → Developer Center      (platform-level integrations, API)
GraFx Publisher → Developer Center   (PublisherInterface, JavaScript API)
All Products → Platform Updates      (release notes for all products)
```

### 4.3 Key concept pages and their URLs (quick reference)

| Topic | URL |
|-------|-----|
| Platform introduction | `/CHILI-GraFx/` |
| Environments | `/CHILI-GraFx/concepts/environments/` |
| Subscriptions | `/CHILI-GraFx/concepts/subscriptions/` |
| Renders | `/CHILI-GraFx/concepts/renders/` |
| User management | `/CHILI-GraFx/users/intro/` |
| Roles and scope | `/CHILI-GraFx/users/roles/`, `/CHILI-GraFx/users/scope/` |
| Integrations | `/CHILI-GraFx/concepts/integrations/` |
| FSSO | `/CHILI-GraFx/concepts/federated-single-sign-on/` |
| Trust/Security | `/CHILI-GraFx/trust/introduction/` |
| GraFx Studio intro | `/GraFx-Studio/` |
| Frames | `/GraFx-Studio/concepts/frames/` |
| Layouts | `/GraFx-Studio/concepts/layouts/` |
| Layout Intent | `/GraFx-Studio/concepts/layout-intent/` |
| Variables | `/GraFx-Studio/concepts/variables/` |
| Actions | `/GraFx-Studio/concepts/actions/` |
| Action Helper Functions | `/GraFx-Studio/concepts/helper-functions/` |
| Design & Run Mode | `/GraFx-Studio/concepts/design-run/` |
| Connectors (concept) | `/GraFx-Studio/concepts/connectors/` |
| Media connectors | `/GraFx-Studio/concepts/connectors-media/` |
| Data connectors | `/GraFx-Studio/concepts/connectors-data/` |
| Template management | `/GraFx-Studio/concepts/template-management/` |
| User Interfaces | `/GraFx-Studio/concepts/user-interface/` |
| Self-service | `/GraFx-Studio/concepts/self-service/` |
| Output settings | `/GraFx-Studio/concepts/output-settings/` |
| Headless | `/GraFx-Studio/concepts/headless/` |
| Brand Kits (concept) | `/GraFx-Studio/concepts/brandkits/` and `/GraFx-Brand-Kits/concepts/brandkit/` |
| GraFx Genie | `/GraFx-Studio/concepts/grafx-genie/` |
| Smart Crop | `/GraFx-Studio/concepts/genie-smart-crop/` |
| Media vs DAM | `/GraFx-Media/concepts/media-vs-dam/` |
| Fonts vs Families | `/GraFx-Fonts/concepts/fonts-vs-families/` |
| Editor comparison | `/CHILI-GraFx/applications/editor-comparison/` |

### 4.4 Key guide/how-to pages and their URLs (quick reference)

| Topic | URL |
|-------|-----|
| Hello World (Studio) | `/GraFx-Studio/guides/hello-world/` |
| Create layouts | `/GraFx-Studio/guides/layouts/` |
| Define template variables | `/GraFx-Studio/guides/template-variables/define/` |
| Create Actions | `/GraFx-Studio/guides/actions/create/` |
| Write Actions JavaScript | `/GraFx-Studio/guides/actions/javascript/` |
| Animate a frame | `/GraFx-Studio/guides/animate-frame/` |
| Create output settings | `/GraFx-Studio/guides/output/settings/` |
| Output PDF | `/GraFx-Studio/guides/output/pdf/` |
| Output JPG/PNG | `/GraFx-Studio/guides/output/image/` |
| Output MP4 | `/GraFx-Studio/guides/output/mp4/` |
| Output GIF | `/GraFx-Studio/guides/output/gif/` |
| Output HTML | `/GraFx-Studio/guides/output/html/` |
| Manage collections | `/GraFx-Studio/guides/manage-collections/` |
| Manage user interfaces | `/GraFx-Studio/guides/manage-user-interfaces/` |
| Create projects | `/GraFx-Studio/guides/create-projects/` |
| Connector Hub | `/GraFx-Studio/guides/connector-hub/` |
| Smart Crop | `/GraFx-Studio/guides/smart-crop/` |
| Upload media | `/GraFx-Media/guides/upload-media/` |
| Browse media | `/GraFx-Media/guides/browse/` |
| Set Subject Area | `/GraFx-Media/guides/smart-crop-subject-area/` |
| Upload fonts | `/GraFx-Fonts/guides/upload-fonts/` |
| Create a Brand Kit | `/GraFx-Brand-Kits/guides/create/` |
| Edit a Brand Kit | `/GraFx-Brand-Kits/guides/edit/` |
| Import a Brand Kit | `/GraFx-Brand-Kits/guides/import/` |
| Setup FSSO (OIDC) | `/CHILI-GraFx/guides/setup-fsso/oidc/` |
| Setup FSSO (SAML) | `/CHILI-GraFx/guides/setup-fsso/saml/` |
| Manage user groups | `/CHILI-GraFx/guides/manage-user-groups/` |
| Onboarding intro | `/CHILI-GraFx/guides/onboarding/intro/` |
| InDesign conversion (Studio) | `/GraFx-Studio/convert/Adobe-InDesign/` |
| Photoshop conversion (Studio) | `/GraFx-Studio/convert/Adobe-Photoshop/` |
| InDesign conversion (Publisher) | `/GraFx-Publisher/convert/Adobe-InDesign/` |
| Publisher JavaScript intro | `/GraFx-Publisher/guides/javascript/` |

### 4.5 Release notes location and structure

- **Main URL:** `/release-notes/`
- **All releases:** `/release-notes/releases/`
- **Operational updates:** `/release-notes/operational-updates/`
- **Experimental policy:** `/release-notes/experimental/`
- **RSS feed:** `/release-notes/rss/`
- **Yearly archives:** `/release-notes/archive/{YYYY}/` (2022–2026)
- **Individual note URL pattern:** `/release-notes/{YYYY}/{MM}/{DD}/{slug}`

Release notes are organized by date (reverse chronological) and by category (Releases or Operational Updates). Each entry includes a date, category tag, read time estimate, product icon, optional version number, and sections for "✨ New & Improved" and "🐛 What's Fixed". Products covered: GraFx Studio (versioned v1.21–v1.38+), GraFx Publisher (versioned v2026.x.x.x), CHILI GraFx Platform, GraFx Media, GraFx Fonts, GraFx Labs, Environment API, Plugins, Studio UI, and Connectors.

### 4.6 Developer Center key entry points

| Topic | URL |
|-------|-----|
| Developer Center landing | `/GraFx-Developers/overview/` |
| GraFx Studio integration overview | `/GraFx-Developers/grafx-studio/overview/` |
| References (SDK, API, GitHub) | `/GraFx-Developers/grafx-studio/references/` |
| SDK Quickstart | `/GraFx-Developers/grafx-studio/editor-engine/studio-sdk-quickstart/01-overview/` |
| Workshop: Building a Custom UI | `/GraFx-Developers/grafx-studio/editor-engine/workshop-building-a-custom-ui/01-setting-up-the-project` |
| Workshop: Building a Template Store | `/GraFx-Developers/grafx-studio/workshop-building-a-template-store/05-constructing-a-mock-database/` |
| Templates vs Projects | `/GraFx-Developers/grafx-studio/supplementary-materials/templates-vs-projects/` |
| VDP with Output API | `/GraFx-Developers/grafx-studio/supplementary-materials/variable-data-printing-with-output-api/` |
| Managing Integrations | `/GraFx-Developers/environment-api/02-managing-integrations/` |
| Making API Calls | `/GraFx-Developers/environment-api/04-making-api-calls/` |
| API Reference (Swagger) | `/GraFx-Developers/environment-api/reference/` |
| Connectors introduction | `/GraFx-Developers/connectors/connectors-introduction/` |
| Connector CLI | `/GraFx-Developers/connectors/connector-cli/` |
| Build a Data Connector | `/GraFx-Developers/connectors/data-connector/build-a-simple-data-connector/` |
| Media Connector Fundamentals | `/GraFx-Developers/connectors/media-connector/media-connector-fundamentals/` |

### 4.7 External resources

| Resource | URL |
|----------|-----|
| CHILI publish Academy | `https://product.chili-publish.academy/` |
| Studio SDK npm package | `@chili-publish/studio-sdk` |
| Studio SDK GitHub | `https://github.com/chili-publish/studio-sdk` |
| Studio UI GitHub | `https://github.com/chili-publish/studio-ui` |
| Documentation source GitHub | `https://github.com/chili-publish/grafx-documentation` |
| Integration login endpoint | `https://integration-login.chiligrafx.com/oauth/token` |
| Browser support | First-party: Chromium-based (latest 3 stable versions). Best-effort: others. |

---

## 5. Quick-reference: complete site map

```
docs.chiligrafx.com/
├── CHILI-GraFx/                          (~40+ pages)
│   ├── Introduction
│   ├── applications/overview/
│   ├── applications/editor-comparison/
│   ├── concepts/ (8: environments, fsso, grafx-labs, integrations, renders, sandbox, storage, subscriptions)
│   ├── admin/
│   ├── users/ (8: intro, scope, roles, template-designer, creation, deactivate, delete, transition)
│   ├── guides/ (11: role-access, individual-access, user-groups, group-membership, group-access, create-studio-template, create-publisher-template, fsso-intro/oidc/saml/entra-id-example)
│   ├── guides/grafx-labs/ (2: product-image-creator, product-image-composer)
│   ├── guides/onboarding/ (6: intro, migration, logging-in, navigation, applications, upgrade)
│   ├── trust/ (8: introduction, security-policy, compliance, data-centers, gdpr, user-generated-content, AI, definitions)
│   ├── support/
│   └── browser-support/
│
├── GraFx-Studio/                         (~105 pages)
│   ├── Introduction
│   ├── overview/ (12 pages: workspace elements)
│   ├── concepts/ (35+ pages: all features)
│   ├── guides/ (45+ pages: design, automate, animate, output, connectors, general)
│   ├── connectors/ (8 pages: 5 media + 3 data)
│   └── convert/ (3 pages: intro, InDesign, Photoshop)
│
├── GraFx-Publisher/                      (~5-10 pages)
│   ├── Introduction
│   ├── convert/Adobe-InDesign/
│   ├── guides/javascript/
│   ├── guides/javascript/document/
│   └── guides/hello-world/
│
├── GraFx-Media/                          (~10 pages)
│   ├── Introduction
│   ├── overview/ (elements, filetypes)
│   ├── concepts/ (media-vs-dam, genie-smart-crop)
│   └── guides/ (browse, search, manage-folders, upload-media, smart-crop-subject-area)
│
├── GraFx-Fonts/                          (~7 pages)
│   ├── Introduction
│   ├── overview/ (elements, supported-font-types)
│   ├── concepts/ (fonts-vs-families, fonts-in-publisher)
│   └── guides/ (upload-fonts, manage-fonts)
│
├── GraFx-Brand-Kits/                     (~7 pages)
│   ├── Introduction
│   ├── overview/
│   ├── concepts/ (brandkit, elements)
│   └── guides/ (create, edit, import)
│
├── release-notes/                        (blog-style, 50+ entries)
│   ├── Overview (main feed)
│   ├── releases/ (category filter)
│   ├── operational-updates/ (category filter)
│   ├── experimental/ (policy page)
│   ├── rss/ (RSS feed)
│   └── archive/ (2022, 2023, 2024, 2025, 2026)
│
└── GraFx-Developers/                    (~30+ pages)
    ├── overview/
    ├── grafx-studio/
    │   ├── overview/
    │   ├── references/
    │   ├── editor-engine/ (SDK quickstart, custom UI workshop)
    │   ├── workshop-building-a-template-store/
    │   └── supplementary-materials/ (templates-vs-projects, VDP)
    ├── environment-api/ (managing-integrations, making-api-calls, reference)
    └── connectors/ (introduction, CLI, docs, data-connector/, media-connector/)
```

---

*This KNOWLEDGE.md was generated from a comprehensive crawl of docs.chiligrafx.com on March 2, 2026. All information is factual and derived directly from the published documentation.*