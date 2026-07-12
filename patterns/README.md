# EASRA Pattern Catalog

**Patterns** are reusable, opinionated designs that solve a recurring problem in enterprise AI. Where **architectures** (EA-xxx) describe the *system-level blueprint* and **reference models** describe the *thinking frames*, patterns describe **how to actually build a specific slice** — with a diagram, interfaces, controls, KPIs, and known trade-offs.

Inspired by [Microsoft Azure Architecture Center](https://learn.microsoft.com/azure/architecture/patterns/) and the *Enterprise Integration Patterns* tradition.

## Pattern Template

Every pattern in EASRA follows a common structure:

- **Context** — when this pattern applies
- **Problem** — what it solves
- **Solution** — the design, with a diagram
- **Interfaces** — inputs, outputs, contracts
- **Controls** — safety, quality, cost controls
- **KPIs** — how to measure success
- **Trade-offs** — what you give up
- **Variants** — common adaptations
- **Anti-patterns** — what to avoid
- **Reference implementations** — links to concrete code (when available)

## Catalog

| ID     | Pattern                          | Layer(s)                     | Status         |
|--------|----------------------------------|------------------------------|----------------|
| PAT-001 | [AI Gateway](PAT-001-AI-Gateway.md)                       | L2 Gateway                    | 🟡 Draft |
| PAT-002 | [Multi-Agent Orchestration](PAT-002-Multi-Agent.md)        | L3 Runtime                    | 🟡 Draft |
| PAT-003 | [Verification Loop](PAT-003-Verification.md)               | L5 Verification               | 🟡 Draft |
| PAT-004 | [Prompt Intelligence](PAT-004-Prompt-Intelligence.md)      | L2 Gateway, L7 Guardrails     | 🟡 Draft |
| PAT-005 | [Retrieval-Augmented Generation (RAG)](PAT-005-RAG.md) | L2, L4                        | 🌱 Stub |
| PAT-006 | [Memory](PAT-006-Memory.md)                            | L3                            | 🌱 Stub |
| PAT-007 | [Human-in-the-Loop](PAT-007-HITL.md)                   | L3, L7                        | 🌱 Stub |
| PAT-008 | [Model Router](PAT-008-Router.md)                      | L2, L6                        | 🌱 Stub |
| PAT-009 | [Continuous Evaluation](PAT-009-Continuous-Eval.md)    | L5                            | 🌱 Stub |
| PAT-010 | [Feedback Curation](PAT-010-Feedback-Curation.md)      | L5, L6                        | 🌱 Stub |

## Relationship to Architectures

Patterns are *composable pieces* of the architectures:

- **EA-001** (system reference) → composed of many patterns
- **EA-002** (AI Gateway) → productized as **PAT-001**
- **EA-003** (Runtime Plane) → productized as **PAT-002** + **PAT-007**
- **EA-005** (Knowledge Plane) → productized as **PAT-005**
- **EA-006** (Model Router) → productized as **PAT-008**
- **EA-007** (Prompt Intelligence) → productized as **PAT-004**
- **EA-008** (Memory Plane) → productized as **PAT-006**
- **EA-010** (Verification Plane) → productized as **PAT-003** + **PAT-009** + **PAT-010**

See the [Capability Model](../reference-models/capability-model.md) for how layers, architectures, and patterns line up.
