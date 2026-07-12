# PAT-007 · Human-in-the-Loop (HITL)

**Status:** Stub (v0.0.1) · **Sprint:** planned Sprint-03 · **Layer:** L3, L7 · **Taxonomy:** `PAT-`

> Placeholder page. The full HITL pattern will land in **Sprint-03**.

## Context

Some AI actions are too high-stakes, ambiguous, or novel for full automation — irreversible external effects, regulated decisions, or low-confidence outputs where a wrong answer costs more than a slow one.

## Problem

How do we integrate humans as a **first-class, observable, SLA-bound step** in an agentic workflow — without turning the platform into a queue-of-tickets that erodes AI's speed advantage?

## Solution (outline)

- **Approval checkpoints** are declarative: a step config says *"if condition X, pause and require reviewer role Y."*
- **HITL queue** is a service with SLAs, escalation, and a durable inbox — not an email chain
- Reviewer decisions are signed and captured as span attributes (`easra.hitl.decision`, `easra.hitl.reviewer_id`, `easra.hitl.reason`)
- SLA breach has a **declared default** (usually: abort with reason), never silent-drop
- HITL never stops observability — the paused task remains visible

## Interfaces (to be specified)

- `POST /v1/hitl/requests` — enqueue an approval request
- `POST /v1/hitl/requests/{id}/decide` — reviewer decision
- SSE `GET /v1/hitl/requests/{id}/events`

## Controls

- Role/permission required per checkpoint type
- Immutable audit trail of every decision
- Kill-switch can force-close any pending request

## KPIs

- Queue wait time p50 / p95
- Approval rate
- SLA-breach rate (and default-action rate)
- Auto-escalation rate

## Trade-offs

- More HITL → higher trust, lower throughput
- Coarse triggers (approve *everything* over $X) vs. fine triggers (per-tool + per-tenant policy)

## Anti-patterns

- HITL email chains without SLAs
- Silent SLA breaches (task neither approved nor aborted)
- Approvals without capturing the reviewer's *reason*

## Related

- Enforced in [EA-003 · Runtime Plane](../architectures/EA-003-Runtime-Plane.md) HITL/Safety pillar
- Consumes verification signals from [EA-010 · Verification Plane](../architectures/EA-010-Verification-Plane.md)

## Changelog

- v0.0.1 · Sprint-02 · Stub created as part of the pattern-catalog completion plan.
