# CSDL_UIT v1.2 — Implementation Plan

Status: DESIGN ONLY. No production implementation is authorized merely by this plan.

## 1. Sequence principle

Do not build the full system in one pass.

Use a vertical-slice strategy:

1. stabilize v1.1.1 content/localization;
2. implement one complete Learning Unit end-to-end;
3. validate learning UX with a human;
4. generalize reusable components;
5. expand chapter coverage;
6. add review/exam systems last.

This prevents a large amount of UI code from being built around an untested learning flow.

## 2. Preconditions

Before v1.2 implementation begins:

- PR #4 Vietnamese-first localization is reviewed and resolved separately;
- v1.1.1 content-completeness scope is decided;
- visible Properties/raw metadata issue has a documented Reference Mode solution;
- canonical `research/coverage_matrix.md` remains the scope baseline;
- existing v1.1.0 tag/release remains immutable;
- Pages deployment remains human-controlled.

## 3. Milestone A — Learning architecture prototype

Target one difficult, representative skill:

**`theory/candidate-keys`**

Why this skill:

- depends on closure;
- has algorithmic trace;
- has a clear worked/faded/cold sequence;
- contains common misconceptions;
- connects directly to normalization and exam questions.

Deliver:

- Learning Mode shell;
- stage navigation;
- one concept map;
- one execution trace;
- one recall checkpoint;
- one worked example;
- one faded example;
- one cold problem;
- layered hints;
- one error-diagnosis path;
- local progress persistence;
- switch to Reference Mode.

Do NOT build full spaced repetition, mock exams, or all chapters yet.

### Acceptance Gate A

Human can complete the candidate-key unit on desktop and mobile without needing the Quartz Explorer.

Automated checks:

- production build passes;
- links pass;
- KaTeX passes;
- localStorage schema unit tests pass;
- no horizontal overflow at 390 / 900 / 1440 px;
- keyboard navigation smoke passes.

## 4. Milestone B — Reusable Learning Unit system

After Gate A passes, extract reusable primitives:

- `LearningShell`;
- `ConceptMap`;
- `TraceStepper`;
- `RecallPrompt`;
- `WorkedExample`;
- `FadedExample`;
- `ProblemCard`;
- `HintDrawer`;
- `DiagnosisPanel`;
- `MasteryIndicator`;
- `ReferenceModeLink`.

Define deterministic content loading from Markdown/frontmatter/static data.

### Acceptance Gate B

Implement three structurally different skills using the same primitives:

1. Candidate Keys — algorithmic;
2. GROUP BY/HAVING — SQL reasoning;
3. 3NF vs BCNF — compare/classification.

If these require three one-off page implementations, architecture fails.

## 5. Milestone C — Chapter learning maps + diagnostics

Build chapter landing experiences for Ch01–Ch06.

Each chapter gets:

- 3–5 core concept map;
- prerequisites;
- priority badges derived from coverage matrix;
- 3–6 question entry diagnostic;
- route recommendation based on diagnostic results.

No ML/adaptive backend.

### Acceptance Gate C

For each chapter, a new learner can answer:

- What are the core concepts?
- What should I learn first?
- What can I skip/condense based on diagnostic performance?

within one screen plus one interaction.

## 6. Milestone D — Content expansion

Convert/add Learning Units according to `CONTENT_CONTRACT.md`.

Priority order from exam/coverage evidence:

1. Ch02 ER + relational mapping gaps;
2. Ch03 relational algebra / division;
3. Ch04 SQL reasoning;
4. Ch05 RBTV;
5. Ch06 FD / normalization;
6. Ch01 overview consolidation.

Rationale: current Garden already has relatively deep Ch03–Ch06 concepts but weak exercise volume and large Ch01/Ch02 gaps.

### Exercise production rule

Never bulk-generate filler.

For each skill:

1. canonical worked example;
2. faded variant;
3. cold canonical;
4. reasoning variant;
5. exam trap;
6. transfer when pedagogically justified.

## 7. Milestone E — Review Engine

Implement versioned client-side state:

- mastery per skill;
- review due dates;
- mistake notebook;
- recent sessions.

Recommended first deterministic interval policy:

```text
Again → +0 day / relearn
Hard  → +1 day
Good  → +3 days
Second Good → +7 days
Third Good  → +21 days
```

Do not pretend this heuristic is an optimal memory model. Keep it transparent and replaceable.

### Acceptance Gate E

- reload preserves progress;
- reset/export/import works;
- corrupt/old schema fails safely;
- site still functions if localStorage is unavailable;
- review queue prioritizes due + weak skills.

