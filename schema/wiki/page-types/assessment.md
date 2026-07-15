---
spec: page-type
type: assessment
tier: interpretive
instigators: [agent, user]
status: stable
updated: 2026-07-13
---

# `assessment` Page Type

**Question answered:** What is validated, speculative, risky, contradicted, or unknown?

**Instigation:** interpretive tier — created by an agent or at user request when a verdict falls due: an experiment's revisit trigger fires, evidence quality needs review, or a contradiction needs adjudication (`schema/wiki/page-types/registry.md`, Instigator Tiers).

**When to use:**
- Epistemic status, design validation, risk analysis, research gaps, contradiction tracking, evidence quality review.

**When NOT to use:**
- Not for describing how a system works or what is being built (that is a design dossier — `schema/design/dossier.md`).
- Not for integrating current understanding (use `synthesis`).

**Location:** `wiki/{topic}/assessments/{assessment-slug}.md` or `wiki/{topic}/subtopics/{subtopic}/assessments/{assessment-slug}.md`

**Expected sections:**
- Scope
- Bottom Line
- Validated
- Plausible but Unvalidated
- Speculative
- Contradictions / Risks
- Missing Evidence
- Related Artifacts

---

Part of the `schema/wiki/page-types/` registry — see `schema/wiki/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
