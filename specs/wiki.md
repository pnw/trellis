# Trellis Wiki Specification

Version 0.1.0 — Draft

Conforms to Open Knowledge Format (OKF) 0.1

Trellis Wiki is a human- and agent-readable format for maintaining durable,
typed knowledge from preserved sources. A wiki is a self-contained directory
of Markdown documents and raw source snapshots. Topic and type directories
make the corpus legible from the filesystem; YAML frontmatter makes every
knowledge document self-describing; citations preserve provenance.

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**,
and **MAY** express conformance requirements.

---

## 1. Motivation

Agent-maintained knowledge needs more structure than a folder of notes and less
infrastructure than a database or knowledge service. The format must remain:

- readable without special tooling;
- parseable without a bespoke SDK;
- diffable and versionable in Git;
- durable when external sources disappear or change;
- explicit about the role, provenance, and epistemic status of each document;
- navigable by both people and agents through ordinary files and links.

### 1.1 Goals

1. Define a portable, OKF-conformant wiki bundle.
2. Preserve the source material behind substantive claims.
3. Define a small vocabulary of typed knowledge documents with distinct
   structures and semantics.
4. Separate source reliability from claim-level judgment.
5. Support progressive synthesis without requiring a database, server, or
   search service.
6. Define enough structure for deterministic conformance checks while leaving
   interpretation to authors and reviewers.

### 1.2 Non-goals

- Prescribing how an agent acquires, ingests, queries, or maintains a wiki.
- Prescribing orchestration, approval, or multi-agent workflows.
- Requiring a search engine, vector store, graph database, or hosted service.
- Defining project planning or implementation artifacts.
- Replacing Git history, source-control review, or domain-specific schemas.

---

## 2. Terminology

- **Wiki bundle** — The `wiki/` directory as a self-contained unit of
  distribution.
- **Topic** — A broad subject directory directly under `wiki/`. A topic groups
  documents by subject before grouping them by type.
- **Subtopic** — An optional narrower subject under a topic's `subtopics/`
  directory.
- **Typed page** — A Markdown knowledge document whose `type` frontmatter
  determines its role and required structure.
- **Raw source** — An immutable snapshot of material from outside the derived
  wiki: an article, paper, chat, repository extract, dataset, or other input.
- **Source capture** — A source-isolated account of what one raw source
  contributes, including a within-source reliability judgment.
- **Interpretive page** — A construct, entity, synthesis, assessment, or
  comparison derived from one or more source captures.
- **Normative page** — A decision or invariant asserted by the wiki's owner or
  project rather than inferred from evidence.
- **Evidence** — The reliability class of one source, recorded on its source
  capture.
- **Confidence** — A derived judgment about support for a construct or entity,
  based on cited evidence and source independence.
- **Novelty** — A judgment about how established the name or framing of a
  construct or entity is.
- **Resource** — A URL, repository-relative path, or other stable identifier
  naming the origin of a raw source.

---

## 3. Bundle Structure

A conforming bundle uses this structure:

```text
wiki/
├── index.md                         # REQUIRED — OKF directory index
├── overview.md                      # REQUIRED — wiki front door
├── raw/                             # REQUIRED — immutable source snapshots
│   ├── articles/
│   ├── papers/
│   ├── chats/
│   ├── repos/
│   └── data/
└── <topic>/
    ├── sources/
    ├── constructs/
    ├── entities/
    ├── syntheses/
    ├── assessments/
    ├── comparisons/
    ├── decisions/
    ├── invariants/
    └── subtopics/
        └── <subtopic>/
            └── <type-directory>/
```

Only directories needed by the bundle need to exist. `wiki/`, `raw/`,
`index.md`, and `overview.md` are always required.

Topics MUST be organized first by subject and then by type. A page's directory
and frontmatter type MUST agree according to Section 6. Subtopics MAY nest when
that materially improves navigation, but producers SHOULD keep the hierarchy
shallow.

