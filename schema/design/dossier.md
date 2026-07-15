---
spec: design-surface
status: stable
updated: 2026-07-15
---

# The Design Surface: Dossiers

Agent-agnostic schema for the `designs/` surface. This file is part of the shared `schema/` layer referenced by `AGENTS.md`. It is normative and standalone; rationale lives in decision pages in the lab wiki, discovered by decision archaeology.

The design surface is **separate from the wiki** and governed by different rules. A wiki page is claim-shaped: its authority comes from evidence — sources, tiers, independence, derived confidence. A design is commitment-shaped: its authority comes from lifecycle state — what has been ratified, what is being built, what shipped. No amount of citation makes a design "more true," and no design carries the wiki's epistemic machinery (`evidence`, `confidence`, `novelty`).

The surface carries its **own type vocabulary**, scoped to dossiers (see The Dossier Type System below). Pages have designed types on every surface: a design file declares what it is in frontmatter rather than leaving its role to be inferred from its path. Wiki types are never valid here, and dossier types are never valid on wiki pages.

**Question a design answers:** What are we building (or what did we build), and where is it in being built?

**Instigation:** user-instigated. Agents draft and propose designs in conversation; they do not create dossiers unprompted.

## The Dossier

Each design is a **dossier**: a directory containing everything the design needs, compartmentalized. Containment organizes the dossier — standard names fix where each concern lives — and every standard file also *declares* its role with a dossier-scoped `type`: position and type must agree, and lint checks the agreement.

```
designs/
  index.md                     # catalog: one line per dossier
  {design-slug}/
    design.md                  # REQUIRED — the target specification (type: design)
    phases/
      phase-1.md               # REQUIRED* — first implementation scope (type: phase)
      phase-2.md …             # optional — further scoped phases, only if deliberately roadmapped
      later.md                 # REQUIRED* — deferred design scope not claimed by any phase (type: roadmap)
    obligations.md             # REQUIRED* — work the design imposes outside its boundary (type: roadmap)
    alternatives/              # optional — a fan-out of candidate variants
      {variant-slug}.md        #   each with the same scope and framing as design.md (type: alternative)
      weighing.md              #   the analysis across variants: trade-offs, costs,
                               #   implications, blast radius (type: weighing)
    ...                        # optional supporting assets (diagrams, data, notes) — untyped workspace
```

\* Required while the dossier is **live** (`draft` or `active`). Terminal dossiers are frozen records and keep whatever skeleton they have — the freeze rule forbids adding files to them (see Lifecycle).

**`phases/` contains a complete partition of the design's scope: phase-1 + phase-N + later = everything in `design.md`.** That equation is the verifiable target — every part of the target specification is claimed by exactly one phase file or falls to `later.md`, nothing is scoped twice, and nothing is lost. `later.md` is the remainder that closes the partition.

**Every standard file is required on a live dossier — an empty concern is stated, never inferred.** A missing file is always ambiguous between "nothing there" and "nobody wrote it," so each standard file exists even when its concern is empty: an unphased design's `phase-1.md` states that phase 1 implements the design in full; a fully-phased design's `later.md` states that the phase files cover the design; a design imposing no external obligations says so in `obligations.md`. Only further `phase-N.md` files are optional, because `later.md` already accounts for everything they would claim. `alternatives/` is likewise exempt from this rule: its absence is itself the information — no fan-out occurred.

- **`design.md`** (`type: design`) is the design: the standalone target specification, complete in itself, and the only file in the dossier outside artifacts may point at. Phase scoping, sequencing, and "do this first" content do not belong in it.
- **`phases/phase-1.md`** (`type: phase`) captures the first implementation scope — the slice usually most necessary to understand in design iterations. This is where implementation gets specific: which existing abstractions and interfaces are boundaries not to be touched, what will have been implemented against the design when the phase ends. An unphased design's `phase-1.md` simply states that phase 1 implements the design in full — so "no phases" and "forgot the phases" are distinguishable by construction. Phases are numbered without zero-padding (`phase-1`, `phase-2`, … `phase-10`); a design with enough phases for sort order to matter is a smell `later.md` exists to prevent.
- **`phases/later.md`** (`type: roadmap`) is the grab bag of deferred design scope: everything in `design.md` not claimed by a phase file. Its existence removes any obligation to scope or roadmap subsequent phases up front — deliberate phasing stays available, never required.
- **`obligations.md`** (`type: roadmap`) captures what the design's *completion* obligates of the rest of the system: work out of the design's own scope but which the design requires, due on completion of one or more phases. It is non-phased and lives outside `phases/` because it is not part of the design's scope partition — it is induced external work. The name states the species (obligations induced on other systems), not the genus (any "follow-up"), so it is not confused with `later.md`'s deferred design scope.
- **`later.md` and `obligations.md` are scoped roadmaps**, not append-only lists: pruned as items resolve or graduate into phase files, never accumulated. An item leaves when it is implemented, absorbed into a phase, or deliberately dropped. A roadmap file that only grows is being used as a journal — that is the failure mode to watch.
- `alternatives/` holds candidate variants during (or after) a design fan-out. A design need not start with alternatives, and alternatives may be added after the design exists; when a fan-out precedes convergence, the initial idea is simply the first alternative, and the variant that wins graduates by becoming (or being merged into) `design.md`. `weighing.md` is the adjudication document — it is disposable analysis that supports the choice, not durable comparative knowledge.
- Everything inside a dossier other than `design.md` is workspace: mutable, reorganizable, and never a link target from outside the dossier. Non-standard supporting assets are untyped and outside the skeleton; content that deserves a type belongs in a standard file or an ordinary wiki page.

