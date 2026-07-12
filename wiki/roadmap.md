# Roadmap

A forward-looking backlog for the Trellis method: open design questions, candidate topics, self-maintenance items, and the meta-experiment log. Pruned as items resolve, not accumulated. Practice-side items (AI SDLC, intent compiler, the pilot) live in the `ai-research` peer wiki's roadmap.

See also: [[wiki/overview]] | [[wiki/index]] | [[wiki/log]]

## Open Design Question Backlog

### Federation / Trellis

- First real instantiation: run `seed/interview.md` to create the pilot project wiki (couples to ai-research's pilot playbook — that wiki becomes downstream instance #2) — [[wiki/llm-wiki/designs/trellis-repo-design]].
- First real upgrade: exercise the three-breadcrumb inheritance path when the first post-split schema change lands — [[wiki/llm-wiki/designs/wiki-federation-and-inheritance]].
- Retrieval across wikis: is per-wiki search plus the peer registry enough at n≤3, or is qmd multi-collection indexing worth wiring? — [[wiki/llm-wiki/designs/wiki-federation-and-inheritance]].
- Does `episodes.md` earn its place, and do its entry criteria hold? — [[wiki/llm-wiki/designs/wiki-federation-and-inheritance]].
- Move-log details: per wiki root or per repo; regeneration vs. append-on-commit — [[wiki/llm-wiki/designs/wiki-federation-and-inheritance]].
- Does this lab wiki eventually want a `trellis` topic distinct from `llm-wiki` (method-specific designs vs. pattern research)? — [[wiki/llm-wiki/designs/trellis-repo-design]].

### Method / Project Application

- Which project artifacts to standardize first (`AGENTS.md`, decisions, workflows, evals, handoffs); minimum project wiki that measurably improves implementation quality; how to promote lessons back to the method layer without creating noise; full schema vs. a lighter form for project wikis — [[wiki/llm-wiki/designs/project-wiki-application-guide]], [[wiki/llm-wiki/designs/project-wiki-template]].
- Task graph format, file-ownership/locking convention, role-context duplication vs. linking, eval metrics that prove multi-agent throughput rather than added ceremony — [[wiki/llm-wiki/designs/multi-agent-project-wiki-pattern]].
- Should confidence derivation be fully scripted vs. remain a partial lint judgment call; do effectiveness-vs-design-intent claim scopes need structured representation — [[wiki/llm-wiki/designs/evidence-tier-schema]].

### Agent Context / Retrieval

- Optimal index granularity at different wiki sizes; tag-based vs. topic-based indexing for cross-cutting queries; whether confidence should influence routing — [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]].
- Whether tag hierarchy can be derived automatically vs. must be curated; at what scale a tag DAG pays off vs. flat tags; whether this wiki's tags warrant domain-centric fused summaries — [[wiki/agent-context/subtopics/retrieval/constructs/hierarchical-tag-chains]], [[wiki/agent-context/subtopics/retrieval/constructs/domain-centric-knowledge-fusion]].
- Whether the ETH Zurich context-file findings transfer from coding repos to research wikis specifically — [[wiki/agent-context/subtopics/context-files/constructs/context-file-effectiveness]].

## Candidate New Topics

Carried from the pre-split survey (2026-07-08, anchors verified by web search, none captured yet); all are method-side:

- **Diátaxis as a comparator for the page-type registry** — the only widely adopted documentation type-system; its "quadrant mixing" failure mode is this wiki's mixed-role lint check under another name. Would test whether the registry's types derive from principled axes or accumulated habit.
- **Wikipedia's maintenance ecology** — assessment classes, the WP 1.0 bot, maintenance templates, quality-assessment literature; directly transferable questions about lint tiers, `status`, and assessment staleness.
- **Wiki eval harness (probe-question QA)** — synthetically generated QA pairs answered through the query workflow, scored for groundedness/abstention; would make "did retrieval or schema changes improve answer quality" measurable rather than vibes.
- **Methodology grounding for self-experimentation** — action research, design science research, n-of-1 designs; decades of literature on exactly [[wiki/llm-wiki/designs/wiki-self-experimentation]]'s weak points (observer-operator conflation, n=1 inference limits).
- **Calibration scoring for hypothesis lines** — Tetlock-style scoring of the meta-experiment log's predictions at verdict time; near-zero added ceremony.
- **Note-craft and page granularity** — Zettelkasten/evergreen-note/progressive-summarization literature checked against what actually helps agent retrieval.
- **Knowledge-organization theory for the tag system** — faceted classification, controlled vocabularies, SKOS; keeps the tag system from re-deriving solved problems.
- **Agent memory / provenance standards** (W3C PROV) — relevant to the evidence/confidence schema and to `moves.log`-style provenance.
- **Personal-to-team knowledge federation** — three tiers (personal research wiki, project wikis, future team wiki); the federation design covers two-wiki mechanics, not the team layer.

