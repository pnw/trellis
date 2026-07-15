---
title: "Two-Session Reconciliation: Dossier Phasing and Surface-Scoped Types"
source: claude-code-thread
created: 2026-07-15
captured: 2026-07-15
condensed: true
condensed_by: "the session's own agent (Claude Code), capturing from within the session"
---

# Two-Session Reconciliation: Dossier Phasing and Surface-Scoped Types

**Condensation notice:** this transcript is condensed, by the session's own agent capturing from within the session. The owner's messages are reproduced **verbatim**; the agent's output is condensed. Fourth round of the session recorded in `raw/chats/design-as-directory-brain-dump.md`, `raw/chats/design-as-directory-adversarial-review.md`, and `raw/chats/design-scoped-types-and-naming.md`.

## Context

The owner ran two parallel sessions on the same design-type brain dump, and they diverged. The other session's result merged to main first: the design-surface separation (`raw/chats/design-surface-separation-claude-code-thread.md` — dossiers under `designs/`, `design` removed from the wiki registry, containment as the organizing principle, no `type` field on design files). This session's unmerged branch held the phasing model (target spec split from phase scoping; `phases/phase-1.md` + `later.md` + `obligations.md`; null-check required files; the scope-partition framing; typed subsidiary pages via scoped types and a `roadmap` type).

## Owner Instruction (verbatim)

> I ended up with two chats on the same topic that have diverged a bit. The other chat has been merged but it’s missing much of the important changes here. Review what’s on main with the design refactor and supplement with the changes in this chat. Flag any incompatibilities and if there are none then implement the merge

## Agent Review (condensed)

Flagged the divergence as containing real incompatibilities, not just missing content. Convergences: both sessions repealed designs-die-into-decisions, freeze designs at terminal states, and link only to directory roots. Cleanly graftable: the phasing package (main's dossier still mixes target spec with an Obligations section — the brain dump's original failure mode). Incompatible, requiring owner rulings: (1) this session's "pages have designed types" ruling vs. main's "role from position, no type field — type is an error on the design surface"; (2) this session's ratified scoped-type mechanism vs. main's recorded deferral of the same alternative; (3) the wiki `roadmap` registry type, whose sharing motivation dissolves if dossier files are untyped; (4) lifecycle enums (`finalized/deprecated` vs. `draft|active|implemented|superseded|abandoned`) and duplicate supersessions of designs-die-into-decisions.

## Owner Rulings (verbatim)

On whether dossier subsidiary files carry a declared type or follow main's containment rule:

> Keep the type. Pages must have types. “Just ratified spec” is a meaningless argument when that was merged on the incorrect assumption that it included this conversation

On whether the wiki `roadmap` page type still earns its registry row:

> With the split, my understanding was that the design was free to implement its own schema of types scoped to design dossiers

## Resolution (condensed)

Main's two-surface architecture is the base; this session's content transposes onto it. The design surface defines its **own type vocabulary scoped to dossiers** — `design | phase | roadmap | alternative | weighing` — defined in `schema/design/dossier.md`, never valid on wiki pages; the wiki registry stays at eight types and gains no `roadmap` row (the surface split obviates it — the scoped-schema ruling covers the design-side roadmap files, and `wiki/roadmap.md` remains a meta-file). The dossier gains the phasing skeleton (`phases/phase-1.md`, `phases/later.md`, `obligations.md`, required while a dossier is live; terminal dossiers are frozen and exempt, which is what makes the migration honest — no backfill into frozen records), the scope-partition framing, the null-check rule, and the freeze-retains-phase-documents rule. Main's lifecycle enum wins; this session's `finalized` folds into `implemented`-freeze. The seven live dossiers received backfilled skeletons; all ten received `type: design`.

## Reading Notes

The first ruling overrides the dossier spec's containment-only typing: main's merge cannot claim ratification against a conversation it never saw. The second ruling reframes the roadmap-type question rather than answering keep-or-drop directly: the design surface owns a scoped type schema, which is this session's scoped-subtype mechanism (option 1 from `raw/chats/design-scoped-types-and-naming.md`) transposed from "scoped under a parent wiki type" to "scoped to a surface." Whether root wiki meta-files (`wiki/roadmap.md` in particular) should themselves be typed under the owner's "pages must have types" principle is left open and recorded in [[wiki/roadmap]].
