---
name: query-trellis-wiki
description: Search and synthesize answers from a Trellis Wiki with source-linked citations. Use when a user asks a question that should be answered from an existing Trellis Wiki corpus.
---

# Query a Trellis Wiki

1. Do not load the complete Wiki specification for an ordinary query. Read
   `wiki/index.md` and `wiki/overview.md` before searching broadly. If the
   question requires interpreting conformance or type semantics, ensure the
   selected specification is in active context, resolving it from
   `trellis.wiki.specification`, an explicit user selection, or the
   repository-local specification. Reload it after compaction if semantic work
   continues.
2. Locate relevant topic pages using available text or indexed search. Treat
   optional search tooling as an optimization; direct file search must work.
3. Read only the pages and raw sources needed to answer the question. Prefer
   source captures for what one source says and synthetic pages for integrated
   conclusions.
4. Check evidence, confidence where defined, contradictions, timestamps, and
   source independence before drawing a conclusion.
5. Answer with links to the relevant wiki pages or original resources. Clearly
   distinguish sourced findings from inference.
6. If the answer reveals reusable knowledge missing from the wiki, offer to
   save it using the appropriate page type; do not write it without authority.