Filenames MUST use lowercase kebab-case and the `.md` extension. Raw sources
MAY retain an extension appropriate to their media type.

### 3.1 Reserved filenames

Trellis adopts the OKF reserved filenames:

| Filename | Meaning |
|---|---|
| `index.md` | Directory index for progressive disclosure. |
| `log.md` | Optional chronological update log. |

The root `index.md` is required. Additional `index.md` files and any `log.md`
files are optional. When present, they MUST follow Sections 8 and 9.

`overview.md` is a Trellis typed page, not an OKF reserved file.

---

## 4. Document Model

Every Markdown file in the bundle other than `index.md` and `log.md` is an OKF
concept document. It MUST be UTF-8 Markdown beginning with parseable YAML
frontmatter and a non-empty `type`.

Every topic page uses these common fields:

```yaml
---
title: Human-readable title
type: <Trellis page type>
description: One sentence describing the page.
sources:
  - ../../sources/example-source.md
  - https://example.com/external-source
timestamp: 2026-07-15T18:30:00Z
tags: [subject, concern]
---
```

| Field | Requirement |
|---|---|
| `title` | REQUIRED. Human-readable display name. |
| `type` | REQUIRED. One of the Trellis types in Section 6 or a registered extension type. |
| `description` | REQUIRED. One-sentence summary used for indexes, search, and previews. |
| `sources` | REQUIRED. YAML list of repository-relative paths or absolute URLs grounding the page. It MAY be empty only when the page is explicitly self-authored and has no external grounding. |
| `timestamp` | REQUIRED. ISO 8601 datetime of the last meaningful content change. |
| `tags` | REQUIRED on every page inside a topic or subtopic. YAML list of subject and concern labels; it MAY be empty. |

Paths in `sources` and `related` frontmatter are plain paths or URLs, not
Markdown links. Links in page bodies use standard Markdown syntax.

Tags describe subject matter and cross-cutting concerns. They MUST NOT repeat a
page's `type` merely to classify the document and SHOULD NOT mechanically repeat
its directory path. A tag should remain meaningful when viewed without the
page's location.

Unknown frontmatter fields MAY be added. Consumers MUST preserve unknown fields
when round-tripping and MUST tolerate unknown OKF types, even when those
documents do not satisfy Trellis-specific conformance.

### 4.1 Overview

`wiki/overview.md` is the required front door to the bundle:

```yaml
---
title: Wiki Overview
type: overview
description: Purpose, scope, and navigation for this wiki.
sources: []
timestamp: 2026-07-15T18:30:00Z
---
```

It MUST contain these exact second-level headings:

1. `## Purpose`
2. `## Scope`
3. `## Navigation`
4. `## Current Understanding`

The Purpose section MUST state one governing goal for the wiki. Scope defines
what serves that goal and what belongs elsewhere. The overview is a living
front door, not a substitute for topic syntheses.

---

## 5. Raw Sources and Provenance

`wiki/raw/` contains immutable source snapshots. A raw file MUST NOT be edited
in place after capture. If the external resource changes, the producer creates
a new snapshot so the two versions can be compared directly.

Binary and non-Markdown sources retain their original format and require no
frontmatter. A Markdown raw source MUST begin with this minimal envelope:

```yaml
---
type: raw-source
resource: https://example.com/original
timestamp: 2026-07-15T18:30:00Z
---
```

| Field | Requirement |
|---|---|
| `type` | REQUIRED. Exactly `raw-source`. |
| `resource` | REQUIRED. URL, repository-relative path, or stable identifier for the source's origin. |
| `timestamp` | REQUIRED. ISO 8601 datetime when this snapshot was captured. |

The source body follows the envelope unchanged. The envelope is acquisition
metadata and is not part of the original source body.

Every source capture MUST cite at least one file under `wiki/raw/`. Derived
topic pages normally cite source captures. Direct raw citations remain valid
when no capture exists yet.

