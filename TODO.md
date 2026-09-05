# TODO — CSDL_UIT

## Completed Milestones
- [x] Phase A: Research Snapshot Frozen (`v1.1-editorial-practice` @ `6aef91e`)
- [x] Phase B2: Theory Handbook v1.1 Frozen (`v1.1-theory-redesign` @ `61eb5c8`)
- [x] Phase C1: Practical Handbook Architecture & Proof Frozen (`v1.1-practice-handbook` @ `f7dd840`)
- [x] Phase C2: Full Practical Handbook Frozen (`v1.1-practice-handbook` @ `59c519b`)
- [x] Phase D1: Knowledge Garden Architecture Proof Frozen (`v1.1-knowledge-garden` @ `922afe07bea7f28abf30c49054159a09a31be743`)
- [x] Phase D2: Quartz Knowledge Garden Production Candidate Built & Verified (`v1.1-quartz-garden` @ `be34ef3ef79956d9c1c2541782cabc82e66d0c6e`)
- [x] Workflow Migration: Phuchello Agent Workflow v2 Adopted
- [x] Integration Review: Independent Blind Audit Completed (`v1.1-integration-review` @ `reports/v1.1_glm53_blind_integration_review.md`)
- [x] Pre-merge Defect Remediation (`v1.1-release-candidate`)
- [x] Release-gate Hardening and GitHub CI validation
- [x] Gate 2: fast-forward release candidate to `main` @ `ad0ef293d0b85ba59de8ffad8966bd0d40720580`
- [x] Gate 3: tag and publish immutable `v1.1.0` at the same commit
- [x] Gate 4: manual Pages deployment (`workflow_dispatch` run `33761760360`, SUCCESS)

## Completed — v1.1.1 Maintenance
- [x] Reproduce live math-rendering defect from deployed v1.1.0 artifact
- [x] Identify root cause: `@quartz-community/latex` disabled in `garden/quartz.config.yaml`
- [x] Enable KaTeX rendering on `v1.1.1-maintenance`
- [x] Add post-build `scripts/validate_garden_render.py` regression smoke gate
- [x] Wire render smoke into `.github/workflows/validate.yml`
- [x] Open maintenance PR #3 to `main`
- [x] GitHub-hosted CI passes with render smoke enabled (runs `33763735969` and `33764039396`)
- [x] Apply duplicate H1 / redundant TOC cleanup without changing Garden prose
- [x] Replace nested desktop TOC/backlinks scrollbars with one context-rail scrollbar
- [x] Shorten visible left-rail site title
- [x] Merge PR #3 to `main` (`5e4b0c17ec709aabe999a9d922c6679c3a3797ca`)
- [x] Human-authorized Pages deployment for the maintenance fix (`workflow_dispatch` run `33765891591`, SUCCESS)

## Active Queue — v1.1.1 Vietnamese-first Localization QA Pass (`v1.1.1-vietnamese-ui`)
- [x] Audit all 57 notes in `garden/content/**/*.md`
- [x] Localize frontmatter titles and first H1s to Vietnamese-first while preserving technical English in parentheses
- [x] Localize explicit wikilink display aliases across notes
- [x] Localize breadcrumbs root to `Trang chủ`
- [x] Preserve all existing file paths and slugs unchanged
- [x] Preserve formulas, SQL, canonical provenance IDs, Theory/Practice handbooks, and PDFs
- [x] Extend `scripts/validate_garden_d2.py` with deterministic Vietnamese title prefix regression checks
- [x] Rebuild Quartz and run full verification suite
- [x] Inspect representative rendered pages
- [x] Open PR #4 to `main`
- [x] GitHub-hosted CI passed on original localization head (`33769457047`)
- [x] Final polish: remove remaining English-only visible aliases (`Closure`, `Setup`, `Date conversion`, `Multi-row trigger`, `Debugging`, `Exam patterns`, etc.)
- [x] Final polish: hide reader-facing `Properties`/frontmatter panel
- [x] Final polish: hide modified-date/read-time content metadata
- [x] Final polish: change browser suffix from `Knowledge Garden` to `Vườn tri thức`
- [x] Final functional verification on `ff682dc86552c355113cc1c8e13a85f9042db08c`: Actions run `33771223152` SUCCESS
- [x] Confirm bookkeeping-only head `a96002b433a071378b3cc3a78f060c24a555d7f5` remained green: Actions run `33771348905` SUCCESS
- [x] Correct RBTV Impact Matrix notation to `+`, `-`, `+(Thuộc tính)` and reserve `-(*)` for an operation that cannot be performed
- [x] Verify RBTV correction on functional head `b3839faddeaef4234b3b7c4543976ca6833eb1a8`: Actions run `33938087301` SUCCESS
- [x] Human mentor review of PR #4
- [ ] Merge PR #4 only after explicit authorization
- [ ] Human-authorized Pages deployment after merge
- [ ] Desktop + mobile live visual smoke after deployment
- [ ] Decide whether to tag `v1.1.1`

