# `design` Page Type

**Question answered:** How does this system or architecture work?

**When to use:**
- Architecture descriptions, workflow designs, system models, implementation plans, process specifications, design docs.

**When NOT to use:**
- Not for reusable abstractions divorced from a specific system (use `construct`).
- Not for evaluating evidence or risk (use `assessment`).

**Location:** `wiki/{topic}/designs/{design-slug}.md` or `wiki/{topic}/subtopics/{subtopic}/designs/{design-slug}.md`

**Expected sections:**
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

---

Part of the `schema/page-types/` registry — see `schema/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
