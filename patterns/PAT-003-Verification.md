# PAT-003 · Verification Loop

> **Layer:** L5 Verification
> **Status:** Draft

## Context

An AI system is in production. It works most of the time. But you cannot answer with confidence: *"Is it getting better or worse this week?"* — because no repeatable evaluation runs against real traffic, and no feedback signal loops back to improve it.

## Problem

- Manual, ad-hoc quality checks that don't scale
- No regression protection on prompt / model / retriever changes
- No mechanism to turn production observations into eval sets
- Model updates ship on vibes, not evidence

## Solution

Establish a **closed-loop verification cycle**:

```
     ┌──────── Production traffic ────────┐
     │                                    │
     ▼                                    │
  Traces + feedback signals               │
     │                                    │
     ▼                                    │
  Dataset curation ──► Eval datasets      │
                         │                │
                         ▼                │
                   Offline eval  ◄────── Prompt / model / agent change
                         │
                         ▼
                   Regression gate ──► Promote / block
                         │
                         ▼
                   Online / continuous eval on live traffic
                         │
                         ▼
                   Alerts + scorecards + feedback back into curation
```

## Interfaces

- **Trace schema:** OTel `gen_ai.*` semantic conventions + custom EASRA fields
- **Dataset format:** JSONL with `{ input, expected, tags, source_trace_id }`
- **Grader contract:** `{ score: 0..1, verdict: pass|fail, rationale? }`
- **Regression gate:** fails a build/deploy if a defined metric drops > threshold

## Controls

- **Human-in-the-loop for grader disagreement** — never fully trust automated graders
- **Data minimization** — curated datasets scrub PII before persistence
- **Bias monitoring** — segment metrics by tenant, geography, cohort

## KPIs

- **Coverage:** % of production traces contributing to curated datasets
- **Regression MTTR:** time from a quality regression alert to a rolled-back version
- **Grader-vs-human agreement:** validate your graders themselves
- **Cost of eval / total AI cost:** verification should be cheap enough to run continuously

## Trade-offs

- Non-trivial upfront investment
- Requires cross-team ownership (platform + product + risk)
- Grader design is itself an ongoing craft

## Anti-patterns

- **Eval only pre-deploy** — production drift will surprise you
- **One grader to rule them all** — use a small suite of orthogonal graders
- **Eval sets that never change** — datasets must evolve with production data

## Related

- [PAT-009 · Continuous Evaluation](README.md) *(planned)*
- [PAT-010 · Feedback Capture & Curation Loop](README.md) *(planned)*
- [EA-006 · Verification Plane](../architectures/EA-001-Enterprise-AI-Systems.md) *(planned)*
- [Capability Model → L5 Verification](../reference-models/capability-model.md)
