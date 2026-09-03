# PHUCHELLO AGENT WORKFLOW v2 — OPERATING PROTOCOL

Repository: `Phuchello/CSDL_UIT` | Purpose: IT004 Database Courseware & Knowledge Garden
Protocol: Workflow v2 (Thin Control Plane + JIT Context + Machine-Readable State)

---

## 1. BOOT SEQUENCE (MANDATORY)

Execute these steps on every session boot:
1. Read `AGENTS.md` (this file).
2. Read `.agent/STATE.yaml` (canonical operational runtime state).
3. Inspect environment: `git status`, current branch, and HEAD commit.
4. Read `.agent/task-contract.json` if an active task contract exists.
5. Retrieve additional files **Just-In-Time** via `docs/index.md`.
*(Do NOT read `PROJECT_STATE.md`, `TODO.md`, or `DECISIONS.md` on boot unless specifically needed).*

---

## 2. HARD SAFETY BOUNDARIES & FROZEN BASELINES

- **Writable Scope**: ONLY `Phuchello/CSDL_UIT`. NEVER modify `Phuchello/phuchello`.
- **Frozen Baselines** (do not alter without explicit mentor authorization):
  - `main`: `6ccf5a408934ab93760ac3242511beb43b05f24f`
  - Phase A (`v1.1-editorial-practice`): `6aef91eb2cb4a0b41827573bc03ec55640d19786`
  - Theory v1.1 (`v1.1-theory-redesign`): `61eb5c8a60106be4251ce090a17c6c3482284332`
  - Practice v1.1 (`v1.1-practice-handbook`): `59c519b94ede86f07fbc1778b120d0c8c3188b80`
  - D1 Architecture (`v1.1-knowledge-garden`): `922afe07bea7f28abf30c49054159a09a31be743`

---

## 3. PROGRESSIVE DISCLOSURE & DOCUMENTATION MAP

- Consult **`docs/index.md`** to locate relevant reference documents JIT.
- Do not scan the repository or re-read unchanged files without a concrete requirement.
- The repository files and git commit history are the single source of truth, not chat memory.

---

## 4. VERIFICATION & TASK CONTRACT

- Automated verification is mandatory: run `./scripts/agent/verify.ps1 -Mode Fast` (or `-Mode Full`).
- An active task is governed by **`.agent/task-contract.json`**. An acceptance item's `passes` flag may only be set to `true` after its corresponding check passes.
- Stop and reassess after two materially similar test/build failures.

---

## 5. MODEL ECONOMY & CONTEXT DISCIPLINE

- **Model Tier**: Normal/Low for mechanical edits and state updates; High for content and debugging; Extra-High for architecture, migrations, or persistent failures.
- **Context Monitoring**: Normal (0–40%), Watch (40–60%), Checkpoint Soon (60–75%).
- At **75%+ Context Pressure**: Stop expanding scope $\rightarrow$ Verify current work $\rightarrow$ Update `.agent/STATE.yaml` and `.agent/task-contract.json` $\rightarrow$ Commit & Push $\rightarrow$ Hand off to a fresh session.
