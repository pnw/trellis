# Wiki Page Format

Agent-agnostic schema for wiki page frontmatter. This file is part of the shared `schema/` layer referenced by `AGENTS.md`; tool-specific adapters (`.kiro/steering/`, `CLAUDE.md`) must reference it rather than duplicating it.

Every wiki page uses YAML frontmatter following this schema:

```yaml
---
title: Page Title                              # REQUIRED — human-readable display name
type: source-capture | construct | entity | synthesis | design | assessment | comparison | decision | invariant
description: One-sentence summary of this page.       # REQUIRED — used by index generators and agent navigation
sources:                                       # REQUIRED — provenance; wikilinks for vault files, URLs for external
  - "[[wiki/topic/sources/source-page]]"
  - https://example.com/external-source
related:                                       # Optional — explicit graph edges to other pages
  - "[[wiki/topic/constructs/related-page]]"
tags: [topic-a, topic-b]                       # Optional — cross-cutting categories for filtering
created: YYYY-MM-DD                            # REQUIRED — date page was first created
timestamp: YYYY-MM-DDTHH:MM:SSZ               # REQUIRED — ISO 8601 datetime of last meaningful change (OKF-compatible)
status: draft | stable | deprecated            # Optional — lifecycle status
# --- source-capture pages only ---
evidence: empirical-primary | empirical-secondary | official-docs | expert-analysis | vendor-claim | llm-generated  # REQUIRED — source reliability tier
# --- non-source pages only ---
confidence: high | medium | low                # Optional — claim credibility, derived from cited sources (see rules below)
# --- construct pages only ---
novelty: established | emerging | exploratory | coined  # How established this term/framing is
aka: ["alt name 1", "alt name 2"]              # Alternative names in the literature
coined_by: "Person or group"                   # Who originated the term
# --- entity pages only ---
novelty: established | emerging | exploratory | coined  # How established this entity is
aka: ["alt name 1", "alt name 2"]              # Alternative names, handles, affiliations
# --- invariant pages only ---
enforcement: automated | manual | convention | external | unenforced  # REQUIRED — how the constraint is guaranteed
---
```

## Required Fields

| Field | Purpose |
|-------|---------|
| `title` | Human-readable display name |
| `type` | Page kind — one of: `source-capture`, `construct`, `entity`, `synthesis`, `design`, `assessment`, `comparison`, `decision`, `invariant` |
| `description` | Single sentence summarizing the page (for index entries, search, progressive disclosure) |
| `sources` | Provenance — list of source references. Use repository-root wikilinks such as `[[wiki/topic/sources/source-page]]` for files in this vault; use URLs for external sources |
| `created` | Date page was first created (`YYYY-MM-DD`) |
| `timestamp` | ISO 8601 datetime of last meaningful change (`YYYY-MM-DDTHH:MM:SSZ`). OKF-compatible. |

## Epistemic Fields: Two Axes, Two Layers

The wiki separates **source reliability** from **claim credibility**, following the two-axis model used by the NATO/Admiralty grading system, ICD 203, and GRADE (see [[wiki/llm-wiki/syntheses/epistemic-metadata-frameworks]] and [[wiki/llm-wiki/designs/evidence-tier-schema]]):

- **`evidence`** (source-capture pages, REQUIRED) — a property of the source in isolation, assigned once at ingest.
- **`confidence`** (non-source pages, optional) — a property of the page's claims, derived from the evidence tiers and independence of its cited sources.

Source-capture pages must NOT carry `confidence`; non-source pages must NOT carry `evidence`.

**Normative types (`decision`, `invariant`) are a special case.** They assert a choice or a rule rather than reporting evidence, so `confidence` (which rates evidence-derived credibility) is optional and usually omitted — a constraint you declare for your own project is not evidence-graded. Their required `sources` field still applies but names whatever *grounds* the choice or rule: a design page, a source-capture (when the constraint comes from a standard or paper), or the raw chat where it was decided. When a normative page's rationale *does* lean on empirical sources, `confidence` may be set by the usual rules to signal how well-founded that rationale is.

**Distinction: `decision` vs `invariant`.** A decision is an *event*; an invariant is *state*. Use `decision` (ADR) when recording *a specific choice made at a point in time* among alternatives; use `invariant` when declaring *a rule or constraint that must continually hold* in a system (e.g., "raw/ files are never edited in place" is an invariant; "we chose grep-based search over vector RAG" is a decision). A decision may *establish* an invariant, but they are distinct artifacts on different clocks: the decision record stays frozen as history, while the invariant outlasts it as the live register agents check work against — and the invariant's Removal Path is where repeal is analyzed (a decision-derived invariant links and inverts its establishing decision). Neither implies the other: many decisions impose no standing constraint, and invariants may be inherited or discovered-and-ratified rather than decided (see the origin taxonomy in `schema/page-types.md`).

