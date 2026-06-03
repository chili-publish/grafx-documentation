# Use of AI in CHILI GraFx

CHILI GraFx uses artificial intelligence to support creative automation workflows. AI is embedded in specific parts of the platform to reduce manual work and improve consistency. It is not a standalone product and it does not operate independently of user-defined rules, templates, or constraints.

## Where AI is used

AI is applied selectively and always in support of existing platform capabilities. Today, AI powers three distinct capabilities:

- **GraFx Genie Actions** — generates template logic (code) from your input, helping you build smart, automated templates faster. See [Actions](/GraFx-Studio/guides/actions/create/).
- **GraFx Genie Vision** — analyses uploaded images to detect the subject and the Point of Interest, producing the metadata that powers [Smart Crop](/GraFx-Media/concepts/genie-smart-crop/).
- **GraFx Labs** — an experimental space that currently exposes AI-powered image generation and manipulation. See [GraFx Labs](/CHILI-GraFx/concepts/grafx-labs/).

AI augments these workflows without removing user control.

## What AI does not do

AI in CHILI GraFx has clear boundaries:

- It does not act autonomously
- It does not publish, approve, or distribute content
- It does not bypass template constraints or brand rules
- It does not make creative, legal, or business decisions

All outputs remain under user control.

## Data usage and training

- Customer data is only processed to deliver the Services provided by the platform
- Customer data is **not** used to train, enrich, or improve AI models for any other purpose
- There is no cross-customer data usage
- There is no reuse of customer data outside the scope of the Services

## AI transparency and content marking

CHILI GraFx aims to make it clear when content has been shaped by AI. How this is surfaced depends on the capability, because each produces a different kind of output:

- **GraFx Genie Actions** produces standard template logic in plain JavaScript — the same kind of script a developer would write by hand. It is reviewed and controlled by the template designer and runs only within the fenced logic of a template.
- **GraFx Genie Vision** records, in the asset's metadata, whether its Subject Area and Point of Interest were determined by AI or set manually — so it is always possible to tell AI-detected values apart from human-defined ones. These values can be reviewed and overridden by the user at any time.
- **GraFx Labs** labels AI-generated images as created using generative AI (recorded as a *Content Creator: Created using Generative AI* marker on the image), so generated visuals can be recognised as such.

## Handling metadata from your content

When you bring content into CHILI GraFx, the metadata attached to it is preserved while the asset is stored on the platform.

How metadata travels beyond that point — for example across connectors, when content is exported in a different file format than it was uploaded in, or when several assets are combined into a single output — depends on the workflow and the formats involved. Recognising and carrying through metadata markers, including any that indicate AI involvement, is an area we continue to develop as standards and customer needs evolve. If you rely on specific metadata being retained end to end, we recommend validating it for your particular workflow.

## Security, Compliance, and AI Governance

AI components are subject to the same security and compliance standards as the rest of the CHILI GraFx platform. All AI-powered functionality is managed within our [ISO-certified framework](/CHILI-GraFx/trust/compliance/#compliance_1), ensuring that safeguards and controls are strictly aligned with the risk level of each specific capability.

**AI Tooling and Dynamic Evaluation**

Because AI capabilities evolve rapidly, CHILI GraFx does not maintain a fixed or exhaustive list of AI tools. Instead of a static list, we apply a continuous governance model to ensure every component remains compliant:

- Integrated risk management: All AI tools undergo formal Risk Management and Tool Qualification before deployment.
- External dependency evaluation: AI components are reviewed under our standard Third-Party Dependency protocols to ensure data integrity and security.
- Purpose-driven assessment: Each capability is continuously assessed for data handling, security impact, and alignment with CHILI GraFx’s quality standards.

Only AI components that pass these internal audits and meet compliance criteria are made available within the platform.

## Ethical Engineering of Artificial Intelligence

CHILI GraFx is committed to the responsible engineering of artificial intelligence. AI components are designed, implemented, and validated using defined safeguards to ensure they operate within their intended scope.

Where applicable, AI functionality is evaluated to reduce the risk of unintended bias and to ensure consistent and predictable behavior. AI is used to support creative and operational workflows, not to replace human judgment or decision-making.

All AI capabilities are developed and deployed in line with CHILI GraFx’s broader governance, security, and compliance principles.