## The Dossier Type System

Dossier files carry a `type` from the surface's own vocabulary, defined here and only here:

| Type | File(s) | Role |
|------|---------|------|
| `design` | `design.md` | The target specification — the dossier's document of record |
| `phase` | `phases/phase-{n}.md` | One implementation scope against the design |
| `roadmap` | `phases/later.md`, `obligations.md` | A pruned, forward-looking backlog scoped to this design |
| `alternative` | `alternatives/{variant-slug}.md` | One candidate variant in a fan-out |
| `weighing` | `alternatives/weighing.md` | The adjudication analysis across variants |

The vocabulary is scoped to the design surface: these types are never valid on wiki pages, wiki types are never valid here, and the wiki's registry does not list them — the surface boundary is the namespace. The skeleton determines which type each standard file must declare; a mismatch is a lint error. This is deliberate redundancy, not ceremony: the path fixes *where* a role lives, the declared type makes the file self-describing to any consumer that reads content without paths (OKF-style interop, search snippets, future tooling).

## `design.md` Format

```yaml
---
title: Design Title                            # REQUIRED
type: design                                   # REQUIRED — dossier type (see The Dossier Type System)
description: One-sentence summary.             # REQUIRED
status: draft | active | implemented | superseded | abandoned   # REQUIRED — lifecycle state
created: YYYY-MM-DD                            # REQUIRED
timestamp: YYYY-MM-DDTHH:MM:SSZ                # REQUIRED — last meaningful change
sources: []                                    # Optional — grounding (wiki pages, captures, chats, URLs)
related: []                                    # Optional — graph edges (wiki pages or dossier roots)
tags: []                                       # Optional
---
```

Subsidiary standard files carry the same shape with their slot's type: required `title`, `type`, `description`, `created`, `timestamp`; `sources` optional (a subsidiary's provenance is its design). `status` is required only on `design.md`; on `phase` pages an optional `status: pending | in-progress | complete` records phase state; on alternatives an optional lifecycle `status` may mark a dead variant `abandoned`.

No `evidence`, `confidence`, `novelty`, or `enforcement` anywhere on the design surface — those are wiki-surface epistemic fields and are errors here. A design file's `type` must come from the dossier vocabulary above; wiki types are equally errors.

**Expected sections** (adapt to the design; breadcrumbs, not rails):

- Purpose
- System Boundary
- Core Model
- Components
- Workflow / Data Flow
- Constraints / Invariants (constraints the design imposes; standing repo-wide rules still belong to wiki `invariant` pages)
- Evidence and Rationale (grounding links into the wiki)
- Open Design Questions

There is no Obligations section: obligations are a standard file (`obligations.md`), not spec content — the specification stays a pure statement of the target state. Likewise, phasing and sequencing live in `phases/`, never in `design.md`.

## Lifecycle

`status` is the design's governing axis:

| State | Meaning |
|-------|---------|
| `draft` | Being explored; not ratified. Fan-outs usually happen here. |
| `active` | Ratified and operative: guiding an ongoing build, or itself the protocol agents execute. |
| `implemented` | Terminal. The artifact shipped; the document **changes tense** — it freezes as the historical record of intent-as-built. |
| `superseded` | Terminal. Replaced; name the successor (a newer dossier or a decision). |
| `abandoned` | Terminal. Dropped without shipping; keep the record. |

While a dossier is live, phase files scope implementation against `design.md`: when a phase completes, move its unfinished remainder to `phases/later.md` or a successor phase, and prune `later.md`/`obligations.md` as items resolve.

A design does not die into anything. At a terminal state it becomes history: the **whole dossier freezes** — `design.md` and every subsidiary document are retained exactly as they stand, as the record of what was specified and how implementation was phased against it. Do not delete phase documents at freeze, and do not add skeleton files to a frozen dossier (the live-only skeleton requirement exists precisely so freezing never forces backfill). A frozen design is authoritative about what was designed and why, never about what the system currently is — do not maintain an `implemented` design as living documentation of the shipped artifact; the artifact documents itself, and drift between the two is read against the document. Post-terminal evolution is a new design or a decision, not an edit that changes the frozen record's meaning (timestamp-touching fixes to links, typos, or schema-conformance metadata are fine).

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
