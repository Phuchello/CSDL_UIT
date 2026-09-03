# CSDL_UIT v1.2 — Learning Content Contract

Status: DESIGN ONLY.

## 1. Purpose

This contract defines when a CSDL_UIT topic is a complete **Learning Unit** rather than a passive note.

A Learning Unit must support the sequence:

> **Map → Understand → Trace → Retrieve → Practice → Diagnose → Review**

A Markdown page containing only definition + prose + links does not satisfy this contract.

## 2. Required unit metadata

Recommended semantic frontmatter for new/converted learning units:

```yaml
title: "Khóa ứng viên (Candidate Keys)"
type: learning-unit
chapter: ch06
skill_id: candidate-keys
priority: core             # core | exam | practice | supporting | extension
prerequisites: [closure]
related: [theory/closure, theory/minimal-cover]
exam_weight: high          # low | medium | high | very-high
has_trace: true
has_recall: true
has_practice: true
has_diagnosis: true
provenance: verified-artifact
```

Existing canonical provenance fields remain authoritative and must not be weakened.

## 3. Required instructional blocks

Every core Learning Unit must contain or link to the following blocks.

### A. One-sentence purpose

Answer:

> “Tại sao phải học cái này?”

Maximum ~60 words.

### B. 80/20 concept map

Show 3–5 ideas only.

Example:

```text
Superkey
   ↓ + minimality
Candidate Key
   ↓ choose one
Primary Key
```

### C. Mental model

Explain:

- input;
- operation/rule;
- changing state;
- stopping condition;
- output.

### D. Execution trace

At least one step-by-step state transition for algorithmic topics.

Examples:

- closure rounds;
- relational algebra intermediate relations;
- SQL logical processing order;
- trigger inserted/deleted transitions;
- ER → relation mapping.

If the concept is not algorithmic, provide a structured compare/classification trace instead.

### E. Worked example

Requirements:

- realistic but minimal;
- no irrelevant data;
- each step states **why** it is legal/useful;
- final answer is not shown before the reasoning path.

### F. Self-explanation checkpoint

At least 2 prompts such as:

- “Tại sao bước này đúng?”
- “Nếu bỏ điều kiện này thì chuyện gì xảy ra?”
- “Điểm khác với khái niệm X là gì?”

### G. Faded example

Remove selected intermediate steps from the worked example.

Learner must fill them before seeing the answer.

### H. Cold problem

A canonical problem solved without hints.

Passing it is required for `INDEPENDENT` mastery.

### I. Variant / transfer problem

Change the surface form or combine one neighboring skill.

Passing delayed/mixed variants contributes to `ROBUST` mastery.

### J. Error diagnosis

At least 2 common wrong paths with explicit error classes.

Example:

```yaml
error_classes:
  - id: minimality-not-checked
    symptom: "Tìm được superkey và kết luận ngay là candidate key"
    repair: "Thử loại từng thuộc tính và kiểm tra bao đóng lại"
```

### K. Recall set

3–7 prompts suitable for delayed retrieval.

Use varied forms:

- definition from memory;
- compare;
- trace next state;
- diagnose;
- generate example;
- transfer.

## 4. Exercise taxonomy

Problem bank difficulty is defined by **reasoning demand**, not cosmetic size.

### L0 — Recognition

Identify or classify a concept.

### L1 — Mechanism

Predict the next state / step.

### L2 — Canonical application

Solve the standard pattern.

### L3 — Reasoning variant

Surface details change; learner must select the right procedure.

### L4 — Exam trap

Targets a documented misconception or UIT-style trap.

### L5 — Transfer

Requires combining concepts or handling an unfamiliar schema.

A strong core skill should eventually have at least:

- 2 × L1;
- 3 × L2;
- 2 × L3;
- 2 × L4;
- 1 × L5.

This is a target, not a requirement to generate low-quality filler.

## 5. Problem object schema

Recommended static problem representation:

