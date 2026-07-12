# EASRA

**Enterprise AI Systems Reference Architecture**

> The open, vendor-neutral reference standard for building, governing, and operating enterprise-grade AI systems.

[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)](#)
[![Sprint](https://img.shields.io/badge/sprint-02-orange.svg)](ROADMAP.md)
[![Flagship](https://img.shields.io/badge/EA--001-v1.0-8A2BE2.svg)](architectures/EA-001-Enterprise-AI-Systems.md)
[![Gateway](https://img.shields.io/badge/EA--002-v0.1-0A84FF.svg)](architectures/EA-002-Enterprise-AI-Gateway.md)
[![Runtime](https://img.shields.io/badge/EA--003-v0.1-7A5EC2.svg)](architectures/EA-003-Runtime-Plane.md)
[![Azure%20Impl](https://img.shields.io/badge/impl-azure%2Fai--gateway-1F6FEB.svg)](implementations/azure/ai-gateway/README.md)
[![Capability%20Model](https://img.shields.io/badge/capability%20model-v0.1-1F6FEB.svg)](reference-models/capability-model.md)
[![License](https://img.shields.io/badge/license-TBD-lightgrey.svg)](#license)

![EA-001 Enterprise AI Systems Reference Architecture v1.0](diagrams/EA-001-Enterprise-AI-Systems-Reference-Architecture-v1.png)

<sub>▲ **EA-001 v1.0 · Enterprise AI Systems Reference Architecture** — the flagship EASRA blueprint. Full page: [architectures/EA-001-Enterprise-AI-Systems.md](architectures/EA-001-Enterprise-AI-Systems.md).</sub>

---

## What EASRA Is

EASRA is a **reference standard**, not a product and not a tutorial. It defines:

- The **architectures** (EA-xxx) an enterprise needs to run AI safely and at scale.
- The **capability model** (7 layers, ~60 capabilities) to measure where you stand today.
- The **patterns** (PAT-xxx) to build the pieces reusably.
- The **reference models** (capability · operating · deployment · governance · runtime) to reason across them.
- The **specification, handbook, checklists, and ADRs** to make the whole thing operable.

Think of it as *TOGAF for enterprise AI*, informed by *Azure Architecture Center*, *OpenTelemetry*, and modern agent frameworks.

## What EASRA Is Not

- **Not a vendor product.** Every capability is described in vendor-neutral terms.
- **Not tied to one cloud, one model provider, or one framework.** Reference implementations for Azure, AWS, GCP, and Kubernetes will land under [`implementations/`](implementations/).
- **Not a replacement for organization-specific security & compliance review.** It gives you the blueprint and the controls map; your controls team still owns approval.

---

## Flagship Artifacts

| Artifact | What it is | Where |
|---|---|---|
| **EA-001** — Enterprise AI Systems Reference Architecture | The 7-plane blueprint of an enterprise AI platform | [architectures/EA-001-Enterprise-AI-Systems.md](architectures/EA-001-Enterprise-AI-Systems.md) |
| **EA-002** — Enterprise AI Gateway | The single policy-enforcing ingress for all AI traffic | [architectures/EA-002-Enterprise-AI-Gateway.md](architectures/EA-002-Enterprise-AI-Gateway.md) |
| **Capability Model** | 7 layers, ~60 capabilities, 5-level maturity scale | [reference-models/capability-model.md](reference-models/capability-model.md) |
| **Pattern Catalog** | Reusable designs (PAT-001…) with diagrams, KPIs, controls | [patterns/README.md](patterns/README.md) |

---

## Architecture Map

The full EASRA architecture set:

| ID | Architecture | Capability layer | Status |
|----|--------------|-------------------|--------|
| **EA-001** | [Enterprise AI Systems Reference Architecture](architectures/EA-001-Enterprise-AI-Systems.md) | All | ✅ **v1.0 (Sprint-02)** |
| **EA-002** | [Enterprise AI Gateway](architectures/EA-002-Enterprise-AI-Gateway.md) | L2 Gateway | ✅ v0.1.0 |
| **EA-003** | [Runtime Plane](architectures/EA-003-Runtime-Plane.md) | L3 Runtime | ✅ **v0.1 (Sprint-02)** |
| **EA-004** | Control Plane | L6 Operations | ⏳ Planned |
| **EA-005** | Knowledge Plane | L4 Knowledge | ⏳ Planned |
| **EA-006** | Verification Plane | L5 Verification | ⏳ Planned |
| **EA-007** | Guardrails Plane | L7 Guardrails | ⏳ Planned |
| **EA-008** | Observability Plane | L5 + L7 | ⏳ Planned |

Track progress in [ROADMAP.md](ROADMAP.md).

---

## Pattern Catalog (excerpt)

| ID | Pattern | Layer |
|----|---------|-------|
| [PAT-001](patterns/PAT-001-AI-Gateway.md) | AI Gateway | L2 |
| [PAT-002](patterns/PAT-002-Multi-Agent.md) | Multi-Agent Orchestration | L3 |
| [PAT-003](patterns/PAT-003-Verification.md) | Verification Loop | L5 |
| [PAT-004](patterns/PAT-004-Prompt-Intelligence.md) | Prompt Intelligence | L2, L7 |
| PAT-005 … PAT-010 | RAG · HITL · Router · Guardrailed Tool Use · Continuous Eval · Feedback Curation | *(planned)* |

Full catalog & template: [patterns/README.md](patterns/README.md).

---

## Reference Models

The "thinking frames" of EASRA:

| Model | Question it answers |
|-------|----------------------|
| [Capability Model](reference-models/capability-model.md) | *What capabilities does an enterprise AI platform need?* |
| [Operating Model](reference-models/operating-model.md) | *Who owns what, and how is AI operated?* |
| [Deployment Model](reference-models/deployment-model.md) | *Where does AI run — cloud, edge, on-prem, hybrid?* |
| [Governance Model](reference-models/governance-model.md) | *How are policy, risk, safety decisions made and enforced?* |
| [Runtime Model](reference-models/runtime-model.md) | *How does a single request execute end-to-end at runtime?* |

---

## Repository Layout

```
EASRA/
├── README.md
├── ROADMAP.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
│
├── architectures/          ← canonical EA-xxx architecture pages
│   ├── EA-001-Enterprise-AI-Systems.md
│   ├── EA-002-Enterprise-AI-Gateway.md
│   └── EA-003-Runtime-Plane.md
│
├── reference-models/       ← capability / operating / deployment / governance / runtime models
│   ├── capability-model.md
│   ├── operating-model.md
│   ├── deployment-model.md
│   ├── governance-model.md
│   └── runtime-model.md
│
├── patterns/               ← PAT-xxx reusable pattern catalog
│   ├── README.md
│   ├── PAT-001-AI-Gateway.md
│   ├── PAT-002-Multi-Agent.md
│   ├── PAT-003-Verification.md
│   └── PAT-004-Prompt-Intelligence.md
│
├── diagrams/               ← source (SVG / .drawio) + PNG exports
│   ├── EA-001-Enterprise-AI-Systems-Reference-Architecture-v1.svg
│   ├── EA-001-Enterprise-AI-Systems-Reference-Architecture-v1.png
│   ├── EA-002-Enterprise-AI-Gateway.svg
│   ├── EA-002-Enterprise-AI-Gateway.png
│   ├── EA-003-Runtime-Plane.svg
│   └── EA-003-Runtime-Plane.png
│
├── docs/                   ← guides, decisions, glossary
│   ├── README.md
│   ├── architecture/
│   ├── patterns/
│   ├── decisions/          ← ADRs
│   └── glossary.md
│
├── specification/          ← formal EASRA specification (numbered)
├── handbook/               ← L00–L07 practitioner handbook
├── benchmarks/             ← performance / cost / quality / grounding
├── checklists/             ← adoption & review checklists
├── conference/             ← whitepaper, decision book, slides
├── examples/               ← illustrative samples
├── implementations/        ← concrete cloud implementations
│   ├── README.md
│   └── azure/
│       └── ai-gateway/     ← EA-002 on Azure: APIM + Functions + Redis + Foundry
├── reference-implementation/
├── security-reference/
├── verification-reference/
├── llmops-guide/
├── research/
├── templates/
├── assets/                 ← logos, banners, images
└── .github/                ← issue & PR templates
```

---

## Quick Start (for readers)

1. Read the flagship: **[EA-001 · Enterprise AI Systems Reference Architecture](architectures/EA-001-Enterprise-AI-Systems.md)**
2. Read the gateway: **[EA-002 · Enterprise AI Gateway](architectures/EA-002-Enterprise-AI-Gateway.md)**
3. Score your enterprise: **[Capability Model](reference-models/capability-model.md)** (7 layers × 5 maturity levels)
4. Browse reusable designs: **[Pattern Catalog](patterns/README.md)**
5. Track progress: **[ROADMAP.md](ROADMAP.md)**

## Quick Start (for adopters)

- **CTO / Chief Architect:** score your org on the [Capability Model](reference-models/capability-model.md) → derive a 12-month roadmap → pick 3 patterns to standardize first.
- **Platform team:** implement [PAT-001 · AI Gateway](patterns/PAT-001-AI-Gateway.md) as your first EASRA-aligned build.
- **Risk / Governance:** map internal controls to [Capability Model → L7 Guardrails](reference-models/capability-model.md).
- **Product team:** align on the L1 Experience and L3 Runtime capabilities before you scope your next AI feature.

---

## Roadmap Highlights

**Sprint-02 (in progress)**
- ✅ EA-002 Enterprise AI Gateway (this release)
- ✅ Capability Model v0.1
- ✅ Pattern catalog (PAT-001..PAT-004)
- ⏭️ Redesigned EA-001 with unified Fluent-style iconography
- ⏭️ Draw.io sources for EA-001 and EA-002
- ⏭️ First reference implementation (Azure)

**Sprint-03**
- EA-003 Runtime Plane, EA-005 Knowledge Plane, EA-006 Verification Plane
- Complete pattern catalog (PAT-005..PAT-010)
- Expanded benchmarks (performance · cost · latency · quality · grounding · verification · agent · security)

**Sprint-04**
- EA-004 Control Plane, EA-007 Guardrails Plane, EA-008 Observability Plane
- AWS + GCP + Kubernetes reference implementations
- GitHub Pages docs site
- **v1.0** tagged release + Architecture Whitepaper + Architecture Decision Book

Full plan: [ROADMAP.md](ROADMAP.md).

---

## Contributing

We welcome issues, discussions, and PRs. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before opening a PR.

Open PRs against **`Develop`**.

## License

License **TBD** — will be finalized before the v1.0 tag. Until then, treat the contents as *"all rights reserved, view-only"* unless the maintainer states otherwise in writing.

## Maintainer

- **Karthikeyan Dhanakotti** ([@KarthikeyanDhanakotti](https://github.com/KarthikeyanDhanakotti))

---

*EASRA is an independent, community-driven reference standard. It is not affiliated with or endorsed by any vendor.*
