# `invariant` Page Type

**Question answered:** What must always hold here, and what would removing it take?

**When to use:**
- A named constraint that must hold across all states/time of a specific system, workflow, or protocol — with a violation cost and some commitment to keeping it true.
- Standing consequences of decisions: the constraint a choice established, outliving the choice event itself.
- Inherited or observed constraints being *ratified*: conditions nobody chose (vendor limits, environment policy, legacy structure) that the project has examined and now treats as binding. Writing the Removal Path is the ratification act — it is what upgrades "observed" to "binding."

**When NOT to use:**
- Not a mere observation that a condition currently holds (that is `design` or `entity` content). An invariant requires a cost to breaking it and an analyzed reason not to remove it.
- Not a portable idea divorced from any specific system (use `construct` — e.g. source isolation is defined as a construct because it is a named idea you reason with, though it reads almost as an invariant).
- Not an end-to-end description of how a system works (use `design`). A design page's local `Invariants` section remains the right home for constraints meaningful only within that one design; promote to an `invariant` page when the constraint is cross-cutting, independently citable, or carries a non-obvious removal analysis.
- Not an evaluation of whether something holds or how risky it is (use `assessment` — an assessment may *test* an invariant).
- Not a point-in-time choice among options (use `decision`). A decision is an event; an invariant is state — the decision records the establishment moment, the invariant is the standing register checked against (see Relationship to `invariant` under `decision`).
- **Do not restate a `schema/` operating rule as an invariant page.** This wiki's own rules are canonical in `schema/` and enforced by `scripts/lint.py`; reference the canonical statement instead of duplicating it.

**Location:** `wiki/{topic}/invariants/{invariant-slug}.md` or `wiki/{topic}/subtopics/{subtopic}/invariants/{invariant-slug}.md`

**Expected sections:**
- Statement (the constraint, stated precisely, quantified over all states/time it governs)
- Scope (the system and operations it binds; boundary of applicability)
- Rationale (what the constraint buys; what breaks without it)
- Enforcement (how it is guaranteed in practice; link the mechanism — lint rule, tooling, review step, or documented convention)
- Violation Modes (what an accidental breach looks like while the invariant stands, how it is detected, its cost)
- Removal Path (deliberate repeal, as opposed to breach: open with the invariant's origin — decided, inherited, or discovered-and-ratified — then what would have to be true to remove it, the work required, and the downstream effects. Decision-derived invariants link and invert their establishing decision; inherited ones record the ratification analysis here. Depth proportionate to the constraint's centrality. This is the section most likely to rot as the system evolves — re-check it when citing.)
- Exceptions (bounded carve-outs, or "None")
- Related Artifacts (designs it constrains, constructs it derives from, assessments that test it, the decision that established it if one exists)
- Evidence and Sources

**Type-specific frontmatter:** `enforcement` (required — see `schema/page-format.md`). Invariant pages carry derived `confidence` like other non-source pages; it rates the support for the Rationale and Removal Path, not the rule itself.

---

Part of the `schema/page-types/` registry — see `schema/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
