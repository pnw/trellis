# Trellis Design Specification

Version 0.1.0 — Draft

Conforms to Open Knowledge Format (OKF) 0.1

Trellis Design is a human- and agent-readable format for recording what is to
be built, the constraints that shape it, and optional implementation scoping
or alternative analysis. Each design is a dossier: a directory whose required
`design.md` is the authoritative target and whose optional subdocuments are
progressive enhancements.

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**,
and **MAY** express conformance requirements.

---

## 1. Motivation

Designs often mix the target, implementation plan, rejected alternatives, and
follow-up work in one changing document. That makes it difficult to tell what
is authoritative, what is provisional, and what has been deferred. Trellis
Design gives each concern a stable place while requiring only the target
specification for simple work.

### 1.1 Goals

1. Make `design.md` a complete, standalone declaration of the target.
2. Keep the minimum valid design to one file.
3. Add phases, deferred scope, prerequisites, external obligations, and
   alternatives only when they provide value.
4. Give each optional artifact an explicit type and contract.
5. Preserve the historical meaning of completed or abandoned designs.
6. Remain readable, diffable, portable, and strictly OKF-conformant.

### 1.2 Non-goals

- Prescribing how a design is proposed, approved, staffed, or implemented.
- Requiring phasing, roadmapping, prerequisites, alternatives, or external
  obligations.
- Serving as live documentation for the system after the design terminates.
- Replacing issue trackers, project-management systems, or source control.
- Defining research or knowledge-base artifacts.

---

## 2. Terminology

- **Design** — The target specification in `design.md`.
- **Dossier** — The directory containing a design and its optional supporting
  artifacts.
- **Target** — The state, behavior, or system declared by `design.md`.
- **Live design** — A design with status `draft` or `active`.
- **Terminal design** — A design with status `implemented`, `superseded`, or
  `abandoned`.
- **Phase** — One bounded implementation scope against the target.
- **Later scope** — Target scope intentionally deferred beyond the numbered
  phases.
- **Prerequisite** — A condition that must hold before the design or a phase can
  begin.
- **Obligation** — Work the design induces outside its own target boundary.
- **Alternative** — A candidate change to the complete target or a bounded part
  of it.
- **Evaluation** — The comparison of alternatives against the authoritative
  target and, when applicable, one another.
- **Progressive enhancement** — An optional artifact group that becomes
  conditionally complete when its directory or file is present.

---

## 3. Dossier Structure

The minimum conforming dossier contains one file:

```text
designs/
└── <design-slug>/
    └── design.md                  # REQUIRED
```

A fully enhanced dossier may contain:

```text
designs/
└── <design-slug>/
    ├── design.md                  # REQUIRED — type: design
    ├── phases/                    # OPTIONAL AS A UNIT
    │   ├── phase-1.md             # one or more — type: phase
    │   ├── phase-2.md
    │   └── later.md               # required with phases/ — type: roadmap
    ├── prerequisites.md           # OPTIONAL — type: prerequisites
    ├── obligations.md             # OPTIONAL — type: obligations
    ├── alternatives/              # OPTIONAL AS A UNIT
    │   ├── <candidate>.md          # one or more — type: alternative
    │   └── evaluation.md          # required — type: evaluation
    └── assets/                    # OPTIONAL — supporting assets
```

The dossier slug and all Markdown filenames MUST use lowercase kebab-case.
Numbered phases use `phase-<n>.md` without zero padding.

`design.md` is the only universally required file. The existence of an
optional enhancement activates that enhancement's complete structural contract
in Sections 6–9.

A collection of dossiers MAY provide an OKF `index.md`, but the collection
index is not part of an individual dossier's conformance.

---

## 4. Document Model

Every standard dossier document and every extension document is an OKF concept
document. It MUST be UTF-8 Markdown beginning with parseable YAML frontmatter
and a non-empty `type`.

Standard dossier documents use these common fields:

```yaml
---
title: Human-readable title
type: <dossier type>
description: One sentence describing this artifact.
timestamp: 2026-07-15T18:30:00Z
---
```

| Field | Requirement |
|---|---|
| `title` | REQUIRED. Human-readable display name. |
| `type` | REQUIRED. The type fixed by the artifact's structural position. |
| `description` | REQUIRED. One-sentence summary. |
| `timestamp` | REQUIRED. ISO 8601 datetime of the last meaningful change. |

The following fields are REQUIRED on `design.md` and optional on other dossier
documents:

```yaml
sources: []
related: []
tags: []
```

Each field is a YAML list and MAY be empty.

