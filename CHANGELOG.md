# Changelog

All notable changes to **EASRA** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned (Sprint-02 remainder)
- Draw.io sources for EA-001, EA-002, and EA-003
- License finalization
- Tagged pre-release `v0.2.0`

---

## [0.1.2] — 2026-07-12 — Sprint-02 Reviewer Response

### Changed
- **README repositioned** — dropped the "Think of it as *TOGAF for enterprise AI*" line per external review. EASRA now stands on its own as *"an open reference architecture and specification for designing, governing, deploying, and operating Enterprise AI systems."*
- **README — new EASRA Taxonomy section** — formal artifact classes: `EA-` Reference Architectures, `RM-` Reference Models, `PAT-` Architecture Patterns, `ADR-` Architecture Decisions, `SPEC-` Specifications, `IMPL-` Reference Implementations, `CHK-` Checklists.
- **README — new "Relation to Other Frameworks" section** — acknowledges TOGAF, Azure Architecture Center, AWS Well-Architected, OpenTelemetry, NIST AI RMF, ISO 42001, EU AI Act, LangGraph, Microsoft Agent Framework, Semantic Kernel, MCP.
- **Architecture map expanded to 15 views (EA-001..EA-015)** — Control Plane, Knowledge Plane, Model Router, Prompt Intelligence, Memory Plane, MCP/Tool Fabric, Verification Plane, Guardrails Plane, Observability Plane, Security & Identity, Governance & Compliance, Deployment Topologies scheduled across Sprint-03 & Sprint-04.
- **ROADMAP Sprint-03** rewritten to the reviewer-aligned plan: add 7 architecture views (EA-004..EA-010), complete pattern catalog (PAT-005..PAT-010), grow ADRs to ~20, second cloud implementation begins.
- **`reference-models/capability-model.md`** — softened TOGAF reference to a neutral comparison.
- **`reference-models/README.md`** — same treatment.

### Notes
- External review score progression: 9.1 → **9.5**. Reviewer's biggest recommendation ("stop thinking of EASRA as documentation, start thinking of it as a standard") is now baked into the taxonomy.

---

## [0.1.1] — 2026-07-12 — Sprint-02 Reference Standard

### Added
- **EA-001 v1.0 — redesigned flagship diagram** with unified Fluent-style iconography, four labeled bands (Consumption · Control · Runtime & Data · Evidence), colored plane pills, right-side Governance pillar, refined typography, and 1920 × 1200 SVG canvas.
  - `diagrams/EA-001-Enterprise-AI-Systems-Reference-Architecture-v1.svg`
  - `diagrams/EA-001-Enterprise-AI-Systems-Reference-Architecture-v1.png`
- **EA-003 · Runtime Plane (Agent Orchestration)** — third flagship architecture:
  - `diagrams/EA-003-Runtime-Plane.svg` + `.png` — 4 bands (Orchestration · Execution · Tools & Actions · Memory & State) + HITL/Safety pillar
  - `architectures/EA-003-Runtime-Plane.md` — full page (design goals, component detail, `POST /v1/runtime/tasks` interface contract, OTel `gen_ai.*` + `easra.*` observability contract, failure modes)
- **Azure reference implementation** for EA-002 AI Gateway:
  - `implementations/README.md` + `implementations/azure/README.md` — implementations index & Azure service palette
  - `implementations/azure/ai-gateway/README.md` — overview, capability-to-service map, cost sketch, quick start
  - `implementations/azure/ai-gateway/architecture.md` — mermaid diagram + stage-by-stage EA-002 → Azure mapping
  - `implementations/azure/ai-gateway/bicep/` — `main.bicep` + modules (`apim`, `functions`, `redis`, `keyvault`, `loganalytics`) + `parameters/dev.bicepparam`
  - `implementations/azure/ai-gateway/policies/` — `api-inbound.xml` (auth + quota + content safety), `fragment-pii-scrub.xml`, `fragment-cost-attribution.xml`
  - `implementations/azure/ai-gateway/docs/deploy.md` — deployment guide
  - `implementations/azure/ai-gateway/samples/router-policy.example.json` — router policy sample

### Changed
- `README.md` — hero image switched to EA-001 v1.0; new badges (EA-003, Azure impl); architecture map updated (EA-001 v1.0, EA-003 v0.1); repository layout reflects `architectures/EA-003-*.md`, v1 diagram filenames, and `implementations/azure/ai-gateway/`
- `architectures/EA-001-Enterprise-AI-Systems.md` — points to v1.0 files as canonical; v0.0.1 kept as archive
- `ROADMAP.md` — Sprint-02 marked ✅ Reference Standard with all deliverables; Sprint-03 focused on Knowledge/Verification/second cloud
- `docs/README.md` — Architecture Views extended with EA-003 status

