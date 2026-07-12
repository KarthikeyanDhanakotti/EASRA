# Contributing to EASRA

Thanks for your interest in contributing! EASRA is a community-driven reference architecture, and every contribution — from typo fixes to full patterns — is welcome.

By participating, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## Ways to Contribute

- **Report issues** — bugs in diagrams, wrong facts, broken links, unclear docs
- **Propose patterns** — new reference patterns, decision guides, or ADRs
- **Improve diagrams** — cleaner visuals, better source files, alt-text
- **Review PRs** — thoughtful review is a first-class contribution
- **Share adoption stories** — anonymized case studies help the whole community

---

## Branching Model

- `main` — stable, released content only
- `Develop` — integration branch for the current sprint
- `feature/<short-name>` — one branch per change, cut from `Develop`
- `fix/<short-name>` — bug fixes
- `docs/<short-name>` — documentation-only changes

Open PRs against **`Develop`** unless a maintainer directs otherwise.

---

## Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short summary>

<optional body>

<optional footer>
```

Common types:

| Type       | When to use                                                |
|------------|------------------------------------------------------------|
| `feat`     | New content (pattern, ADR, spec, diagram)                  |
| `fix`      | Correction to existing content                             |
| `docs`     | README, glossary, contributing, formatting                 |
| `chore`    | Repo housekeeping (templates, CI, tooling)                 |
| `refactor` | Restructure without changing meaning                       |
| `style`    | Whitespace, markdown lint, non-substantive edits           |

Example: `feat(patterns): add RAG evaluation pattern`

---

## Pull Request Checklist

- [ ] PR targets the `Develop` branch
- [ ] Title follows Conventional Commits
- [ ] Linked issue (if applicable)
- [ ] Docs updated (README / ROADMAP / CHANGELOG entry under `[Unreleased]`)
- [ ] Diagrams have source files committed alongside exports
- [ ] Any new terms added to `docs/glossary.md`
- [ ] Reviewed for accuracy, neutrality, and vendor-agnosticism

---

## Style Guide

### Markdown
- Use ATX headings (`#`, `##`, `###`)
- One sentence per line where practical (helps diff review)
- Prefer tables over long bullet lists for comparisons
- Link liberally; avoid orphan pages

### Diagrams
- **Source first**: commit editable source (`.drawio`, `.svg`, `.excalidraw`) alongside any exported `.png`
- Keep exports at reasonable resolution (≥ 1600px wide for architecture diagrams)
- Include a short caption and, where useful, alt-text
- Prefer neutral color palettes; no vendor logos in canonical diagrams

### Writing
- Vendor-neutral by default. If a specific product is discussed, mark it clearly as an example.
- Avoid marketing language ("world-class", "revolutionary"). Prefer precise, engineering-grade prose.
- Define acronyms on first use.

---

## ADRs (Architecture Decision Records)

Significant architectural decisions must be recorded as ADRs in `docs/decisions/`.
See `docs/decisions/0001-record-architecture-decisions.md` for the template and rationale.

Filename format: `NNNN-short-kebab-title.md` (four-digit, zero-padded).

---

## Reporting Security Issues

Please **do not** open public issues for security-sensitive concerns.
Contact the maintainer privately via GitHub (`@KarthikeyanDhanakotti`) and we will coordinate a fix.

---

## Getting Help

- Open a **Discussion** for open-ended questions
- Open an **Issue** for concrete problems or proposals
- Tag `@KarthikeyanDhanakotti` if a PR is stuck without review after 7 days
