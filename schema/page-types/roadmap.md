---
spec: page-type
type: roadmap
tier: authored
instigators: [user]
status: stable
updated: 2026-07-14
---

# `roadmap` Page Type

**Question answered:** What future work is intended, and under what revisit conditions?

**Instigation:** structural, governed here rather than by the instigator tiers (`schema/page-types/registry.md`). A roadmap exists because its scope needs a standing backlog — the wiki as a whole (`wiki/roadmap.md`), or a design that a directory skeleton requires to carry `phases/later.md` and `obligations.md`. Agents maintain roadmaps continuously; they do not manufacture new roadmap instances outside a container that calls for one.

**When to use:**
- A pruned, forward-looking backlog for one scope: open questions, candidate work, self-maintenance items, deferred scope, induced obligations, a meta-experiment log.

**When NOT to use:**
- Not for recording a choice already made (use `decision`).
- Not for describing how something works (use `design`).
- Not for evaluating evidence or risk (use `assessment`).
- Not an append-only journal of what happened (that is `wiki/log.md`, a meta-file).

**Location:** skeleton-placed, exempt from folder/type agreement. Known instances: `wiki/roadmap.md` (the wiki's backlog) and, inside a design directory, `phases/later.md` (deferred design scope) and `obligations.md` (work the design imposes on other systems). There is no `roadmaps/` type folder.

**Frontmatter:** required `title`, `type: roadmap`, `description`, `created`, `timestamp`; optional `status` and `related`. **`sources` is not required and normally absent** — a roadmap asserts intended work, it does not cite evidence. Roadmap pages carry no `evidence`, `confidence`, `novelty`, or `enforcement`.

**Expected content:** items grouped as suits the scope (backlog sections, a meta-experiment log). Each item states the work and, where useful, a revisit trigger. Items link the artifacts they concern with wikilinks.

## Discipline: Pruned, Not Accumulated

A roadmap is maintained state, not a log. Items **leave** when they are done, absorbed into an artifact (a phase file, a design, a decision), or deliberately dropped — the file shrinks and churns rather than growing forever. This is what distinguishes a roadmap from the append-only `wiki/log.md`, and it is the single failure mode to watch: a roadmap that only grows is being used as a journal.

A design's `later.md` and `obligations.md` are the same type applied at design scope; they follow the same prune-not-accumulate discipline, localized to one design (`schema/page-types/design.md`, Directory Form).

---

Part of the `schema/page-types/` registry — see `schema/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