Values in `sources` and `related` are repository-relative paths or absolute
URLs. Unknown fields MAY be added. Consumers MUST preserve unknown fields when
round-tripping and tolerate unknown OKF types.

The epistemic grading fields `evidence`, `confidence`, `novelty`, and
`enforcement` are outside the dossier vocabulary and MUST NOT appear on dossier
documents. A design is governed by its lifecycle state, not by
evidence-grading metadata.

The standard dossier vocabulary is:

| File | Required type |
|---|---|
| `design.md` | `design` |
| `phases/phase-<n>.md` | `phase` |
| `phases/later.md` | `roadmap` |
| `prerequisites.md` | `prerequisites` |
| `obligations.md` | `obligations` |
| `alternatives/<candidate>.md` | `alternative` |
| `alternatives/evaluation.md` | `evaluation` |

All non-standard supporting files MUST live under `assets/`. Supporting assets
are opaque dossier workspace and need no frontmatter, even when their media type
is Markdown. A Markdown asset intended to participate as an OKF concept document
MUST declare an extension type beginning with `x-` and remain readable as a
generic OKF concept. Consumers ignore opaque supporting assets when checking
document conformance.

---

## 5. `design.md`

`design.md` is the dossier's authoritative declaration of the target. Optional
artifacts scope, compare, or record consequences of the target; they do not
override it.

Required frontmatter:

```yaml
---
title: Design Title
type: design
description: One sentence describing the target.
status: draft | active | implemented | superseded | abandoned
timestamp: 2026-07-15T18:30:00Z
trellis_design_version: "0.1.0"
sources: []
related: []
tags: []
---
```

The body MUST address these minimum content areas:

1. purpose;
2. system boundary;
3. core model;
4. components;
5. architecture;
6. workflow or data flow;
7. constraints and design-local invariants;
8. behavioral statements or acceptance criteria;
9. decisions;
10. evidence and rationale; and
11. open design questions.

Authors MAY adapt, combine, or reorder headings to fit the design. Canonical
headings are `## Purpose`, `## System Boundary`, `## Core Model`,
`## Components`, `## Architecture`, `## Workflow / Data Flow`,
`## Constraints / Invariants`, `## Behavioral Statements (Acceptance
Criteria)`, `## Decisions`, `## Evidence and Rationale`, and `## Open Design
Questions`. An inapplicable content area may be stated as `None.` rather than
expanded ceremonially. Architecture describes the arrangement and relationships
of components. Behavioral statements define observable acceptance criteria.
Decisions record target-local choices necessary to understand the design.
Motivation, goals, non-goals, terminology, interfaces, state transitions, error
behavior, and examples MAY be added or incorporated where they make the target
clearer.

The target MUST be complete without reading phases, prerequisites, obligations,
alternatives, or their evaluation. It MUST describe desired behavior and
constraints rather than an implementation sequence.

### 5.1 Lifecycle

`status` is the design's governing state:

| Status        | Meaning                                                                     |
| ------------- | --------------------------------------------------------------------------- |
| `draft`       | The target is being developed and is not yet operative.                     |
| `active`      | The target is ratified and guides current work.                             |
| `implemented` | Terminal. The target was delivered.                                         |
| `superseded`  | Terminal. Another design replaced this target; the successor is identified. |
| `abandoned`   | Terminal. The target was dropped without delivery.                          |

A live design MAY change meaning. When a design becomes `implemented`, its
language changes tense as needed to preserve the intent-as-built record. At any
terminal state, the whole dossier freezes: `design.md` and every subsidiary
document are retained as they stand. Standard documents MUST NOT be added,
removed, or rewritten to change meaning after termination.

Substantive evolution requires a successor design. Corrections that do not
change meaning, such as fixing a typo, broken link, or conformance metadata,
remain allowed and update the timestamp. A terminal design describes what was
intended and why; it is not maintained as live documentation of the implemented
system. No dossier document is deleted merely because its work completed.

---

## 6. Phases Enhancement

The `phases/` directory is optional. When it exists, it MUST contain:

1. one or more numbered phase documents beginning with `phase-1.md`; and
2. `later.md`.

Together, the numbered phase scopes and later scope MUST cover every part of
`design.md`. Overlap is permitted:

```text
sum(numbered phase scopes) + later scope >= design.md
```

No target requirement may disappear merely because implementation is phased.

### 6.1 Numbered phase

Frontmatter:

```yaml
---
title: Phase 1
type: phase
description: The bounded implementation scope for this phase.
status: pending | in-progress | complete # OPTIONAL
timestamp: 2026-07-15T18:30:00Z
---
```

