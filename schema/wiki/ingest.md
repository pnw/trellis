# Ingest Workflow

Agent-agnostic workflow for processing a new source into the wiki. This file is part of the shared `schema/` layer referenced by `AGENTS.md`.

## Workflow

Ingest is two-staged. **Stage 1 (capture)** is bounded and source-isolated: executable by a delegated capture agent given only the raw source and this spec, with no other vault context — impartiality of the capture is the point. **Stage 2 (review and routing)** is vault-aware and judgment-bearing: performed by the orchestrating agent, reading the capture rather than the raw source. One session may run both stages; the boundary between them is normative even when the executor is a single agent.

### Stage 1 — Capture

1. **Acquire the source.** If the user provides a URL, save it to `raw/` first (see Web Source Handling and PDF Source Handling below). If the source is already in `raw/`, read it directly.
2. **Create the source-capture page** at `wiki/{topic}/sources/{source-slug}.md` or `wiki/{topic}/subtopics/{subtopic}/sources/{source-slug}.md` with `type: source-capture` frontmatter and a required `evidence` tier (see `schema/wiki/page-format.md`). The source-capture is source-isolated — it records what this source says plus capture-time assessment derivable from the source alone; it may point to other pages but never imports, endorses, or reconciles with them.
3. **List routing candidates.** Fill the Contribution Routing section with candidate contributions derivable from the source alone — concepts it introduces, named things it describes, claims that could change broader understanding. A vault-aware capturer may name concrete wikilink targets; a context-free capture agent names candidates by shape and name, and Stage 2 resolves them against the vault.

Stage 1 ends here. The capture is the handoff artifact: Stage 2 consumes it in place of the raw source.

### Stage 2 — Review and Routing

4. **Discuss** the capture's takeaways and routing candidates with the user before writing downstream pages, unless the user has asked for autonomous ingest.
5. **Decide promotions** per the instigator tiers in `schema/wiki/page-types/registry.md`. Ingest is an occasion for interpretation, not a justification: every capture raises the question "does this change the derived layer?", and a defensible answer is often no. A single source may justify a new interpretive page when the promotion test passes (priced by the confidence rules); mere mention never does. Authored-tier pages (`decision`, `invariant`) are not created here without user instigation, and neither are design dossiers (`schema/design/dossier.md`).
6. **Route promoted contributions directly to affected typed artifacts.** Update or create those artifacts. Do not force contributions through construct pages first.
7. **Detect contradictions.** Check the capture's claims against existing vault content — a Stage 2 responsibility, since a context-free capturer cannot see the vault. Adjudicate downstream in the affected synthesis or assessment, citing both sources — never inside the capture.
8. **Backlink audit** — scan existing wiki pages for mentions of concepts from this source. Add root-relative wikilinks such as `[[wiki/topic/constructs/page-name]]` in both directions where missing.
9. **Re-derive confidence** on downstream pages the source touched: check each page's `confidence` against the derivation ceiling in `schema/wiki/page-format.md` (a new corroborating or contradicting source can raise or lower it).
10. **Update `wiki/index.md`** — add new entries, grouped by topic, subtopic when present, then type.
11. **Refresh the local search index** — run `scripts/qmd-index.sh` (best-effort; safe to skip if it fails, e.g. embedding model downloads blocked by network policy — see `wiki/agent-context/subtopics/retrieval/entities/qmd.md`). The index itself is not committed; the script is what every agent/session reruns to reproduce it.
12. **Append to `wiki/log.md`** — add a bullet under today's date heading (create the heading at the top if it doesn't exist). Format: `* **Ingest**: Processed [Source Title](wiki/topic/sources/source-slug.md) from <origin>. Created/updated pages X, Y, Z.` Note any contradictions found.

## Source-Capture Format

