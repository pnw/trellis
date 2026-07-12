# Ingest Workflow

Agent-agnostic workflow for processing a new source into the wiki. This file is part of the shared `schema/` layer referenced by `AGENTS.md`.

## Workflow

1. **Acquire the source.** If the user provides a URL, save it to `raw/` first (see Web Source Handling and PDF Source Handling below). If the source is already in `raw/`, read it directly.
2. **Discuss** key takeaways with the user before writing anything, unless the user explicitly asks for autonomous ingest.
3. **Create source-capture page** at `wiki/{topic}/sources/{source-slug}.md` or `wiki/{topic}/subtopics/{subtopic}/sources/{source-slug}.md` with `type: source-capture` frontmatter and a required `evidence` tier (see `schema/page-format.md`). The source-capture is source-isolated — it records what this source says plus capture-time assessment derivable from the source alone; it may point to other pages but never imports, endorses, or reconciles with them.
4. **Identify contribution shapes.** Determine which downstream artifacts this source affects:
   - Does it introduce or update constructs?
   - Does it introduce or update entities?
   - Does it update a synthesis?
   - Does it update a design?
   - Does it update an assessment?
   - Does it update a comparison?
   - Does it establish or update an invariant (a standing constraint with an enforcement story and a removal cost)?
5. **Route contributions directly to affected typed artifacts.** Update or create those artifacts. Do not force contributions through construct pages first. If the source contradicts existing vault content, the contradiction is adjudicated here — in the downstream synthesis or assessment, citing both sources — never inside the source-capture.
6. **Backlink audit** — scan existing wiki pages for mentions of concepts from this source. Add root-relative wikilinks such as `[[wiki/topic/constructs/page-name]]` in both directions where missing.
7. **Re-derive confidence** on downstream pages the source touched: check each page's `confidence` against the derivation ceiling in `schema/page-format.md` (a new corroborating or contradicting source can raise or lower it).
8. **Update `wiki/index.md`** — add new entries, grouped by topic, subtopic when present, then type.
9. **Refresh the local search index** — run `scripts/qmd-index.sh` (best-effort; safe to skip if it fails, e.g. embedding model downloads blocked by network policy — see `wiki/agent-context/subtopics/retrieval/entities/qmd.md`). The index itself is not committed; the script is what every agent/session reruns to reproduce it.
10. **Append to `wiki/log.md`** — add a bullet under today's date heading (create the heading at the top if it doesn't exist). Format: `* **Ingest**: Processed [Source Title](wiki/topic/sources/source-slug.md) from <origin>. Created/updated pages X, Y, Z.` Note any contradictions found.

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

List the downstream artifacts this source may create or update.

Examples:
- `[[wiki/intent-compiler/designs/intent-compiler-design]]` — updates design model
- `[[wiki/intent-compiler/constructs/process-weights]]` — defines or updates construct
- `[[wiki/intent-compiler/assessments/validation-assessment]]` — affects validation status

## Extraction Notes

Use sparingly for source emphasis, ambiguity, OCR/PDF issues, or interpretation boundaries.
```

The sections from Core Contribution through Methodology are faithful reportage of the source. Limitations and Caveats, Reliability Notes, and Extraction Notes are the capturer speaking. Keep the two groups structurally separate.

## Key Rules

- **Source capture is source-isolated (epistemic, not navigational).** The body records only what this source says; pointers to other pages are fine, adjudication is not.
- **Assign `evidence` at capture time.** Source type gives the starting tier; Reliability Notes may justify a downward adjustment.
- **Contribution routing fans out after source capture.** Each contribution goes directly to the affected artifact type.
- **Do not force every contribution through construct pages.** A source may update a synthesis, design, or assessment directly.
- **Never edit existing files in `raw/` in place.** Fidelity is what makes re-capture audits and upstream change detection possible — the two purposes `raw/` exists for.
- If a topic directory doesn't exist yet, create it.
- Place new pages in the type folder that matches frontmatter: `sources/`, `constructs/`, `entities/`, `syntheses/`, `designs/`, `assessments/`, `comparisons/`, or `invariants/`.
- Create or reuse a subtopic under `subtopics/` only when the narrower cluster materially improves navigation.
- If a page already covers this concept, update it rather than creating a duplicate.
- Note contradictions explicitly in downstream pages: cite both the new and existing source.
- Set downstream `confidence` per the derivation rules in `schema/page-format.md` — never above the ceiling the cited sources support.

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