Every factual claim, data point, or attributed finding in a page body MUST
include a standard Markdown link to the supporting capture, raw source, or
external resource.

---

## 6. Page Types

The standard vocabulary is:

```text
overview | raw-source | source-capture | construct | entity | synthesis |
assessment | comparison | decision | invariant
```

`overview` and `raw-source` use the special locations and formats in Sections
4.1 and 5. All other types live under a topic or subtopic.

| Type | Directory | Primary question |
|---|---|---|
| `source-capture` | `sources/` | What does this source contribute? |
| `construct` | `constructs/` | What reusable abstraction is this? |
| `entity` | `entities/` | Who or what is this named thing? |
| `synthesis` | `syntheses/` | What do we currently understand about this area? |
| `assessment` | `assessments/` | What is validated, uncertain, risky, contradicted, or unknown? |
| `comparison` | `comparisons/` | How do these things differ, and when does each fit? |
| `decision` | `decisions/` | What choice was made among alternatives, and why? |
| `invariant` | `invariants/` | What must continue to hold, and what would removing it take? |

A page that strongly answers more than one primary question SHOULD be split.

### 6.1 `source-capture`

A source capture reports one raw source without importing or reconciling claims
from the rest of the wiki. This **source isolation** keeps the capture
regenerable, prevents circular corroboration, and separates faithful reportage
from later synthesis.

Additional frontmatter:

```yaml
evidence: empirical-primary | empirical-secondary | official-docs | expert-analysis | vendor-claim | llm-generated
```

`evidence` is REQUIRED. `related` MAY contain navigational pointers to affected
or adjacent pages; source isolation is epistemic, not navigational.
`confidence`, `novelty`, and `status` MUST NOT appear.

Evidence values:

| Value | Meaning |
|---|---|
| `empirical-primary` | Original systematic data collection with reported methodology. |
| `empirical-secondary` | Systematic aggregation of others' data, such as a review or meta-analysis. |
| `official-docs` | Authoritative documentation, specification, or standard. |
| `expert-analysis` | Reasoned expert or practitioner analysis without systematic data. |
| `vendor-claim` | Commercially motivated product or marketing material. |
| `llm-generated` | Model-authored research, synthesis, or conversation. |

The value rates the source in isolation. Within-source signals such as
methodology transparency, sample size, conflicts of interest, firsthand versus
relayed claims, and internal consistency may justify a weaker tier. Reliability
Notes records the justification for any downward adjustment.

The body MUST contain these exact second-level headings, in this order:

1. `## Source Identity`
2. `## Core Contribution`
3. `## Key Claims`
4. `## Evidence and Results`
5. `## Methodology`
6. `## Limitations and Caveats`
7. `## Reliability Notes`
8. `## Important References and Linked Material`
9. `## Contribution Routing`
10. `## Extraction Notes`

An inapplicable section states `Not applicable.` rather than being omitted.
Core Contribution through Methodology are faithful reportage. Limitations and
Caveats, Reliability Notes, Contribution Routing, and Extraction Notes are the
capturer's bounded assessment and routing observations.

Important References and Linked Material lists substantive works, tools,
repositories, primary sources, and related reading identified by the source.
Each entry SHOULD explain why the reference matters. Navigation, advertising,
share links, generic homepages, and unrelated author-profile links SHOULD be
excluded. Contribution Routing contains candidates for downstream review, not
commitments to create or update pages.

### 6.2 `construct`

A construct defines a reusable abstraction, mechanism, pattern, or named
intellectual building block. It is not a glossary entry and not a named person,
organization, tool, or system.

Additional required frontmatter:

```yaml
novelty: established | emerging | exploratory | coined
confidence: high | medium | low
status: draft | stable | deprecated
related: []
```

Optional construct metadata:

```yaml
aka: [alternative name]
coined_by: Person, group, or source
```

`aka` records alternative names for retrieval and disambiguation. `coined_by`
identifies the originator when known.

