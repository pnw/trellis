---
spec: page-type
type: construct
tier: interpretive
instigators: [agent, user]
status: stable
updated: 2026-07-13
---

# `construct` Page Type

**Question answered:** What reusable abstraction is this?

**Instigation:** interpretive tier — created by an agent at ingest review or query time, or at user request, when the promotion test passes: the wiki will reason with this abstraction again, independent of the source that introduced it (`schema/page-types/registry.md`, Instigator Tiers). Never a mandatory ingest step.

**When to use:**
- Reusable ideas, abstractions, mechanisms, patterns, or named theoretical structures.
- Named intellectual building blocks used by the wiki's reasoning, synthesis, design, or analysis.

**When NOT to use:**
- Not a mandatory intermediate step for all source material.
- Not merely a glossary term.
- Not for named persons, organizations, tools, or systems (use `entity`).

**Location:** `wiki/{topic}/constructs/{construct-slug}.md` or `wiki/{topic}/subtopics/{subtopic}/constructs/{construct-slug}.md`

**Expected sections:**
- Definition
- Why It Matters
- Mechanism / Structure
- Distinctions
- Evidence and Sources
- Related Artifacts
- Open Questions (optional)

**Type-specific frontmatter:** `novelty`, `aka`, `coined_by`

---

Part of the `schema/page-types/` registry — see `schema/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
