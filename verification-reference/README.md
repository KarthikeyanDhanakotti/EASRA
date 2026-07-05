# EASRA AI Verification Reference

The **AI Verification Reference** is EASRA's authoritative body of guidance on making Enterprise AI outputs *verifiable*, not merely *evaluated*. Verification is a first-class layer in EASRA (L9), distinct from evaluation (L10), and this pillar defines the taxonomy, checkers, metrics, and methodology.

Per [Design Principle P3](../specification/002-design-principles.md), every AI output is verifiable.

## Verification vs. evaluation

| Property | Verification (L9) | Evaluation (L10) |
|----------|-------------------|------------------|
| When | On the request path, before the response is returned. | Off the request path, over aggregated traces. |
| Latency budget | Sub-second (part of request latency). | Minutes to hours. |
| Purpose | Gate this response. | Improve the system. |
| Output | `Verdict` = allow / escalate / block. | Metric time-series and regression alerts. |
| Component | `K-L9-VE` + checkers. | `K-L10-EVAL`. |

## 1. The seven verification classes

Per [Spec 011 §C9](../specification/011-capability-model.md).

| Class | ID | Purpose | Reference checker | Anchoring component |
|-------|----|---------|-------------------|--------------------|
| Grounding | C9.1 | Every factual claim is supported by retrieved evidence. | Sentence-level entailment vs. retrieved chunks (Ragas, NLI). | `K-L9-GRD` |
| Citation | C9.2 | Every citation resolves to an entry in the Source Registry. | Citation-string ↔ `K-L5-SRC` lookup. | `K-L9-CIT` |
| Factuality | C9.3 | Claims agree with a trusted ground-truth source. | Small verifier LLM / grader model. | `K-L9-FCT` |
| Format | C9.4 | Response conforms to declared schema / JSON / policy. | JSON Schema, Pydantic, regex. | `K-L9-FMT` |
| Policy | C9.5 | Response satisfies data-class, jurisdictional, consent policy. | Policy engine query. | `K-L9-POL` |
| Business rule | C9.6 | Domain-specific invariants (e.g., "no discount > 20%"). | Rule engine / custom validators. | `K-L9-BR` |
| Confidence | C9.7 | Combine signals; produce allow / escalate / block. | Scoring model + policy. | `K-L9-CS` |

## 2. Reference checker catalogue

| Checker ID | Class | Reference implementation | Notes |
|------------|-------|--------------------------|-------|
| CHK-GRD-01 | Grounding | Ragas `faithfulness`, `answer_relevancy` | Requires retrieved contexts. |
| CHK-GRD-02 | Grounding | Custom NLI-based checker on small model | Lower latency. |
| CHK-CIT-01 | Citation | Regex + Source Registry lookup | Deterministic. |
| CHK-FCT-01 | Factuality | Grader LLM (`gpt-4o-mini`-class) with rubric | Cost-sensitive. |
| CHK-FMT-01 | Format | JSON Schema validator | Deterministic. |
| CHK-POL-01 | Policy | OPA / Cedar policy evaluation | Deterministic. |
| CHK-BR-01 | Business rule | Custom Python validators registered in a rulebook | Domain-owned. |
| CHK-CS-01 | Confidence | Weighted scorer + threshold policy | Configurable. |

## 3. Grounding metrics — precise definitions

Every grounding checker MUST publish metrics against these definitions:

- **Groundedness (rate)** — fraction of atomic claims in the response supported by at least one retrieved chunk under the entailment threshold.
- **Citation validity (rate)** — fraction of cited spans resolving to a Source Registry entry.
- **Citation precision (rate)** — fraction of cited spans that are actually supported by the referenced source.
- **Hallucination rate** — 1 − Groundedness for factual claims.
- **Groundedness latency** — checker p95 latency.

## 4. Golden-set methodology

Every capability that produces free-form text MUST maintain a **golden set** used both for offline evaluation and for regression tests on prompt / model / retrieval changes.

- **Size floor** — ≥ 200 items per capability at v0.1.0, ≥ 1 000 at v1.0.
- **Labels** — expected answer, expected citations, expected policy verdict, expected business-rule verdict, sensitivity label.
- **Provenance** — every item has a source, an author, and a licence.
- **Refresh policy** — 10% rotation per quarter.

## 5. Continuous verification loop

Production traces (from `K-L10-OTEL`) are sampled and re-verified off-line by `K-L10-EVAL` using the same checkers as `K-L9-VE`. Divergence between on-line `Verdict` and off-line verdict is an alert.

## 6. Failure semantics

| Verdict | Action | Downstream effect |
|---------|--------|-------------------|
| allow | Response streamed. | Normal. |
| escalate | Response held; HITL invoked. | Latency spike; must be within escalation SLO. |
| block | Response replaced with `ErrorEnvelope`. | Audit event; user-visible error. |

## 7. Anti-patterns

- Treating evaluation metrics (BLEU, ROUGE) as verification signals.
- Relying on a single grader model without a confidence policy.
- Verifying only the final answer of a multi-step agent (each step must be verifiable).
- Publishing evaluations without publishing checker versions and thresholds.

## Related

- [Spec 002 §P3](../specification/002-design-principles.md)
- [Spec 011 §C9](../specification/011-capability-model.md)
- [Spec 012 §L9](../specification/012-component-catalogue.md)
- [Architectures / Runtime — D-R5 Guardrail + Verification Decision Flow (planned)](../architectures/runtime/)
- [Benchmarks — B-VER](../benchmarks/)
