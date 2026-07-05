# Cloud & Runtime Implementations

Concrete, per-vendor mappings of the vendor-neutral EASRA architecture to real cloud and open-source stacks. Each implementation guide takes every EASRA layer, capability, and component from the frozen specification and shows how to realise it on a specific platform — **without changing the architecture**.

Implementations do not extend EASRA; they satisfy it. A mapping is EASRA-conformant when it covers all 16 capability domains ([Spec 011](../specification/011-capability-model.md)) and preserves every trust boundary ([Spec 009](../specification/009-trust-boundaries.md)) and NFR ([Spec 010](../specification/010-nfr.md)).

## Available guides

| Platform | Status | Location |
|----------|--------|----------|
| Microsoft Azure | Draft | [azure/](./azure/) |
| Amazon Web Services | Draft | [aws/](./aws/) |
| Google Cloud | Draft | [gcp/](./gcp/) |
| Open-source (Kubernetes + CNCF) | Draft | [open-source/](./open-source/) |

## What every guide must contain

Every guide MUST cover:

1. **Layer mapping** — every EASRA layer to the platform's native services (or a documented gap).
2. **Component mapping** — every [`K-L*-*`](../specification/012-component-catalogue.md) component to a concrete service or product.
3. **Interface mapping** — how the platform realises [Spec 006](../specification/006-interface-specification.md) interfaces (native or via adapters).
4. **Trust boundary mapping** — how [Spec 009](../specification/009-trust-boundaries.md) boundaries land on the platform's identity, network, and encryption primitives.
5. **NFR mapping** — how each NFR in [Spec 010](../specification/010-nfr.md) is achieved (SLOs, quotas, DR, cost model).
6. **Deployment topology** — Terraform / Bicep / CDK / Helm scaffolding aligned to [D-D1](../diagrams/deployment-topology.md) and the planned D-D2..D-D5.
7. **Cost model** — per-request cost baseline for the [reference implementation](../reference-implementation/).
8. **Known gaps** — where the platform cannot satisfy EASRA at v0.1.

## Contributing a new implementation

- Open an ADR for the new platform ([`../adr/`](../adr/)).
- Follow the section skeleton in the existing guides.
- Cite the platform's authoritative documentation; do not restate it.
- Publish a **Capability Maturity Statement** against [Spec 011](../specification/011-capability-model.md).

## Conformance

An implementation is considered EASRA-conformant when it declares maturity M ≥ 2 for every subcapability it implements, publishes M0 for those it does not (with justification), and passes the (planned) [conformance test suite](../reference-implementation/).
