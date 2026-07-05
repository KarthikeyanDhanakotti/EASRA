# L8 — Guardrails & Safety

| Field | Value |
|-------|-------|
| Layer | L8 |
| Depends on Specs | 004, 005, 006, 009 |
| Status | Skeleton |

## 1. Purpose

L8 inspects and blocks unsafe inputs, prompts, tool arguments, and outputs at four checkpoints. Guardrails are a *control layer* — not evaluation, not verification.

## 2. Responsibilities

- **In scope.** Input, prompt, tool-arg, output guardrails; prompt-injection, PII, toxicity, jailbreak detection; format/schema enforcement.
- **Out of scope.** Verification (L9), policy authorship (L14 — L8 *consumes* L14 policies).

## 3. Design principles

**P2 Security**, **P8 Failure Isolation** (fail closed on integrity, safe on availability), **P4 Observability**.

## 4. Patterns

- Fast rules first, then classifiers, then LLM-based checks (cost + latency tiering).
- Parallel guardrail execution where checks are independent.
- Structured verdicts with reasons (never a boolean pass/fail with no context).

## 5. Anti-patterns

- Guardrails only in the system prompt.
- Guardrails run after tool execution rather than before.
- Silent bypass on guardrail service outage.

## 6. Failure modes

| Failure | Policy |
|---------|--------|
| Integrity check unavailable | Fail closed |
| Availability check unavailable | Degrade safely (per control) |

## 7. Observability

Checkpoint, guardrail ID, decision, reason, latency, override events.

## 8. Production checklist

- [ ] All four checkpoints wired.
- [ ] Failure policy documented per control.
- [ ] False-positive override path in place.
