# PAT-010 · Feedback Curation

**Status:** Stub (v0.0.1) · **Sprint:** planned Sprint-03 · **Layer:** L5, L6 · **Taxonomy:** `PAT-`

> Placeholder page. The full Feedback Curation pattern will land in **Sprint-03**.

## Context

An AI system generates a firehose of implicit and explicit feedback: thumbs-up/down, edits, corrections, silent aborts, HITL decisions. Left unstructured, this data becomes noise. Curated, it becomes the next round of evaluation sets and fine-tuning corpora.

## Solution (outline)

- **Feedback capture** at every layer (Experience thumbs, HITL decisions, Verifier signals, cache-bypass patterns)
- Feedback events flow to a **curation store** with schema `{trace_id, model, prompt, response, feedback_signal, reviewer_type}`
- **Curation pipeline** — de-dup, PII redact, quality-filter, label
- **Auto-promoted** into offline eval datasets (with review gate)
- **Auto-suggested** as fine-tuning candidates (with review gate)
- Loop is observable — every dataset entry traces back to the feedback event that created it

## Interfaces (to be specified)

- `POST /v1/feedback` — capture event schema
- Curation → eval dataset promotion contract
- Curation → fine-tuning dataset promotion contract

## Controls

- Consent capture at feedback time (tenant-level policy)
- PII redaction is mandatory before storage
- Human review gate before any promotion to training data

## KPIs

- Feedback capture rate (per turn, per session)
- Curation-to-dataset conversion rate
- Time-from-feedback-to-eval-inclusion
- Fine-tune candidate acceptance rate

## Trade-offs

- Signal-to-noise: raw thumbs are easy but noisy; edits are richer but rarer
- Automation vs. review: fully-auto risks drift, fully-manual doesn't scale — need tiered gates

## Anti-patterns

- Fine-tuning on unredacted user prompts
- Treating implicit signals (cache-bypass, retry) as ground truth without validation
- No feedback consent → downstream legal risk

## Related

- Realizes [EA-010 · Verification Plane](../architectures/EA-010-Verification-Plane.md)
- Pairs with [PAT-009 · Continuous Eval](PAT-009-Continuous-Eval.md)
- Governed by [EA-004 · Control Plane](../architectures/EA-004-Control-Plane.md)

## Changelog

- v0.0.1 · Sprint-02 · Stub created as part of the pattern-catalog completion plan.
