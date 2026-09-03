# PHUCHELLO AGENT WORKFLOW v1 — OPERATING PROTOCOL

Repository: `Phuchello/CSDL_UIT`
Effective: 2026-09-03
Status: ACTIVE

This protocol governs every AI agent operating in this repository. The repository is the single source of truth; conversation history is ephemeral.

---

## 1. BOOT SEQUENCE

Every session MUST begin with these steps before performing any work:

1. **Read `AGENTS.md`** (this operating protocol).
2. **Read `PROJECT_STATE.md`** (current state, blockers, Exact Next Action).
3. **Read `TODO.md`** (active actionable queue).
4. **Read `DECISIONS.md`** only when relevant to design choices, architecture, or scope boundaries.
5. **Inspect environment**: Run `git status`, verify current branch and HEAD commit.
6. **Execute `Exact Next Action`** from `PROJECT_STATE.md` unless explicitly overridden by the user.

---

## 2. CORE WORKFLOW CYCLE

```
UNDERSTAND ──► PLAN ──► EXECUTE ──► TEST ──► VERIFY ──► REVIEW ──► CHECKPOINT
```

1. **UNDERSTAND**: Read only the relevant files needed for the task (progressive disclosure).
2. **PLAN**: Formulate a concrete, testable plan before mutating code or content.
3. **EXECUTE**: Apply minimal, precise edits. Preserve all unrelated working functionality.
4. **TEST**: Run automated checks, linters, validators, and compilers.
5. **VERIFY**: Check outputs against acceptance criteria. Distinguish:
   - `VERIFIED`: Confirmed by automated test/build/runtime execution.
   - `PARTIALLY VERIFIED`: Static analysis passes but runtime/browser check was not executed.
   - `NOT VERIFIED`: Assumption or unverified change.
6. **REVIEW**: Confirm no regressions, no unauthorized file mutations, and no scope creep.
7. **CHECKPOINT**: Synchronize state files (`PROJECT_STATE.md`, `TODO.md`, `CHANGELOG_AGENT.md`), commit, and push.

---

## 3. OPERATING RULES & SAFETY

### Hard Repository Safety
- **ONLY modify**: `Phuchello/CSDL_UIT`.
- **NEVER modify**: `Phuchello/phuchello` (profile repository).
- **Frozen Branches & Artifacts**:
  - `main` (`6ccf5a4`) — Frozen.
  - `v1.1-editorial-practice` (Phase A @ `6aef91e`) — Frozen.
  - `v1.1-theory-redesign` (Theory v1.1 @ `61eb5c8`) — Frozen.
  - `v1.1-practice-handbook` (Practice v1.1 @ `59c519b`) — Frozen.
  - `v1.1-knowledge-garden` (D1 Architecture @ `c7ba7e4`) — Frozen.
  - DO NOT mutate frozen source files (`book/`, `practice/`, `research/v1.1_phase_a/`, `site/`) unless explicitly authorized.

### Information & Context Discipline
- **Repository is source of truth**: Do not rely on chat memory; read state files and source files.
- **Progressive disclosure**: Do not scan or read the entire repository by default. Read only files pertinent to the active task.
- **No redundant reads**: Do not re-read unchanged files without specific reason.
- **Two-failure limit**: If two materially similar attempts fail, STOP and reassess root causes before continuing.
- **Preserve working code**: Never break working unrelated features to complete a task.

---

## 4. CONTEXT PRESSURE MANAGEMENT

Monitor context usage during long-running workflows:

| Context Usage | Level | Protocol Action |
| :--- | :--- | :--- |
| **0–40%** | `NORMAL` | Standard progressive work. |
| **40–60%** | `WATCH` | Be concise, avoid large file dumps. |
| **60–75%** | `CHECKPOINT SOON` | Wrap up current unit of work, run tests, plan checkpoint. |
| **75%+** | `CRITICAL` | **STOP EXPANDING** $\rightarrow$ Verify current changes $\rightarrow$ Checkpoint state files $\rightarrow$ Commit & Push $\rightarrow$ Hand off to fresh session. |

Always checkpoint before:
- Risky refactors or major dependency changes.
- Model tier switches.
- Session end or context pressure limits.

---

## 5. MODEL ECONOMY

Select the appropriate model tier based on task complexity:

- **Normal / Low (`flash_lite` / `flash`)**:
  - Mechanical edits, documentation updates, state file updates, formatting, simple CSS tweaks, grep/file searches, running test scripts.
- **High (`inherit` / `flash` high)**:
  - Medium implementation, debugging, content writing, schema/validator scripts, test construction.
- **Extra High (`pro`)**:
  - Architectural decisions, ambiguous root cause debugging, major migrations, security audits, final critical releases, or after two substantial failures.

---

## 6. COMPLETION STANDARD

A task or milestone is marked **DONE** if and only if:
1. The requested behavior or fix exists and is complete.
2. All relevant automated verification passes (compilation, linting, tests, builds).
3. No known regressions remain in existing features.
4. All state files (`PROJECT_STATE.md`, `TODO.md`, `CHANGELOG_AGENT.md`) are synchronized.
5. Exact Next Action is clearly stated for the subsequent session.
