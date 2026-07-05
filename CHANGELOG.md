# Changelog

All notable changes to EASRA are recorded here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses the versioning scheme defined in [GOVERNANCE.md](./GOVERNANCE.md).

## [Unreleased]

### Added
- `implementations/` — vendor mapping guides for Azure, AWS, GCP, and open-source (Kubernetes + CNCF), each with per-layer + trust-boundary + NFR mapping and known-gap sections.
- `benchmarks/` — benchmark categories (latency, throughput, cost, safety, verification, reliability, cache, continuous eval), reference workloads (W-SARAG / W-MAC / W-TOOL / W-STREAM / W-INJ / W-COST), and benchmark-spec skeleton.
- `security-reference/` — threat catalogue (OWASP LLM Top 10 + MITRE ATLAS mapped to EASRA layers), controls catalogue, standards-mapping status, threat-model roster, red-team + incident-response outlines.
- `verification-reference/` — verification-vs-evaluation contract, seven verification classes with checker catalogue, grounding metric definitions, golden-set methodology, continuous verification loop, anti-patterns.
- `llmops-guide/` — reference delivery pipeline, prompt/model/tool lifecycles, evaluation strategy table, cost engineering, observability conventions, reference SLOs, AI-specific runbook roster.
- `conference/` — talk deck / workshop / abstract slot list, suggested outlines for keynote / deep-dive / enterprise brief / half-day workshop, citation guidance.
- Specification 011 — Capability Model (16 capability domains C0–C15, ~70 subcapabilities, 5-level maturity model, freezing rule).
- Specification 012 — Component Catalogue (~60 components across L0–L15 plus cross-cutting substrate, with `K-L*-*` ID scheme and status legend).
- `architectures/` folder with the five-view scaffold: `logical/`, `runtime/`, `deployment/`, `operational/`, `security/` (each with a README naming its diagrams and anchoring specs).
- `diagrams/CATALOGUE.md` — authoritative inventory of the target ~25-diagram set with ID scheme D-<view><n> and status legend.
- Diagram D-R1 — Master Runtime Execution Flow (`diagrams/runtime-execution-flow.md`), showing decision points, cache lookups, guardrails, model fallback, tool impact-class gating, verification verdicts, and streaming.

### Changed
- `README.md` — repositioned EASRA as an **open architecture standard** with 10 explicit deliverables; adds Standard Deliverables table with status; refreshed nav bar and repo structure.
- `specification/README.md` — reading-order table extended to specs 011 and 012.
- `ROADMAP.md` — restructured to the reviewer-recommended process: Phase 1 Draft Spec, Phase 2 Capability & Component Freeze, Phase 3 Complete 5-Architecture Diagram Set, Phase 4 Handbook, Phase 5 Cloud mappings (partially done), Phase 6 v1.0, Phase 7 Ecosystem, Phase 8 Research. Added cross-phase Standard Deliverables table.

## [0.1.0] — 2026-07-05

### Added
- Initial repository scaffold: `specification/`, `handbook/`, `diagrams/`, `examples/`, `reference-implementation/`, `adr/`, `research/`.
- Dual-licensed under CC-BY-4.0 (docs) and Apache-2.0 (code).
- Root documents: `README.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `ROADMAP.md`, `CHANGELOG.md`, `.gitignore`.
- Specification 001 — Introduction, Vision and Scope.
- Specification 002 — Design Principles (P1–P10).
- Specification 003 — Terminology (glossary of ~80 EASRA terms).
- Specification 004 — Reference Architecture (16 logical layers).
- Specification 005 — Layer Definitions (responsibilities, inputs, outputs, invariants per layer).
- Specification 006 — Interface Specification (contracts between layers).
- Specification 007 — Data Flow (request, response, cache, memory, tool, evaluation flows).
- Specification 008 — Sequence Diagrams (six canonical request patterns).
- Specification 009 — Trust Boundaries (four boundaries: Edge, Reasoning, Tool, Data).
- Specification 010 — Non-Functional Requirements (latency, throughput, availability, safety, cost, compliance).
- Diagrams: high-level architecture, trust boundaries, deployment topology, CI/CD pipeline, observability plane.
- Handbook scaffolding for all 16 layers.
- Worked example scaffolding for single-agent RAG.
- Reference-implementation scaffold with conformance-test outline.
- ADR-0000 template, ADR-0001 (Record architecture decisions), ADR-0002 (Vendor-neutral scope).
- GitHub issue templates, PR template, and docs CI workflow.

[Unreleased]: https://github.com/KarthikeyanDhanakotti/EASRA/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/KarthikeyanDhanakotti/EASRA/releases/tag/v0.1.0
