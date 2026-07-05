# Benchmark Specification — <Benchmark ID>

Every EASRA benchmark is described by a spec file following this template, per [benchmarks/README.md](../benchmarks/README.md).

| Field | Value |
|-------|-------|
| ID | <e.g. B-LAT-SARAG> |
| Category | <B-LAT / B-THR / B-COST / B-SAFE / B-VER / B-REL / B-CACHE / B-EVAL> |
| Workload | <W-SARAG / W-MAC / W-TOOL / W-STREAM / W-INJ / W-COST> |
| Target EASRA version | v0.1.0 |
| Owner | <name / team> |
| Last revised | <YYYY-MM-DD> |

## 1. Purpose

*One paragraph: what this benchmark measures and why it matters. Cite the EASRA NFR ([Spec 010](../specification/010-nfr.md)) it maps to.*

## 2. Workload

*Reference the workload definition (from [benchmarks/README.md](../benchmarks/README.md)) and any workload-specific deviations.*

## 3. Inputs

- **Dataset** — name, size, licence, citation, hash.
- **Request pattern** — RPS, ramp, warm-up, duration.
- **Seeds** — RNG seed(s).
- **Pinned versions** — models, embeddings, prompts, tools, checkers.

## 4. Runner

- Container image (digest).
- Command line.
- Configuration file(s).
- Instrumentation (OTEL span attributes emitted).

## 5. Metrics

For each metric: **Name · Definition · Unit · Aggregation · Reporting**.

| Metric | Definition | Unit | Aggregation | Reporting |
|--------|------------|------|-------------|-----------|
| e.g. e2e-latency | Time from `ClientRequest` to first byte of final response. | ms | p50 / p95 / p99 | JSON |
| e.g. cost-per-request | Sum of model + tool costs per completed request. | USD | mean, p95 | JSON |

## 6. Environment

- Hardware / instance type.
- Region, tenancy.
- Network profile.
- Any co-tenants.

## 7. Reporting format

*Point to a JSON schema (planned) under `../reference-implementation/benchmarks/schemas/`.*

## 8. Repeatability

- Required number of trials.
- Variance bound (e.g. ± 5% on p95).
- Warm-up policy.
- Publication rule (adopters may not omit failing metrics).

## 9. Baseline result set

*Populate on first publication.*

| Date | Runner digest | Model / prompt / tool versions | Result |
|------|---------------|--------------------------------|--------|
|  |  |  |  |

## 10. Change control

Additions / renames / metric-definition changes require an ADR and a bump to the benchmark version.
