# Logical Architecture

## Purpose

The **Logical Architecture** describes *what* Enterprise AI systems are made of, *how the parts compose*, and *what each part is responsible for* — independent of any runtime execution, deployment target, operational tooling, or security control.

It is the source of truth for structure. Every other architecture view in EASRA is a projection of, and consistent with, this view.

## Audience

- Architects, principal engineers, standards reviewers.
- Anyone modifying a layer, component, or interface.

## Scope

- The 16 EASRA layers.
- The capability domains satisfied by each layer.
- The named components at each layer.
- The interfaces between layers.
- Cross-cutting substrate components.

Out of scope: request execution (→ Runtime), physical placement (→ Deployment), monitoring (→ Operational), threat model (→ Security).

## Anchoring specifications

| Spec | Purpose |
|------|---------|
| [004 Reference Architecture](../../specification/004-reference-architecture.md) | Definitive 16-layer model. |
| [005 Layer Definitions](../../specification/005-layer-definitions.md) | Per-layer responsibilities, inputs, outputs, invariants, failure modes. |
| [006 Interface Specification](../../specification/006-interface-specification.md) | Normative interfaces between layers. |
| [011 Capability Model](../../specification/011-capability-model.md) | Frozen capability vocabulary. |
| [012 Component Catalogue](../../specification/012-component-catalogue.md) | Frozen component inventory. |

## Diagrams

See the [Diagram Catalogue](../../diagrams/CATALOGUE.md) for status, IDs, and paths.

| ID | Title | Status |
|----|-------|--------|
| D-L1 | High-Level Architecture (16 layers) | Done — [`../../diagrams/high-level-architecture.md`](../../diagrams/high-level-architecture.md) |
| D-L2 | Component Master Diagram | Planned |
| D-L3 | Memory Architecture (L4 zoom-in) | Planned |
| D-L4 | Knowledge & Retrieval Architecture (L5 zoom-in) | Planned |
| D-L5 | Guardrails & Verification Architecture (L8+L9 zoom-in) | Planned |

## Change control

Any change to the layer count, layer numbering, or layer scope requires an ADR ([`../../adr/`](../../adr/)) with a 14-day public comment period, per [GOVERNANCE.md](../../GOVERNANCE.md).
