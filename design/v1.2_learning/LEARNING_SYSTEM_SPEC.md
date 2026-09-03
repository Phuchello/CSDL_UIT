# CSDL_UIT v1.2 — Learning System Specification

Status: DESIGN ONLY — no implementation authorized by this document.

## 1. Product thesis

CSDL_UIT v1.2 is not a chatbot, LMS clone, or prettier wiki. It is a static-first **active learning system** that minimizes passive reading and guides a learner through the shortest reliable path from first exposure to durable, transferable understanding.

Core loop:

> **Map → Understand → Trace → Retrieve → Practice → Diagnose → Review**

The site should optimize for the question:

> **“After this session, what can I explain and solve without looking at the material?”**

rather than:

> “How many pages did I read?”

## 2. Evidence-informed design principles

The design combines stable findings from learning science with interaction patterns that fit IT004:

1. **Retrieval practice + spacing**
   - Recall before re-reading.
   - Schedule re-exposure after delay instead of immediate repeated reading.
   - Evidence reference: Carpenter, Pan & Butler (2022), *Nature Reviews Psychology*, “The science of effective learning with spacing and retrieval practice”.

2. **Worked examples before independent problem solving for novices**
   - Show expert reasoning first, then progressively remove guidance.
   - Evidence reference: Paas & van Merriënboer (2020), cognitive-load / guidance-fading review.

3. **Segmenting + signaling + coherence**
   - One learning objective per screen/step.
   - Remove metadata and navigation that do not help the current task.
   - Highlight the causal/algorithmic step currently being learned.
   - Evidence reference: Mayer multimedia learning principles.

4. **Mastery by skill, not completion by page**
   - A concept is not “done” because it was opened.
   - Inspired by skill/unit mastery patterns such as Khan Academy, adapted to a local static implementation.

5. **Learn by doing**
   - Prefer short interactions and decisions over dense prose.
   - Inspired by interactive STEM lesson patterns such as Brilliant, without copying its interface or gamification.

6. **Interleaving only after foundations exist**
   - New learners first receive blocked, highly guided examples.
   - Mixed practice appears after the learner can solve canonical variants.

## 3. Non-goals

v1.2 MUST NOT depend on:

- chatbot or generative AI;
- user accounts;
- server database;
- cloud analytics;
- leaderboard / XP grinding;
- decorative gamification;
- hidden proprietary adaptive model.

The core experience must work as static GitHub Pages plus client-side state.

## 4. Two explicit site modes

### 4.1 Learning Mode — default for study

Show only what helps the current learning step:

- concept title and chapter context;
- 80/20 concept map;
- worked example / trace;
- recall prompt;
- exercise;
- feedback and mistake classification;
- progress/mastery state.

Hide by default:

- raw frontmatter properties;
- modified timestamp;
- backlinks;
- graph;
- source IDs;
- full Explorer tree;
- large metadata panels.

These remain available in Reference Mode.

### 4.2 Reference Mode — Knowledge Garden

Preserve current Quartz strengths:

- Explorer;
- search;
- graph;
- backlinks;
- sources and provenance;
- full theory text;
- PDFs;
- cross-links.

This is for lookup and exploration, not the default learning path.

## 5. Canonical learning loop

Every core skill should support these stages.

### Stage A — Map

Goal: answer “what problem does this concept solve and where does it fit?”

Maximum 3–5 key ideas.

Example for normalization:

`Functional Dependency → Closure → Candidate Keys → Minimal Cover → 3NF/BCNF`

### Stage B — Understand

Explain:

- why the concept exists;
- what information flows through it;
- what changes state;
- what conditions stop or invalidate the process;
- how it differs from neighboring concepts.

### Stage C — Trace

Make algorithm/state transitions visible.

Examples:

- attribute closure: set expansion round by round;
- relational algebra: relation after each operator;
- SQL: logical query-processing order;
- trigger: inserted/deleted state before/after operation;
- ER mapping: entity/relationship transformed into relations.

### Stage D — Retrieve

Collapse/hide the explanation and ask 2–5 closed-book questions.

Do not grade mere recognition when production/derivation is possible.

### Stage E — Practice

Use the scaffold ladder:

1. Worked example.
2. Faded example.
3. Guided problem.
4. Cold problem.
5. Variant / transfer problem.

### Stage F — Diagnose

When an answer is wrong, classify the mental-model failure instead of only showing the right answer.

Examples:

- forgot candidate-key minimality;
- confused 3NF rescue condition with BCNF;
- selected wrong aggregation grain;
- used NOT IN without considering NULL;
- used evidence relation as the candidate domain in a universal query;
- treated a trigger as row-by-row.

### Stage G — Review

A mastered skill returns as retrieval/mixed practice after delay.

Default review intervals are heuristic and editable:

`+1 day → +3 days → +7 days → +21 days`