```markdown
# Title

## Source Identity

- Raw source: [[raw/articles/slug.md]] or [[raw/papers/slug.md]]
- Source type: article | paper | chat transcript | repo snapshot | dataset | report
- Author(s):
- Published/retrieved:
- Original URL:
- Scope:

## Core Contribution

Briefly state what this source contributes.

## Key Claims

- Claim 1
- Claim 2
- Claim 3

## Evidence and Results

Data, experiments, examples, measured results, or concrete observations.

## Methodology

For papers, experiments, surveys, benchmarks, and empirical work.

## Limitations and Caveats

Limitations stated by the source and obvious extraction limitations.

## Reliability Notes

Within-source credibility signals, assessable from the source alone: methodology transparency, sample size, conflict of interest, firsthand vs relayed claims, internal consistency. If these justify assigning a lower `evidence` tier than the source type nominally suggests, record the justification here. Omit the section when there is nothing notable.

## Important References and Linked Material

List meaningful references from the source.

Format: `- [Descriptive title](url) — why this reference matters.`

Include: papers/articles/posts cited in the body, tools/repos/projects discussed, primary sources the article is about, related reading suggested by the author, academic references that may become future ingests.

Exclude: navigation/header/footer links, ads/promotions/sponsored content, share/bookmark links, generic homepage links, author bio/social links unless directly relevant.

## Contribution Routing

List candidate contributions — the downstream artifacts this source may create or update. Candidates, not commitments: Stage 2 decides what is actually promoted (`schema/wiki/page-types/registry.md`, Instigator Tiers).

Examples (vault-aware capturer, concrete targets):
- `[[wiki/intent-compiler/syntheses/intent-compiler-current-understanding]]` — updates topic synthesis
- `[[wiki/intent-compiler/constructs/process-weights]]` — defines or updates construct
- `[[wiki/intent-compiler/assessments/validation-assessment]]` — affects validation status

A context-free capture agent cannot know vault paths; it names candidates by shape and name instead:
- introduces the concept "process weights" — candidate construct
- describes the tool FooSearch — candidate entity
- reports results contradicting the common framing of X — candidate synthesis or assessment input

## Extraction Notes

Use sparingly for source emphasis, ambiguity, OCR/PDF issues, or interpretation boundaries.
```

The sections from Core Contribution through Methodology are faithful reportage of the source. Limitations and Caveats, Reliability Notes, and Extraction Notes are the capturer speaking. Keep the two groups structurally separate.

## Key Rules

- **Source capture is source-isolated (epistemic, not navigational).** The body records only what this source says; pointers to other pages are fine, adjudication is not.
- **Assign `evidence` at capture time.** Source type gives the starting tier; Reliability Notes may justify a downward adjustment.
- **Routing candidates are listed at capture; promotion is decided at review.** The instigator tiers and promotion test in `schema/wiki/page-types/registry.md` govern what actually gets created — ingest is an occasion for interpretation, not a justification.
- **Do not force every contribution through construct pages.** A promoted contribution may update a synthesis or assessment directly.
- **Never edit existing files in `raw/` in place.** Fidelity is what makes re-capture audits and upstream change detection possible — the two purposes `raw/` exists for.
- If a topic directory doesn't exist yet, create it.
- Place new pages in the type folder that matches frontmatter: `sources/`, `constructs/`, `entities/`, `syntheses/`, `assessments/`, `comparisons/`, `decisions/`, or `invariants/`.
- Create or reuse a subtopic under `subtopics/` only when the narrower cluster materially improves navigation.
- If a page already covers this concept, update it rather than creating a duplicate.
- Note contradictions explicitly in downstream pages: cite both the new and existing source.
- Set downstream `confidence` per the derivation rules in `schema/wiki/page-format.md` — never above the ceiling the cited sources support.

## Web Source Handling

When the user provides a URL that returns readable article content (blogs, news, documentation):

1. Fetch the page (full content).
2. Save to `raw/articles/{kebab-case-slug}.md` with this frontmatter:
   ```
   ---
   title: (from the page's H1 or title)
   source: (the original URL)
   retrieved: (today's date YYYY-MM-DD)
   ---
   ```
3. After the frontmatter, save the **article body only**. Strip navigation, sidebars, footers, ads, and the numbered link reference index. Preserve all body text, headings, lists, blockquotes, code blocks, and tables verbatim.

## Chat / Conversation Source Handling

When capturing a conversation (ChatGPT/Codex threads, Claude Code sessions, chat exports) into `raw/chats/`:

1. **Prefer verbatim exports.** A raw chat file should be an episode-grade record: the actual messages, unedited. Use platform share links, transcript exports, or full copies when available.
2. **Condensation must declare itself.** When only an agent-condensed transcript is feasible (e.g., capturing the current session from within it), the raw file's frontmatter and lead must say it is condensed and by whom, and the owner's own statements must be quoted verbatim, never paraphrased. A condensed transcript is already an interpretation — extraction has happened before the provenance boundary — so it cannot be silently presented as raw.
3. Source-captures citing a condensed transcript note the condensation in Reliability Notes (such captures are `llm-generated` tier regardless).

## PDF Source Handling

When the URL points to an academic paper:

1. **Fetch the landing page** to extract metadata (title, authors, abstract, venue, date, DOI).
2. **Download the PDF** with `curl -sL -o` to `raw/papers/pdf/{kebab-case-slug}.pdf`.
3. **Convert to text** using pdfminer.six:
   ```python
   from pdfminer.high_level import extract_text
   text = extract_text('path/to/file.pdf')
   ```
4. **Save to `raw/papers/{kebab-case-slug}.md`** with metadata frontmatter, abstract, and full text.
