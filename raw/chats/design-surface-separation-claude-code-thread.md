---
title: "Claude Code Thread: Design Alternatives and the Design-Surface Separation"
source: claude-code-thread
created: 2026-07-15
captured: 2026-07-15
condensed: true
condensed_by: "the session's own agent (Claude Code), capturing from within the session"
---

# Claude Code Thread: Design Alternatives and the Design-Surface Separation

**Condensation notice:** this transcript is condensed, by the session's own agent capturing from within the session. The owner's messages are reproduced **verbatim** (as nested blockquotes, including dictation artifacts); the agent's responses are condensed summaries of the originals. Per the verbatim-chat raw rule, a condensed transcript is already an interpretation — extraction has happened before the provenance boundary.

Claude Code session, 2026-07-15. The owner opened with a proposal for structured design alternatives inside the wiki's design type and asked for a critical assessment plus adversarial review; the thread reframed designs as a separate, lifecycle-governed surface outside the wiki, and the owner directed implementation.

## User Prompt 1

> - [ ] A critical part of design work is exploring alternatives, which is something that the current design directories are not able to accommodate at this point. Sure I can make it into the design, but the framing of the design document is an authoritative future state standalone document which captures a single implementation. Often times my design process is to start with a fan out of ideas, which is essentially draft up three alternative design variations and then evaluate the pros and cons against each other. How that might translate to. The design document is an alternative’s directory with one or more alternative design documents that have a similar scope and framing to the top level design document plus an assessment file also within that directory which provides the analysis on top of the various alternatives, weighing, trade-offs pros and cons, implications, obligations cost, blast radius, etc. The goal here is not to prescribe exactly a workflow that he designed must start with alternatives because sometimes I’ll start with the design and then capture alternatives. One way to handle that is that any initial design idea starts off as the first alternative and eventually graduates to the design. There are a variety of options here. The situation itself is an example of. I have a goal in mind and there are variations on how I might achieve it and while I don’t necessarily want to capture this conversation as this format with structured alternative documents, but I’m just using this as an example. Give me your critical assessment and feedback and follow up with an adversarial review.

## Claude Response 1 (condensed)

Grounded the assessment in the schema as it stood, then argued the instinct was right but the mechanism fought four existing pieces of machinery:

- A nested `alternatives/` directory breaks the folder/type invariant mechanically (`scripts/lint.py` checks `path.parent.name`) and introduces a second nesting mechanism beside `subtopics/`.
- The proposed in-directory "assessment" is a `comparison` by the schema's own decision tree; choosing a type by location rather than by question inverts the artifact model.
- Persisting full rejected-alternative documents collides with the then-current "blueprints die into decisions" lifecycle — artifacts with no defined death.
- "Every design starts as alternative #1" is a rail, not a breadcrumb; graduation-by-file-move generates `moves.log` churn while `status` frontmatter already exists.

Counterproposal: sibling draft designs + a `comparison` + death-into-decision, plus a short variants convention in the design spec. Adversarial pass attacked all three positions, conceding that the directory proposal solves live-fan-out discoverability *structurally* while the convention solves it only socially, and flagging the unpriced question of epistemic machinery on speculative variants. Verdict: adopt the goal, reject the mechanism, hold the directory idea in reserve with a falsifiable revisit trigger.

## User Prompt 2

