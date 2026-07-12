# EASRA Roadmap

EASRA delivers as a series of small, tagged sprints. Each sprint ships a coherent set of architectures, patterns, models, or implementations — not a big-bang release.

Legend: ✅ done · 🟡 in progress · ⏭️ next · ⏳ planned

---

## Sprint-01 — Foundation ✅

**Delivered:** repo structure, governance, foundation docs, and the EA-001 Sprint-01 first-draft diagram.

- ✅ Repository structure (`docs/`, `diagrams/`, `assets/`, `.github/`)
- ✅ `README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`
- ✅ Glossary, architecture overview stub, ADR-0001
- ✅ Issue & PR templates
- ✅ EA-001 v0.0.1 SVG + PNG (first draft)
- ✅ `architectures/EA-001-Enterprise-AI-Systems.md`
- ✅ `docs/README.md` with Architecture Views index

---

## Sprint-02 — Reference Standard ✅

**Goal:** Elevate EASRA from a foundation repo into a **reference standard** — canonical flagship diagram, second and third architectures, capability model, pattern catalog, and first cloud reference implementation.

- ✅ **EA-001 v1.0** redesigned — Fluent-style iconography, four labeled bands, Governance pillar, 1920×1200 SVG
- ✅ **EA-002 Enterprise AI Gateway** — SVG + PNG + full architecture page
- ✅ **EA-003 Runtime Plane v0.1** — planner · workflow · tools/MCP · memory · HITL pillar
- ✅ **Capability Model v0.1** — 7 layers, ~60 capabilities, 5-level maturity scale
- ✅ **Reference Models scaffold** — capability (full) + operating/deployment/governance/runtime (stubs)
- ✅ **Pattern Catalog scaffold** — PAT-001 AI Gateway, PAT-002 Multi-Agent, PAT-003 Verification, PAT-004 Prompt Intelligence
- ✅ **README redesigned** as an "Architecture Standard" front door
- ✅ **Azure reference implementation** — `implementations/azure/ai-gateway/` (Bicep, APIM policies, deploy guide)
- ⏭️ Draw.io sources for EA-001 / EA-002 / EA-003 (kept as follow-up)
- ⏭️ License finalization
- ⏭️ Tagged pre-release `v0.2.0`

**Exit criteria met:** flagship v1.0 diagram published, three architectures live, capability model usable for gap-analysis, pattern catalog reviewable, first cloud reference implementation shipped end-to-end.

---

## Sprint-03 — Knowledge, Verification, Second Cloud ⏭️

- ⏭️ **EA-005 Knowledge Plane** — corpora, retrieval, features, data contracts
- ⏭️ **EA-006 Verification Plane** — tracing, offline/online eval, curation
- ⏭️ Complete pattern catalog **PAT-005..PAT-010** (RAG, HITL, Router, Guardrailed Tool Use, Continuous Eval, Feedback Curation)
- ⏭️ **Operating / Deployment / Runtime models** fleshed out
- ⏭️ Expanded benchmarks (`benchmarks/performance` · `cost` · `latency` · `quality` · `grounding` · `verification` · `agent` · `security`)
- ⏭️ **Azure Runtime Plane implementation** (`implementations/azure/runtime-plane/`) using Durable Functions + Foundry Agents
- ⏭️ **AWS reference implementation** for the AI Gateway

---

## Sprint-04 — Control, Guardrails, Observability → v1.0 ⏳

- ⏳ **EA-004 Control Plane** — model registry, lifecycle, rollout, quota governance
- ⏳ **EA-007 Guardrails Plane** — safety, policy engine, threat model
- ⏳ **EA-008 Observability Plane** — unified telemetry, scorecards, alerting
- ⏳ **Governance Model** fleshed out with NIST AI RMF / ISO 42001 / EU AI Act mappings
- ⏳ **GCP + Kubernetes** reference implementations
- ⏳ **GitHub Pages** docs site
- ⏳ **Conference assets**: whitepaper, architecture decision book, review checklist, capability model handout, reference cards
- ⏳ **v1.0** tagged release

---

## Backlog / Under Consideration

- Multi-tenant deployment topologies (silo · pool · bridge)
- On-device / edge inference patterns (WinML, ONNX runtime)
- MCP / tool-server catalog and hardening guide
- Data-quality plane for AI (feature stores, embedding drift, corpus governance)
- LangGraph / Agent Framework / Semantic Kernel mapping guides
- Formal EASRA maturity assessment tool (spreadsheet + web app)

---

## Release Cadence

- **Sprints:** ~2 weeks each (indicative)
- **Releases:** tagged at end of each sprint once exit criteria are met
- **Versioning:** [SemVer](https://semver.org/); `0.x` while the standard is stabilizing, `1.0` at end of Sprint-04
