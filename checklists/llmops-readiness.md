# Checklist — LLMOps Readiness

**Purpose.** Delivery, evaluation, cost, and incident-response gate for an Enterprise AI system claiming EASRA conformance.

**When to use.** Before every production release. Every quarter, to track LLMOps drift.

## Delivery pipeline ([llmops-guide §1](../llmops-guide/README.md))

- [ ] Source control for code, prompts, policies, evaluators (`K-L12-SCM`).
- [ ] CI runs lint + sec-scan + unit + prompt-tests + offline eval on every PR (`K-L12-CI`).
- [ ] Artefact registry stores signed containers / prompts / models / policies (`K-L12-AR`).
- [ ] CD supports canary + blue-green + shadow + rollback (`K-L12-CD`).
- [ ] Auto-eval gate blocks promotion on regression.
- [ ] Rollback exercised in the last quarter.

## Prompt lifecycle ([llmops-guide §2](../llmops-guide/README.md))

- [ ] Every production prompt is signed and registered in `K-L3-PR`.
- [ ] Retired prompts remain immutable for ≥ 1 minor version.
- [ ] Golden-set gate is enforced before promotion.

## Model lifecycle ([llmops-guide §3](../llmops-guide/README.md))

- [ ] Every model is signed and registered in `K-L6-MRG`.
- [ ] Selection ADR exists per production model.
- [ ] Fallback route tested per model (`K-L6-FB`).

## Tool lifecycle ([llmops-guide §4](../llmops-guide/README.md))

- [ ] Every tool declares an impact class in `K-L7-TREG`.
- [ ] High-impact tools have HITL wired.
- [ ] Per-tool rate limit + quota enforced.

## Evaluation strategy ([llmops-guide §5](../llmops-guide/README.md))

- [ ] Offline evaluation on every PR.
- [ ] Canary evaluation before ramp beyond 5%.
- [ ] Continuous evaluation on production traces (`K-L10-EVAL`).

## Cost engineering ([llmops-guide §6](../llmops-guide/README.md))

- [ ] Cost ledger active for every request (`K-L11-LG`).
- [ ] Per-capability budget defined + enforced (`K-L1-TBM`).
- [ ] Graceful degradation path documented (cache → smaller model → fallback → error).
- [ ] Weekly cost review compares actual vs. budget.

## Observability ([llmops-guide §7](../llmops-guide/README.md))

- [ ] Every trace uses W3C TraceContext.
- [ ] Required span attributes emitted (`easra.layer`, `easra.component`, `easra.capability`, `easra.request_id`, `easra.prompt_version`, `easra.model_version`, `easra.tool_version`).
- [ ] Cost events carry request ID.
- [ ] Agent / prompt / tool traces emitted (`K-L10-AT`, `K-L10-PT`, `K-L10-TT`).

## SLOs ([llmops-guide §8](../llmops-guide/README.md))

- [ ] End-to-end request latency p95 SLO defined per capability.
- [ ] Availability SLO defined.
- [ ] Verification allow-rate SLO defined.
- [ ] Cost SLO per request defined.
- [ ] Safety-incident SLO = 0 user-visible bypasses.

## Incident response ([llmops-guide §9](../llmops-guide/README.md))

- [ ] Runbooks exist for prompt injection, indirect injection, grounding regression, PII leakage, cost anomaly, tool misuse, model policy bypass.
- [ ] On-call ownership per component.
- [ ] Post-mortem policy documented.

## Multi-region ([llmops-guide §10](../llmops-guide/README.md))

- [ ] Region-by-region promotion enforced.
- [ ] Regional evaluators active.
- [ ] Region-local rollback tested.