The body MUST address definition, significance, mechanism or structure,
distinctions from neighboring concepts, supporting evidence, and open questions
when any remain. Authors MAY adapt headings to the subject.

### 6.3 `entity`

An entity documents a named person, organization, project, tool, model,
repository, paper, dataset, standard, or system.

Additional required frontmatter:

```yaml
novelty: established | emerging | exploratory | coined
confidence: high | medium | low
status: draft | stable | deprecated
related: []
```

Optional entity metadata:

```yaml
aka: [alternative name, handle, or affiliation]
```

The body MUST address identity, relevance to the wiki, associated artifacts,
and material caveats. Authors MAY adapt headings to the subject.

### 6.4 Novelty

`novelty` is required only for constructs and entities:

| Value | Meaning |
|---|---|
| `established` | Longstanding literature, existence, or broad adoption. |
| `emerging` | Actively forming or growing across multiple sources. |
| `exploratory` | Early, limited, or one of several unsettled framings. |
| `coined` | Originated in this wiki's sources with no known external use. |

Novelty rates the name or framing, not the credibility of the page's claims.

### 6.5 Confidence

`confidence` is required only for constructs and entities. It is derived from
the cited source captures and their independence:

| Value | Ceiling |
|---|---|
| `high` | At least two independent sources, at least one empirical, with no uncontested contradiction in the wiki. |
| `medium` | One empirical source; multiple independent non-empirical sources; or official documentation corroborated independently. |
| `low` | One non-empirical source; only LLM-generated sources; or material claims contested in the wiki. |

Sources are independent only when they do not share authorship or commercial
interest and do not derive from one another. An LLM summary and the sources it
summarizes are not independent. Multiple documents from the same vendor about
that vendor's product count as one source for corroboration.

Wikis operated by the same owner and agents count as one source for independence
purposes. Moving or repeating a claim across repositories does not create
corroboration.

Official documentation may support a system-intent claim such as what a
product is designed to do, but it does not independently establish an
effectiveness claim. A construct or entity whose material claims are limited to
system intent MAY reach `medium` from the relevant official documentation alone.

An external resource without a source capture has no assigned evidence tier.
For confidence derivation it counts as at most `expert-analysis` until captured
and assessed. A producer MUST NOT infer a stronger tier from the URL or publisher
alone.

### 6.6 `synthesis`

A synthesis integrates source captures and other artifacts into the current
understanding of a topic. It is not a long construct definition or a sequence
of source summaries.

Additional required frontmatter:

```yaml
status: draft | stable | deprecated
related: []
```

The body MUST address the central question, current synthesis, supporting
evidence, tensions or contradictions, implications, related artifacts, and
conditions that should trigger an update. Authors MAY adapt headings.

A synthesis MUST NOT carry `confidence`; support and uncertainty belong in its
claim-level reasoning.

### 6.7 `assessment`

An assessment evaluates evidence, validation, risk, contradiction, gaps, or
uncertainty. It states a verdict rather than merely gathering information.

Additional required frontmatter:

```yaml
status: draft | stable | deprecated
related: []
```

The body MUST address scope, bottom line, what is validated, what is plausible
but unvalidated, what remains speculative, contradictions or risks, and missing
evidence. Authors MAY adapt headings.

An assessment MUST NOT carry `confidence`; its body is the structured judgment.

### 6.8 `comparison`

A comparison evaluates two or more concepts, entities, or approaches against a
shared question. It is not a broad topic synthesis.

Additional required frontmatter:

```yaml
status: draft | stable | deprecated
related: []
```

The body MUST address the comparison question, a summary, explicit comparison
criteria, selection guidance, failure modes, and related artifacts. Authors MAY
adapt headings.

A comparison MUST NOT carry `confidence`; differences in support belong beside
the claims or criteria they qualify.

### 6.9 `decision`

A decision records a point-in-time choice among alternatives. It is an event:
later reversal creates a new decision that supersedes the old one.

Additional required frontmatter:

```yaml
status: proposed | accepted | superseded
related: []
```

