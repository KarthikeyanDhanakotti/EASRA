# EASRA Roadmap

This roadmap describes the planned evolution of EASRA from initial draft to a stable, adoptable v1.0 and beyond. Dates are omitted intentionally — EASRA advances when material is ready, not on a calendar.

## Guiding release principles

- **v0.x is a draft.** Interfaces, layer boundaries, and principles may change. Consumers should pin to a commit hash.
- **v1.0 freezes the architecture.** Layer count, layer numbering, interface contracts, and the design principles are stable and covered by the deprecation policy.
- **v1.x is additive.** New handbook chapters, examples, ADRs, cloud mappings, and reference-implementation modules land here.
- **v2.0 is reserved** for a coordinated, breaking evolution informed by ≥ 12 months of production adoption.

---

## Phase 1 — Draft Specification (v0.1)

**Goal:** publish the complete draft specification and a coherent high-level architecture.

- [x] Repository scaffold and licensing
- [x] Specification 001 — Introduction, Vision, Scope
- [x] Specification 002 — Design Principles
- [x] Specification 003 — Terminology
- [x] Specification 004 — Reference Architecture (16 layers)
- [x] Specification 005 — Layer Definitions
- [x] Specification 006 — Interface Specification
- [x] Specification 007 — Data Flow
- [x] Specification 008 — Sequence Diagrams
- [x] Specification 009 — Trust Boundaries
- [x] Specification 010 — Non-Functional Requirements
- [x] Publication-grade high-level architecture diagram
- [x] Trust boundary, deployment-topology, CI/CD, observability diagrams
- [x] ADR template + first two ADRs
- [x] Public repository, docs CI, license, changelog

## Phase 2 — Capability & Component Freeze (v0.1 → v0.3)

**Goal:** freeze the vocabulary and inventory before scaling out diagrams, so every future artefact is derived, not invented.

- [x] Specification 011 — Capability Model (C0–C15 + subcapabilities + 5-level maturity)
- [x] Specification 012 — Component Catalogue (~60 components with ID scheme K-L*-*)
- [x] Five-architecture scaffold (`architectures/logical|runtime|deployment|operational|security/`)
- [x] Diagram Catalogue (`diagrams/CATALOGUE.md`) — 25-diagram inventory with IDs D-L1..S5
- [x] Master Runtime Execution Flow diagram (D-R1)
- [ ] Public discussion opened on GitHub Discussions
- [ ] First external reviewers onboarded
- [ ] Specification 013 — Conformance Test Suite (planned)
- [ ] Specification 014 — Standards Mapping (NIST AI RMF, ISO 42001, EU AI Act, OWASP LLM, MITRE ATLAS) (planned)

## Phase 3 — Complete the Five-Architecture Diagram Set (v0.3 → v0.7)

**Goal:** ship the remaining ~20 diagrams that turn each of the five architecture views into a reviewable, publication-quality set. Each diagram references only components in [Spec 012](./specification/012-component-catalogue.md).

### Logical view (target: 5 diagrams)
- [x] D-L1 High-Level Architecture
- [ ] D-L2 Component Master Diagram
- [ ] D-L3 Memory Architecture (L4 zoom-in)
- [ ] D-L4 Knowledge & Retrieval Architecture (L5 zoom-in)
- [ ] D-L5 Guardrails & Verification Architecture (L8 + L9 zoom-in)

### Runtime view (target: 6 diagrams)
- [x] D-R1 Master Runtime Execution Flow
- [x] D-R2..R4 Sequence diagrams S1–S3 (in Spec 008)
- [ ] D-R5 Guardrail + Verification Decision Flow
- [ ] D-R6 Cache Lookup Sequence

### Deployment view (target: 5 diagrams)
- [x] D-D1 Single-Region Topology
- [ ] D-D2 Multi-Region Active-Active Topology
- [ ] D-D3 Kubernetes Placement Map
- [ ] D-D4 State & Cache Placement
- [ ] D-D5 Disaster Recovery Topology

### Operational view (target: 5 diagrams)
- [x] D-O1 Observability Plane
- [x] D-O2 CI/CD Pipeline
- [ ] D-O3 Continuous Evaluation Loop
- [ ] D-O4 Cost & Budget Enforcement Loop
- [ ] D-O5 Incident Response Runbook Overview

