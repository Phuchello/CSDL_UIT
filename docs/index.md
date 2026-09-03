# CSDL_UIT Documentation Map

> **Usage Guide**: This document is a lightweight navigation map for Just-In-Time (JIT) retrieval. **Read only the section relevant to your active task.** Do not scan or read all linked documents by default.

---

## 1. Architecture & Knowledge Garden
- **D1 Visual & Information Architecture (Normative)**: [`design/v1.1_site/`](../design/v1.1_site/)
  - `DESIGN_SYSTEM.md`: Color palette, typography, responsive layouts.
  - `INFORMATION_ARCHITECTURE.md`: Route contracts, metadata schemas, graph principles.
- **v1.2 Active Learning System (Design Only)**: [`design/v1.2_learning/`](../design/v1.2_learning/)
  - `LEARNING_SYSTEM_SPEC.md`: Product philosophy, learning loop, mastery states, adaptation rules, review/mistake model.
  - `CONTENT_CONTRACT.md`: Required instructional blocks, exercise taxonomy, IT004 coverage and QA contract.
  - `UX_WIREFRAMES.md`: Learning/Reference modes, dashboard, trace, recall, practice, review and exam wireframes.
  - `IMPLEMENTATION_PLAN.md`: Vertical-slice rollout, milestones, release boundaries and acceptance gates.
- **Quartz v5 Static Site Engine**: [`garden/`](../garden/)
  - `garden/content/`: Source Markdown notes and semantic frontmatter.
  - `garden/quartz.config.yaml`: Quartz theme, plugins, and graph configuration.
  - `garden/QUARTZ_UPSTREAM.md`: Pinned upstream commit, patch audit, and update policy.

---

## 2. Frozen Research & Canonical Provenance
- **Source Inventory**: [`research/v1.1_phase_a/source_inventory.md`](../research/v1.1_phase_a/source_inventory.md)
  - Canonical Microsoft Learn `TECH-A01`–`TECH-A11` IDs.
  - Course textbooks, syllabi, and official university references.
- **Artifact Registry**: [`research/v1.1_phase_a/artifact_registry.md`](../research/v1.1_phase_a/artifact_registry.md)
  - 31 canonical exam, practical, and review artifacts with verified URLs/hashes.
- **Exam Pattern Map**: [`research/v1.1_phase_a/exam_pattern_map.md`](../research/v1.1_phase_a/exam_pattern_map.md)
  - Verified distribution of problem types across UIT academic terms.

---

## 3. Practice Handbook & Fixture Contracts
- **Runnable Database Fixture**: [`practice/sql/`](../practice/sql/)
  - Canonical scripts: `01_schema.sql`, `02_seed.sql`, `03_queries_basic.sql`, `04_queries_advanced.sql`, `05_triggers.sql`, `06_test_cases.sql`, `reset.sql`.
- **Example Registry**: [`practice/EXAMPLE_REGISTRY.md`](../practice/EXAMPLE_REGISTRY.md)
  - Mapping of runnable query examples, IDs, and expected outputs.
- **Practice Handbook Quality Assurance**: [`reports/v1.1_practice_full_qa.md`](../reports/v1.1_practice_full_qa.md)
  - 71-page normalized practical handbook verification.

---

## 4. Theory Handbook & Editorial Copy
- **Theory Source Files**: [`book/`](../book/)
  - Chapters 00–06, exam playbook, cheat sheet, references.
- **Theory Quality Assurance**: [`reports/v1.1_theory_qa.md`](../reports/v1.1_theory_qa.md)
  - 64-page normalized theory handbook verification and typography audit.

---

## 5. Operational State & Decisions
- **Canonical Runtime State**: [`.agent/STATE.yaml`](../.agent/STATE.yaml)
- **Active Task Acceptance Contract**: [`.agent/task-contract.json`](../.agent/task-contract.json)
- **Durable Decisions Log**: [`DECISIONS.md`](../DECISIONS.md)
- **Human-Readable Task Queue**: [`TODO.md`](../TODO.md)
- **Historical Milestone State**: [`PROJECT_STATE.md`](../PROJECT_STATE.md)
- **Agent Audit Trail**: [`CHANGELOG_AGENT.md`](../CHANGELOG_AGENT.md)
- **Verification Reports**: [`reports/`](../reports/)