## 8. Milestone F — Mistake-driven practice

Build a canonical error taxonomy.

First target classes:

- candidate-key minimality;
- superkey vs candidate key;
- 3NF rescue vs BCNF;
- wrong universal-query candidate domain;
- NOT IN + NULL;
- wrong aggregation grain;
- WHERE vs HAVING;
- JOIN multiplicity/unexpected duplicates;
- row-by-row trigger thinking;
- impact-table operation scope;
- ER cardinality vs participation;
- incorrect ER relationship mapping.

A mistake entry should offer:

- repair explanation;
- one similar problem;
- one later mixed review item.

## 9. Milestone G — Exam Engine

Build only after enough question coverage exists.

Features:

- mixed skill selection;
- optional timer;
- no scaffolds;
- question flagging;
- deterministic scoring where possible;
- rubric/checklist for free response where exact automatic scoring is inappropriate;
- post-exam skill/error report;
- “create review session from mistakes”.

### Initial exam target

4–6 curated mock exams, not dozens of low-quality generated exams.

## 10. Milestone H — Reference Mode cleanup

Preserve the Knowledge Garden, but improve default reader presentation:

- hide Properties panel by default;
- hide raw description metadata;
- move provenance/source details into disclosure;
- keep graph/backlinks/search available;
- keep Vietnamese-first navigation;
- retain stable slugs and backlinks.

Learning and Reference modes share the same canonical academic content; avoid duplicated factual copies.

## 11. Technical architecture recommendation

Keep Quartz v5 as static generator.

Preferred structure conceptually:

```text
garden/
  content/                 # canonical reference notes
  learning/                # static learning-unit/problem data OR generated data
  quartz/                  # Quartz engine/components
  quartz/components/...    # reusable learning UI components
  quartz/static/...        # static assets
```

Exact implementation path should be chosen after checking Quartz plugin/component extension points. Avoid forking large upstream areas when a local component/plugin is sufficient.

## 12. Data contract

Use stable IDs independent from filenames:

```text
skill_id: candidate-keys
problem_id: ck-l3-004
error_id: minimality-not-checked
```

This allows title localization and future slug maintenance without corrupting learner progress.

## 13. CI additions for implementation phase

Potential new deterministic gates:

- learning-unit schema validator;
- duplicate skill/problem ID detector;
- prerequisite graph cycle detector;
- problem → skill target validity;
- error-class registry validity;
- Learning Mode route smoke;
- localStorage schema tests;
- mobile overflow checks;
- no raw metadata visible in Learning Mode;
- cold problem cannot expose solution before submit;
- hidden/scaffold state accessible by keyboard.

## 14. Human QA scenarios

Automated tests cannot validate whether the learning sequence feels understandable.

Minimum mentor smoke scenarios:

### Scenario 1 — novice

Learner knows nothing about candidate keys.

Expected:

- understands purpose before formal detail;
- can follow trace;
- can solve faded problem;
- failure on cold problem produces actionable diagnosis.

### Scenario 2 — partially prepared

Learner passes diagnostic on closure but not candidate keys.

Expected:

- does not repeat unnecessary closure basics;
- receives condensed prerequisite refresher;
- enters candidate-key faded path.

### Scenario 3 — review learner

Learner returns after delay.

Expected:

- retrieval problem appears before theory;
- successful recall advances review interval;
- failed recall links directly to repair unit.

### Scenario 4 — mobile

390 px viewport.

Expected:

- one task focus;
- no horizontal page overflow;
- math/code usable;
- sticky actions do not obscure content.

## 15. Release strategy

Recommended version boundary:

### v1.1.1

- Vietnamese-first UX;
- visual cleanup;
- content completeness improvements;
- more exercises if completed safely;
- no major learning-engine dependency.

### v1.2.0

- Learning Mode foundation;
- mastery state;
- worked→faded→cold flow;
- diagnostics;
- mistake diagnosis;
- basic review queue.

### v1.3.0

- broad exercise bank;
- mixed/interleaved review;
- Exam Engine;
- richer mistake-driven sessions.

Do not make v1.1.1 dependent on finishing v1.2 architecture.

## 16. Stop conditions

Stop and redesign before expanding if any of these occur:

- Learning Mode becomes another dense Quartz page with extra widgets;
- skill progress is based mainly on pages viewed;
- content must be duplicated between Learning and Reference modes;
- every new unit requires custom UI code;
- question count grows faster than QA capacity;
- adaptive rules become opaque/unexplainable;
- metadata/provenance becomes visible noise in the default learning flow;
- mobile requires horizontal page scrolling.