## Wiki Self-Maintenance

- **Federation bootstrap — executed 2026-07-12.** This repo is the result. Remaining: Phase 2 (validate `seed/interview.md` by instantiating the pilot wiki) and the first real upgrade. See Open Design Question Backlog above.
- **Retrieval implementation (from 2026-07-08).** `scripts/qmd-index.sh` (BM25 works everywhere; semantic/hybrid blocked in sandboxed sessions by network egress — see [[wiki/agent-context/subtopics/retrieval/entities/qmd]]). Carried from ai-research with the split.
- **Lint judgment tier stays manual.** `scripts/lint.py` covers the deterministic tier only; contradictions, circular reporting, isolation violations, thin topics, and the new serves-the-goal check are agent work per `schema/lint.md`. The single-goal principle and outbound-only link responsibility await `invariant` pages (flagged in [[wiki/llm-wiki/designs/wiki-federation-and-inheritance]] as invariant candidates — write them once the split has settled rather than mid-migration).

### Meta-Experiment Log

Open experiments per [[wiki/llm-wiki/designs/wiki-self-experimentation]]: one line each — what changed, expected benefit, revisit trigger. Pruned on verdict (verdicts become assessments in `wiki/llm-wiki/assessments/`).

- **Evidence-tier schema (adopted 2026-07-07).** Expected: agents weight sources by tier and confidence stops inflating. Revisit: after the next ~10 ingests by sessions that didn't design it — does the tier actually change routing/derivation behavior? (Adoption findings already in [[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]]; this open item is the behavioral question only.)
- **QMD retrieval graduation (adopted 2026-07-08, ahead of trigger).** Expected: better cross-cutting query hit-rate than pure agentic search at 130+ pages. Revisit: first few real queries — did `qmd search` find anything `Grep` would have missed, and did anyone use it at all?
- **Roadmap file (adopted 2026-07-08).** Expected: open questions get worked instead of re-discovered; file stays pruned rather than accumulating. Revisit: 2026-08 — compare item count added vs. resolved (now across both this and the ai-research roadmap).
- **Self-experimentation protocol itself (adopted 2026-07-08).** Expected: practice changes get hypothesis lines and eventual verdicts at near-zero ceremony. First firing passed same-day. Keep open — verdict into an assessment after ~3 more practice changes show the habit holds across cold sessions.
- **Verbatim-chat raw rule (adopted 2026-07-08).** Expected: `raw/chats/` regains episode-grade regenerability. Revisit: next 3 chat ingests — verbatim used where available, condensation declared where not? (Two declared-condensed captures with verbatim owner quotes landed 2026-07-10 — on track.)
- **`invariant` page type (adopted 2026-07-08).** Expected: constraints stop hiding in design-page sections; removal analyses get cited when changes are proposed. Revisit: after the next few schema/tooling changes. Watch for: invariant pages duplicating `schema/` operating rules.
- **Design-lifecycle rule (adopted 2026-07-12).** Blueprints die into decisions when their artifact ships (`schema/page-types/design.md`; [[wiki/llm-wiki/decisions/designs-die-into-decisions]]). Expected: design pages stop accumulating as stale mirrors of shipped artifacts; rationale stays findable via decision archaeology. Revisit: at the next shipped design — does the collapse happen unprompted in a cold session?
- **Project-wiki meta-file exemption (adopted 2026-07-12, pending pilot).** Coordination artifacts (task graph, error book, handoffs) are meta-files outside the type system; knowledge pages map to registry types ([[wiki/llm-wiki/designs/project-wiki-template]], Reconciliation section). Expected: the pilot wiki instantiates without inventing new page types or fighting the schema. Revisit: at pilot-wiki creation — did the exemption hold, or do coordination artifacts want typed pages?
- **Federation / repo split (adopted 2026-07-12).** Expected: each wiki's health becomes measurable against its single goal; method work stops competing with practice work; downstream friction reports become arms-length operational evidence. Revisit: 2026-08 — is the lab workload still real here, did ai-research's practice throughput improve, and has any breadcrumb (pin, per-type diff, move log) actually been followed?
