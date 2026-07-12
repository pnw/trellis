# `decision` Page Type

**Question answered:** What choice was made among alternatives, and why?

A normative artifact — an architecture/design decision record (ADR). It records a *specific choice already made*, the alternatives weighed, and the reasoning, so the decision is referenceable and the rejected paths aren't silently re-litigated. A decision is an **event**: it happened once, at a point in time, and its record is never edited into a different choice — a changed mind is a *new* decision that supersedes this one.

**When to use:**
- A concrete choice among alternatives whose rationale and rejected options have lasting value (tool/library/pattern selection, a build-vs-defer call, an architectural direction).
- When you want the *why* behind a choice preserved independent of the design that resulted from it.

**When NOT to use:**
- A rule or constraint that must continually hold (use `invariant`). A decision is an event; an invariant is state. The choice moment belongs here; any standing constraint the choice imposed belongs in an invariant page that future work is checked against.
- A description of how the resulting system works (use `design`).
- An evaluation of evidence or risk without a choice being made (use `assessment`).

**Relationship to `invariant`:** a decision may *establish* an invariant — the constraint it imposes outlives the choice event and becomes state, registered as its own `invariant` page that links back here as its origin. The two artifacts then evolve on different clocks: the decision record stays frozen as history, while the invariant is the live register agents check work against, and the invariant's Removal Path is the analysis that would invert this decision. Neither implies the other: many decisions constrain nothing ongoing (one-time picks with no standing rule), and many invariants have no establishing decision (inherited or discovered-and-ratified constraints — see the origin taxonomy under `invariant`). Deprecating a decision does not silently repeal the invariants it established: the superseding decision must name the invariants it repeals, re-grounds, or leaves standing.

**Location:** `wiki/{topic}/decisions/{slug}.md` or `wiki/{topic}/subtopics/{subtopic}/decisions/{slug}.md`

**Expected sections:**
- Context (the forces and situation prompting the decision)
- Decision (the choice, stated plainly)
- Alternatives Considered (options weighed and why they lost)
- Consequences (what this enables, costs, and follow-on obligations)
- Invariants Established (link the `invariant` page(s) this choice created; omit when none — deciding whether a consequence is a standing constraint is part of writing the decision)
- Status (reuse the `status` field: `draft` = proposed, `stable` = accepted, `deprecated` = superseded — name the superseding decision and dispose of any invariants this one established)
- Related Artifacts

**Type-specific frontmatter:** none required. `confidence` is optional and usually omitted (a decision is asserted, not evidence-graded); `sources` may point at the design, source-capture, or chat that grounds the choice.

---

Part of the `schema/page-types/` registry — see `schema/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
