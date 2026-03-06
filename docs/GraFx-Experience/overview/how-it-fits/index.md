## How GraFx Experience Fits in the CHILI GraFx Platform

Each application in CHILI GraFx has a clear role. Together, they form a controlled flow from design to execution.

### Role of GraFx Experience

GraFx Experience is the interface for non-design users.  
It exposes Design Systems in a guided way, so users can personalize content without breaking brand rules or layout logic.

Users do not design. They execute.

### Connection to GraFx Studio

**GraFx Studio** is where Design Systems are authored.

In GraFx Studio, designers:
- Build the underlying file (template)
- Define layout behavior and constraints
- Add business logic and variables
- Decide what end users can and cannot change

GraFx Experience consumes these Design Systems and enforces the rules defined in GraFx Studio.

### Connection to GraFx Media

**GraFx Media** provides the visual assets used during execution.

Images, videos, and other media used in GraFx Experience come from approved sources. This ensures:
- Brand consistency
- Reuse of approved assets
- No dependency on local files or ad-hoc uploads

### Connection to GraFx Brand Kits

**GraFx Brand Kits** define brand identity.

Colors, fonts, and styles are centralized and reused across the platform.  
GraFx Experience applies these automatically so end users do not need to understand brand guidelines to stay compliant.

### DAM-agnostic by design

GraFx Experience does not require a specific DAM.

You can:
- Use **GraFx Media** as the asset source
- Connect external DAMs and other content systems using the **Connector Framework**
- Pull in data from other platforms through the platform’s APIs and connectors

The Connector Framework provides a standardized way to integrate external content and data systems into the CHILI GraFx platform, so Experience can operate within your existing tech ecosystem.

### End-to-end flow

1. Design Systems are created in **GraFx Studio**
2. Brand identity and assets are centralized
3. GraFx Experience exposes these systems to end users
4. Users personalize content within defined guardrails
5. Final assets are generated for print or digital use

### What this enables

- Self-serve production without design tools
- Consistent brand execution at scale
- Clear separation between design and execution
- Integration with existing data and asset systems

GraFx Experience is the bridge between design intent and real-world execution.