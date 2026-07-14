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

A design separates the **target specification** (what the future state is) from the **phasing of implementation against it** (what gets built when, and inside which existing boundaries). The directory holds one typed page plus untyped subsidiary documents under standard names, so any consumer knows where to look:

```
wiki/{topic}/designs/{design-slug}/
  design.md          # REQUIRED — the target specification; the typed design page
  phases/
    phase-1.md       # REQUIRED — first implementation scope against the design
    phase-2.md …     # optional — further scoped phases, only if deliberately roadmapped
    later.md         # REQUIRED — deferred design scope not claimed by any phase file
  follow-ups.md      # REQUIRED — obligations the design imposes outside its own boundary
```

**Every standard file is required — an empty concern is stated, never inferred.** A missing file is always ambiguous between "nothing there" and "nobody wrote it," so each standard file exists even when its concern is empty: an unphased design's `phase-1.md` states that phase 1 implements the design in full; a fully-phased design's `later.md` states that the phase files cover the design; a design imposing no external obligations says so in `follow-ups.md`. Only further `phase-N.md` files are optional, because `later.md` already accounts for everything they would claim.

- **`design.md`** is the standalone requirements document: the target future state, complete in itself. It carries the page frontmatter and is the only typed page in the directory. Phase scoping, sequencing, and "do this first" content do not belong in it.
- **`phases/phase-1.md`** captures the first implementation scope — the slice usually most necessary to understand in design iterations. This is where implementation gets specific: which existing abstractions and interfaces are boundaries not to be touched, what will have been implemented against the design when the phase ends. Every design directory has one, even when the design will be implemented in one go — an unphased design's `phase-1.md` simply states that phase 1 implements the design in full. This makes absence unambiguous: there is never a question of "no phases" versus "forgot the phases".
- **`phases/later.md`** is the grab bag of deferred design scope: everything in `design.md` not claimed by a phase file. Its existence removes any obligation to scope or roadmap subsequent phases up front — further `phase-N.md` files are allowed whenever the user wants to phase deliberately, never required.
- **`follow-ups.md`** captures follow-ups to the *completion* of the design: work that is out of the design's scope but which the design requires of the rest of the system, due on completion of one or more phases. It is non-phased and lives outside `phases/` because it is not deferred design scope — it is induced external work.
- **`later.md` and `follow-ups.md` are scoped roadmaps, not append-only lists.** They follow the same dynamics as `wiki/roadmap.md`, localized to one design: pruned as items resolve or graduate into phase files, never accumulated. An item leaves when it is implemented, absorbed into a phase, or deliberately dropped.
- The standard names are reserved and load-bearing; additional supporting files in the directory are allowed.

**Subsidiary documents are not pages.** Phase files, `later.md`, `follow-ups.md`, and any other supporting files carry no frontmatter and no `type` — they are parts of the one design artifact, transient scoping records rather than knowledge artifacts, and they do not appear in the index. The design's frontmatter (`sources`, `timestamp`, `status`) speaks for the directory.

**Linking.** A wikilink to a design targets the directory path — `[[wiki/{topic}/designs/{design-slug}]]` — never `…/design-slug/design`. This keeps link targets identical between legacy single-file designs and directory designs, so converting a design breaks no inbound links (including peer-wiki links). Subsidiary files may be linked by full path (e.g. `[[wiki/{topic}/designs/{design-slug}/phases/phase-1]]`) when the phase document itself is the referent.

**Conversion.** New designs use directory form. A legacy single-file design converts the next time it needs phase or follow-up content or receives substantive revision: move `{design-slug}.md` to `{design-slug}/design.md`, create `phases/phase-1.md`, and record the move in `wiki/moves.log`.

## Lifecycle: Designs Finalize

A design describes a **desired state the system can be measured against** — it is not a transient description of an implementation, and it does not die when its artifact ships.

- **Live** (`status: draft` or `stable`) — `design.md` is the current desired state and may be revised as understanding evolves. Phase files scope implementation against it; when a phase completes, move its unfinished remainder to `phases/later.md` or a successor phase. `later.md` and `follow-ups.md` are pruned as items resolve.
- **Finalized** (`status: finalized`) — when the design's lifecycle through implementation ends, the design is finalized and therefore **immutable**: `design.md` and every subsidiary document are retained exactly as they stand, as the record of what was specified and how implementation was phased against it. Do not delete phase documents at finalization; do not maintain any of it further.
- **Superseded** (`status: deprecated`) — systems evolve; later designs supersede or amend earlier ones. Supersession is expressed by a new design that links the old one; on a finalized design, updating `status` and adding that link is the only permitted edit — its body is never revised to track the system.

Decision pages still record choices and rejected alternatives whenever that rationale is worth preserving on its own, but a design is not collapsed into them on shipping.

---

Part of the `schema/page-types/` registry — see `schema/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