> Some points
> * designing is inherently a workflow, not route information capture and assessment. This is a tension with the framing of the wiki
> * As I continue to think about how to make designs useful to me for how I think and want information structured, the more I think that designs are separate from the wiki. This is a larger structural change, but it helps better refine the relationship between wiki and design. You can help me come up with a better more precise framing for each of them, but my first draft is that the wiki is for durable knowledge capture, and the designs are more workflow oriented, even if what we capture here is just the assets and their purpose and meaning and may be a little bit of workflow, but does not implement the full workflow itself, which is still something that I’m refining separately.
> * You mentioned containment I think it’s a critical point. Yes, there’s tension between a compartmentalized design directory with whatever information is relevant to the design. And that conflicts with how we framed the wiki but again it’s a little bit of a moot point if we recognize that designs are their own thing that need to be governed by separate rules from the wiki.
> * One of the implications for this change is that we also need to split the schema. The wiki and design sections have their own distinct schema. They still follow the same general rules regarding things like okf and other general guidelines, but the specifics of the chemist themselves are allowed to diverge and focus on their individual court purpose. A consideration downstream of that is I wonder if it makes sense for all of the types to therefore be parent scoped like how we have design/phase. The question is are all of the page types scoped to the top level organization structure. Is a comparison scoped to a design different than a comparison scoped to a wiki topic. My intuition tells me that while they may share a name and framing, and possibly even purpose, things like their structure or contents may be different depending on the context. That’s just an idle idea thinking more on the ramifications of a shift like this.
> * This also reframes previous iterations on understanding what makes an effective design like the idea of a design dying into decisions. An assertion like that never really sat well with me because a design as a design and well it may incorporate decisions. It is not a decision itself the two don’t directly translate. The question of what do designs die into becomes less relevant because designs are no longer framed by a wiki, and it may have its own lifecycle and end state. Designed don’t die into anything because the current framing of the design is a standalone document, capturing a design, and it is inherently durable, assuming it gets implemented and reaches its final lifecycle state. This allows us to ask additional follow on questions like for a design that has been implemented and has been marked as completed. What then is the relationship between that new and final design document in the information it contains to the wiki itself. Answering that question at this point is premature as I have no direct experience with that situation yet, but it’s worth keeping in mind for future consideration. For now the two are just separate things that don’t have any defined workflows regarding how one may graduate into the other or what that might look like in terms of specific documents.  Thinking a little bit better about this comment as I work through this problem, I mentioned earlier that this redesign of the design type itself has a lot of overlap with what we’re discussing as relevant to the design type documents. This type of follow on observation about how the new design does not include any requirements for how the design section in the wiki section relate to each other is an example of something that might go in the obligations section of a design. It’s a downstream and implication of this change, but it’s not something that’s in scope for the design itself and it’s not something that unnecessarily. Neither want to think about right now but it’s a downstream implication that should be captured about the design for future use.

## Claude Response 2 (condensed)

Endorsed the split and located its strongest evidence in the registry itself: `design` was the only type in the authored instigator tier but the descriptive/epistemic family — the misclassification behind every earlier awkwardness. Main contributions:

- **Sharpened framing:** "durable vs. workflow" fails (completed designs are durable too; ingest is a workflow). Proposed cut: **the wiki is evidence-governed, a design is lifecycle-governed** — wiki pages are claim-shaped ("what do we know and how do we know it"), designs commitment-shaped ("what are we building and where is it"); wiki retrospective, designs prospective until terminal.
- **Containment:** legitimate once the surface is separate (the dossier as unit), with one surviving adversarial point — dossiers can become knowledge traps; durable byproducts of design work must still flow to the wiki. Proposed the cheap early rule: reference direction — designs cite wiki freely, wiki links only to dossier roots.
- **Scoped types:** precedent exists (downstream type subsetting); a type's identity is the question it answers, sections per-scope; deliberately defer the machinery until the design schema has concrete types.
- **Lifecycle reframe:** conceded "dies into decisions" was a coping mechanism for evidence-governed designs, but its motivating rot problem survives — resolved as "a design **changes tense**": at terminal state it freezes as the historical record of intent, durable like a decision record, never living documentation of the shipped artifact.
- Noted the ingest machinery as a future graduation hypothesis (a completed design is structurally a candidate source), agreed defining it now is premature, and confirmed the undefined wiki-relationship is exactly an Obligations-section item — the new frame giving that observation an address is evidence for the frame.

## User Prompt 3

> Implement

## Claude Response 3 (condensed)

Implemented the separation: split `schema/` into `schema/wiki/` and `schema/design/` (new `dossier.md` spec; `structure.md` kept at root as the repo-wide layout), removed `design` from the wiki type registry and lint, migrated all nine design pages to top-level `designs/{slug}/design.md` dossiers with lifecycle statuses and `moves.log` tombstones, updated `AGENTS.md`, manifest, seed, and Kiro adapters, captured this thread as raw + source-capture, and recorded the decision superseding [[wiki/llm-wiki/decisions/designs-die-into-decisions]], with the design-of-the-design-surface written as the first dossier under its own rules.
