---
spec: page-type
type: synthesis
tier: interpretive
instigators: [agent, user]
status: stable
updated: 2026-07-13
---

# `synthesis` Page Type

**Question answered:** What do we currently understand about this area?

**Instigation:** interpretive tier — created by an agent or at user request when a real question, a contradiction between captures, or accumulated captures demand integration (`schema/page-types/registry.md`, Instigator Tiers). Ingest is an occasion to ask whether a synthesis is due, never by itself a justification for one.

**When to use:**
- Cross-source conclusions, current state of research, thematic summaries, broad topic understanding.
- Integrating multiple sources, constructs, entities, or other artifacts.

**When NOT to use:**
- Not merely a long construct definition.
- Not merely a source capture.
- Not a design doc.

**Location:** `wiki/{topic}/syntheses/{synthesis-slug}.md` or `wiki/{topic}/subtopics/{subtopic}/syntheses/{synthesis-slug}.md`

**Expected sections:**
- Central Question
- Current Synthesis
- Supporting Evidence
- Tensions and Contradictions
- Implications
- Related Artifacts
- Update Triggers

---

Part of the `schema/page-types/` registry — see `schema/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
