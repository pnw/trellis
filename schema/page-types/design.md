---
spec: page-type
type: design
tier: authored
instigators: [user]
status: stable
updated: 2026-07-14
---

# `design` Page Type

**Question answered:** How does this system or architecture work?

**Instigation:** authored tier — user-instigated (`schema/page-types/registry.md`, Instigator Tiers). Agents draft and propose designs in conversation; they do not create design pages unprompted.

**When to use:**
- Architecture descriptions, workflow designs, system models, implementation plans, process specifications, design docs.

**When NOT to use:**
- Not for reusable abstractions divorced from a specific system (use `construct`).
- Not for evaluating evidence or risk (use `assessment`).

**Location:** `wiki/{topic}/designs/{design-slug}/` or `wiki/{topic}/subtopics/{subtopic}/designs/{design-slug}/` — a design is a **directory**, not a single file (see Directory Form below). Legacy single-file designs (`designs/{design-slug}.md`) remain valid until converted.

**Expected sections** (in `design.md`):
- Purpose
- System Boundary
- Core Model
- Components
- Workflow / Data Flow
- Invariants
- Related Constructs
- Evidence and Rationale
- Open Design Questions

**Type-specific frontmatter:** `novelty`

## Directory Form

A design separates the **target specification** (what the future state is) from the **phasing of implementation against it** (what gets built when, and inside which existing boundaries). The directory holds the design page plus typed, skeleton-placed subsidiary pages under standard names, so any consumer knows where to look:

```
wiki/{topic}/designs/{design-slug}/
  design.md          # REQUIRED — the target specification (type: design)
  phases/
    phase-1.md       # REQUIRED — first implementation scope (type: design/phase)
    phase-2.md …     # optional — further scoped phases, only if deliberately roadmapped
    later.md         # REQUIRED — deferred design scope not claimed by any phase (type: roadmap)
  obligations.md     # REQUIRED — work the design imposes outside its boundary (type: roadmap)
```

**`phases/` contains a complete partition of the design's scope: phase-1 + phase-N + later = everything in `design.md`.** That equation is the verifiable target — every part of the target specification is claimed by exactly one phase file or falls to `later.md`, nothing is scoped twice, and nothing is lost. `later.md` is the remainder that closes the partition.

**Every standard file is required — an empty concern is stated, never inferred.** A missing file is always ambiguous between "nothing there" and "nobody wrote it," so each standard file exists even when its concern is empty: an unphased design's `phase-1.md` states that phase 1 implements the design in full; a fully-phased design's `later.md` states that the phase files cover the design; a design imposing no external obligations says so in `obligations.md`. Only further `phase-N.md` files are optional, because `later.md` already accounts for everything they would claim.

- **`design.md`** (`type: design`) is the standalone requirements document: the target future state, complete in itself. Phase scoping, sequencing, and "do this first" content do not belong in it.
- **`phases/phase-1.md`** (`type: design/phase`) captures the first implementation scope — the slice usually most necessary to understand in design iterations. This is where implementation gets specific: which existing abstractions and interfaces are boundaries not to be touched, what will have been implemented against the design when the phase ends. Every design directory has one, even when the design will be implemented in one go — an unphased design's `phase-1.md` simply states that phase 1 implements the design in full. This makes absence unambiguous: there is never a question of "no phases" versus "forgot the phases". Phase files are numbered without zero-padding (`phase-1`, `phase-2`, … `phase-10`); a design with enough phases for sort order to matter is a smell `later.md` exists to prevent.
- **`phases/later.md`** (`type: roadmap`) is the grab bag of deferred design scope: everything in `design.md` not claimed by a phase file — the remainder that closes the partition. Its existence removes any obligation to scope or roadmap subsequent phases up front; further `phase-N.md` files are allowed whenever the user wants to phase deliberately, never required.
- **`obligations.md`** (`type: roadmap`) captures what the design's *completion* obligates of the rest of the system: work out of the design's own scope but which the design requires, due on completion of one or more phases. It is non-phased and lives outside `phases/` because it is not part of the design's scope partition — it is induced external work. The name states the species (obligations induced on other systems), not the genus (any "follow-up"), so it is not confused with `later.md`'s deferred design scope.
- **`later.md` and `obligations.md` are scoped roadmaps** (`type: roadmap`), not append-only lists: localized instances of `wiki/roadmap.md`'s dynamics, pruned as items resolve or graduate into phase files, never accumulated. An item leaves when it is implemented, absorbed into a phase, or deliberately dropped.
- The standard names are reserved and load-bearing; additional supporting files in the directory are allowed (untyped, or carrying a scoped type this spec defines).

