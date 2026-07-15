---
spec: registry
status: stable
updated: 2026-07-13
---

# Page Type Registry

Controlled vocabulary of artifact types for wiki pages. This file is part of the shared `schema/` layer referenced by `AGENTS.md`; tool-specific adapters must reference it rather than duplicating it.

```yaml
type: source-capture | construct | entity | synthesis | assessment | comparison | decision | invariant
```

Types divide into two families. **Descriptive/epistemic** types (`source-capture`, `construct`, `entity`, `synthesis`, `assessment`, `comparison`) capture what sources say, what concepts mean, and what is known or uncertain — they carry the `evidence`/`confidence` epistemic machinery. **Normative** types (`decision`, `invariant`) capture what has been *chosen* or what *must hold* — they are asserted rather than evidence-derived, so `confidence` is optional and usually omitted and their `sources` may point at the design dossier, capture, or chat that grounds the choice rather than an external raw source.

Designs are not a wiki page type. A document answering "what are we building, and where is it in being built?" is commitment-shaped, not claim-shaped, and lives on the design surface (`designs/` dossiers, per `schema/design/dossier.md`) under lifecycle governance rather than evidence governance.

---

## Instigator Tiers

Orthogonal to the descriptive/normative split, types divide into three tiers by *who instigates a page and what triggers its creation*. The type decision tree below answers "what type is this page?"; this table answers "should this page exist, and on whose initiative?"

| Tier | Types | Instigator | Trigger |
|------|-------|------------|---------|
| **Capture** | `source-capture` | ingest | A source arrives. One capture per meaningful source — bounded, source-isolated, delegable to a capture agent with no vault context (`schema/wiki/ingest.md`). |
| **Interpretive** | `construct`, `entity`, `synthesis`, `comparison`, `assessment` | agent (at ingest review or query time) or user | Ingest review surfacing something the wiki will reason with again; recurrence across captures; a real question; a contradiction needing adjudication; a verdict falling due; an explicit user request. |
| **Authored** | `decision`, `invariant` | user | Explicit user request or ratification. Agents draft and propose authored pages in conversation; they do not create them unprompted. (Design dossiers, though not wiki pages, follow the same instigation rule — see `schema/design/dossier.md`.) |

Rules for the interpretive tier:

- **Ingest is an occasion for interpretation, not a justification.** Every capture raises the question "does this change the derived layer?" — asking it is a required review step (`schema/wiki/ingest.md`, Stage 2); answering yes is not. A defensible answer is often no: the contribution stays in the capture until something needs it.
- **Promotion test.** Create a `construct` or `entity` when the wiki will reason with the concept again *independent of the source that introduced it*. Recurrence across captures is retrospective evidence for that; a novel, load-bearing concept from a single source is prospective evidence. Mere mention is neither. Practical form: if the page's Why It Matters section could only restate the one source's claims, it is a paragraph in the capture, not a page.
- **Single-source promotion is priced, not prohibited.** A page citing one source takes the `confidence` ceiling that source supports — `medium` at best, `low` for non-empirical tiers (`schema/wiki/page-format.md`) — and later corroboration raises it. The confidence machinery is the cost model; there is no page-count quota, and per-type counts (`scripts/lint.py` stats output) are an observable, never a target.

---

## Location Rules

The frontmatter `type` is authoritative and must agree with the containing folder: `source-capture` in `sources/`, `construct` in `constructs/`, `entity` in `entities/`, `synthesis` in `syntheses/`, `assessment` in `assessments/`, `comparison` in `comparisons/`, `decision` in `decisions/`, and `invariant` in `invariants/`.

Use `subtopics/` only when a narrower cluster materially improves navigation, such as five or more related pages, a cluster with its own sources and downstream artifacts, or a name readers would naturally seek. Subtopics may nest, but keep the hierarchy shallow unless deeper nesting is clearly useful.

---

## Per-Type Specs

One normative file per page type — the unit a downstream wiki subsets:

- `schema/wiki/page-types/source-capture.md`
- `schema/wiki/page-types/construct.md`
- `schema/wiki/page-types/entity.md`
- `schema/wiki/page-types/synthesis.md`
- `schema/wiki/page-types/assessment.md`
- `schema/wiki/page-types/comparison.md`
- `schema/wiki/page-types/decision.md`
- `schema/wiki/page-types/invariant.md`

### Spec Frontmatter

Files under `schema/wiki/page-types/` carry their own minimal YAML frontmatter — machine-readable metadata for downstream wikis diffing or subsetting the schema:

```yaml
spec: page-type | registry   # what kind of schema file this is
type: construct              # page-type files only — the type this file specifies
tier: capture | interpretive | authored   # page-type files only — instigator tier (see table above)
instigators: [ingest] | [agent, user] | [user]   # page-type files only
status: stable | draft | deprecated
updated: YYYY-MM-DD          # date of last normative change
```

Trigger detail stays prose in the Instigator Tiers table above; the frontmatter carries only what a `git diff schema/` should make legible. Do not add fields beyond these without a schema change.

---

## Controlled Extensibility

Do not invent new types casually. A new type may be introduced only when:

1. The page's primary question is not well-served by an existing type.
2. Forcing it into an existing type would distort the artifact.
3. The new type is likely to recur.
4. The type is added as a new file under `schema/wiki/page-types/` with full definition, plus a registry entry here.
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

Is this page specifying something to be built, or an operative protocol — a commitment rather than a claim?
  -> not a wiki page: a design dossier (schema/design/dossier.md)

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