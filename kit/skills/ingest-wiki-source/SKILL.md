---
name: ingest-wiki-source
description: Preserve a source in wiki/raw, create a source-isolated capture, and route durable contributions into a Trellis Wiki. Use when a user provides a paper, article, chat, repository, dataset, or other source to ingest or refresh.
---

# Ingest a Wiki Source

1. Read the complete Wiki specification selected by the project. In this
   repository, use `../../../specs/wiki.md`.
2. Inspect `wiki/index.md` and `wiki/overview.md`, then locate the relevant
   topic and existing pages.
3. Preserve a new immutable snapshot under `wiki/raw/`. For a changed resource,
   keep the earlier snapshot and create a new one. Add the `raw-source`
   envelope to Markdown snapshots.
4. Create one `source-capture` page using the exact required headings. Report
   only what that source says; keep vault-wide reconciliation out of it.
5. Assign `evidence` from within-source signals and explain material caveats in
   Reliability Notes.
6. Review Contribution Routing against the existing wiki. Update or create
   interpretive pages only when the contribution changes reusable knowledge.
7. Re-evaluate `confidence` on affected constructs and entities. Express
   synthetic uncertainty in synthesis, assessment, and comparison bodies.
8. Maintain relative links, backlinks, timestamps, and the root index.
9. Run `python3 ../../scripts/lint.py wiki <path-to-wiki>` when available.
10. Summarize the raw snapshot, capture, routed changes, contradictions, and
    anything deliberately left unpromoted.
