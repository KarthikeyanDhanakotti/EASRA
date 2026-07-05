# Operational Architecture

## Purpose

The **Operational Architecture** describes *how the deployed system is observed, evaluated, delivered, and evolved safely*. It is the set of control loops around the runtime — the LLMOps discipline for Enterprise AI.

## Audience

- SREs, LLMOps, quality and evaluation engineers.
- Release managers.
- Product owners consuming KPIs and cost telemetry.

## Scope

- Observability plane — traces, metrics, logs, agent / prompt / tool traces, cost telemetry.
- Continuous evaluation — production traces feeding evaluators.
- CI / CD — source control, gates, artefact registry, canary / blue-green / shadow, rollback.
- SLOs, error budgets, alerting.
- Cost telemetry and budget enforcement.
- Feedback loops from users, evaluators, incidents, and business outcomes.
- Runbooks and on-call ownership per component.

## Anchoring specifications

| Spec | Purpose |
|------|---------|
| [010 Non-Functional Requirements](../../specification/010-nfr.md) | SLOs, cost, evaluation NFRs. |
| [005 Layer Definitions §L10, §L12, §L15](../../specification/005-layer-definitions.md) | Observability, LLMOps, Business Outcomes. |
| [006 Interface Specification](../../specification/006-interface-specification.md) | Trace, cost, and eval-record interfaces. |

## Diagrams

| ID | Title | Status |
|----|-------|--------|
| D-O1 | Observability Plane | Done — [`../../diagrams/observability-plane.md`](../../diagrams/observability-plane.md) |
| D-O2 | CI / CD Pipeline | Done — [`../../diagrams/cicd-pipeline.md`](../../diagrams/cicd-pipeline.md) |
| D-O3 | Continuous Evaluation Loop | Planned |
| D-O4 | Cost & Budget Enforcement Loop | Planned |
| D-O5 | Incident Response Runbook Overview | Planned |

## Change control

New control loops require an entry in [010 NFRs](../../specification/010-nfr.md) and a supporting diagram.