The body MUST contain these exact second-level headings, in this order:

1. `## Context`
2. `## Decision`
3. `## Alternatives Considered`
4. `## Consequences`
5. `## Invariants Established`

An empty Invariants Established section states `None.` Decisions MUST NOT carry
`evidence`, `confidence`, or `novelty`.

A decision records a specific choice and MUST NOT be edited into a different
choice. Reversal creates a new decision whose `related` list identifies the
superseded record. A superseding decision MUST identify every invariant
established by the earlier decision and state whether each is repealed,
re-grounded, or left standing. Superseding a decision does not silently retire
its invariants.

Use a decision when the choice and rejected alternatives have lasting value.
Do not use it as the target specification, as a standing constraint, or as an
assessment that reaches no choice.

### 6.10 `invariant`

An invariant declares a standing constraint that must continue to hold. It is
state, not the historical choice that established it.

Additional required frontmatter:

```yaml
status: proposed | active | retired
related: []
```

The body MUST contain these exact second-level headings, in this order:

1. `## Statement`
2. `## Scope`
3. `## Rationale`
4. `## Enforcement`
5. `## Violation Modes`
6. `## Removal Path`
7. `## Exceptions`

Enforcement describes the actual automated, manual, conventional, or external
mechanism keeping the constraint true. The Removal Path distinguishes deliberate
repeal from accidental violation. Invariants MUST NOT carry `evidence`,
`confidence`, `novelty`, or an `enforcement` frontmatter field.

An invariant MUST name a binding constraint, its scope, the cost or consequence
of violation, and a meaningful path to deliberate removal. Its origin is one of:

- **decided** — established by a decision, which the Removal Path links and
  inverts;
- **inherited** — imposed by an external or legacy boundary; or
- **discovered-and-ratified** — observed, examined, and deliberately accepted as
  binding.

A condition that merely happens to be true is not an invariant. A constraint
local to one design remains in that design unless it is cross-cutting,
independently referenceable, or requires its own removal analysis. A project
MUST NOT duplicate a governing specification rule as an invariant; it links to
the canonical rule instead. Retiring an invariant is a deliberate state change,
not an accidental breach.

### 6.11 Extension types

A producer MAY add extension types. An extension MUST:

1. use a name beginning with `x-`;
2. define its purpose, directory, required frontmatter, and body contract in a
   document reachable from the root index;
3. obey the common topic-page fields when it lives under a topic;
4. remain readable as a generic OKF concept to consumers that do not know it.

Official optional kits MAY register extension types using the same mechanism.

---

## 7. Links and Citations

All internal links MUST use standard Markdown links with paths relative to the
current document:

```markdown
See the [source isolation construct](../constructs/source-isolation.md).
```

Absolute URLs identify external resources and content in other repositories.
Custom wikilink syntax such as `[[target]]` is not part of Trellis Wiki.

The prose surrounding a link expresses the relationship; links are otherwise
untyped directed edges. Fragment links MAY target headings.

A Trellis producer MUST maintain resolvable internal links. An OKF consumer
MUST still tolerate broken links and render the remaining document.

---

## 8. Index Files

The root `wiki/index.md` is required and is the master knowledge catalog. It
MUST contain relative Markdown links with a short description for `overview.md`
and every typed topic page, grouped by topic, subtopic when present, and type.
Raw snapshots are reached through their source captures and need not be listed.

The root index declares conformance versions:

```yaml
---
okf_version: "0.1"
trellis_wiki_version: "0.1.0"
---
```

No other `index.md` may contain frontmatter. Directory indexes use ordinary
Markdown headings and lists:

```markdown
# Constructs

- [Source Isolation](constructs/source-isolation.md) — Keeps captures faithful
  to one source.
```

Entries SHOULD reproduce the target page's description. Producers MAY generate
indexes, but the committed index is part of the bundle.

---

## 9. Log Files

An optional `log.md` follows OKF's chronological log format:

