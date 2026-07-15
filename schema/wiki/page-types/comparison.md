---
spec: page-type
type: comparison
tier: interpretive
instigators: [agent, user]
status: stable
updated: 2026-07-13
---

# `comparison` Page Type

**Question answered:** How do these things relate or differ?

**Instigation:** interpretive tier — created by an agent or at user request when a real question or tradeoff decision calls for the comparison (`schema/wiki/page-types/registry.md`, Instigator Tiers).

**When to use:**
- X vs Y, approach comparisons, tradeoff analysis, pattern comparisons, system comparisons, conceptual distinctions.

**When NOT to use:**
- Not when the real purpose is a broad synthesis.
- Not when the real purpose is defining one construct.

**Location:** `wiki/{topic}/comparisons/{comparison-slug}.md` or `wiki/{topic}/subtopics/{subtopic}/comparisons/{comparison-slug}.md`

**Expected sections:**
- Comparison Question
- Summary
- Comparison Table
- When to Use X
- When to Use Y
- Failure Modes
- Related Artifacts

---

Part of the `schema/wiki/page-types/` registry — see `schema/wiki/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
