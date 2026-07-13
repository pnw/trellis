---
spec: page-type
type: design
tier: authored
instigators: [user]
status: stable
updated: 2026-07-13
---

# `design` Page Type

**Question answered:** How does this system or architecture work?

**Instigation:** authored tier — user-instigated (`schema/page-types/registry.md`, Instigator Tiers). Agents draft and propose designs in conversation; they do not create design pages unprompted.

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

## Lifecycle: Blueprints Die into Decisions

A design page whose subject is not yet built is a blueprint. When the artifact it specifies ships, the design's descriptive content is superseded by the artifact itself — do not maintain a prose mirror of something that exists. At that point:

- Extract the choice rationale and rejected alternatives into one or more `decision` pages.
- Delete or deprecate the descriptive sections.
- Keep as live `design` content only what is still operative (protocols agents execute) or still unbuilt.

Designs that never ship an artifact — operative protocols, option maps kept for future reconsideration — are not blueprints and do not expire this way.

---

Part of the `schema/page-types/` registry — see `schema/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
