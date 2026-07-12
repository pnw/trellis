# Page Type Registry

Controlled vocabulary of artifact types for wiki pages. This file is part of the shared `schema/` layer referenced by `AGENTS.md`; tool-specific adapters must reference it rather than duplicating it.

```yaml
type: source-capture | construct | entity | synthesis | design | assessment | comparison | decision | invariant
```

Types divide into two families. **Descriptive/epistemic** types (`source-capture`, `construct`, `entity`, `synthesis`, `design`, `assessment`, `comparison`) capture what sources say, what concepts mean, and what is known or uncertain — they carry the `evidence`/`confidence` epistemic machinery. **Normative** types (`decision`, `invariant`) capture what has been *chosen* or what *must hold* — they are asserted rather than evidence-derived, so `confidence` is optional and usually omitted and their `sources` may point at the design, capture, or chat that grounds the choice rather than an external raw source.

---

## Location Rules

The frontmatter `type` is authoritative and must agree with the containing folder: `source-capture` in `sources/`, `construct` in `constructs/`, `entity` in `entities/`, `synthesis` in `syntheses/`, `design` in `designs/`, `assessment` in `assessments/`, `comparison` in `comparisons/`, `decision` in `decisions/`, and `invariant` in `invariants/`.

Use `subtopics/` only when a narrower cluster materially improves navigation, such as five or more related pages, a cluster with its own sources and downstream artifacts, or a name readers would naturally seek. Subtopics may nest, but keep the hierarchy shallow unless deeper nesting is clearly useful.

---

## Per-Type Specs

One normative file per page type — the unit a downstream wiki subsets:

- `schema/page-types/source-capture.md`
- `schema/page-types/construct.md`
- `schema/page-types/entity.md`
- `schema/page-types/synthesis.md`
- `schema/page-types/design.md`
- `schema/page-types/assessment.md`
- `schema/page-types/comparison.md`
- `schema/page-types/decision.md`
- `schema/page-types/invariant.md`

---

## Controlled Extensibility

Do not invent new types casually. A new type may be introduced only when:

1. The page's primary question is not well-served by an existing type.
2. Forcing it into an existing type would distort the artifact.
3. The new type is likely to recur.
4. The type is added as a new file under `schema/page-types/` with full definition, plus a registry entry here.
5. The definition includes: purpose, question answered, when to use, when not to use, and expected sections.
6. Never add a new type without first asking the user.

---

## Type Decision Tree

```
Is this page a faithful capture of one raw source?
  -> source-capture

Is this page defining a reusable abstraction, mechanism, pattern, or named intellectual building block?
  -> construct

Is this page about a named person, organization, tool, model, repo, paper, project, or system?
  -> entity

Is this page integrating multiple sources/artifacts into the current understanding of a topic?
  -> synthesis

Is this page documenting how a system, architecture, workflow, or process works?
  -> design

Is this page evaluating evidence, confidence, validation, uncertainty, risk, gaps, or open questions?
  -> assessment

Is this page comparing two or more things?
  -> comparison

Is this page recording a specific choice made among alternatives, with rationale?
  -> decision

Is this page declaring a rule or constraint that must always hold?
  -> invariant
```

If a page strongly matches multiple types, split it.

Normative vs descriptive is the first cut: if the page *asserts* what was chosen or what must hold, it is `decision` or `invariant`; if it *reports or reasons about* what is known, it is one of the seven descriptive types.