`status` is optional on a phase. When present, it MUST be `pending`,
`in-progress`, or `complete`.

The body MUST contain these exact second-level headings:

1. `## Scope`
2. `## Deliverables`
3. `## Completion Criteria`
4. `## Dependencies and Constraints`
5. `## Design Coverage`

Design Coverage identifies the target sections or requirements claimed by the
phase. A phase scopes implementation; it MUST NOT redefine the target.

### 6.2 Later scope

Required frontmatter:

```yaml
---
title: Later Scope
type: roadmap
description: Target scope deferred beyond the numbered phases.
timestamp: 2026-07-15T18:30:00Z
---
```

The body MUST contain `## Deferred Scope`. When numbered phases cover the
entire target, the section states `None; the numbered phases cover the target.`

`later.md` is a current, pruned remainder, not an append-only journal. While the
dossier is live, an item leaves when it is implemented, claimed by a numbered
phase, or deliberately dropped. Terminal freeze then preserves the remainder as
it stands.

---

## 7. Prerequisites Enhancement

`prerequisites.md` is optional. It records conditions that must hold before the
design or a named phase can begin. It does not contain target scope and does not
participate in phase coverage.

Required frontmatter when present:

```yaml
---
title: Prerequisites
type: prerequisites
description: Conditions required before this design or a phase can begin.
timestamp: 2026-07-15T18:30:00Z
---
```

The body MUST contain `## Prerequisites`. Each prerequisite SHOULD identify the
condition, the design or phase it gates, and how satisfaction is verified.

`prerequisites.md` is a current, pruned register rather than an append-only
journal. While the dossier is live, a prerequisite leaves when it is satisfied,
incorporated into the target, or deliberately dropped. Terminal freeze then
preserves the register as it stands.

---

## 8. Obligations Enhancement

`obligations.md` is optional. It records work required outside the target's own
boundary as a consequence of completing one or more phases or the design as a
whole. It does not contain target scope and does not participate in phase
coverage.

Required frontmatter when present:

```yaml
---
title: External Obligations
type: obligations
description: Work this design requires outside its target boundary.
timestamp: 2026-07-15T18:30:00Z
---
```

The body MUST contain `## Obligations`. Each obligation SHOULD identify the
affected system, triggering phase or design scope, required outcome, and
completion condition.

`obligations.md` is a current, pruned register rather than an append-only
journal. While the dossier is live, an obligation leaves when it is completed,
absorbed into another operative artifact, or deliberately dropped. Terminal
freeze then preserves the register as it stands.

---

## 9. Alternatives Enhancement

The `alternatives/` directory is optional. When it exists, it MUST contain:

1. one or more candidate documents of type `alternative`; and
2. `evaluation.md` of type `evaluation`.

All candidates in the directory MUST address the same design question and
scope. That scope MAY be the complete target or a bounded part of it.

### 9.1 Alternative

Frontmatter:

```yaml
---
title: Candidate Name
type: alternative
description: One-sentence summary of this candidate.
status: draft | active | implemented | superseded | abandoned # OPTIONAL
timestamp: 2026-07-15T18:30:00Z
---
```

An alternative MUST be self-contained and complete without alternative-specific
subsidiary documents. Its body MUST:

1. contain `## Scope`, identifying the complete or bounded target area and its
   baseline in `design.md`;
2. address the Section 5 content contract for the proposed fork; and
3. contain `## Prerequisites`, `## Obligations`, and `## Downstream Impacts`.

The Section 5 headings remain adaptable, combinable, and reorderable.
Prerequisites may gate the candidate or a phase it changes. Obligations record
external work the candidate induces. Downstream Impacts state what the fork
means for the authoritative design as a whole. A section with no applicable
content states `None.`

An alternative is a candidate only. It has no authority over `design.md`.

### 9.2 Evaluation

Required frontmatter:

```yaml
---
title: Alternatives Evaluation
type: evaluation
description: Comparison and current judgment across the design alternatives.
timestamp: 2026-07-15T18:30:00Z
---
```

The body MUST contain these exact second-level headings:

1. `## Decision Question`
2. `## Criteria`
3. `## Comparison`
4. `## Judgment`
5. `## Unresolved Questions`

Comparison MUST evaluate every candidate against the corresponding baseline in
`design.md`. With multiple candidates, it MUST also compare them with one
another. A bounded candidate uses the affected target area as its direct
baseline and its Downstream Impacts for design-wide consequences.

Judgment MUST state the present conclusion. `Unresolved` is a valid conclusion
when the available information does not support a recommendation. A single
candidate still requires evaluation because it differs from the authoritative
target.

