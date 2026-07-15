---
spec: design-surface
status: stable
updated: 2026-07-15
---

# The Design Surface: Dossiers

Agent-agnostic schema for the `designs/` surface. This file is part of the shared `schema/` layer referenced by `AGENTS.md`. It is normative and standalone; rationale lives in decision pages in the lab wiki, discovered by decision archaeology.

The design surface is **separate from the wiki** and governed by different rules. A wiki page is claim-shaped: its authority comes from evidence — sources, tiers, independence, derived confidence. A design is commitment-shaped: its authority comes from lifecycle state — what has been ratified, what is being built, what shipped. No amount of citation makes a design "more true," and no design carries the wiki's epistemic machinery (`evidence`, `confidence`, `novelty`).

**Question a design answers:** What are we building (or what did we build), and where is it in being built?

**Instigation:** user-instigated. Agents draft and propose designs in conversation; they do not create dossiers unprompted.

## The Dossier

Each design is a **dossier**: a directory containing everything the design needs, compartmentalized. Containment is the organizing principle — a file's role comes from its position in the dossier, not from a type field.

```
designs/
  index.md                     # catalog: one line per dossier
  {design-slug}/
    design.md                  # REQUIRED — the design document itself
    alternatives/              # optional — a fan-out of candidate variants
      {variant-slug}.md        #   each with the same scope and framing as design.md
      weighing.md              #   the analysis across variants: trade-offs, costs,
                               #   implications, obligations, blast radius
    ...                        # optional supporting assets (diagrams, data, notes)
```

- `design.md` is the design. It is the only file in the dossier outside artifacts may point at.
- `alternatives/` holds candidate variants during (or after) a design fan-out. A design need not start with alternatives, and alternatives may be added after the design exists; when a fan-out precedes convergence, the initial idea is simply the first alternative, and the variant that wins graduates by becoming (or being merged into) `design.md`. `weighing.md` is the adjudication document — it is disposable analysis that supports the choice, not durable comparative knowledge.
- Everything inside a dossier other than `design.md` is workspace: mutable, reorganizable, and never a link target from outside the dossier.

## `design.md` Format

```yaml
---
title: Design Title                            # REQUIRED
description: One-sentence summary.             # REQUIRED
status: draft | active | implemented | superseded | abandoned   # REQUIRED — lifecycle state
created: YYYY-MM-DD                            # REQUIRED
timestamp: YYYY-MM-DDTHH:MM:SSZ                # REQUIRED — last meaningful change
sources: []                                    # Optional — grounding (wiki pages, captures, chats, URLs)
related: []                                    # Optional — graph edges (wiki pages or dossier roots)
tags: []                                       # Optional
---
```

No `type`, `evidence`, `confidence`, or `novelty` — those are wiki-surface fields and are errors here. Alternatives and `weighing.md` carry the same frontmatter minus `status` (optional on them; a dead variant may be marked `abandoned`).

**Expected sections** (adapt to the design; breadcrumbs, not rails):

- Purpose
- System Boundary
- Core Model
- Components
- Workflow / Data Flow
- Constraints / Invariants (constraints the design imposes; standing repo-wide rules still belong to wiki `invariant` pages)
- Obligations (downstream implications and deferred follow-ons this design creates but does not resolve)
- Evidence and Rationale (grounding links into the wiki)
- Open Design Questions

## Lifecycle

`status` is the design's governing axis:

| State | Meaning |
|-------|---------|
| `draft` | Being explored; not ratified. Fan-outs usually happen here. |
| `active` | Ratified and operative: guiding an ongoing build, or itself the protocol agents execute. |
| `implemented` | Terminal. The artifact shipped; the document **changes tense** — it freezes as the historical record of intent-as-built. |
| `superseded` | Terminal. Replaced; name the successor (a newer dossier or a decision). |
| `abandoned` | Terminal. Dropped without shipping; keep the record. |

A design does not die into anything. At a terminal state it becomes history: authoritative about what was designed and why, never about what the system currently is. Do not maintain an `implemented` design as living documentation of the shipped artifact — the artifact documents itself, and drift between the two is read against the document. Post-terminal evolution is a new design or a decision, not an edit that changes the frozen record's meaning (timestamp-touching fixes to links or typos are fine).

## Linking Rules

- Design files may link freely: to wiki pages (`[[wiki/...]]`), to other dossier roots (`[[designs/other-slug]]`), within their own dossier by full path (`[[designs/slug/alternatives/variant]]`), and to peers (`peer::...`).
- A link target of `[[designs/{slug}]]` (the dossier root) resolves to that dossier's `design.md`.
- **Wiki pages link only to dossier roots**, never into dossier internals — internals are mutable workspace and make fragile targets. This is the reference-direction rule: designs consume wiki knowledge freely; wiki references into the design surface are sparing and root-only.
- Filenames are kebab-case; wikilinks are repository-root-relative, as everywhere in the repo.

## Index and Moves

- `designs/index.md` is the surface's catalog: one line per dossier — `* [[designs/{slug}]] — description (status)`. Update it when dossiers are created, change status, or are removed.
- Renaming or deleting a **dossier root** gets a `wiki/moves.log` line like any wiki or raw move — dossier roots are the surface's stable addresses. Churn inside a dossier (adding, renaming, or pruning alternatives and assets) is workspace activity and is not logged.

## Relationship to the Wiki

Defined minimally, by intent:

- Designs cite wiki pages as grounding; the wiki is the design surface's evidence library.
- Knowledge produced during design work that outlives the design (research findings, benchmarks, discovered constraints) belongs in the wiki via the normal ingest/promotion machinery — a dossier must not become a knowledge trap.
- A choice among alternatives whose rationale has lasting value is still recorded as a wiki `decision` page; the dossier's `weighing.md` is the working analysis behind it, not its replacement.
- Whether and how a completed design's content graduates into the wiki is **deliberately undefined** — no workflow exists yet. Do not invent one ad hoc; proposals go through a schema change.
