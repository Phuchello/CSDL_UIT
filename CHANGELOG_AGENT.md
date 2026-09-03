# AGENT CHANGELOG

Operational record of changes made by AI agents under Phuchello Agent Workflow. Entries are concise and audit-focused.

---

## 2026-09-03 — Milestone D2 contract hardening and mentor review remediation
- **Commit**: pending (`fix(garden): harden d2 graph chain core depth trigger and pdf contract`)
- **Scope**:
  - Enforced deterministic mandatory graph-chain validation across `theory/division` ↔ `theory/double-not-exists` ↔ `practice/lab-03` ↔ `errors/wrong-universal-candidate` using verified in-body Markdown edges.
  - Deepened all remaining skeletal core notes (`relational-algebra`, `division`, `double-not-exists`, `rbtv-impact`, `functional-dependencies`, `closure`, `3nf`, `bcnf`, `lossless-decomposition`) to full standalone teaching depth with formal definitions, algorithm steps, and dry-run tables.
  - Clarified Trigger NULL case: explicitly distinguished schema-level `DeptId NOT NULL` DDL rejection from defensive trigger check `i.DeptId IS NULL`.
  - Adopted strict single public PDF lowercase naming convention, copying exactly one file per handbook and adding built-output validation for exactly two PDFs.
  - Eliminated provenance overclaims: distinguished community-mirror artifacts from official syllabus exams; replaced "luôn xuất hiện" and "bắt buộc phải dùng Trigger" with evidence-safe phrasing.
  - Hardened `scripts/validate_garden_d2.py` with mandatory chain edges, core depth thresholds, trigger schema distinction, provenance overclaim scans, and built output PDF checks.
  - Rebuilt Quartz (109 emitted files), checked 2,810 internal links (0 broken), and regenerated all 10 review captures in `dist/review/v1.1_quartz/`.
- **Verification**:
  - `scripts/agent/validate_state.py`: PASS (11 criteria synchronized).
  - `scripts/validate.py`: PASS (6/6).
  - `scripts/validate_garden_d2.py`: PASS (all checks).
  - `scripts/agent/check_links.py`: PASS (2,810 links checked, 0 broken).
  - `scripts/agent/verify.ps1 -Mode Full`: PASS (all 6 checks).
  - `git diff --check`: PASS (zero trailing whitespace).
- **Next Checkpoint**: Human mentor review and authorization on branch `v1.1-quartz-garden`.

---

## 2026-09-03 — Milestone D2 content-contract correction
- **Commit**: `2685729d0712d9133ba3eeabd051bc4354b989da`
- **Scope**:
  - Eliminated all invented source IDs (`TECH-MS*`, `UIT-E*`), replacing them with canonical IDs (`TECH-A01`–`TECH-A11`, `UIT-O01`–`UIT-O11`, `EXAM-*`, `PRAC-*`, `LOC-LEC-*`) derived strictly from frozen Phase A ledgers.
  - Resolved all ambiguous and broken `related` frontmatter targets across the garden.
  - Added rich Markdown `[[wikilinks]]` to note bodies across all 57 notes (zero notes without body graph links).
  - Deepened core theory notes (`3nf`, `bcnf`, `candidate-keys`, `minimal-cover`, `lossless-decomposition`, `closure`, `functional-dependencies`).
  - Restored canonical multi-row trigger event discrimination contract in `practice/multi-row-trigger.md` matching `practice/sql/05_triggers.sql`.
  - Enforced case-safe dual-PDF navigation contract (removed legacy `CamNang` link; lowercase URL paths).
  - Hardened `scripts/validate_garden_d2.py` with comprehensive provenance, link, trigger, and PDF assertions.
  - Generated 10 fresh review screenshots into `dist/review/v1.1_quartz/` using headless browser capture.
- **Verification**:
  - `scripts/agent/validate_state.py`: PASS.
  - `scripts/validate.py`: PASS (6/6).
  - `scripts/validate_garden_d2.py`: PASS.
  - `scripts/agent/check_links.py`: PASS (2684 links checked, 0 broken).
  - `scripts/agent/verify.ps1 -Mode Full`: PASS (all 6 checks).
- **Next Checkpoint**: Human mentor review and authorization on branch `v1.1-quartz-garden`.

---

## 2026-09-03 — Workflow v2 guardrail hardening
- **Commit**: `2625d3b8e17baaa9872297c958e766574c169120`
- **Scope**:
  - Corrected `docs/index.md` practice fixture paths to match canonical scripts (`01_schema.sql` through `reset.sql`).
  - Replaced absolute `file:///` links in `docs/index.md` with repository-relative Markdown links.
  - Hardened `scripts/agent/verify.ps1` Full mode with deterministic asset preparation (`scripts/copy_garden_assets.mjs`) and explicit `Push-Location garden` execution.
  - Added semantic cross-checks to `scripts/agent/validate_state.py` (contract sync, boolean passes, unique IDs, non-empty branch/next_action).
  - Materialized previous v2 migration commit SHA in state files.
- **Verification**:
  - `scripts/agent/verify.ps1 -Mode Fast`: PASS.
  - `scripts/agent/verify.ps1 -Mode Full`: PARTIAL (accurately detects uninstalled garden dependencies).
  - `git diff --check`: PASS.
- **Next Checkpoint**: D2 source / graph / content-integrity correction.

---

## 2026-09-03 — Workflow v2 migration
- **Commit**: `13447239d458982fe2acab9622220bb0daf012bb`
- **Scope**:
  - Upgraded repository control plane to Phuchello Agent Workflow v2.
  - Replaced heavy `AGENTS.md` with thin control plane (40–70 lines) and JIT retrieval.
  - Created canonical machine-readable runtime state (`.agent/STATE.yaml`).
  - Created machine-readable task acceptance contract (`.agent/task-contract.json`).
  - Created central repository documentation map (`docs/index.md`).
  - Implemented executable verification script (`scripts/agent/verify.ps1`).
  - Updated compatibility state documents and decision log (DEC-001/DEC-008).
  - Fixed frozen D1 commit reference to `922afe07bea7f28abf30c49054159a09a31be743`.
- **Verification**:
  - Validated YAML/JSON syntax of `.agent/` state files.
  - Executed `./scripts/agent/verify.ps1 -Mode Fast`.
  - Zero modifications to product/content/frozen artifacts.
- **Next Checkpoint**: D2 source / graph / content-integrity correction.

---

## 2026-09-03 — Workflow v1 bootstrap
- **Commit**: `07e4d720dfaa677a76cbd8e9bbbe48ea3cdf776e`
- **Scope**:
  - Added repository operating protocol (`AGENTS.md`).
  - Compacted operational state (`PROJECT_STATE.md`) with explicit single `Exact Next Action`.
  - Reconciled actionable queue (`TODO.md`) with P0 focus on D2 content-contract correction.
  - Added durable decision log (`DECISIONS.md`) for DEC-001 through DEC-007.
  - Initialized agent changelog (`CHANGELOG_AGENT.md`).
- **Verification**:
  - Confirmed all 5 state files exist and match specification.
  - Confirmed 0 modifications to `garden/`, `book/`, `practice/`, `research/`, `site/`, or any product artifacts.
  - Confirmed git branch remains `v1.1-quartz-garden` at base `58b5474be54971b886c28508a9702bcc22d5ac15`.
- **Next Checkpoint**: D2 source / graph / content-integrity correction.
