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
3. Add phases, deferred scope, external obligations, and alternatives only
   when they provide value.
4. Give each optional artifact an explicit type and contract.
5. Preserve the historical meaning of completed or abandoned designs.
6. Remain readable, diffable, portable, and strictly OKF-conformant.

### 1.2 Non-goals

- Prescribing how a design is proposed, approved, staffed, or implemented.
- Requiring phasing, roadmapping, alternatives, or external obligations.
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
- **Obligation** — Work the design induces outside its own target boundary.
- **Alternative** — One candidate approach to a shared design question.
- **Evaluation** — The comparison and current judgment across alternatives.
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
    ├── obligations.md             # OPTIONAL — type: obligations
    ├── alternatives/              # OPTIONAL AS A UNIT
    │   ├── <candidate-a>.md        # at least two — type: alternative
    │   ├── <candidate-b>.md
    │   └── evaluation.md          # required — type: evaluation
    └── <supporting-assets>         # OPTIONAL
```

The dossier slug and all Markdown filenames MUST use lowercase kebab-case.
Numbered phases use `phase-<n>.md` without zero padding.

`design.md` is the only universally required file. The existence of an
optional enhancement activates that enhancement's complete structural contract
in Sections 6–8.

A collection of dossiers MAY provide an OKF `index.md`, but the collection
index is not part of an individual dossier's conformance.

---

## 4. Document Model

Every Markdown file in a dossier is an OKF concept document. It MUST be UTF-8
Markdown beginning with parseable YAML frontmatter and a non-empty `type`.

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

The following fields are optional on any dossier document:

```yaml
sources: []
related: []
tags: []
```

Values in `sources` and `related` are repository-relative paths or absolute
URLs. Unknown fields MAY be added. Consumers MUST preserve unknown fields when
round-tripping and tolerate unknown OKF types.

The standard dossier vocabulary is:

| File | Required type |
|---|---|
| `design.md` | `design` |
| `phases/phase-<n>.md` | `phase` |
| `phases/later.md` | `roadmap` |
| `obligations.md` | `obligations` |
| `alternatives/<candidate>.md` | `alternative` |
| `alternatives/evaluation.md` | `evaluation` |

Non-Markdown supporting assets need no frontmatter. A non-standard Markdown
asset MUST declare an extension type beginning with `x-` and remain readable as
a generic OKF concept.

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
---
```

The body MUST contain these exact second-level headings, in this order:

1. `## Motivation`
2. `## Goals`
3. `## Non-goals`
4. `## Terminology`
5. `## Design`
6. `## Constraints`
7. `## Open Questions`

Sections remain present when empty and state `None.`. The Design section MAY
use any lower-level headings needed to specify boundaries, components,
interfaces, data flows, state transitions, error behavior, or examples.

The target MUST be complete without reading phases, obligations, alternatives,
or their evaluation. It MUST describe desired behavior and constraints rather
than an implementation sequence.

### 5.1 Lifecycle

`status` is the design's governing state:

| Status | Meaning |
|---|---|
| `draft` | The target is being developed and is not yet operative. |
| `active` | The target is ratified and guides current work. |
| `implemented` | Terminal. The target was delivered. |
| `superseded` | Terminal. Another design replaced this target. |
| `abandoned` | Terminal. The target was dropped without delivery. |

A live design MAY change meaning. A terminal dossier is a historical record:
substantive evolution requires a successor design. Corrections that do not
change meaning, such as fixing a typo or broken link, remain allowed and update
the timestamp.

A terminal design describes what was intended and why. It is not maintained as
live documentation of the implemented system.

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

Required frontmatter:

```yaml
---
title: Phase 1
type: phase
description: The bounded implementation scope for this phase.
status: pending | in-progress | complete
timestamp: 2026-07-15T18:30:00Z
---
```

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

`later.md` is a current remainder, not an append-only journal.

---

## 7. Obligations Enhancement

`obligations.md` is optional. It records work required outside the target's own
boundary as a consequence of completing the design. It does not contain target
scope and does not participate in phase coverage.

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
affected system, triggering design scope, required outcome, and completion
condition.

---

## 8. Alternatives Enhancement

The `alternatives/` directory is optional. When it exists, it MUST contain:

1. at least two candidate documents of type `alternative`; and
2. `evaluation.md` of type `evaluation`.

All candidates MUST address the same design question and enough common criteria
to permit direct evaluation.

### 8.1 Alternative

Required frontmatter:

```yaml
---
title: Candidate Name
type: alternative
description: One-sentence summary of this candidate.
timestamp: 2026-07-15T18:30:00Z
---
```

The body MUST contain these exact second-level headings:

1. `## Summary`
2. `## Design`
3. `## Strengths`
4. `## Costs and Risks`
5. `## Consequences`

An alternative is a candidate only. It has no authority over `design.md`.

### 8.2 Evaluation

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

Judgment MUST state the present conclusion. `Unresolved` is a valid conclusion
when the available information does not support a recommendation. Requiring an
evaluation prevents a directory of candidates from being mistaken for equally
operative designs.

An evaluated candidate becomes authoritative only when its accepted content is
represented in `design.md`.

---

## 9. Links

All internal links MUST use standard Markdown syntax with paths relative to the
current document:

```markdown
See the [first phase](phases/phase-1.md).
```

Absolute URLs identify external resources. Custom wikilink syntax such as
`[[target]]` is not part of Trellis Design.

A producer MUST maintain resolvable internal links. An OKF consumer MUST still
tolerate a broken link and render the remaining document.

---

## 10. Producer and Consumer Behavior

A producer:

- MUST keep `design.md` complete and authoritative;
- MUST apply each standard artifact's structural type and body contract;
- MUST satisfy the complete conditional contract of any enhancement present;
- MUST update timestamps after meaningful changes;
- MUST use successor dossiers for substantive post-terminal evolution;
- SHOULD keep optional artifacts only while they provide useful information.

A consumer:

- MUST read ordinary Markdown and parse YAML frontmatter;
- MUST treat `design.md` as the target specification;
- MUST treat phases as implementation scope, not target overrides;
- MUST treat alternatives as candidates and evaluation as judgment;
- MUST tolerate unknown fields and extension types;
- SHOULD preserve unknown metadata when editing or round-tripping documents.

---

## 11. Conformance

A dossier conforms to Trellis Design 0.1 when:

1. It conforms to OKF 0.1.
2. It contains `design.md` with the required metadata and exact body sections.
3. `design.md` declares `trellis_design_version: "0.1.0"`.
4. Every Markdown file has parseable YAML frontmatter and a non-empty type.
5. Every standard artifact's path, type, metadata, and body agree.
6. If `phases/` exists, it contains numbered phases and `later.md`, and their
   combined coverage includes the complete target.
7. If `obligations.md` exists, it follows the obligations contract.
8. If `alternatives/` exists, it contains at least two candidates and a complete
   evaluation.
9. Every internal Markdown link resolves.

A document may be valid OKF without being Trellis Design-conformant. Consumers
MUST distinguish validation from readability.

---

## 12. Versioning

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
---

# Example Design

## Motivation

The project needs a small example capability.

## Goals

- Define the capability's observable behavior.

## Non-goals

- Prescribe implementation sequencing.

## Terminology

- **Capability** — The behavior introduced by this design.

## Design

The system exposes the capability through its existing public boundary.

## Constraints

- Existing callers remain compatible.

## Open Questions

None.
```

This one file is a complete conforming dossier. Enhancements are added only
when their conditional contracts are useful.
