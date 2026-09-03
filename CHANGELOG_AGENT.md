# AGENT CHANGELOG

Operational record of changes made by AI agents under Phuchello Agent Workflow. Entries are concise and audit-focused.

---

## 2026-09-03 — Pre-merge defect remediation (M-01, M-02, M-03) on v1.1-release-candidate
- **Commit**: pending (`fix: remediate pre-release defects on v1.1-release-candidate`)
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

---

## 2026-09-03 — Blind public product & integration review (GLM 5.3)
- **Commit**: `b2bdaa680cad403418a8bc86d300237191a083b5`
- **Scope**:
  - Executed independent, blind, zero-trust audit across Theory Handbook, Practice Handbook, and Quartz Knowledge Garden on isolated review branch `v1.1-integration-review`.
  - Conducted academic correctness audit: verified formal definitions, division empty-set theorem ($R \div \emptyset = \pi_X(R)$), outer candidate domain separation in SQL, Armstrong axioms, 7-class IT004 RBTV taxonomy, and BCNF/3NF standard definitions.
  - Executed live runnability audit on Microsoft SQL Server 2025 Developer Edition: verified `00_create_training_db.sql` through `06_test_cases.sql` and `reset.sql` (tests A–H verified with exact error codes).
  - Executed runtime browser and responsive layout audit: verified zero horizontal overflow at 390px, 900px, 1440px across key routes, verified search interaction, and verified PDF downloads.
  - Audited integration topology: confirmed `v1.1-quartz-garden` is a direct linear fast-forward descendant of `main` (`6ccf5a408934ab93760ac3242511beb43b05f24f`) with zero merge conflicts.
  - Identified 2 MAJOR pre-integration defects: M-01 (obsolete root `README.md` linking to legacy `CamNang` PDF) and M-02 (incompatible `.github/workflows/pages.yml` deploying `book/` instead of `garden/public`).
  - Produced comprehensive audit report in `reports/v1.1_glm53_blind_integration_review.md`, set status to `integration_review_blocked`, completed review task contract, and reconciled `TODO.md`.
- **Verification**:
  - `scripts/agent/validate_state.py`: PASS (9 criteria synchronized).
  - `scripts/validate.py`: PASS (6/6).
  - `scripts/validate_garden_d2.py`: PASS (all 14 checks).
  - `scripts/agent/check_links.py`: PASS (2,819 links checked, 0 broken).
  - `scripts/agent/verify.ps1 -Mode Full`: PASS (all 6/6 checks).
  - `git diff --check`: PASS (zero trailing whitespace).
  - Product diff = ZERO (only allowed review/workflow files modified).
- **Next Checkpoint**: Remediate findings M-01 and M-02, then proceed to fast-forward merge to `main`.

---

## 2026-09-03 — Milestone D2 freeze patch and final safe_product_commit checkpoint
- **Commit**: `be34ef3ef79956d9c1c2541782cabc82e66d0c6e` (safe_product_commit checkpoint)
- **Scope**:
  - Replaced unsupported provenance phrase "ma trận đề thi chính thức" in `theory/rbtv-impact.md` with evidence-safe phrasing: "slide bài giảng chính thức (`LOC-LEC-LONG-CH05`) và bản đồ mẫu đề thực chứng Phase A".
  - Extended `OVERCLAIM_PATTERNS` in `scripts/validate_garden_d2.py` to mechanically reject `ma trận đề (thi )?chính thức`.
  - Matched independent candidate projection in `theory/division.md` to actual selected attributes ($\pi_{\text{StudentId, FullName}}(C)$), and qualified empty-set aggregation failure so it is not falsely claimed when candidate domain is itself empty.
  - Rebuilt Quartz production site (109 emitted files in 1.0s), verified 2,819 internal links (0 broken), and regenerated fresh visual evidence across all 10 review captures.
  - Finalized D2 task contract (all 14 criteria passed), materialized `safe_product_commit: be34ef3ef79956d9c1c2541782cabc82e66d0c6e` in `.agent/STATE.yaml`, and transitioned workflow to integration review.
- **Verification**:
  - `scripts/agent/validate_state.py`: PASS (14 criteria synchronized).
  - `scripts/validate.py`: PASS (6/6).
  - `scripts/validate_garden_d2.py`: PASS (all 14 checks).
  - `scripts/agent/check_links.py`: PASS (2,819 links checked, 0 broken).
  - `scripts/agent/verify.ps1 -Mode Full`: PASS (all 6/6 checks).
  - `git diff --check`: PASS (zero trailing whitespace).
- **Next Checkpoint**: Human mentor integration review and authorization on branch `v1.1-quartz-garden`.
