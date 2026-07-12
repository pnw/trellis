# `source-capture` Page Type

**Question answered:** What does this source contribute?

**When to use:**
- Papers, articles, chat transcripts, repo snapshots, datasets, reports, documentation pages, or other raw source material.
- One source-capture page per meaningful raw source.

**When NOT to use:**
- Do not use as the canonical design, synthesis, or assessment page.
- Do not synthesize across the vault in the source-capture itself.

**Source isolation (invariant):** the body records only what this source says, plus capture-time assessment derivable from the source alone. A capture may *point to* other pages (`related` frontmatter, Contribution Routing) but must never *import, endorse, or reconcile with* what other pages say. Contradictions with other sources are routed downstream during ingest — the adjudication lives in a synthesis or assessment, never in the capture. This isolation is epistemic, not navigational; it is what keeps captures regenerable from their raw source, keeps corroboration independent (no circular reporting), and keeps captures immune to vault staleness. See [[wiki/llm-wiki/constructs/source-isolation]].

**Reportage vs capture-time assessment:** sections divide into faithful reportage of the source (Core Contribution, Key Claims, Evidence and Results, Methodology) and the capturer speaking (Limitations and Caveats, Reliability Notes, Extraction Notes). Keep them structurally separate so downstream pages can safely prefer the capture over the raw source.

**Location:** `wiki/{topic}/sources/{source-slug}.md` or `wiki/{topic}/subtopics/{subtopic}/sources/{source-slug}.md`

**Expected sections:**
- Source Identity
- Core Contribution
- Key Claims
- Evidence and Results
- Methodology (for empirical work)
- Limitations and Caveats
- Reliability Notes (within-source credibility signals: methodology transparency, sample size, conflict of interest, firsthand vs relayed; justifies any downward `evidence` tier adjustment)
- Important References and Linked Material
- Contribution Routing
- Extraction Notes (sparingly)

**Type-specific frontmatter:** `evidence` (required — see `schema/page-format.md`). Source-captures do not carry `confidence`.

---

Part of the `schema/page-types/` registry — see `schema/page-types/registry.md` for the full vocabulary, location rules, extensibility rules, and the type decision tree. This file is the normative spec for one page type and is standalone: it carries no rationale or history (see decision pages in the wiki for those, when they exist).
