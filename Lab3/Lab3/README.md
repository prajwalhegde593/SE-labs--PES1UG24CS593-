# Lab 3 — Component Modelling and Architectural Pattern Selection

Continuation of Labs 1 and 2. The requirements baseline from Lab 1 is evaluated against three
architectural styles, one style is selected, and the system is modelled as a UML component diagram.

**Architecture selected: Layered.**

## Deliverables

1. `Lab3_Component_Diagram.pdf`
   - Three layers: Presentation, Business Logic, Data Access
   - Seven internal components, two client applications, two external systems
   - Nine named interfaces in provided (ball) and required (socket) notation
   - Four `«use»` dependencies, with protocols labelled on every connector
   - PNG copy: `Lab3_Component_Diagram.png`; editable source: `Lab3_Component_Diagram.drawio`

2. `Lab3_Architecture_Justification.docx`
   - Comparison of Microservices, Client–Server and Layered against this scenario
   - Two scenario-specific reasons for the selection
   - One security advantage and one performance benefit
   - PDF copy: `Lab3_Architecture_Justification.pdf`

## Components

| Component | Source | Layer | Responsibility |
|---|---|---|---|
| Web Portal UI Component | Identified | Presentation | Interface for both the Client Buyer and the Digital Artist |
| Order Manager Component | Given in handout | Business | Orchestrates brief, milestone, draft and approval flow |
| Payment Service Component | Given in handout | Business | Calls the external gateway, reports verified payment |
| Watermarking Service Component | Identified | Business | Applies and verifies the diagonal overlay before publication |
| Entitlement & Audit Component | Identified | Business | One entitlement per verified payment; immutable audit events |
| Asset Store Adapter Component | Identified | Data Access | Sole holder of private storage credentials; mints signed URLs |
| Commission Database Component | Identified | Data Access | Transactional store for commissions, entitlements and audit log |

External systems: Payment Gateway, Object Storage (S3-compatible).

## Interfaces

| Interface | Provider → Consumer | Protocol |
|---|---|---|
| IBuyerPortal | Web Portal UI → Client Buyer Portal | HTTPS / TLS 1.2+ |
| IArtistStudio | Web Portal UI → Digital Artist Studio | HTTPS / TLS 1.2+ |
| ICommissionAPI | Order Manager → Web Portal UI | REST / JSON |
| **IPayment** | Payment Service → Order Manager | payment processing requests *(given)* |
| IWatermark | Watermarking Service → Order Manager | asynchronous job queue |
| IEntitlement | Entitlement & Audit → Order Manager | in-process call |
| IPersistence | Commission Database → Order Manager | JDBC / SQL |
| IAssetStore | Asset Store Adapter → Watermarking Service | store original / preview |
| ISignedUrl | Asset Store Adapter → Entitlement & Audit | 60-minute expiry |

`«use»` dependencies: Payment Service → Payment Gateway (HTTPS, tokenised), Asset Store Adapter →
Object Storage (signed URL), Entitlement & Audit → Commission Database (append-only audit).

## Why layered

Argued in full in the justification document. In summary: FR-005 requires that payment verification,
entitlement creation and download authorisation always agree, which is a transactional problem rather
than a scaling one; FR-001 requires that no unwatermarked draft can ever reach the buyer, which a single
code path from upload to publication enforces structurally; the Data Access Layer is the only holder of
private-storage credentials, so a compromised UI layer cannot reach an original; and because URL signing
is a local operation on an in-process call chain, NFR-001's target of 95% of URLs within 2 seconds is met
without a network hop, with watermarking pushed to an asynchronous worker off the critical path.

## Traceability to Lab 1

- FR-001 (diagonal watermark on every draft) → Watermarking Service Component
- FR-002 (creative brief submission) → Web Portal UI, Order Manager Component
- FR-003 (accept commission, milestones, versioned WIP uploads) → Order Manager, Asset Store Adapter
- FR-004 (review, feedback, revision, approval) → Web Portal UI, Order Manager
- FR-005 (unlock final files only after verified payment) → Payment Service, Entitlement & Audit
- NFR-001 (signed URLs, 60-minute expiry, 2-second generation) → Asset Store Adapter
- NFR-002 (99.9% availability, 365-day immutable audit) → Entitlement & Audit, Commission Database

## Project Details

- SRN: PES1UG24CS593
- Problem Statement: 58
- Project: Digital Art Commission & Watermarking Portal
- Domain: Media, Events & Community
- Target Actors: Client Buyer, Digital Artist, Payment Gateway
