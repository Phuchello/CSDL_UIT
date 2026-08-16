# Book Architecture — IT004 CSDL UIT
**Updated**: 2026-08-13 (Post-Recovery Audit)

## Principles
1. **Every concept**: Intuition → Definition → Visual/Table → Dry Run → Formal → Exam Pattern → Trap → Practice → Solution
2. **UIT-first**: Follow UIT slide structure, UIT notation, UIT datasets
3. **T-SQL only**: All SQL is SQL Server dialect
4. **Source-verified**: Claims must trace to UIT slides or standard textbooks

## Chapter Structure

### Phần 0: Cách học IT004 (ch00_intro.html) — ✅ DONE
- Bản đồ môn, pipeline, dependency graph
- Roadmap GK/CK, dataset schemas, top 10 traps
- Target: 15-20KB ✅

### Chương 1: Tổng quan CSDL (ch01_overview.html) — ✅ DONE
- Data/Info, File System, DBMS, 3-level architecture, Schema/Instance, Data Independence, Data Models
- Target: 15-20KB ✅

### Chương 2: ER & Mô hình quan hệ (ch02_er_relational.html) — 🔴 REWRITE
**Current gap**: No ER diagrams, missing weak entities/ISA, placeholder exercises

**Required architecture**:
- A. Relational Model (attribute, domain, tuple, relation, schema, instance, degree, cardinality, NULL, predicate, keys)
- B. ER Model
  - Entity, Entity Set, Attribute types (key, composite, multivalued, derived)
  - Relationship, Degree, Cardinality (1:1, 1:N, M:N)
  - Participation (total, partial), Min-max notation with Vietnamese examples
  - Weak entity, Identifying relationship ← MISSING
  - Recursive/Unary relationships ← MISSING
  - ISA/Specialization ← NICE TO HAVE (badge advanced if outside syllabus)
- C. 9-step ER analysis process with 3 worked examples (easy → hard)
- D. ER → Relational Schema mapping (1:1, 1:N, M:N, weak entity, multivalued)
- E. 10 exercises with detailed solutions
- F. One-Page Recall
- Target: 40-55KB

### Chương 3: Đại số quan hệ (ch03_relational_algebra.html) — 🔴 REWRITE (BENCHMARK)
**Current gap**: Operators are 1-3 lines each, only 1 data table, placeholder solutions

**Required architecture**:
- A. Each operator (σ, π, ρ, ×, ⋈θ, equi-join, natural join, ∪, ∩, −, ÷, γ/ℑ, outer join):
  - Meaning, Input/Output, Condition, Notation
  - Before/After data table (3-8 rows)
  - Vietnamese keyword mapping
  - Common traps
- B. Keyword dictionary (complete mapping table)
- C. Phép chia (Division) — dedicated 5+ page section
  - Set-theoretic intuition
  - Formal definition: R÷S = πX(R) − πX((πX(R) × S) − R)
  - Dry run with intermediate tables
  - Double NOT EXISTS equivalent
  - COUNT DISTINCT equivalent
  - 3-way comparison table
- D. 30+ exercises with DETAILED step-by-step solutions
- E. One-Page Recall
- Target: 50-70KB

### Chương 4: SQL Server / T-SQL (ch04_sql.html) — 🟡 REVISE
**Current gap**: 12/18 exercises missing solutions, few data tables outside JOINs

**Required fixes**:
- Complete all 18+ exercise solutions with step-by-step
- Add data tables for aggregation, subquery sections
- Add Method C (EXCEPT) SQL code in "Tất cả" section
- Verify all SQL against T-SQL syntax
- Target: maintain 35-45KB

### Chương 5: Ràng buộc toàn vẹn (ch05_constraints.html) — 🟢 POLISH
**Best chapter currently**. Fix typo, minor polish.
- Target: maintain 25-30KB

### Chương 6: PTH, Khóa & Dạng chuẩn (ch06_fd_normalization.html) — 🔴 REWRITE
**Current gap**: 141-line skeleton

**Required architecture**:
- 6.1 Functional dependency X→Y (intuition, formal, trivial/non-trivial, examples)
- 6.2 Armstrong axioms (3 axioms + 3 derived, each with proof and example)
- 6.3 Proof template (2 worked proofs)
- 6.4 Attribute closure X⁺ (algorithm, pseudocode, 3 dry runs with iteration tables)
- 6.5 Superkey/Candidate key verification using closure
- 6.6 Finding ALL candidate keys (LHS/RHS/N/LR analysis + branching + 2 worked examples)
- 6.7 Minimal cover (4 steps + 2 full worked examples)
- 6.8 Normal Forms (1NF, 2NF, 3NF, BCNF — each with: formal def, human def, check method, counterexample, trap)
- 6.9 Highest NF determination (decision tree + worked examples)
- 6.10 Decomposition (badge ADVANCED if outside syllabus)
- 6.11 15+ exercises with detailed solutions
- 6.12 One-Page Recall
- Target: 45-60KB

### Chương 7: Thực hành SQL Server (ch07_practical.html) — 🟡 REVISE
**Add**: lab exercises, full sample database creation scripts
- Target: 18-25KB

### Exam Playbook (exam_playbook.html) — 🔴 REWRITE
**Current**: 64-line stub

**Required**:
- ER checklist, ĐSQH keyword→operator, SQL keyword→pattern
- All "tất cả/không/cả hai/mỗi/lớn nhất" patterns
- FD checklist, Key search checklist, NF decision tree
- 90-minute time allocation
- 2-3 sample exam walkthroughs
- Target: 20-30KB

### Cheat Sheet (cheat_sheet.html) — 🔴 REWRITE
**Current**: 60-line stub

**Required**:
- 6-8 dense pages covering all 6 chapters
- Formulas, syntax, decision trees, key ideas, common traps
- Designed for quick scan before exam
- Target: 18-25KB

## Total Target Size
~300-400KB HTML content (currently ~160KB, but half is broken/skeletal)

## Assembly
- Each chapter file: content only (no DOCTYPE/html/head/body wrapper)
- CSS linked from book.css
- index.html assembles all chapters with proper wrapper
- PDF generated only after QA pass