### `evidence` Tiers (source-capture only)

Ordered strongest to weakest:

| Tier | Meaning |
|------|---------|
| `empirical-primary` | Original systematic data collection: RCTs, controlled experiments, mining studies, surveys, benchmarks with reported methodology |
| `empirical-secondary` | Systematic aggregation of others' data: SLRs, meta-analyses, research summaries |
| `official-docs` | Authoritative documentation, specifications, standards. Authoritative for what a system does or intends — not for effectiveness claims about itself |
| `expert-analysis` | Argumentation without systematic data: position papers, practitioner guides, experience reports, industry syntheses |
| `vendor-claim` | Commercially motivated product or marketing content |
| `llm-generated` | Model-authored research, syntheses, or design conversations (deep research reports, chat threads) |

The source *type* gives the starting tier; capture-time signals recorded in the source-capture's Reliability Notes section (methodology transparency, sample size, conflict of interest, firsthand vs relayed claims) may justify assigning a lower tier, GRADE-style. Record the adjusted tier in `evidence` and the justification in Reliability Notes.

### `confidence` Derivation Rules (non-source pages)

`confidence` is derived, not asserted. Ceiling rules:

- **`high`** — at least two *independent* cited sources, at least one at an empirical tier, and no uncontested contradicting evidence in the vault.
- **`medium`** — a single empirical source; or multiple independent non-empirical sources; or official docs corroborated by an independent source.
- **`low`** — a single non-empirical source; only `llm-generated` sources; or claims contested within the vault.

**Independence:** sources are independent only if they do not share authorship or commercial interest and do not derive from one another. Three vendor documents describing that vendor's own product are one source for corroboration purposes. Citing an LLM-generated synthesis alongside the sources it summarized is circular reporting, not corroboration. **Across federated wikis:** citing a peer wiki's source-capture imports its `evidence` tier at face value, but wikis operated by the same owner and agents count as one source for independence purposes — a claim does not gain corroboration by being cited across repos that share an operator.

Scoped claims: `official-docs` and `vendor-claim` sources are authoritative for design-intent claims about their own systems ("Blitzy generates an Agent Action Plan"), and weak for effectiveness claims ("this improves productivity"). Pages whose claims are purely design-intent may reach `medium` on such sources alone; effectiveness claims cannot.

## Other Optional Fields (All Types)

| Field | Purpose |
|-------|---------|
| `related` | Explicit relationship edges to other wiki pages (repository-root wikilinks) |
| `tags` | Cross-cutting categories for filtering and grouping |
| `status` | Lifecycle: `draft` (incomplete), `stable` (ready for use), `deprecated` (superseded) |

Freshness is tracked by `timestamp` plus lint staleness rules — there is no assertable freshness field. Usefulness is never asserted in frontmatter; it is revealed by inbound links and reuse (orphan detection in lint).

## Type-Specific Fields

### `construct` pages