```json
{
  "id": "ck-l3-004",
  "skill": "candidate-keys",
  "level": 3,
  "prompt": "...",
  "answerType": "structured-text",
  "hints": ["goal", "rule", "next-state"],
  "solution": ["step-1", "step-2"],
  "errorClasses": ["minimality-not-checked"],
  "sources": ["UIT-O05"]
}
```

Problems may live in Markdown/JSON as implementation chooses, but IDs and skill mapping must be deterministic.

## 6. Chapter-level completeness contract

A chapter is considered learning-complete only when it has:

1. chapter map;
2. prerequisite map;
3. core Learning Units;
4. diagnostic entry set;
5. guided/cold practice for each core skill;
6. mixed review set;
7. exam-trap set;
8. at least one chapter challenge;
9. mistake/error taxonomy coverage;
10. links to Reference Mode sources.

## 7. IT004 coverage target

Use `research/coverage_matrix.md` as the canonical scope map.

### Ch01 — Tổng quan CSDL

Must cover at minimum:

- Data vs Information;
- File System vs DBMS;
- Database / DBMS / DBS;
- redundancy / inconsistency;
- data independence;
- ANSI/SPARC 3-level architecture;
- schema vs instance;
- major data models.

### Ch02 — ER & mô hình quan hệ

Must cover:

- entity / entity set;
- attribute types;
- relationship / degree;
- cardinality;
- participation;
- min-max notation;
- ER diagram reasoning;
- relation / tuple / attribute / domain;
- keys and foreign keys;
- ER → relational mapping for 1:1, 1:N, M:N and relationship attributes.

### Ch03 — Đại số quan hệ

Must cover:

- selection / projection / rename;
- product / joins;
- union/intersection/difference;
- division;
- aggregation/grouping;
- universal-query reasoning.

### Ch04 — SQL Server / T-SQL

Must cover:

- DDL / DML;
- filtering / NULL;
- JOIN family;
- aggregation + GROUP BY/HAVING;
- subqueries / correlated subqueries;
- EXISTS / NOT EXISTS;
- universal query patterns;
- views / procedures / triggers to syllabus depth.

### Ch05 — Ràng buộc toàn vẹn

Must cover UIT taxonomy and impact-table reasoning plus declarative-vs-trigger implementation choices.

### Ch06 — PTH & chuẩn hóa

Must cover:

- FD classification;
- Armstrong axioms + derived rules;
- closure;
- superkey / candidate key;
- all candidate keys;
- minimal cover;
- 1NF/2NF/3NF/BCNF;
- highest normal form;
- lossless decomposition / dependency preservation to syllabus depth.

## 8. Coverage targets for v1.2 implementation planning

These are content-capacity targets, not auto-generation quotas.

| Area | Minimum target |
|---|---:|
| Core Learning Units | 30–40 |
| Real exercises | 50+ |
| Exam-style reasoning questions | 25+ |
| Full mixed mock exams | 4–6 |
| Compare experiences | 8+ |
| Diagnostic sets | 6 chapter sets |
| Recall prompts | 3–7 per core skill |
| Error classes | 25+ meaningful misconceptions |

Prefer 50 strong exercises over 300 near-duplicates.

## 9. Vietnamese-first editorial rule

Human-facing text must be Vietnamese-first.

Preferred form:

- `Khóa ứng viên (Candidate Keys)`
- `Phủ tối thiểu (Minimal Cover)`
- `Đại số quan hệ (Relational Algebra)`

Preserve natural technical tokens when translation would reduce clarity:

- SQL Server;
- T-SQL;
- JOIN;
- GROUP BY;
- NULL;
- 3NF / BCNF;
- Double NOT EXISTS.

## 10. Content QA gate

A new Learning Unit cannot be marked complete until:

- source/provenance is valid;
- academic meaning matches canonical CSDL_UIT material;
- formulas/code pass existing validation;
- internal links pass;
- required instructional blocks exist;
- cold problem exists;
- at least one diagnosed misconception exists;
- Vietnamese-first visible title passes;
- rendered mobile/desktop smoke passes.