**Subsidiary documents are typed pages, scoped to the design.** Phase and roadmap files carry frontmatter and a `type` like any page (`design/phase` or `roadmap`) — pages have designed types, not path-inferred ones. They differ from ordinary pages in placement and provenance: they are located by the directory skeleton rather than a type folder, their existence is required by the container rather than individually instigated, and they do not appear in `wiki/index.md` (the design's own index entry represents the whole directory). See the scoped-type addendum below and `schema/page-types/roadmap.md`.

**Linking.** A wikilink to a design targets the directory path — `[[wiki/{topic}/designs/{design-slug}]]` — never `…/design-slug/design`. This keeps link targets identical between legacy single-file designs and directory designs, so converting a design breaks no inbound links (including peer-wiki links). Subsidiary pages may be linked by full path (e.g. `[[wiki/{topic}/designs/{design-slug}/phases/phase-1]]`) when the phase or roadmap document itself is the referent.

**Conversion.** New designs use directory form. A legacy single-file design converts the next time it needs phase or obligation content or receives substantive revision: move `{design-slug}.md` to `{design-slug}/design.md`, create the required skeleton (`phases/phase-1.md`, `phases/later.md`, `obligations.md`), and record the move in `wiki/moves.log`.

## Scoped Type: `design/phase`

A design directory defines one scoped page type for its phase documents, `design/phase` (the scoped-type mechanism is in `schema/page-types/registry.md`, Scoped Types). It is a real page type — phase pages declare it in frontmatter — but it is defined here in the parent's spec rather than the top-level registry, is never reached through the type decision tree (the directory skeleton places it), and travels with `design` in any downstream subset.

**Question answered:** What is the scope of one implementation phase against this design?

**Location:** `wiki/{topic}/designs/{design-slug}/phases/phase-{n}.md` only (n a non-padded positive integer).

**Frontmatter:** required `title`, `type: design/phase`, `description`, `created`, `timestamp`; optional `status` (`pending` | `in-progress` | `complete`) and `related`. **`sources` is not required** — a phase's provenance is its design. Phase pages carry no `evidence`, `confidence`, `novelty`, or `enforcement`: a phase is an asserted scope of work, not an evidence-graded claim.

**Expected content:** the slice of `design.md` this phase implements; the existing abstractions and interfaces that are boundaries not to be touched; what will have been built against the design when the phase completes.

The `later.md` and `obligations.md` documents are **not** `design/phase` — they are the top-level `roadmap` type (`schema/page-types/roadmap.md`), because their maintenance discipline (a pruned forward-looking backlog) is shared with `wiki/roadmap.md` and is not phase-specific.

## Lifecycle: Designs Finalize

A design describes a **desired state the system can be measured against** — it is not a transient description of an implementation, and it does not die when its artifact ships.

- **Live** (`status: draft` or `stable`) — `design.md` is the current desired state and may be revised as understanding evolves. Phase files scope implementation against it; when a phase completes, move its unfinished remainder to `phases/later.md` or a successor phase. `later.md` and `obligations.md` are pruned as items resolve.
- **Finalized** (`status: finalized`) — when the design's lifecycle through implementation ends, the design is finalized and therefore **immutable**: `design.md` and every subsidiary document are retained exactly as they stand, as the record of what was specified and how implementation was phased against it. Do not delete phase documents at finalization; do not maintain any of it further.
- **Superseded** (`status: deprecated`) — systems evolve; later designs supersede or amend earlier ones. Supersession is expressed by a new design that links the old one; on a finalized design, updating `status` and adding that link is the only permitted edit — its body is never revised to track the system.

Decision pages still record choices and rejected alternatives whenever that rationale is worth preserving on its own, but a design is not collapsed into them on shipping.

---

Part of the `schema/page-types/` registry — see `schema/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
