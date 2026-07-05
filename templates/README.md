# EASRA Templates

Reusable starter templates for the EASRA ecosystem — for new repositories, for adopter artefacts, and for standard deliverables.

## Available templates

| Template | Purpose | Location |
|----------|---------|----------|
| **GitHub Profile README** | Ready-to-paste profile README establishing the Enterprise-AI-Systems-Engineering identity. | [`github-profile-README.md`](./github-profile-README.md) |
| **Repository Starter** | Skeleton README + folder layout aligned to the [Repository Quality Checklist](../checklists/repository-quality.md). | [`repository-template/`](./repository-template/) |
| **Capability Maturity Statement** | Adopters use this to declare their per-capability maturity ([Spec 011 §5](../specification/011-capability-model.md)). | [`capability-maturity-statement.md`](./capability-maturity-statement.md) |
| **Threat Model** | Per-workload STRIDE-style threat model referenced from the [Security Reference](../security-reference/README.md). | [`threat-model.md`](./threat-model.md) |
| **Benchmark Spec** | Skeleton for authoring a new EASRA benchmark ([benchmarks/](../benchmarks/README.md#benchmark-specification-skeleton)). | [`benchmark-spec.md`](./benchmark-spec.md) |
| **Ecosystem Style Guide** | Visual + writing conventions every EASRA-family repo follows. | [`ecosystem-style-guide.md`](./ecosystem-style-guide.md) |

## How to use

1. Copy the template into the target repository / folder.
2. Rename per the target's naming.
3. Fill in every `TODO` and every `<placeholder>`.
4. Delete any section that does not apply, with a one-line justification.

## Contributing a new template

- Open an ADR proposing the template ([`../adr/`](../adr/)).
- Follow the existing templates' shape (Purpose / Fields / Rendered example / Notes).
- Every template MUST cite the spec / checklist / component it supports.
