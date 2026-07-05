# Contributing to EASRA

Thank you for considering a contribution to the **Enterprise AI Systems Reference Architecture (EASRA)**. EASRA aims to become a durable, vendor-neutral standard, so contributions are held to a high bar of clarity, neutrality, and evidence.

## Ways to contribute

| Contribution type | Where it lives | Typical review |
|-------------------|----------------|----------------|
| Fix typos, broken links, formatting | Any file | 1 maintainer |
| Clarify existing spec text (no semantic change) | `specification/` | 1 maintainer |
| Add or revise a handbook chapter | `handbook/` | 1 maintainer + 1 domain reviewer |
| Add or update a diagram | `diagrams/` | 1 maintainer |
| Add a worked example | `examples/` | 1 maintainer |
| Propose a change to a layer boundary, interface, or design principle | ADR in `adr/` + change to `specification/` | 2 maintainers + public comment period (14 days) |
| New research contribution | `research/` | 1 maintainer |

## Ground rules

1. **Vendor neutrality is non-negotiable.** Specification and handbook text must not name a specific vendor, product, or SaaS as *the* solution. Vendor mappings belong in the "Cloud Implementation" subsection of a chapter and must cover at least two of {Azure, AWS, GCP, open-source}.
2. **Architecture before implementation.** New material must first explain the problem, responsibility, and interface — then implementation choices.
3. **Evidence over opinion.** Claims about failure modes, latency, cost, or security should reference standards (NIST, OWASP, ISO), published research, or reproducible measurements — not personal experience alone.
4. **Backwards-compatible unless via ADR.** Any change that renumbers layers, renames interfaces, or removes a principle must go through an ADR.
5. **No unsourced benchmarks.** Do not include performance numbers without a linked, reproducible methodology.

## Contribution workflow

1. **Open an issue first** for anything larger than a typo. Describe the problem and the proposed direction.
2. **Fork** the repository and create a branch: `git checkout -b <type>/<short-description>` where `<type>` is one of `spec`, `handbook`, `diagram`, `example`, `adr`, `research`, `docs`, `chore`.
3. **Make the change.** Keep PRs focused — one logical change per PR.
4. **Update the changelog.** Add an entry under the `Unreleased` section of [CHANGELOG.md](./CHANGELOG.md).
5. **Open a pull request.** Use the PR template. Link the issue.
6. **Address review comments.** Maintainers may request restructuring for neutrality or clarity.

## Style guide

- **Markdown**: ATX headings (`#`), sentence-case titles, one sentence per line for spec files (easier diffs).
- **Diagrams**: Prefer Mermaid inline in Markdown. Only add rendered images (`.png`, `.svg`) if the diagram cannot be expressed in Mermaid; always keep the source (`.drawio`, `.mmd`).
- **File names**: Lowercase, hyphenated, no spaces. Specification files are numbered (`NNN-topic.md`), ADRs are numbered (`NNNN-title.md`), handbook chapters use the layer number (`L05-knowledge-and-retrieval.md`).
- **Terminology**: Follow [specification/003-terminology.md](./specification/003-terminology.md). If you need a term that isn't there, add it in the same PR.

## ADR process

Architecture Decision Records govern any change to layer boundaries, interfaces, principles, or the trust-boundary model.

1. Copy [`adr/0000-template.md`](./adr/0000-template.md) to the next available number.
2. Fill in Context, Decision, Consequences, Alternatives, and Status = `Proposed`.
3. Open a PR titled `ADR-NNNN: <title>`.
4. The PR remains open for a **14-day public comment period** (calendar days).
5. Two maintainers must approve for the ADR to move to `Accepted`.
6. Merged ADRs may not be edited except for typos; they are superseded by new ADRs.

## Code contributions

Reference implementation and example code follow the language's idiomatic style:

- **Python**: `ruff` + `black` + `mypy --strict`.
- **TypeScript**: `eslint` + `prettier` + `tsc --strict`.
- **Tests required** for any code that lives under `reference-implementation/`.
- **No secrets**, no cloud account IDs, no customer data — anywhere.

## Governance

See [GOVERNANCE.md](./GOVERNANCE.md) for maintainer roles, decision rights, and the process for becoming a maintainer.

## Code of Conduct

By participating you agree to abide by the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Report violations to the maintainer(s) listed in [GOVERNANCE.md](./GOVERNANCE.md).

## Licensing of contributions

By contributing you agree that your contributions will be licensed under the same dual license as the repository:

- Documentation and diagrams: **CC-BY-4.0**
- Code: **Apache-2.0**

You retain copyright to your contribution.
