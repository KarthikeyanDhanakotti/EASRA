# Checklist — EASRA Adoption Assessment

**Purpose.** A self-scored assessment for teams deciding whether to adopt EASRA and, if so, what maturity to target.

**When to use.** Before a formal adoption decision. Every quarter thereafter, to track drift.

**Scoring.** For each item: **M0 Absent · M1 Ad hoc · M2 Defined · M3 Managed · M4 Optimised**, per [Spec 011 §5](../specification/011-capability-model.md). Target: M ≥ 3 by go-live.

## Capability coverage

For each of the 16 capability domains ([Spec 011 §3](../specification/011-capability-model.md)), record current maturity and target maturity.

| Domain | Current | Target | Owner | Notes |
|--------|---------|--------|-------|-------|
| C0 Interact with Users | | | | |
| C1 Govern Ingress | | | | |
| C2 Orchestrate Reasoning | | | | |
| C3 Engineer Prompts | | | | |
| C4 Manage Memory | | | | |
| C5 Retrieve Knowledge | | | | |
| C6 Serve Models | | | | |
| C7 Execute Tools & Actions | | | | |
| C8 Enforce Safety & Guardrails | | | | |
| C9 Verify Outputs | | | | |
| C10 Observe & Evaluate | | | | |
| C11 Optimise Performance & Cost | | | | |
| C12 Deliver Safely (LLMOps) | | | | |
| C13 Secure the System | | | | |
| C14 Govern Risk & Compliance | | | | |
| C15 Deliver Business Value | | | | |

## Non-functional readiness ([Spec 010](../specification/010-nfr.md))

- [ ] SLOs defined per capability with error budgets.
- [ ] Multi-region strategy (or explicit single-region acceptance).
- [ ] Per-request cost model + ledger.
- [ ] Safety incident-response playbook.
- [ ] Continuous evaluation loop wired to production traces.

## Trust boundary posture ([Spec 009](../specification/009-trust-boundaries.md))

- [ ] TB-A (User → Gateway) enforced.
- [ ] TB-B (Reasoning → Model) enforced.
- [ ] TB-C (Reasoning → Tool) enforced.
- [ ] TB-D (System → Data) enforced.

## Governance readiness

- [ ] ADR process in place.
- [ ] Model / prompt / tool registries active.
- [ ] Standards mapping documented ([security-reference](../security-reference/README.md)).
- [ ] Capability Maturity Statement published (see [template](../templates/capability-maturity-statement.md)).

## Decision

- [ ] **Go** — implementation scoped, owners assigned, timelines set.
- [ ] **Adopt-with-gaps** — go with an explicit gap register and closure plan.
- [ ] **Defer** — deferred; blockers listed.