| Field | Required | Purpose |
|-------|----------|---------|
| `novelty` | Yes | How established this term/framing is in the field. One of: `established` (3+ years of literature or broad industry adoption), `emerging` (actively being named/formalized by multiple groups, < 3 years), `exploratory` (idea exists under different names; this framing is one of several), `coined` (originated in this wiki's sources with no external usage) |
| `aka` | When applicable | Alternative names for the same concept in the literature. List of strings. |
| `coined_by` | When known | Person, group, or source that originated the term. String. |

### `design` pages

| Field | Required | Purpose |
|-------|----------|---------|
| `novelty` | Yes | How established this design pattern/architecture is. One of: `established` (3+ years of literature or broad industry adoption), `emerging` (actively being named/formalized by multiple groups, < 3 years), `exploratory` (design draws on known patterns but combines them in a novel way), `coined` (originated in this wiki's sources with no external precedent as a combined system) |

### `entity` pages

| Field | Required | Purpose |
|-------|----------|---------|
| `novelty` | Yes | How established this entity is. One of: `established` (3+ years of existence or broad industry adoption), `emerging` (actively growing, < 3 years old), `exploratory` (early-stage, limited adoption or pre-release), `coined` (originated in this wiki's sources with no external usage) |
| `aka` | When applicable | Alternative names, handles, or affiliations. |

### `invariant` pages

| Field | Required | Purpose |
|-------|----------|---------|
| `enforcement` | Yes | How the constraint is guaranteed. One of: `automated` (lint/CI/type-system checks it), `manual` (relies on a human or agent review step), `convention` (documented expectation only), `external` (enforced by something outside the project's control — vendor limits, network policy, regulation), `unenforced` (asserted, no mechanism yet). |

Invariant pages do not use `novelty` — an invariant is a constraint on a specific system, not a framing whose establishment in the field is at issue.

## Source Citation Rules

- `source-capture` pages cite raw files directly (e.g., `[[raw/articles/karpathy-llm-wiki-knowledge-base-guide.md]]`).
- Other descriptive page types (construct, entity, synthesis, design, assessment, comparison) normally cite source-capture pages (e.g., `[[wiki/llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide]]`).
- Normative pages (decision, invariant) may instead cite the design, capture, or chat that grounds them.
- Raw files may still be cited directly when no source-capture page exists yet.
- External URLs may be cited when no raw file exists. External URLs are un-tiered until captured; for confidence derivation, treat them as at most `expert-analysis` until a source-capture assigns a real tier.

## Inline Citation Rules

Every factual claim, data point, or referenced finding in the page body must link to its source. Do not leave parenthetical attributions (e.g., "(Dubey, 2026)") without a corresponding link.

**Acceptable link formats in body text:**

- Wikilink to source-capture page: `[[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]`
- Wikilink inline with context: `— [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]`
- External URL when no source-capture exists: `[Title](https://example.com/article)`

**Where inline citations appear:**

- "Evidence and Sources" sections (constructs)
- "Evidence and Rationale" sections (designs)
- "Supporting Evidence" sections (syntheses)
- "Validated" / "Plausible" / "Speculative" sections (assessments)
- Any bullet or paragraph making a specific factual claim elsewhere in the page

**Rule of thumb:** If you removed the link, could a reader find the source? If not, add a link.

## Tag Guidelines

Tags answer: "What is this page about?" — they should be meaningful on their own without knowing the file path.

**Principles:**

1. Tags describe subject matter and concerns, not document type or location.
2. Do not echo the `type` field — `source-capture`, `construct`, `comparison` are never tags.
3. Proper-noun concept tags are encouraged when they identify a specific idea that could appear across multiple directories (e.g., `llm-wiki`, `intent-compiler`, `okf`).
4. Tags are not blacklisted for matching a directory name — `llm-wiki` as a tag means "this page discusses the LLM Wiki concept," not "this file lives in the llm-wiki/ directory."
5. Do not automatically tag every page with its parent directory.
6. Tags should be independently meaningful.

**Good tag categories:**

- Domain/concept identifiers: `llm-wiki`, `intent-compiler`, `okf`, `rag`
- Concerns/capabilities: `cost-optimization`, `validation`, `knowledge-management`, `architecture`
- Techniques/methods: `prompting`, `compilation`, `curation`, `formatting`
- Subject matter: `comments`, `web-apis`, `coding-style`, `graphs`
- People (for entity pages): `people`

## YAML Syntax Rules

- **Colons in values must be quoted.** Any value containing `:` must be wrapped in double quotes (e.g., `title: "LLM Wiki: The Complete Guide"`).

## Notes

- `novelty` answers "how well-established is this *name and framing*?" — distinct from `confidence` which answers "how well-supported are the *claims* on this page?"
- A page can have `confidence: high` (well-sourced claims) but `novelty: coined` (the term itself is original to this wiki).
- `evidence` answers "how reliable is this *source*?" — a property of the source alone, assignable at ingest without reference to the rest of the vault, which is what keeps it compatible with source isolation (see [[wiki/llm-wiki/constructs/source-isolation]]).
- For design pages, certainty of evidence is distinct from strength of recommendation (GRADE's distinction): a design may carry `confidence: medium` yet strongly recommend action when the cost of acting is low. Express this in a one-line prose epistemic note in the body, not a new field.
- `invariant` pages are normative — a rule imposed on a system, not a claim about the world — so their `confidence` rates the empirical/argumentative support for the Rationale and Removal Path sections, not the rule itself. The `enforcement` field records the guarantee mechanism separately; whether the invariant actually holds is tested in assessments, not asserted in frontmatter.
- `aka` enables search and disambiguation.
