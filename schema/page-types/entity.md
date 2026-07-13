---
spec: page-type
type: entity
tier: interpretive
instigators: [agent, user]
status: stable
updated: 2026-07-13
---

# `entity` Page Type

**Question answered:** Who or what is this named thing?

**Instigation:** interpretive tier — created by an agent at ingest review or query time, or at user request, when the promotion test passes: the wiki will reason about this named thing again, independent of the source that introduced it (`schema/page-types/registry.md`, Instigator Tiers).

**When to use:**
- Named persons, organizations, projects, tools, models, repos, systems, papers, datasets, standards.

**When NOT to use:**
- Not for abstract reusable ideas (use `construct`).

**Location:** `wiki/{topic}/entities/{entity-slug}.md` or `wiki/{topic}/subtopics/{subtopic}/entities/{entity-slug}.md`

**Expected sections:**
- Identity
- Relevance to the Wiki
- Associated Artifacts
- Notes (optional)

**Type-specific frontmatter:** `aka`

---

Part of the `schema/page-types/` registry — see `schema/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
