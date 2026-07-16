---
name: create-design-dossier
description: Create or extend an OKF-conformant Trellis Design dossier. Use when a user asks to design a system, feature, protocol, workflow, or change; compare design alternatives; or add implementation phases after approving the design work.
---

# Create a Design Dossier

1. Read the complete Design specification selected by the project. In this
   repository, use `../../../specs/design.md`.
2. Establish the target's motivation, goals, non-goals, terminology, behavior,
   constraints, and open questions from the user's request and project context.
3. Create only `<slug>/design.md` by default. Use
   `../../templates/design/design.md` as an editable starting point.
4. Add a progressive enhancement only when the design needs it:
   - `phases/` requires numbered phases plus `later.md`, covering the target;
   - `obligations.md` records consequences outside the target boundary;
   - `alternatives/` requires at least two candidates plus `evaluation.md`.
5. Keep `design.md` authoritative. Phases scope it; alternatives do not override
   it; evaluation may state that judgment remains unresolved.
6. Use relative Markdown links and update timestamps after meaningful changes.
7. Run `python3 ../../scripts/lint.py design <path-to-dossier>` when available.
8. Present the target and any enhancements for review. Do not begin
   implementation unless the user also requested it.
