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
    later.md         # deferred design scope not claimed by any phase file
  follow-ups.md      # optional — obligations the design imposes outside its own boundary
```

- **`design.md`** is the standalone requirements document: the target future state, complete in itself. It carries the page frontmatter and is the only typed page in the directory. Phase scoping, sequencing, and "do this first" content do not belong in it.
- **`phases/phase-1.md`** captures the first implementation scope — the slice usually most necessary to understand in design iterations. This is where implementation gets specific: which existing abstractions and interfaces are boundaries not to be touched, what will have been implemented against the design when the phase ends. Every design directory has one, even when the design will be implemented in one go — an unphased design's `phase-1.md` simply states that phase 1 implements the design in full. This makes absence unambiguous: there is never a question of "no phases" versus "forgot the phases".
- **`phases/later.md`** is the grab bag of deferred design scope: everything in `design.md` not claimed by a phase file. Its existence removes any obligation to scope or roadmap subsequent phases up front — further `phase-N.md` files are allowed whenever the user wants to phase deliberately, never required. Omit `later.md` only when the phase files cover the design in full.
- **`follow-ups.md`** captures follow-ups to the *completion* of the design: work that is out of the design's scope but which the design requires of the rest of the system, due on completion of one or more phases. It is non-phased and lives outside `phases/` because it is not deferred design scope — it is induced external work.
- The standard names are reserved and load-bearing; additional supporting files in the directory are allowed.

**Subsidiary documents are not pages.** Phase files, `later.md`, `follow-ups.md`, and any other supporting files carry no frontmatter and no `type` — they are parts of the one design artifact, transient scoping records rather than knowledge artifacts, and they do not appear in the index. The design's frontmatter (`sources`, `timestamp`, `status`) speaks for the directory.

**Linking.** A wikilink to a design targets the directory path — `[[wiki/{topic}/designs/{design-slug}]]` — never `…/design-slug/design`. This keeps link targets identical between legacy single-file designs and directory designs, so converting a design breaks no inbound links (including peer-wiki links). Subsidiary files may be linked by full path (e.g. `[[wiki/{topic}/designs/{design-slug}/phases/phase-1]]`) when the phase document itself is the referent.

**Conversion.** New designs use directory form. A legacy single-file design converts the next time it needs phase or follow-up content or receives substantive revision: move `{design-slug}.md` to `{design-slug}/design.md`, create `phases/phase-1.md`, and record the move in `wiki/moves.log`.

## Lifecycle: Blueprints Die into Decisions

A design page whose subject is not yet built is a blueprint. When the artifact it specifies ships, the design's descriptive content is superseded by the artifact itself — do not maintain a prose mirror of something that exists. The lifecycle rule operates on `design.md`; subsidiary phase files are working documents on a shorter clock — when a phase completes, move its unfinished remainder to `phases/later.md` or a successor phase and prune what shipped rather than maintaining it as history. When the design as a whole ships:

- Extract the choice rationale and rejected alternatives into one or more `decision` pages.
- Delete or deprecate the descriptive sections.
- Keep as live `design` content only what is still operative (protocols agents execute) or still unbuilt.

Designs that never ship an artifact — operative protocols, option maps kept for future reconsideration — are not blueprints and do not expire this way.

---

Part of the `schema/page-types/` registry — see `schema/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
