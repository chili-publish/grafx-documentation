# Feature maturity

Two separate things describe a capability that isn't fully released yet: **how finished it is**, and **how you get access to it**. We always state both, because one does not imply the other — a capability can be well-tested but invitation-only, or self-serve but still unstable.

You will see them written together, for example *beta / Limited Availability* or *alpha / GraFx Labs*.

## How finished it is

**Alpha** — real functionality that is on the roadmap, but incomplete or unstable. It exists to validate the idea and gather deep feedback. Support is best-effort through a named contact rather than a ticket queue, there is no SLA, and the capability can change materially or be removed. Not for production use.

**Beta** — feature-complete or close to it, and built through our standard development process: testing, security screening, release management and monitoring. You get a real support channel with reduced response commitments, but no contractual uptime. Behavior can still change; breaking changes are communicated.

**Production Grade** — fully released, with standard support and a contractual SLA. Changes follow our normal versioning and deprecation policy.

**Deprecated** — being phased out on a published timeline, with support winding down towards removal.

Before any capability touches real customer data, it clears a security and data-handling review — from alpha onwards, without exception.

## How you get access

**GraFx Labs** — self-serve and opt-in, in a clearly isolated area of the platform. Low-touch, and typically carries alpha or beta capabilities. See [GraFx Labs](/CHILI-GraFx/concepts/grafx-labs/) for what is running there today. Each render is charged as a production output, so GraFx Labs is not available on [Sandbox](/CHILI-GraFx/concepts/sandbox/).

**Limited Availability** — a group of invited customers, working directly with us in a hand-held feedback loop.

**General Availability** — open to every client, with standard support. Production Grade.

These are not a fixed sequence. A capability can go straight to a Limited Availability Program, or run in GraFx Labs and never need one — it depends on how much guidance the capability needs.

## Experimental (being retired)

**Experimental** was a single label trying to say both things at once. It is being replaced by the maturity stages and channels above; in practice, anything previously marked Experimental maps to **alpha**.

You may still see the old label on a few pages while the change is rolled out. Historical release notes keep the wording they were published with.

## Getting access

Alpha and beta capabilities are enabled per environment. Contact your account manager or [our support team](/CHILI-GraFx/support/) to ask about a specific capability.
