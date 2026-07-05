# EASRA Architectures — Five Views

EASRA is described through **five architecture views**, each answering a different set of questions and speaking to a different audience. Together they turn the 16-layer logical model into a system engineers, operators, security architects, and auditors can build, run, and defend.

The views are derived from — and consistent with — the frozen [Capability Model](../specification/011-capability-model.md), the [Component Catalogue](../specification/012-component-catalogue.md), and the [Interface Specification](../specification/006-interface-specification.md). Every diagram in [`../diagrams/`](../diagrams/) belongs to exactly one view and is inventoried in the [Diagram Catalogue](../diagrams/CATALOGUE.md).

## The five views

| View | Answers | Primary audience | Sub-folder |
|------|---------|------------------|------------|
| **Logical Architecture** | *What are the parts, how do they compose, and what does each do?* | Architects, senior engineers | [logical/](./logical/) |
| **Runtime Architecture** | *How does a request execute, step by step, across those parts?* | Engineers, SREs, evaluators | [runtime/](./runtime/) |
| **Deployment Architecture** | *Where does each part run, and how is it scaled and made resilient?* | Platform engineers, SREs | [deployment/](./deployment/) |
| **Operational Architecture** | *How is the system observed, evaluated, delivered, and evolved safely?* | SREs, LLMOps, quality engineers | [operational/](./operational/) |
| **Security Architecture** | *What are the trust boundaries, threats, controls, and audit paths?* | Security architects, auditors | [security/](./security/) |

## How the views relate

- The **Logical view** is the source of truth for structure. Every other view is a projection of it.
- The **Runtime view** describes execution over the logical structure.
- The **Deployment view** places the logical structure onto physical / cloud substrate.
- The **Operational view** describes the control loops around the deployed runtime.
- The **Security view** overlays trust boundaries and controls on all four.

```
                        ┌────────────────────────────┐
                        │       Logical View          │
                        │  (structure — source of truth) │
                        └──────────────┬─────────────┘
                                       │
       ┌───────────────┬───────────────┼───────────────┬───────────────┐
       ▼               ▼               ▼               ▼               ▼
 ┌───────────┐  ┌───────────┐  ┌───────────────┐  ┌────────────┐  ┌───────────┐
 │  Runtime  │  │Deployment │  │  Operational   │  │  Security  │  │ (future)  │
 │  view     │  │  view     │  │  view          │  │  view      │  │ views     │
 └───────────┘  └───────────┘  └───────────────┘  └────────────┘  └───────────┘
```

## Scope guardrails

- A view **adds no capability** that is not in the [Capability Model](../specification/011-capability-model.md).
- A view **references no component** that is not in the [Component Catalogue](../specification/012-component-catalogue.md).
- A diagram belongs to **exactly one view**. Cross-view relationships are described in prose, not by placing a diagram in two folders.

## Reading order

1. [Logical Architecture](./logical/) — read this first; it is the frame every other view sits inside.
2. [Runtime Architecture](./runtime/) — read next if you build features.
3. [Deployment Architecture](./deployment/) — read next if you run the system.
4. [Operational Architecture](./operational/) — read alongside deployment.
5. [Security Architecture](./security/) — read alongside all of the above; do not defer it.