An evaluated candidate becomes authoritative only when its accepted content is
represented in `design.md`.

---

## 10. Links

All internal links MUST use standard Markdown syntax with paths relative to the
current document:

```markdown
See the [first phase](phases/phase-1.md).
```

Absolute URLs identify external resources.

A producer MUST maintain resolvable internal links. An OKF consumer MUST still
tolerate a broken link and render the remaining document.

`design.md` is the dossier's only stable link target from outside the dossier.
Documents outside a dossier MUST link to its `design.md`, not to phases,
prerequisites, obligations, alternatives, evaluations, or assets.
Dossier-internal documents MAY link to one another because they share the same
lifecycle and containment boundary.

---

## 11. Producer and Consumer Behavior

A producer:

- MUST keep `design.md` complete and authoritative;
- MUST apply each standard artifact's structural type and body contract;
- MUST satisfy the complete conditional contract of any enhancement present;
- MUST place every non-standard supporting file under `assets/`;
- MUST update timestamps after meaningful changes;
- MUST preserve the whole dossier at a terminal state;
- MUST use successor dossiers for substantive post-terminal evolution;
- SHOULD keep optional artifacts only while they provide useful information
  and the dossier remains live.

A consumer:

- MUST read ordinary Markdown and parse YAML frontmatter;
- MUST treat `design.md` as the target specification;
- MUST treat phases as implementation scope, not target overrides;
- MUST treat prerequisites as gates, not target scope;
- MUST treat obligations as induced external work, not target scope;
- MUST treat alternatives as candidates and evaluation as comparison against
  the authoritative target;
- MUST treat `design.md` as the dossier's only stable external link target;
- MUST tolerate unknown fields and extension types;
- MUST ignore opaque supporting assets when checking document conformance;
- SHOULD preserve unknown metadata when editing or round-tripping documents.

---

## 12. Conformance

A dossier conforms to Trellis Design 0.1 when:

1. It conforms to OKF 0.1.
2. It contains `design.md` with the required metadata and target-content
   contract.
3. `design.md` declares `trellis_design_version: "0.1.0"`.
4. `design.md` contains `sources`, `related`, and `tags` lists.
5. Every standard or extension document has parseable YAML frontmatter and a
   non-empty type.
6. Every standard artifact's path, type, metadata, and body agree.
7. No dossier document carries an epistemic grading field.
8. Every non-standard supporting file is under `assets/`.
9. If `phases/` exists, it contains numbered phases and `later.md`, and their
   combined coverage includes the complete target.
10. If `prerequisites.md` exists, it follows the prerequisites contract.
11. If `obligations.md` exists, it follows the obligations contract.
12. If `alternatives/` exists, it contains one or more self-contained candidates
    for one shared question and scope, plus a complete evaluation against
    `design.md`.
13. Every internal Markdown link resolves.

A document may be valid OKF without being Trellis Design-conformant. Consumers
MUST distinguish validation from readability.

---

## 13. Versioning

Trellis Design versions use semantic versioning:

- A patch release clarifies wording without changing conformance.
- A minor release adds backward-compatible optional fields or enhancements.
- A major release changes required structure or semantics.

Each released version is tagged independently as
`design-v<major>.<minor>.<patch>`. Release tags are immutable by project policy.
A permanent raw specification URL therefore has this form:

```text
https://raw.githubusercontent.com/pnw/trellis/design-v0.1.0/specs/design.md
```

---

## Appendix A. Minimal Design

```text
designs/
└── example-design/
    └── design.md
```

`design.md`:

```markdown
---
title: Example Design
type: design
description: Introduce a bounded example capability.
status: draft
timestamp: 2026-07-15T18:30:00Z
trellis_design_version: "0.1.0"
sources: []
related: []
tags: []
---

# Example Design

## Purpose

Introduce a small example capability with defined observable behavior.

## System Boundary

The capability is exposed through the system's existing public boundary.

## Core Model

The capability is one bounded behavior invoked through that boundary.

## Components

The existing public component owns the capability.

## Architecture

The existing public boundary remains the sole entry point.

## Workflow / Data Flow

A caller invokes the public boundary and receives the capability's result.

## Constraints / Invariants

- Existing callers remain compatible.

## Behavioral Statements (Acceptance Criteria)

- Existing callers continue to receive compatible responses.
- A valid invocation returns the new capability's result.

## Decisions

- Reuse the existing public boundary instead of adding another entry point.

## Evidence and Rationale

The existing boundary already owns adjacent public behavior.

## Open Design Questions

None.
```

This one file is a complete conforming dossier. Enhancements are added only
when their conditional contracts are useful.