```markdown
# Update Log

## 2026-07-15

- **Ingest**: Captured and routed a new source about retrieval.
```

Date headings MUST use `YYYY-MM-DD` and appear newest-first. Each entry MUST be
a bullet beginning with a bold operation label such as `**Ingest**`, `**Lint**`,
or `**Move**`. Logs carry no frontmatter and are not typed pages.

---

## 10. Producer and Consumer Behavior

A producer:

- MUST preserve raw snapshots and provenance;
- MUST apply the correct type contract and directory;
- MUST update timestamps after meaningful content changes;
- MUST keep the root index complete;
- MUST maintain internal links;
- MUST maintain inline provenance for factual claims, data, and attributed
  findings;
- MUST expose known material uncertainty and contradiction in the body of
  synthetic pages;
- SHOULD update existing pages instead of creating near-duplicates;
- SHOULD keep tags meaningful without repeating type or location mechanically.

A consumer:

- MUST read ordinary Markdown and parse YAML frontmatter;
- MUST tolerate unknown fields and types;
- MUST treat unknown types as generic OKF concepts;
- MUST tolerate missing optional directories and broken links;
- SHOULD begin discovery at the root index and overview;
- SHOULD preserve unknown metadata when editing or round-tripping documents.

---

## 11. Conformance

A bundle conforms to Trellis Wiki 0.1 when:

1. It conforms to OKF 0.1.
2. `index.md`, `overview.md`, and `raw/` exist at the bundle root.
3. The root index declares `okf_version: "0.1"` and
   `trellis_wiki_version: "0.1.0"`.
4. Every Markdown file other than `index.md` and `log.md` has parseable YAML
   frontmatter and a non-empty type.
5. Every topic page has the common required fields.
6. Every standard type follows its location, metadata, and body contract.
7. Every Markdown raw source follows the `raw-source` envelope.
8. Every source capture cites a raw source.
9. Every factual claim, data point, and attributed finding has an inline link to
   its support.
10. Every internal Markdown link resolves.
11. The root index catalogs the overview and every typed topic page.

A document may be valid OKF without being Trellis-conformant. Consumers MUST
distinguish validation from readability: failure of a Trellis rule does not make
the document unreadable.

---

## 12. Versioning

Trellis Wiki versions use semantic versioning:

- A patch release clarifies wording without changing conformance.
- A minor release adds backward-compatible optional fields, types, or guidance.
- A major release changes required structure or semantics.

Each released version is tagged independently as `wiki-v<major>.<minor>.<patch>`.
Release tags are immutable by project policy. A permanent raw specification URL
therefore has this form:

```text
https://raw.githubusercontent.com/pnw/trellis/wiki-v0.1.0/specs/wiki.md
```

---

## Appendix A. Minimal Bundle

```text
wiki/
├── index.md
├── overview.md
├── raw/
│   └── articles/
│       └── example-source.md
└── knowledge-management/
    └── sources/
        └── example-source.md
```

`overview.md`:

```markdown
---
title: Example Wiki
type: overview
description: Knowledge relevant to the example project.
sources: []
timestamp: 2026-07-15T18:30:00Z
---

# Example Wiki

## Purpose

Preserve and synthesize knowledge relevant to the example project.

## Scope

Project-relevant research and decisions.

## Navigation

Start with the [index](index.md).

## Current Understanding

The wiki is newly initialized.
```

`raw/articles/example-source.md`:

```markdown
---
type: raw-source
resource: https://example.com/article
timestamp: 2026-07-15T18:30:00Z
---

# Original Article

The preserved source body begins here.
```

`knowledge-management/sources/example-source.md` begins with:

```yaml
---
title: Example Source
type: source-capture
description: Captures the example article's contribution.
sources:
  - ../../raw/articles/example-source.md
timestamp: 2026-07-15T18:45:00Z
tags: [knowledge-management]
evidence: expert-analysis
---
```

Its body contains all ten required source-capture headings from Section 6.1.
