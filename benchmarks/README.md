# EASRA Benchmarks

The **EASRA Benchmarks** pillar defines standard, reproducible measurements for Enterprise AI systems. It exists so that adopters, vendors, and researchers can compare implementations on the same axes with the same methodology, and so that EASRA conformance claims are backed by numbers.

Benchmarks derive from the [Capability Model](../specification/011-capability-model.md) and the [Non-Functional Requirements](../specification/010-nfr.md). They reference only components in the [Component Catalogue](../specification/012-component-catalogue.md).

## Benchmark categories

| ID | Category | Measures | Anchoring NFR |
|----|----------|----------|---------------|
| **B-LAT** | Latency | p50 / p95 / p99 for single-agent RAG, multi-agent, tool-use paths. | N2 |
| **B-THR** | Throughput | Sustained requests / minute per capability at fixed error budget. | N3 |
| **B-COST** | Cost | Cost per 1 000 requests, per 1 000 tokens, per completed task. | N4 |
| **B-SAFE** | Safety | Injection attack success rate, jailbreak rate, PII leakage rate, harmful-content bypass rate. | N5 |
| **B-VER** | Verification quality | Grounding hit rate, citation validity, factuality precision / recall, hallucination rate. | N6 |
| **B-REL** | Reliability | Availability under fault, fallback correctness, recovery time. | N1 |
| **B-CACHE** | Cache effectiveness | Prompt / semantic / response cache hit rate and cost saving. | N4, N11 |
| **B-EVAL** | Continuous evaluation | Time-to-detect regression, false-alarm rate. | N10 |

## Reference workloads

Every benchmark runs against a fixed set of workloads so results are comparable.

| ID | Workload | Description |
|----|----------|-------------|
| **W-SARAG** | Single-Agent RAG | One agent, hybrid retrieval, one model call, verification. |
| **W-MAC** | Multi-Agent Coordination | Two-agent researcher + writer with shared memory. |
| **W-TOOL** | Tool-Use with HITL | Read-tool + write-tool + high-impact-tool with HITL. |
| **W-STREAM** | Streaming | Long streaming response with mid-stream cancellation. |
| **W-INJ** | Injection Adversarial | Direct + indirect prompt-injection attack set. |
| **W-COST** | Cost-Bounded | Fixed per-request budget with fallback and cache paths. |

Reference workload harnesses will land under [`../reference-implementation/benchmarks/`](../reference-implementation/) (planned).

## Benchmark specification skeleton

Every benchmark in this repository MUST be defined by a spec file with:

- **ID and category** (e.g., `B-LAT-SARAG`).
- **Purpose** — what it measures and why.
- **Workload reference** — which workload from the table above.
- **Inputs** — dataset (with citation and licence), request pattern, warm-up procedure.
- **Runner** — deterministic script, container digest, seed, model versions pinned.
- **Metrics** — precise definitions, units, aggregation (percentile / rate / count).
- **Environment** — hardware / instance type, network, region, tenancy.
- **Reporting format** — machine-readable JSON schema for results.
- **Repeatability** — required trials, variance bound, publication rules.

## Publication rules

- Results must publish the runner container digest, the model versions, and the environment.
- Adopters may not omit failing metrics.
- Vendor comparisons must run under identical workloads and pinned versions.

## Contributing a benchmark

1. Open an ADR proposing the benchmark ([`../adr/`](../adr/)).
2. Author the benchmark specification against the skeleton above.
3. Land the runner under [`../reference-implementation/benchmarks/`](../reference-implementation/) (planned).
4. Publish a baseline result set.

## Related

- [Spec 010 — Non-Functional Requirements](../specification/010-nfr.md)
- [Spec 011 — Capability Model](../specification/011-capability-model.md)
- [Reference Implementation](../reference-implementation/)
