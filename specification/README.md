# EASRA Specification Suite

The `specification/` folder contains the ten numbered documents that formally define EASRA. They are the authoritative source of truth. Everything in `handbook/`, `diagrams/`, `examples/`, and `reference-implementation/` derives from these documents.

## Reading order

| # | Document | Read if you are… |
|---|----------|------------------|
| [001](./001-introduction.md) | Introduction, Vision and Scope | New to EASRA. |
| [002](./002-design-principles.md) | Design Principles | Evaluating whether EASRA fits your context. |
| [003](./003-terminology.md) | Terminology | Reading anywhere else in the repo. |
| [004](./004-reference-architecture.md) | Reference Architecture | Doing architecture on a new AI system. |
| [005](./005-layer-definitions.md) | Layer Definitions | Deciding what belongs in which layer. |
| [006](./006-interface-specification.md) | Interface Specification | Building or replacing a layer. |
| [007](./007-data-flow.md) | Data Flow | Reasoning about how data moves. |
| [008](./008-sequence-diagrams.md) | Sequence Diagrams | Reasoning about how requests execute. |
| [009](./009-trust-boundaries.md) | Trust Boundaries | Threat-modelling or hardening. |
| [010](./010-nfr.md) | Non-Functional Requirements | Setting SLOs or writing conformance criteria. |

## Editing the specification

Specification changes follow the process in [`../CONTRIBUTING.md`](../CONTRIBUTING.md) and [`../GOVERNANCE.md`](../GOVERNANCE.md). Structural changes require an ADR and a 14-day public comment period.

## Versioning

Every spec file has a header table with its version. The repository-level version tracked in [`../CHANGELOG.md`](../CHANGELOG.md) references the last coordinated release of the whole suite.

## Conformance

A system is EASRA-conformant when it satisfies the rules in [Specification 001 §12](./001-introduction.md#12-conformance) and the per-NFR conformance rules in [Specification 010](./010-nfr.md).
