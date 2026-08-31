# Phase A Knowledge Garden Architecture

Keep Quartz as the preferred static foundation. The key correction is a single canonical note per exam artifact; year, semester, and type pages are metadata-generated views, not duplicate copies.

## Proposed tree

```text
Home
Start Here/
  Roadmap
  Knowledge Map
  How to Study
Theory/
  01-Overview
  02-ER-and-Relational-Model
  03-Relational-Algebra
  04-SQL-TSQL
  05-Integrity-Constraints
  06-Functional-Dependencies-and-Normalization
Essay Questions/
  Ch1-Tong-Quan
  Ch2-ER-and-Relational-Model
  Ch3-Relational-Algebra
  Ch4-SQL-Reasoning
  Ch5-Integrity
  Ch6-FD-and-Normalization
  Mixed-Exams
Exercises/
  Relational Algebra
  SQL
  FD and Normalization
Practice/
  Setup SQL Server
  Lab 01–05
  QLGV
  QLBH
Exams/
  2016-2017/
  2017-2018/
  2018-2019/
  2019-2020/
  2020-2021/
  2021-2022/
  2022-2023/
  2023-2024/
  2024-2025/
  2025-2026/
Common Errors/
Flashcards/
Cheat Sheets/
Sources/
  Source Register
  Provenance Rules
  Copyright and Linking
```

Do not create parallel `By Year`, `By Semester`, and `By Type` copies. A canonical exam note lives under its year (or stable artifact slug); Quartz search, tags, and generated index pages provide the other views.

## Node purpose and relationships

| node | purpose | source material | connects to |
|---|---|---|---|
| Start Here | Orient a learner and show prerequisites | `UIT-O01`, `UIT-O02`, `LOC-LEC-AN-CH01` | Theory, Practice, Exam Patterns |
| Theory | Canonical concepts and formal definitions | `LOC-LEC-AN-*`, `LOC-LEC-LONG-*`, `TXT-A01`, `TXT-A02` | Exercises, Essays, Sources |
| Essay Questions | Deliberate-response practice with provenance labels | `exam_pattern_map.md`, `essay_bank_plan.md` | Theory, Exams, Common Errors |
| Exercises | Short feedback loops by skill and difficulty | `LOC-REV-2024-10-01`, `LOC-REV-DSQH-2024` | Theory, Essay Questions |
| Practice | SQL Server execution workflow | `LAB-QLBH-QLGV-CORPUS`, `TECH-A01`–`TECH-A11` | Theory/SQL, Exams, Errors |
| Exams | One note per identifiable artifact with metadata-generated views | UIT-O06/O07/O10 and COM-C08/C09 | Essay Questions, Practice |
| Common Errors | Explain misconceptions and failure modes | handbook plus validated examples | Theory, Exercises, Practice |
| Flashcards/Cheat Sheets | Retrieval aids and rapid review | handbook concepts | Theory and Exams |
| Sources | Auditable evidence and rights metadata | `source_inventory.md` | Every content node |

## Frontmatter and tags

```yaml
title: "IT004 HK1 2023-2024 — Final exam artifact"
type: exam # theory|exercise|essay|lab|exam|source|flashcard
year: 2023-2024
semester: HK1
exam_type: final
source_ids: [COM-C09]
provenance: community-mirror-preview
topics: [sql, joins, group-by]
difficulty: unknown
status: verified-artifact # reconstructed-exam-pattern|original-practice
schema: QLBH # QLGV|QLBH|auxiliary|none
```

Controlled tags: `chapter:ch01`…`chapter:ch07`, `type:*`, `assessment:*`, `topic:*`, `difficulty:*`, `status:*`, `provenance:*`, `source-tier:A`…`D`, and `schema:*`.

## Wikilink and graph rules

- Use stable slugs and bilingual aliases; do not link by changing display text.
- Every exam/essay note links to the theory concepts it tests, exercise prerequisites, its source record, and at least one common-error note.
- Every practical page links to the relevant SQL construct, schema page, and troubleshooting note.
- Link only where the relationship is pedagogically meaningful; no tag-spam or random graph edges.
- Use canonical links such as `[[Theory/Relational-Algebra/Division]]`, `[[Essay-Questions/Ch4-SQL-Reasoning]]`, and `[[Practice/SQL-Server/Triggers]]`.
- Year/semester/type indexes query frontmatter and link to canonical notes; they never duplicate note bodies.
- Run a broken-link check before publication.

## Quartz suitability and components

Quartz is suitable because its documented feature set includes nested Explorer navigation, full-text search, Wikilinks, graph view, backlinks, LaTeX, syntax highlighting, Mermaid, breadcrumbs, TOC, dark mode, and Reader Mode. Use stock components first and add only small IT004-specific CSS/JS changes.

Planned components:

- Explorer for the content tree;
- Search with diacritic-tolerant aliases and tag queries;
- Breadcrumbs and TOC on long notes;
- local graph on note pages and a global graph on the map page;
- Backlinks and popover previews;
- LaTeX for RA/FD notation, Mermaid for ER/pipeline diagrams;
- dark/light mode and Reader Mode;
- syntax highlighting for T-SQL;
- generated exam views from `year`, `semester`, and `exam_type` frontmatter.

## Deployment architecture

```text
Markdown + assets
        ↓
Quartz static build (GitHub Actions)
        ↓
GitHub Pages on an approved release branch
        ↓
Public study site + link to canonical PDF
```

Static-first means no login, database, chatbot, analytics, or server runtime. Vietnamese search should be tested with diacritics and without diacritics; retain exact topic tags as a fallback. Risks include broken internal links, inconsistent aliases, rights ambiguity in exam material, and search tokenization of Vietnamese text.

## Visual direction

Keep the IT004 identity academic, technical, student-built, fast, and high-density. Avoid generic AI gradients, copied student branding, fake terminal chrome, database-cylinder clip art, and decorative motion.
