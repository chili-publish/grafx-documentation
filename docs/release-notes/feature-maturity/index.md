# Feature maturity

Every capability is described by two separate things: its **maturity** (how finished and supported it is) and its **channel** (how you get access to it). We always state both, because one does not imply the other — a capability can be well-tested but invitation-only, or open to everyone but still in Beta.

You will see them written together, maturity first, for example *Beta / Limited Availability* or *Alpha / GraFx Labs*. You are always told a capability's maturity, so you can assess the risks before you rely on it.

## Maturity: how finished it is

**Alpha** — real functionality that is on the roadmap, but incomplete or unstable. It exists to validate the idea and gather deep feedback. Support is best-effort and there is no SLA. The capability can change materially or be removed, and we tell you this up front. Not intended for business-critical use.

**Beta** — feature-complete or close to it, and built through our standard development process: testing, security screening, release management and monitoring. Beta capabilities are monitored internally, but without a customer-facing monitoring commitment. You get a real support channel with reduced response commitments, but no contractual uptime. Behavior can still change; breaking changes are communicated.

**Production Grade** — fully released, with standard support and a contractual SLA. Changes follow our normal versioning and deprecation policy.

**Deprecated** — being phased out on a published timeline, with support winding down towards removal.

**Security and data handling** — from Alpha onwards, every capability passes a baseline security and data-handling review before any customer or customer data is involved, without exception. From Beta onwards, capabilities also go through our full standard security review.

## Channel: how you get access

**GraFx Labs** — self-serve and opt-in, in a clearly separated area of the platform. Low-touch, and typically carries Alpha or Beta capabilities. See [GraFx Labs](/CHILI-GraFx/concepts/grafx-labs/) for what is available there today.

**Limited Availability** — a group of invited customers, working directly with us in a hand-held feedback loop. Typically carries Alpha or Beta capabilities.

**General Availability** — open to every client, with no invitation or opt-in required. General Availability describes who has access, not how mature a capability is. Most capabilities in General Availability are Production Grade; some are Beta, and in exceptional cases Alpha. The maturity label determines support, SLA and how much the capability may change.

Channels are not a fixed sequence. A capability can go straight to Limited Availability, or run in GraFx Labs and never need it — it depends on how much guidance the capability needs.

## Experimental (being retired)

**Experimental** was a single label trying to say both things at once. It is being replaced by the maturity stages and channels above; in practice, anything previously marked Experimental maps to **Alpha**.

You may still see the old label on a few pages while the change is rolled out. Historical release notes keep the wording they were published with.

## Getting access

To take part in Limited Availability for a specific capability, contact your account manager or [our support team](/CHILI-GraFx/support/).
