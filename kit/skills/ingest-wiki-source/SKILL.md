---
name: ingest-wiki-source
description: Preserve a source in wiki/raw, create a source-isolated capture, and route durable contributions into a Trellis Wiki. Use when a user provides a paper, article, chat, repository, dataset, or other source to ingest or refresh.
---

# Ingest a Wiki Source

1. Read the complete Wiki specification selected by the project. In this
   repository, use `../../../specs/wiki.md`.
2. Inspect `wiki/index.md` and `wiki/overview.md`, then locate the relevant topic
   and existing pages. Reuse an existing topic or subtopic unless a narrower
   named cluster materially improves navigation.
3. Preserve a new immutable snapshot under `wiki/raw/`. Keep earlier snapshots
   when a resource changes. Markdown snapshots receive the `raw-source`
   envelope; binary sources retain their original format. Preserve readable web
   bodies without navigation or advertising, prefer verbatim chat exports and
   declare any condensation, and retain original PDFs alongside text
   extractions when both are acquired.
4. Create one `source-capture` page for the meaningful source using the exact
   required headings. Report only what that source says; keep vault-wide
   reconciliation out of it. Navigational `related` links are allowed.
5. Assign `evidence` from within-source signals. Explain material caveats in
   Reliability Notes and preserve substantive references in Important
   References and Linked Material.
6. Present the capture and its routing candidates before downstream writes
   unless the user requested autonomous ingest.
7. Review Contribution Routing against the existing wiki. Update or create an
   interpretive page only when the contribution changes knowledge the wiki will
   reason with again. Route directly to the affected types; do not require a
   construct intermediary. Do not create decisions or invariants without user
   request or ratification.
8. Detect contradictions against existing pages and adjudicate them in a
   synthesis or assessment, citing both sources. Never reconcile them inside
   the source capture.
9. Maintain relative links and backlinks, re-evaluate confidence on affected
   constructs and entities, update timestamps and the root index, and append a
   newest-first entry when the optional log is installed.
10. Run `python3 ../../scripts/lint.py wiki <path-to-wiki>` when available, then
    summarize the snapshot, capture, routed changes, contradictions, and
    anything deliberately left unpromoted.
