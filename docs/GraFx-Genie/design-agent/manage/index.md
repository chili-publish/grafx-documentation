# Enable, disable and data

## Availability

The [Design Agent](/GraFx-Genie/design-agent/) is available in [Beta](/release-notes/feature-maturity/#maturity-how-finished-it-is) in the GraFx Studio template workspace, to users with a Template Designer seat. It carries a **Beta** label in the interface. The Design Agent is part of the product, not a [GraFx Labs](/CHILI-GraFx/concepts/grafx-labs/) experiment.

## Opt out per environment

Organisations that do not want AI features in a given environment can switch the Design Agent off.

1. Open the environment's **Environment settings**.
2. Go to **AI opt-out**.
3. Under **GraFx Genie**, switch **Design agent** off.

![The AI opt-out page with two cards: GraFx Labs with its toggle, and GraFx Genie with the Design agent toggle](ai-opt-out.png){.screenshot-full}

The toggle is on by default. When it is off, the Design Agent is hidden for every user in that environment, in the template and the component workspace. The same page holds the **GraFx Labs** toggle; the two are independent. GraFx Genie Vision (Smart Crop) and GraFx Genie for Actions are not affected by either toggle.

Only Subscription Admins and Environment Admins can change the opt-out, see [roles](/CHILI-GraFx/users/roles/). Integrations read and set the same setting through the environment settings endpoint of the Environment API (`applicationsConfig.genie.features`, value `conversational_agents`).

## Who can use it

- **Use the chat:** anyone who can open a template in the GraFx Studio workspace, that is, users with a Template Designer seat.
- **Manage custom skills:** Subscription Admins and Environment Admins, in **Environment settings › Skills**. See [custom skills](/GraFx-Genie/design-agent/skills/).
- **Manage Brand Kit descriptions:** anyone who can edit the Brand Kit in GraFx Brand Kits. See [Brand Kit descriptions](/GraFx-Genie/design-agent/brand-kit-descriptions/).

## Usage

AI calls count against the fair-use allowance of your subscription tier. During the Beta this is a soft, monitored limit; it is not enforced and there is no usage report in the Platform UI. Your Account Manager can tell you where you stand.

## What is logged, and why

To improve the agent, CHILI publish logs the conversations: each message from the user and from the agent, with a timestamp, the environment, the template, the user ID and, per AI call, the model and token usage. Email addresses are not logged. Logs are used to understand how designers work with the agent and where it falls short; they are not used to bill, and customer data is not used to train models for any other purpose, see [Use of AI in CHILI GraFx](/CHILI-GraFx/trust/AI/).

The agent only acts on the template that is open, through the same GraFx Studio operations a designer uses. It does not publish, approve or distribute content, and it does not change assets in GraFx Media or elements in GraFx Brand Kits.
