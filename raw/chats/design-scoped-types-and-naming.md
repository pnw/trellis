---
title: "Scoped Subtypes, Roadmap Type, and File Naming: Design Directory"
source: claude-code-thread
created: 2026-07-14
captured: 2026-07-14
condensed: true
condensed_by: "the session's own agent (Claude Code), capturing from within the session"
---

# Scoped Subtypes, Roadmap Type, and File Naming: Design Directory

**Condensation notice:** this transcript is condensed, by the session's own agent capturing from within the session. The owner's messages are reproduced **verbatim**; the agent's responses are condensed summaries of the originals. Third round of the session that adopted the design-as-directory form (`raw/chats/design-as-directory-brain-dump.md`) and reversed the lifecycle after adversarial review (`raw/chats/design-as-directory-adversarial-review.md`). This round settles how subsidiary documents are typed and what the files are named.

## Context from Round 2

The adversarial review closed with the owner ruling that subsidiary documents stay untyped "for now… until we can define the structure that makes sense in the context of design," while agreeing that they *should* eventually carry their own type — flagging the registry-growth cost and asking the agent for mitigation ideas. The agent offered four mitigation shapes and recommended option 1 (parent-scoped types) backed by path-derivation. This round resolves that thread.

## Agent Assessment of Option 1 (condensed)

Option 1 in practice: an addendum in the design spec defining the scoped types, plus a one-paragraph *mechanism* clause in the registry — pages carry real declared types while the top-level vocabulary stays flat. A scoped type (`design/phase`) is namespaced `{parent}/{name}`, defined in the parent's spec, excluded from the decision tree, not independently subsettable, and skeleton-placed. Precedent: spec frontmatter is already a parent-scoped mini-schema that never entered the registry.

On the vocabulary: merging `later` and `obligations` into one type is right (same kind of document — a pruned forward-looking backlog — distinguished by concern/filename). But if `wiki/roadmap.md` carries that same type, the type cannot be scoped, because it has an instance outside any design. So `roadmap` becomes a **top-level** registry type with instances at multiple scopes (wiki root, design `later.md`/`obligations.md`), while `design/phase` stays scoped. Registry cost: one mechanism clause plus one real type — and that type *retires* the standing `wiki/roadmap.md` meta-file exemption, raising type-system coverage. Typing phases also gives the phase-state gap a home (`status` on the phase page). Sources exemption: roadmap/phase are planning documents (asserted work), so `sources` is not required and they carry no epistemic fields.

## User Prompt (typing question, verbatim)

> what does 1 look like in practice? Is it just an addendum to the design definition that states the page types such that the pages are typed but it doesn't bloat the top level type definitions? I don't want path conventional types like 2, because the whole point of OKF is that pages have designed types. As for the types themselves, the "roadmap" like documents should both have the same type, and I might consider the roadmap to have the same type as well.

## Agent Response (condensed)

Confirmed: an addendum in the design spec plus a registry mechanism clause; pages get real declared types (OKF-honest), top-level vocabulary stays flat. Because `wiki/roadmap.md` carries the type, `roadmap` is top-level (not scoped) with multi-scope instances; `design/phase` is scoped. Two wrinkles noted: the instigator tiers don't fit these pages (structural/skeleton-required, not per-source-instigated) — add a note that skeleton-required pages are governed by their container's spec; and index policy — keep subsidiary pages out of `wiki/index.md` (the design entry represents the directory) while `wiki/roadmap.md` stays listed.

## User Prompt (naming double-check, verbatim)

> just want to double check that the names of the files we've been discussing are the best names or if you have better alternatives

## Agent Response (condensed)

Per-name verdict: keep `design.md` (type↔file symmetry, guessable); keep `phases/` (with `later.md` inside, the directory is a complete scope partition); keep `phase-1.md` (note: number without zero-padding — a design with enough phases for sort order to matter is a smell `later.md` prevents); keep `later.md` (vague out of context but never appears out of context — inside `phases/` the listing reads as a timeline ending in deliberate vagueness; `backlog.md` rejected for importing ticket-tracker connotations). Change `follow-ups.md` → **`obligations.md`**: the owner's own dump used "follow-up items" as the *genus* of two split concerns, so naming one species with the generic term invites the misfiling the split exists to prevent; `obligations` names the species (work the design obligates of other systems) and pairs with the existing spec language. Type names `roadmap` and `design/phase` unaffected.

## User Ruling (verbatim)

> commit to those suggestions and complete all of the other suggestions from the follow up conversion. Direction for those page types is the 1 option to add scoped subtypes contained within the parent type. Ensure to capture "phases/ contains a complete partition of the design's scope — phase-1 + phase-N + later = everything in design.md" as I think that's concise and critical framing of the phases directory that provides a verifiable target.

## Reading Notes

The rulings, restated: (1) rename `follow-ups.md` → `obligations.md`; keep all other file names as-is. (2) Type subsidiary documents via **option 1 — scoped subtypes contained within the parent type**: `design/phase` defined in the design spec (not the registry), and a top-level `roadmap` type shared by `wiki/roadmap.md`, `phases/later.md`, and `obligations.md`. Path-derived typing (option 2) is rejected — OKF's premise is that pages have designed types. (3) Capture verbatim as critical framing: "phases/ contains a complete partition of the design's scope — phase-1 + phase-N + later = everything in design.md" — a verifiable target for the phases directory. "the other suggestions from the follow up conversion" refers to the agent's assessment items across this round: the instigator-tier exemption note, sources/epistemic-field exemption for planning types, index exclusion of subsidiary pages, phase `status` field, and non-padded phase numbering.