---

## [0.1.0] — 2026-07-12 — Sprint-02 Kickoff

### Added
- **EA-002 · Enterprise AI Gateway** — the second flagship architecture:
  - `diagrams/EA-002-Enterprise-AI-Gateway.svg` (hand-authored source)
  - `diagrams/EA-002-Enterprise-AI-Gateway.png` (1600 × 1000 export)
  - `architectures/EA-002-Enterprise-AI-Gateway.md` — full page: goals, 6-stage control path, cross-cutting stores, interface contract, observability contract, failure modes
- **Capability Model v0.1** — the "biggest missing piece" per external review:
  - `reference-models/capability-model.md` — 7 layers (Experience, Gateway, Runtime, Knowledge, Verification, Operations, Guardrails), ~60 capabilities, 5-level maturity scale, capability-to-architecture traceability
- **Reference Models scaffold** (`reference-models/`)
  - `README.md`, `capability-model.md` (full)
  - `operating-model.md`, `deployment-model.md`, `governance-model.md`, `runtime-model.md` (Sprint-02 stubs)
- **Pattern Catalog** (`patterns/`)
  - `README.md` — template, catalog (PAT-001..PAT-010), relationship to architectures
  - `PAT-001-AI-Gateway.md`, `PAT-002-Multi-Agent.md`, `PAT-003-Verification.md`, `PAT-004-Prompt-Intelligence.md` — all with context/problem/solution/interfaces/controls/KPIs/trade-offs/anti-patterns
- **README redesigned** — "Architecture Standard" tone: what EASRA is / is not, flagship artifacts table, full EA-001..EA-008 architecture map, pattern catalog excerpt, reference models table, adopter quick-start
- **Architecture badges** added: EA-001 flagship, EA-002 gateway, Capability Model v0.1

### Changed
- `README.md` — full rewrite to match Sprint-02 scope and reference-standard positioning
- `ROADMAP.md` — restructured: Sprint-01 marked complete; Sprint-02 in progress; Sprint-03 = Runtime/Knowledge/Verification; Sprint-04 = Control/Guardrails/Observability → v1.0
- `docs/README.md` — Architecture Views table extended to EA-002; new sections for Reference Models and Patterns

### Notes
- EA-002 is the reviewer-recommended next artifact and the "API Gateway of Enterprise AI".
- Capability Model closes the reviewer-identified "biggest missing piece" gap.
- Draw.io source files and Sprint-04 architectures (EA-003..EA-008) are tracked in [ROADMAP.md](ROADMAP.md).

---

## [0.0.2] — 2026-07-12

### Added
- **EA-001 · Enterprise AI Systems Reference Architecture** (Sprint-01 first-draft) — the flagship EASRA architecture:
  - `diagrams/EA-001-Enterprise-AI-Systems-Reference-Architecture.svg` (hand-authored source)
  - `diagrams/EA-001-Enterprise-AI-Systems-Reference-Architecture.png` (1600 × 1000 export)
  - `architectures/EA-001-Enterprise-AI-Systems.md` — dedicated architecture page (purpose, seven planes, components, design principles, data flow, related architectures)
- `docs/README.md` — documentation index with **Architecture Views** table (EA-001 → EA-006)
- README hero: EA-001 diagram embedded immediately after title & badges, ahead of the Vision section
- Repository layout updated to include new `architectures/` folder

### Notes
- EA-001 v0.0.1 is an **acknowledged first draft**. The canonical v1.0 diagram — with unified iconography, aligned spacing, higher-resolution SVG, and clearer separation of Control/Runtime/Data planes and Governance pillars — ships in Sprint-02 and will become the whitepaper/conference asset.

---

## [0.0.1] — Sprint-01 Foundation — 2026-07-12

### Added
- Initial repository structure: `docs/`, `diagrams/`, `assets/`, `.github/`
- `README.md` — project overview, goals, non-goals, repo layout
- `ROADMAP.md` — sprint plan and milestones
- `CONTRIBUTING.md` — contribution workflow and standards
- `CODE_OF_CONDUCT.md` — Contributor Covenant v2.1
- `docs/architecture/overview.md` — 10-minute architecture tour (stub)
- `docs/patterns/README.md` — pattern catalog index (stub)
- `docs/decisions/0001-record-architecture-decisions.md` — ADR template & first ADR
- `docs/glossary.md` — shared vocabulary
- `.github/ISSUE_TEMPLATE/` — bug, feature, and question templates
- `.github/PULL_REQUEST_TEMPLATE.md` — PR checklist
- `diagrams/README.md` and `assets/README.md` — placeholders

### Notes
- This is a **foundation package**, not a v1.0 release.
- All architecture artifacts are stubs; production-quality versions ship in Sprint-02.
