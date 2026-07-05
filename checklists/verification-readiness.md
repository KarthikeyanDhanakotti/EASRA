# Checklist — Verification Readiness

**Purpose.** Verification-layer readiness gate for an Enterprise AI system claiming EASRA conformance.

**When to use.** Before promoting a capability to production. Before every material prompt / model / retrieval change.

## Coverage of the seven verification classes ([verification-reference](../verification-reference/README.md))

- [ ] **Grounding** (C9.1) — every factual claim has a retrieved-evidence check.
- [ ] **Citation** (C9.2) — citations resolve to `K-L5-SRC`.
- [ ] **Factuality** (C9.3) — grader / small verifier active.
- [ ] **Format** (C9.4) — schema / JSON validation on structured outputs.
- [ ] **Policy** (C9.5) — data-class / residency / consent checked.
- [ ] **Business rule** (C9.6) — domain rules encoded and executed.
- [ ] **Confidence** (C9.7) — scorer + threshold policy documented.

## Metrics ([verification-reference §3](../verification-reference/README.md))

- [ ] Groundedness rate measured and published per capability.
- [ ] Citation validity rate measured.
- [ ] Citation precision rate measured.
- [ ] Hallucination rate published.
- [ ] Groundedness p95 latency within request budget.

## Golden sets ([verification-reference §4](../verification-reference/README.md))

- [ ] Golden set exists per capability (≥ 200 items at v0.1; ≥ 1 000 at v1.0).
- [ ] Every item has labelled expected answer + expected citations + policy verdict.
- [ ] Provenance and licence recorded per item.
- [ ] Quarterly rotation policy in place (≥ 10%).

## Continuous verification ([verification-reference §5](../verification-reference/README.md))

- [ ] `K-L10-EVAL` re-verifies a production trace sample.
- [ ] Divergence alerts wired.
- [ ] Regression alerts fire on golden-set delta.

## Failure semantics ([verification-reference §6](../verification-reference/README.md))

- [ ] `allow` path measured and within SLO.
- [ ] `escalate` path measured; HITL SLO defined.
- [ ] `block` path measured; user-visible error is `ErrorEnvelope`; audit event emitted.

## Anti-patterns ([verification-reference §7](../verification-reference/README.md))

- [ ] BLEU / ROUGE are NOT used as verification signals.
- [ ] Single grader model NOT relied on without confidence policy.
- [ ] Multi-step agents verified per-step, not only at end.
- [ ] Every published evaluation includes checker versions and thresholds.

## Sign-off

- [ ] Evaluation owner sign-off.
- [ ] Product owner sign-off.
