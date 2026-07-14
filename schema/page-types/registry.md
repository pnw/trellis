---
spec: registry
status: stable
updated: 2026-07-14
---

# Page Type Registry

Controlled vocabulary of artifact types for wiki pages. This file is part of the shared `schema/` layer referenced by `AGENTS.md`; tool-specific adapters must reference it rather than duplicating it.

```yaml
type: source-capture | construct | entity | synthesis | design | assessment | comparison | decision | invariant | roadmap
```

Types divide into three families. **Descriptive/epistemic** types (`source-capture`, `construct`, `entity`, `synthesis`, `design`, `assessment`, `comparison`) capture what sources say, what concepts mean, and what is known or uncertain — they carry the `evidence`/`confidence` epistemic machinery. **Normative** types (`decision`, `invariant`) capture what has been *chosen* or what *must hold* — they are asserted rather than evidence-derived, so `confidence` is optional and usually omitted and their `sources` may point at the design, capture, or chat that grounds the choice rather than an external raw source. **Planning** types (`roadmap`) capture *intended future work* — asserted, not evidence-graded, and provenance-free (`sources` is not required; the backlog cites nothing). See `schema/page-types/roadmap.md`.

A tenth type-string, `design/phase`, is a **scoped type** owned by `design` (see Scoped Types below); it is not a top-level registry type and does not appear in the vocabulary line above.

---

## Instigator Tiers

Orthogonal to the descriptive/normative split, types divide into three tiers by *who instigates a page and what triggers its creation*. The type decision tree below answers "what type is this page?"; this table answers "should this page exist, and on whose initiative?"

| Tier | Types | Instigator | Trigger |
|------|-------|------------|---------|
| **Capture** | `source-capture` | ingest | A source arrives. One capture per meaningful source — bounded, source-isolated, delegable to a capture agent with no vault context (`schema/ingest.md`). |
| **Interpretive** | `construct`, `entity`, `synthesis`, `comparison`, `assessment` | agent (at ingest review or query time) or user | Ingest review surfacing something the wiki will reason with again; recurrence across captures; a real question; a contradiction needing adjudication; a verdict falling due; an explicit user request. |
| **Authored** | `design`, `decision`, `invariant` | user | Explicit user request or ratification. Agents draft and propose authored pages in conversation; they do not create them unprompted. |

`roadmap` and the scoped `design/phase` type sit **outside** this table: their instances are not instigated per-source but required by a container's structure (a design skeleton mandates `phase-1.md`, `later.md`, `obligations.md`) or maintained as a standing surface (`wiki/roadmap.md`). Treat them as authored-tier by origin — they exist because a user created their container — but governed by that container's spec (`schema/page-types/design.md`, `schema/page-types/roadmap.md`) rather than by an instigation trigger.

Rules for the interpretive tier:

- **Ingest is an occasion for interpretation, not a justification.** Every capture raises the question "does this change the derived layer?" — asking it is a required review step (`schema/ingest.md`, Stage 2); answering yes is not. A defensible answer is often no: the contribution stays in the capture until something needs it.
- **Promotion test.** Create a `construct` or `entity` when the wiki will reason with the concept again *independent of the source that introduced it*. Recurrence across captures is retrospective evidence for that; a novel, load-bearing concept from a single source is prospective evidence. Mere mention is neither. Practical form: if the page's Why It Matters section could only restate the one source's claims, it is a paragraph in the capture, not a page.
- **Single-source promotion is priced, not prohibited.** A page citing one source takes the `confidence` ceiling that source supports — `medium` at best, `low` for non-empirical tiers (`schema/page-format.md`) — and later corroboration raises it. The confidence machinery is the cost model; there is no page-count quota, and per-type counts (`scripts/lint.py` stats output) are an observable, never a target.

---

## Location Rules

The frontmatter `type` is authoritative and must agree with the containing folder: `source-capture` in `sources/`, `construct` in `constructs/`, `entity` in `entities/`, `synthesis` in `syntheses/`, `design` in `designs/`, `assessment` in `assessments/`, `comparison` in `comparisons/`, `decision` in `decisions/`, and `invariant` in `invariants/`. A design occupies a directory: the design page is `designs/{design-slug}/design.md`, accompanied by typed, skeleton-placed subsidiary pages (`phases/phase-{n}.md` as `design/phase`; `phases/later.md` and `obligations.md` as `roadmap`) per `schema/page-types/design.md`, Directory Form, and Scoped Types below; legacy single-file `designs/{design-slug}.md` remains valid until converted.

Use `subtopics/` only when a narrower cluster materially improves navigation, such as five or more related pages, a cluster with its own sources and downstream artifacts, or a name readers would naturally seek. Subtopics may nest, but keep the hierarchy shallow unless deeper nesting is clearly useful.

**Skeleton-placed pages are exempt from folder/type agreement.** `roadmap` and `design/phase` pages are located by their container's spec, not a type folder: `wiki/roadmap.md` at the wiki root, and `phases/phase-{n}.md`, `phases/later.md`, `obligations.md` inside a design directory. There is no `roadmaps/` folder. Lint validates these by the container skeleton, not by matching a type folder.

---

## Scoped Types

A top-level type whose directory form contains subsidiary pages may define **scoped types** for them, namespaced `{parent}/{name}` (e.g. `design/phase`). A scoped type is a real page type — subsidiary pages declare it in frontmatter, so pages carry designed types rather than path-inferred ones — but it differs from a registry type in four ways:

1. It is **defined in the parent's spec file** (`schema/page-types/design.md`), not as its own registry entry here. The registry gains this mechanism paragraph, not a row per scoped type.
2. It is **excluded from the type decision tree** — you never classify free content into it; the parent's directory skeleton dictates where it appears.
3. It is **not independently subsettable** — a downstream wiki that vendors `design` vendors `design/phase` with it; the scoped type has no meaning without its parent.
4. Its **location is skeleton-defined**, exempt from folder/type agreement (see above).

This is the controlled-extensibility escape valve for directory-form component pages: it keeps the top-level vocabulary a flat list of independently meaningful knowledge artifacts while still giving every file a real, lintable, OKF-legible type. Adding a scoped type still requires user agreement (it is a schema change to the parent spec), but it does not enlarge the registry. Precedent: spec frontmatter (below) is likewise a parent-scoped mini-schema that never entered the top-level vocabulary.

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
- `schema/page-types/roadmap.md`

The scoped `design/phase` type has no file of its own — it is defined within `schema/page-types/design.md` (Scoped Type: `design/phase`).

### Spec Frontmatter

Files under `schema/page-types/` carry their own minimal YAML frontmatter — machine-readable metadata for downstream wikis diffing or subsetting the schema:

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

Is this page a pruned backlog of intended future work?
  -> roadmap
```

The scoped `design/phase` type is not in this tree: phase pages are placed by a design's directory skeleton, never classified from free content.

If a page strongly matches multiple types, split it.

Normative vs descriptive is the first cut: if the page *asserts* what was chosen or what must hold, it is `decision` or `invariant`; if it *reports or reasons about* what is known, it is one of the seven descriptive types.