### Security view (target: 5 diagrams)
- [x] D-S1 Trust Boundaries & Planes
- [ ] D-S2 Zero-Trust Identity Flow
- [ ] D-S3 Prompt-Injection Defence-in-Depth
- [ ] D-S4 Data Classification & Residency Flow
- [ ] D-S5 High-Impact Action Gate & Audit Trail

## Phase 4 — Handbook (v0.7 → v0.9)

**Goal:** deep-dive per-layer chapters that turn the specification into an engineering handbook.

- [ ] L0  Channels & User Experience
- [ ] L1  Edge · Gateway · Identity
- [ ] L2  AI Orchestration
- [ ] L3  Prompt Intelligence
- [ ] L4  Memory & Context
- [ ] L5  Knowledge & Retrieval
- [ ] L6  AI Models & Model Router
- [ ] L7  Tooling & Actions (MCP, APIs)
- [ ] L8  Guardrails & Safety
- [ ] L9  Verification
- [ ] L10 Observability & Evaluation
- [ ] L11 Performance, Caching & Cost
- [ ] L12 LLMOps & Delivery
- [ ] L13 Security & Zero Trust
- [ ] L14 Governance, Risk & Compliance
- [ ] L15 Business Outcomes & Value
- [ ] Cross-cutting handbook: Cost Engineering
- [ ] Cross-cutting handbook: Multi-Region & DR
- [ ] Cross-cutting handbook: Responsible AI

## Phase 5 — Cloud & Implementation Mappings (v0.9 → v1.0-RC)

**Goal:** demonstrate that the vendor-neutral architecture maps cleanly to real stacks.

- [ ] Azure implementation guide (per layer)
- [ ] AWS implementation guide (per layer)
- [ ] GCP implementation guide (per layer)
- [ ] Open-source implementation guide (per layer)
- [ ] Kubernetes deployment topology
- [ ] Minimum viable reference implementation (single-agent RAG, spec-compliant)

## Phase 6 — v1.0 Release

**Goal:** freeze the architecture and declare it production-ready as a reference.

- [ ] Full specification review by ≥ 5 external architects
- [ ] All 16 handbook chapters merged
- [ ] Reference implementation passing conformance tests
- [ ] Conformance test suite published
- [ ] Website / docs site launched
- [ ] v1.0 tagged; deprecation policy in force

## Phase 7 — Ecosystem (v1.x)

**Goal:** grow adoption and the surrounding ecosystem.

- [ ] Multi-agent worked example
- [ ] Tool-use (MCP) worked example
- [ ] Cost-aware routing worked example
- [ ] Agent Optimizer worked example
- [ ] Conference tutorials and workshops
- [ ] Certification / conformance badge programme (via TSC)
- [ ] Case studies from external adopters

## Phase 8 — Research (parallel to all phases)

**Goal:** advance the state of the art in areas the current architecture reserves as extension points.

- [ ] Enterprise AI Execution Compiler (EAEC)
- [ ] Enterprise AI Verification Framework
- [ ] Constraint-based Agent Verification
- [ ] Execution Graph Optimization
- [ ] Enterprise AI Benchmarks (latency, cost, safety, verification)
- [ ] Cost-aware routing algorithms
- [ ] Multi-model routing under SLOs

## Reserved extension points

The architecture explicitly reserves the following extension points; each will get a full specification when it graduates from research:

- Multi-region deployment
- Disaster recovery
- Multi-model routing
- Cost-aware routing
- AI policy engine
- Agent marketplace
- Agent registry
- Skill registry
- Feature store
- Vector synchronization
- Event bus
- Async workflows

## How to influence the roadmap

- Open a discussion under `Roadmap` on GitHub Discussions.
- File an ADR for structural proposals.
- Contribute a handbook chapter for something on this list — it accelerates its inclusion.

## Deprecation policy (in force from v1.0)

- Deprecations are announced in a minor release (v1.Y).
- Deprecated items remain functional for ≥ 2 minor releases.
- Removal requires a major version bump.
- Every deprecation includes a migration note in the changelog.
