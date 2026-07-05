# EASRA Documentation Site

This folder hosts the configuration and assets for the future EASRA **documentation site**. It does **not** duplicate specification content — the specifications, handbook, architectures, and diagrams remain the source of truth in their respective top-level folders. `docs/` exists to render those into a browsable, searchable site (candidate: MkDocs Material, Docusaurus, or Nextra).

## Planned site structure

```
docs.easra.dev  (or  karthikeyandhanakotti.github.io/EASRA)
├── /                          Vision, principles, layers overview (from README + Spec 001)
├── /specification/            Rendered specifications 001–012
├── /architectures/            Five architecture views + diagram catalogue
├── /implementations/          Azure / AWS / GCP / open-source mappings
├── /benchmarks/               Benchmark specs and result sets
├── /security/                 Security reference (threats / controls / standards)
├── /verification/             Verification reference (classes / checkers / methods)
├── /llmops/                   LLMOps guide
├── /handbook/                 Per-layer chapters
├── /adr/                      ADR index
├── /research/                 Research index
├── /conference/               Talk decks and workshops
└── /changelog/                Release notes
```

## Chosen tooling

TBD via ADR. Candidates:

| Tool | Pros | Cons |
|------|------|------|
| **MkDocs Material** | Lowest friction for markdown-heavy, spec-oriented docs; excellent search; native Mermaid. | Less flexible than JSX-based generators. |
| **Docusaurus** | React-based, versioned docs first-class, plugin ecosystem. | Heavier build; more moving parts. |
| **Nextra** | Modern, Next.js-based, good defaults. | Newer; smaller community than the two above. |

## Publishing

Once tooling is chosen (planned ADR), the site will be built by the same GitHub Actions workflow that runs [`docs.yml`](../.github/workflows/docs.yml) and published to GitHub Pages (or a custom domain).

## Assets

- Logos, colour palette, and diagram style guide live under [`assets/`](./assets/) — planned.
- Every diagram in the site derives from an in-repo source in [`../diagrams/`](../diagrams/) via the [Diagram Catalogue](../diagrams/CATALOGUE.md); the site does not fork diagram content.

## Contributing

Do not add prose content here. Content belongs in the source-of-truth folders (`specification/`, `handbook/`, `architectures/`, etc.); the site consumes them.
