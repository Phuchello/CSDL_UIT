# D1 Human Review Guide

Use this proof as a focused architecture review, not a full handbook audit.

1. Open `site/index.html` (or serve `site/` locally) and verify the home answers what the garden is, what to learn next, Theory vs Practice, weak-topic recovery, and exam entry.
2. Open `#/theory/division` and confirm the three meaningful edges: Double NOT EXISTS, Lab 03, and wrong candidate domain.
3. Open `#/practice/multi-row-trigger` and follow the RBTV → impact table → `inserted`/`deleted` chain.
4. Use Search with `phép chia`, `trigger`, and `NULL`; check category tags and no-backend behavior.
5. Resize to a narrow viewport; open/close Menu, tab through controls, and confirm focus outlines.
6. Check the Sources page for exact URLs and local paths. Student/community material must not be presented as official.
7. Confirm links to both PDFs are repository-local only and that no raw exam attachment is present under `site/`.
8. Run lightweight checks: HTML/script presence, route references, no horizontal overflow in the CSS contract, and `git diff --check`.

## Acceptance notes

- This is a representative proof, not the complete site.
- No Quartz dependency is required for this proof; a future implementation may port the same slugs/content model to Quartz.
- Keep `book/`, `practice/`, and `research/v1.1_phase_a/` untouched while evaluating.