A failure shortens the interval and reopens the relevant stage.

## 6. Mastery state machine

A skill uses explicit states rather than a vague progress percentage.

```text
UNSEEN
  ↓
ORIENTED          — understands purpose and map
  ↓
FOLLOWED          — can follow a worked trace
  ↓
GUIDED            — solves with hints
  ↓
INDEPENDENT       — solves a cold canonical problem
  ↓
ROBUST            — solves a delayed or mixed variant
```

Rules:

- Opening a note never advances mastery.
- `INDEPENDENT` requires a correct cold problem without hints.
- `ROBUST` requires at least one delayed retrieval or mixed problem.
- A failed robust check can demote to `INDEPENDENT` or `GUIDED` depending on error class.
- Mastery is tracked per skill, not per page.

## 7. Rule-based adaptation — no AI required

### 7.1 Entry diagnostic

Before a chapter/unit, ask 3–6 short problems sampling core prerequisites.

Example routing:

- 2/2 correct on a skill → condensed lesson / skip worked basics.
- 1/2 → faded example path.
- 0/2 → full worked-example path.

### 7.2 Hint policy

Hints are layered:

1. remind the goal;
2. point to the relevant rule;
3. reveal the next intermediate state;
4. show the worked step.

Using deeper hints lowers the evidence level for mastery.

### 7.3 Practice sequencing

For a new skill:

`blocked canonical → faded → cold canonical → close variant`

For a stable skill:

`mixed/interleaved → exam trap → transfer`

## 8. Session planner

The home page may generate deterministic study sessions from available time.

### 15 minutes

- 2 min map / retrieval warm-up;
- 5 min one worked/faded example;
- 6 min one cold problem;
- 2 min error note / next review.

### 30 minutes

- 4 min map + recall;
- 8 min core mechanism / trace;
- 12 min 2–3 problems;
- 4 min diagnosis;
- 2 min review scheduling.

### 60 minutes

- 5 min concept map;
- 10 min mechanism;
- 10 min trace / worked example;
- 10 min closed-book retrieval;
- 18 min 3–4 reasoning problems;
- 5 min error diagnosis;
- 2 min review scheduling.

The planner should favor approximately **70% retrieval/practice, 20% feedback/remediation, 10% initial reading** once the learner has enough prerequisite knowledge.

## 9. Mistake Notebook

Stored locally in the browser.

Each entry:

```json
{
  "skill": "candidate-keys",
  "problemId": "ck-l3-004",
  "errorClass": "minimality-not-checked",
  "timestamp": "...",
  "resolved": false
}
```

The site surfaces:

- most frequent error classes;
- weak skills;
- unresolved mistakes;
- recommended review queue.

No server is required.

## 10. Compare Mode

Some IT004 concepts are learned primarily by discrimination.

Dedicated compare experiences should exist for at least:

- superkey vs candidate key vs primary key;
- 3NF vs BCNF;
- WHERE vs HAVING;
- NOT EXISTS vs NOT IN;
- INNER vs LEFT JOIN;
- relational division vs SQL candidate-domain universal query;
- declarative constraints vs triggers;
- row-level intuition vs set-based trigger behavior;
- schema vs instance;
- ER cardinality vs participation.

Each comparison ends with 2–4 classification problems.

## 11. Exam Mode

Exam Mode intentionally removes scaffolding:

- no hints;
- no backlinks;
- no graph;
- no theory links;
- no worked examples;
- optional timer;
- mixed chapter coverage.

After submission, return a **skill/error report**, not only a score.

The primary action is:

> `Tạo buổi ôn từ lỗi của đề này`

which builds a local review queue from failed skills/error classes.

## 12. Progress storage

Use a versioned localStorage schema, for example:

```json
{
  "schemaVersion": 1,
  "skills": {},
  "reviews": [],
  "mistakes": [],
  "sessionHistory": []
}
```

Requirements:

- fully client-side;
- reset/export/import controls;
- schema migration when version changes;
- no personally identifying data;
- site remains useful when storage is unavailable.

## 13. Primary success metrics for human QA

Do not optimize for time-on-site.

Evaluate whether a learner can:

1. find the next useful thing to study in <10 seconds;
2. identify the 3–5 core concepts of a chapter;
3. complete a worked→faded→cold learning sequence without navigating away;
4. understand why a wrong answer is wrong;
5. resume an unfinished skill after reload;
6. receive a focused review queue after errors;
7. switch to Reference Mode when deeper lookup is needed;
8. use the site at 390 px mobile width without horizontal overflow.

## 14. Design constraints inherited from CSDL_UIT

- Vietnamese-first UI.
- Preserve stable content slugs.
- Preserve canonical source/provenance contracts.
- Preserve Quartz static build and GitHub Pages deployment model.
- Existing PDFs remain canonical downloadable handbooks.
- v1.1.x releases remain immutable historical artifacts.