## Active Queue — v1.1.1 YAML Frontmatter Hotfix (`v1.1.1-frontmatter-fix`)
- [x] Prove the vendored Quartz parser had no YAML frontmatter transformer
- [x] Register a built-in transformer that preserves metadata and removes YAML from the Markdown AST
- [x] Add generated-HTML title, raw-frontmatter, breadcrumb, and KaTeX regression checks
- [x] Build the Garden successfully and inspect generated representative pages
- [x] Install Python/PyYAML and run render, link, and full verification gates (all 6 repo validators PASS)
- [x] Commit, push, open PR #6, and await GitHub CI (run `33942734334` SUCCESS)
- [x] Mentor review: all 13 gates PASS (Root cause, Architecture fix, Generated HTML, Frontmatter leak, Browser title, Breadcrumb, KaTeX, Internal links, GitHub CI, Academic scope, main untouched, Pages untouched, v1.1.1 tag untouched)
- [ ] Merge PR #6 only after mentor release authorization (WAIT)
- [ ] Human-authorized Pages deployment after merge
- [ ] Desktop + mobile live visual smoke after deployment

## Active Queue — v1.1.1 Reading and Visual UI Polish (`v1.1.1-reading-polish`)
- [x] Audit live site typography, contrast, and layout issues
- [x] Repair wikilink math syntax leaks (`[[...|$X^+$]]` -> `[[...|X⁺]]`)
- [x] Enforce light-mode default on initial visit while preserving manual dark toggle
- [x] Update Quartz palette to true clean white `#ffffff` with subtle sidebar `#fafbfc`
- [x] Modernize typography to dependency-free system sans across headers and body
- [x] Balance desktop side rails (300px panel, 210px graph) and prevent mobile overflow
- [x] Deduplicate current page title from breadcrumbs
- [x] Extend `scripts/validate_garden_render.py` with reading UI regression gates
- [x] Restore academic notation F_c outside wikilink alias in garden/content/theory/index.md
- [x] Replace broad mobile overflow clipping (overflow-x: hidden on body/.page/article) with architectural element-level constraints (table, pre/code, SVG/canvas/graph, math display, flex/grid min-width: 0)
- [x] Update render regression gate in scripts/validate_garden_render.py to enforce architectural constraints and reject global clipping
- [x] Commit, push branch `v1.1.1-reading-polish`, and update PR #7
- [x] Verify NEW exact-head GitHub Actions CI run (run 33951223266 SUCCESS in 24s)
- [ ] Mentor review and release authorization

## Parallel Design — v1.2 Learning System
- [x] Draft design architecture on `v1.2-learning-system-design`
- [x] Open Draft PR #5
- [x] CI run `33770162203` PASS
- [ ] Do not implement Learning Engine until v1.1.1 localization release path is reviewed

## Deferred Maintenance
- [ ] Triage Garden npm audit findings separately (1 low, 2 high observed during v1.1.0 Pages build)
