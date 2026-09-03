# AGENT CHANGELOG

Operational record of changes made by AI agents under Phuchello Agent Workflow. Entries are concise and audit-focused.

---

## 2026-09-03 — Workflow v2 guardrail hardening
- **Commit**: pending (`chore: harden workflow v2 guardrails`)
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
