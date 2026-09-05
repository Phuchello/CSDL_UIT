# AGENT CHANGELOG

Operational record of changes made by AI agents under Phuchello Agent Workflow. Entries are concise and audit-focused.

---

## 2026-09-05 — v1.2 Learning System Design Synchronization
- **Branch**: `v1.2-learning-system-design` (PR #5)
- **Scope**:
  - Synchronized PR #5 with current `main` baseline (`77951417b5e82b7dbe92748e7462b1680a21d5b2`) via `git merge origin/main`.
  - Preserved all v1.1.1 runtime fixes: YAML frontmatter transformer, Vietnamese-first UI/titles, KaTeX math, light-default theme, system sans typography, white palette, breadcrumb dedup, architectural mobile overflow, and $F_c$ notation preservation.
  - Retained core v1.2 design architecture: static-first, no chatbot/AI tutor, localStorage-only learner state, learning loop (Map → Understand → Trace → Retrieve → Practice → Diagnose → Review), explicit Learning Mode vs Reference Mode, worked → faded → cold progression, and skill-based mastery model.
  - Addressed live Knowledge Garden content-depth finding: confirmed Candidate Keys (`theory/candidate-keys`) as the mandatory first vertical slice; updated `IMPLEMENTATION_PLAN.md` with all 16 required unit blocks, 11 reusable primitives, and learner outcomes (sufficiency + minimality distinction); captured 6 canonical Candidate Keys error classes in `CONTENT_CONTRACT.md`.
  - Reconstructed agent operational state files (`.agent/STATE.yaml`, `.agent/task-contract.json`).
- **Verification**:
  - State validation: `scripts/agent/validate_state.py` (PASS).
  - Validation suite: `scripts/validate_garden_render.py` (PASS), `scripts/validate_garden_d2.py` (PASS), `scripts/agent/check_links.py` (PASS), `scripts/validate.py` (PASS), `scripts/validate_practice_static.py` (PASS), `verify.ps1 -Mode Fast` (PASS).
- **Release Safety**: Main untouched, Pages deployment remains workflow_dispatch only, v1.1.1/v1.2.0 tags untouched, no Candidate Keys implementation files added, no academic content or PDFs changed. PR #5 remains draft awaiting mentor review.

---

## 2026-09-05 — Quartz Reading & Visual UI Polish
- **Branch**: `v1.1.1-reading-polish`
- **Scope**:
  - Repaired wikilink math syntax leaks across notes (`[[...|$X^+$]]` -> `[[...|X⁺]]`, 0 math delimiters in wikilinks).
  - Enforced light-mode default on initial visit via `lightDefaultDarkmodeScript` while preserving user toggle functionality and `localStorage` persistence.
  - Updated Quartz palette to clean white `#ffffff` with subtle sidebar `#fafbfc` and accessible text `#1f2937` / `#111827`.
  - Modernized typography to dependency-free system sans stack across headers, body, and site title (removed Georgia/Times New Roman serif overrides).
  - Balanced desktop side rails (300px width, 210px interactive graph height) and prevented horizontal overflow on 390px mobile viewports.
  - Deduplicated current page title in breadcrumbs (`rootName: "Trang chủ"`, `showCurrentPage: false`).
  - Extended `scripts/validate_garden_render.py` with reading UI regression gates.
- **Verification**:
  - Local verification: `scripts/validate_garden_render.py` (PASS), `scripts/validate_garden_d2.py` (PASS), `scripts/agent/check_links.py` (PASS, 2,819 links checked, 0 broken), `scripts/validate.py` (PASS), `scripts/validate_practice_static.py` (PASS), `verify.ps1 -Mode Fast` (PASS).
  - GitHub Actions CI on PR #7: Run `33945714588` completed with status `success` in 30s on `ubuntu-latest`.
- **Review Remediation (PR #7 Findings)**:
  - Restored academic notation $F_c$ outside wikilink alias in `garden/content/theory/index.md` (`[[theory/minimal-cover|...]] $F_c$`).
  - Removed broad `overflow-x: hidden` clipping on `body`, `.page`, and `article` in `custom.scss`; implemented architectural wide-element constraints (`table` horizontal scroll, `pre/code` touch scroll and inline word break, `img/svg/canvas/graph` `max-width: 100%`, `.katex-display` horizontal scroll, flex/grid `min-width: 0`).
  - Extended `scripts/validate_garden_render.py` with gates ensuring zero broad clipping and enforcing architectural constraints and $F_c$ preservation.
  - GitHub Actions CI on PR #7 remediation head (`2db5984`): Run `33951223266` completed with status `success` in 24s on `ubuntu-latest`.
- **Release Safety**: Main branch untouched, Pages deployment remains workflow_dispatch only, v1.1.1 tag untouched, no bulk academic changes. PR #7 remains open awaiting mentor release authorization.

---

## 2026-09-05 — Quartz YAML frontmatter parsing hotfix
- **Branch**: `v1.1.1-frontmatter-fix` (PR #6)
- **Root Cause**: The vendored Quartz parser registered `remark-parse` and configured community transformers but no YAML frontmatter transformer, so metadata was rendered as ordinary Markdown body content and document titles fell back to `Không có tiêu đề`.
- **Fix**: Added a built-in `FrontMatter` transformer before configured plugins. It parses the leading YAML mapping into `file.data.frontmatter` and removes the YAML node from the Markdown AST.
- **Regression Gate**: Extended `scripts/validate_garden_render.py` to inspect generated titles, raw frontmatter leakage, `Trang chủ` breadcrumbs, and existing KaTeX targets.
- **Verification**:
  - Local verification: Quartz build (59 HTML files emitted), core validator (`validate.py`, 6/6 checks PASS), practice static consistency (`validate_practice_static.py`, PASS), Garden D2 validator (`validate_garden_d2.py`, 15/15 PASS), render smoke (`validate_garden_render.py`, PASS), link crawl (`check_links.py`, 2,937 links, 0 broken, PASS), and state validation (`validate_state.py`, PASS).
  - GitHub Actions CI on PR #6: Run `33942734334` completed with status `success` in 31s on `ubuntu-latest`.
  - Mentor Review: All 13 gates PASS (Root cause, Architecture fix, Generated HTML, Frontmatter leak, Browser title, Breadcrumb, KaTeX, Internal links, GitHub CI, Academic scope, main untouched, Pages untouched, v1.1.1 tag untouched).
- **Release Safety**: No Pages deployment, no `v1.1.1` tag, no `v1.2` implementation, no bulk academic changes. PR #6 remains open awaiting mentor release authorization (`MERGE WAIT`).

## 2026-09-03 — Full Vietnamese-first Localization QA Pass on v1.1.1-vietnamese-ui
- **Scope**:
  - Localized human-facing navigation, frontmatter titles, H1s, and explicit wikilink aliases across all 57 Markdown notes in `garden/content/**/*.md` to Vietnamese-first while preserving standard English technical terms in parentheses (e.g. `Khóa ứng viên (Candidate Keys)`, `Phủ tối thiểu (Minimal Cover)`, `Đại số quan hệ (Relational Algebra)`).
  - Preserved natural product and operator names unchanged (`SQL Server`, `T-SQL`, `JOIN`, `GROUP BY`, `NULL`, `3NF`, `BCNF`, `Double NOT EXISTS`).
  - Preserved all 57 existing file paths and slugs identical.
  - Configured `@quartz-community/breadcrumbs` with `rootName: "Trang chủ"` in `garden/quartz.config.yaml`.
  - Extended `scripts/validate_garden_d2.py` with deterministic regression checks asserting Vietnamese-first title prefixes on major section folders and core conceptual notes.
  - Rebuilt Quartz, verified 0 broken links in 2,937-link crawl, confirmed render smoke and KaTeX math integrity, and audited representative rendered pages.
- **Verification**:
  - `scripts/validate_garden_d2.py`: ALL 15 CHECKS PASS.
  - `scripts/validate_garden_render.py`: PASS.
  - `scripts/agent/check_links.py`: PASS (0 broken links).
  - `scripts/agent/verify.ps1 -Mode Full`: PASS.

---

## 2026-09-03 — Release-gate hardening & CI validation on v1.1-release-candidate
- **Commit**: `e1bd46a` (`fix: use resilient heading marker for Chapter 7 in PDF layout validator`), `c512b14` (`chore: harden release gates and decouple Pages deployment`)
- **Scope**:
  - Decoupled GitHub Pages deployment from `main` pushes in `.github/workflows/pages.yml`; configured as `workflow_dispatch` only (human-authorized publication gate).
  - Updated `docs/BUILD.md` to document the canonical 4-gate release sequence: 1. CI validation on ubuntu-latest $\rightarrow$ 2. Fast-forward merge to `main` $\rightarrow$ 3. Tag & Release $\rightarrow$ 4. Explicit human-authorized Pages dispatch.
  - Added `deployment_gate` and `github_ci_gate` to `.agent/task-contract.json` and `.agent/STATE.yaml`.
  - Maintained historical draft release v1.0.0 untouched.
  - Opened PR #2 from `v1.1-release-candidate` to `main` for CI validation only.
  - Diagnosed and resolved OS-dependent character spacing in PDF text extraction during `scripts/validate.py` by using resilient heading marker `7.1 Tổng quan môi trường` and NFC normalization.
  - Verified GitHub Actions run `33743104644` on `ubuntu-latest`: ALL STEPS PASSED in 28s (Theory & Practice HTML build, Core validator, Practice static consistency, Garden assets copy, Garden npm ci, Garden D2 contract validator, Quartz build, Link crawl).
- **Verification**:
  - GitHub Actions run `33743104644`: PASS (28s, 0 errors).
  - PR #2 checks: PASS (`validate` check green).
  - `scripts/agent/validate_state.py`: PASS (11 criteria synchronized).
  - `git diff --check`: PASS (zero trailing whitespace).
- **Next Checkpoint**: Mentor review of PR #2 before authorized fast-forward merge to `main`.

---

## 2026-09-03 — Pre-merge defect remediation (M-01, M-02, M-03) on v1.1-release-candidate
- **Commit**: `ef942d418f555e7ee48d54f72a402a67ceb9a255`
- **Scope**:
  - **M-01 (Public Surface)**: Rewrote root `README.md` for the v1.1 product suite: Theory Handbook (64p), Practice Handbook (71p), and Quartz Knowledge Garden. Updated public badges, 3-pillar architectural map, quick start commands, repository structure, and Phase A provenance references. Clarified historical status of v1.0 `CamNang` PDF without deleting the file.
  - **M-02 (Release Infrastructure)**: Replaced `.github/workflows/pages.yml` with Node 22 Quartz deployment pipeline running `scripts/copy_garden_assets.mjs` and uploading `garden/public`. Updated `.github/workflows/validate.yml` to test handbook HTML compilations, core validators, static practice consistency, Garden D2 content contract, Quartz site build, and link checks. Updated `docs/BUILD.md` to distinguish handbook compilation from canonical Quartz Pages builds.
  - **M-03 (Canonical Trigger Precedence)**: Factual correction: In SQL Server, foreign key constraints are checked BEFORE AFTER triggers; deleting a department head is blocked declaratively by `FK_tr_departments_head` (Msg 547) before any AFTER DELETE trigger runs. Removed dead/unreachable DELETE enforcement from `practice/sql/05_triggers.sql` (`trg_tr_employees_head_guard`), retained set-based `UPDATE(DeptId)` enforcement (`THROW 51003`). Updated `practice/sql/06_test_cases.sql` (Test F), `practice/EXAMPLE_REGISTRY.md` (`TRG-F`), `practice/chapters/13_debugging_expanded.html`, `garden/content/practice/multi-row-trigger.md`, `scripts/validate_garden_d2.py`, and `scripts/validate_practice_static.py`.
  - **Practice PDF Regeneration & Asset Copy**: Recompiled `practice/index.html`, regenerated `dist/IT004_CSDL_UIT_ThucHanh_VoTrongPhuc.pdf` via Playwright, normalized metadata via `scripts/normalize_practice_pdf.py` (71 pages A4 verified), and synchronized Garden PDF assets via `scripts/copy_garden_assets.mjs`.
  - Rebuilt Quartz production site (109 files emitted), validated 2,819 internal links (0 broken), and confirmed live SQL Server 2025 execution of `reset.sql`, triggers, and tests A–H.
- **Verification**:
  - `scripts/agent/validate_state.py`: PASS (9 criteria synchronized).
  - `scripts/validate.py`: PASS (6/6).
  - `scripts/validate_practice_static.py`: PASS (all checks, runtime sqlcmd detected).
  - `scripts/validate_garden_d2.py`: PASS (all 14 checks).
  - `scripts/agent/check_links.py`: PASS (2,819 links checked, 0 broken).
  - `scripts/agent/verify.ps1 -Mode Full`: PASS (all 6/6 checks).
  - `git diff --check`: PASS (zero trailing whitespace).
  - Live SQL Server 2025 execution: PASS (Test F Msg 547 declarative FK; Test D Msg 51003 trigger; Test A & G PASS).
- **Next Checkpoint**: Mentor review of `v1.1-release-candidate` before fast-forward merge to `main`.
