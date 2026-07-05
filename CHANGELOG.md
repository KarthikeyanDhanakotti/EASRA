# Changelog

All notable changes to EASRA are recorded here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses the versioning scheme defined in [GOVERNANCE.md](./GOVERNANCE.md).

## [Unreleased]

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
