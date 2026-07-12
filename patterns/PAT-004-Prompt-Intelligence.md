# PAT-004 · Prompt Intelligence

> **Layer:** L2 Gateway, L7 Guardrails
> **Status:** Draft

## Context

Prompts entering an AI system may contain PII, secrets, injected instructions from untrusted sources (docs, tool outputs), jailbreak payloads, or sensitive business content that should never leave the enterprise. Post-hoc detection is too late.

## Problem

- Applications can't be trusted to sanitize prompts consistently
- Indirect prompt injection (poisoned documents, tool responses) bypasses app-side checks
- PII/secrets in prompts violate DLP policy and inflate breach blast-radius
- Classification (topic, sensitivity, intent) is needed *before* routing

## Solution

A **prompt-intelligence stage** in the gateway that runs *before* the model is called. Composed of small, fast, layered components:

```
Prompt ─►  redactor  ─►  injection detector ─► classifier ─► [verdict + transformed prompt] ─► router
              │                │                    │
              ▼                ▼                    ▼
          PII / secrets    known payloads     topic · sensitivity · lang
```

- **Redactor:** regex + NER for PII, high-entropy scan for secrets, replace with tokenized placeholders
- **Injection detector:** rule + classifier for direct + indirect injection markers
- **Jailbreak detector:** signature + LLM-as-classifier for known bypass patterns
- **Classifier:** topic, sensitivity level, language, business-domain tag

## Interfaces

- **Input:** raw prompt + context (system prompt, retrieved chunks, tool outputs)
- **Output:** transformed prompt + verdict object:
  ```
  {
    "verdict": "allow|allow_with_redaction|block",
    "risk_score": 0..1,
    "labels": ["pii", "injection_attempt", "sensitive/legal"],
    "redactions": [{"span": "...", "type": "email"}],
    "classification": {"topic": "...", "sensitivity": "internal"}
  }
  ```
- **Downstream signals:** verdict flows into policy (stage 3), router (stage 5), and audit

## Controls

- **Fail-closed** on injection detection for high-sensitivity tenants
- **Redact before persist** — never write raw PII to logs / caches
- **Deterministic re-hydration** — redacted placeholders may be re-hydrated only in the response path, and only if allowed by policy
- **Model isolation** — classifiers themselves must not be able to be prompt-injected

## KPIs

- **Recall on labeled injection set** (target: > 95%)
- **False-positive rate on benign prompts** (target: < 1%)
- **p95 stage latency** (target: < 20 ms)
- **PII-leak-to-cache rate** (target: 0)

## Trade-offs

- Latency budget: prompt intelligence must be fast enough not to dominate p95
- Model-based classifiers cost tokens themselves → prefer distilled small models
- False positives block legitimate work → must be tunable per tenant

## Anti-patterns

- **Regex-only detection** — misses paraphrased injection
- **Classifier-only detection** — misses novel patterns
- **Single global threshold** — sensitivity must be per-tenant / per-use-case
- **Blocking with no telemetry** — every block must be observable & appealable

## Related

- [PAT-001 · AI Gateway](PAT-001-AI-Gateway.md) — this pattern is stage 4 of the gateway
- [EA-002 · Enterprise AI Gateway](../architectures/EA-002-Enterprise-AI-Gateway.md) → *Prompt Intelligence*
- [EA-007 · Guardrails Plane](../architectures/EA-001-Enterprise-AI-Systems.md) *(planned)*
- [Capability Model → L2 & L7](../reference-models/capability-model.md)
