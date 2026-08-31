# Phase A Knowledge Garden Architecture

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
  Verified Exams
  Exam Patterns
  Original Practice
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
  By Year
  By Semester
  By Type
Common Errors/
Flashcards/
Cheat Sheets/
Sources/
  Source Register
  Provenance Rules
  Copyright and Linking
```

## Node purpose and relationships

| node | purpose | source material | connects to |
|---|---|---|---|
| Start Here | Orient a new learner and show prerequisites | `LOC-A01`, UIT-O01/O02 | Theory, Practice, Exam Patterns |
| Theory | Canonical concept notes and formal definitions | handbook chapters, Tier A references | Exercises, Essays, Sources |
| Essay Questions | Deliberate-response practice with provenance labels | `exam_pattern_map.md`, future verified/paraphrased/original prompts | Theory, Exams, Common Errors |
| Exercises | Short feedback loops by skill and difficulty | current handbook exercises, newly authored problems | Theory, Essay Questions |
| Practice | SQL Server execution workflow | `LOC-A07`, GH-C02/C03/C04/C07, Microsoft docs | Theory/SQL, Exams, Errors |
| Exams | Year/semester/type index with summaries, not scans | UIT-O06/O07/O09 and COM-C01/C02 | Essay Questions, Practice |
| Common Errors | Explain misconceptions and failure modes | current handbook plus validated examples | Theory, Exercises, Practice |
| Flashcards/Cheat Sheets | Retrieval aids and rapid review | current handbook concepts | Theory and Exams |
| Sources | Auditable evidence and rights metadata | `source_inventory.md` | Every content node |

## Frontmatter and tags

```yaml
title: "Relational Algebra — Division"
type: theory # theory|exercise|essay|lab|exam-pattern|source|flashcard
chapter: ch03
topics: [relational-algebra, division, universal-query]
assessment: [midterm, final]
difficulty: intermediate
status: original # verified-exam|reconstructed|original
source_ids: [UIT-O01, TXT-A03]
schema: QLGV # QLGV|QLBH|auxiliary|none
```

Controlled tags: `chapter:ch01`…`chapter:ch07`, `type:*`, `assessment:*`, `topic:*`, `difficulty:*`, `status:*`, `source-tier:A`…`D`, and `schema:*`.

## Wikilink and graph rules

- Use stable slugs and bilingual aliases; do not link by changing display text.
- Every essay links to the theory concepts it tests, its exercise prerequisites, its exam-pattern/source record, and at least one common-error note.
- Every practical page links to the relevant SQL construct, schema page, and troubleshooting note.
- Link only where the relationship is pedagogically meaningful; no tag-spam or random graph edges.
- Use canonical links such as `[[Theory/Relational-Algebra/Division]]`, `[[Essay-Questions/Universal-Query]]`, and `[[Practice/SQL-Server/Triggers]]`.
- Run a broken-link check before publication.

## Quartz suitability and components

Quartz is a suitable static foundation because its documented feature set includes nested Explorer navigation, full-text search, Wikilinks, graph view, backlinks, LaTeX, syntax highlighting, Mermaid, breadcrumbs, TOC, dark mode, and Reader Mode. Use the stock components first and add only small IT004-specific CSS/JS changes.

Planned components:

- Explorer for the content tree;
- Search with `Ctrl/Cmd+K` and tag queries;
- Breadcrumbs and TOC on long notes;
- local graph on note pages and a global graph on the map page;
- Backlinks and popover previews;
- LaTeX for RA/FD notation, Mermaid for ER/pipeline diagrams;
- dark/light mode and Reader Mode;
- syntax highlighting for T-SQL.

## Deployment architecture

```text
Markdown + assets
        ↓
Quartz static build (GitHub Actions)
        ↓
GitHub Pages on main
        ↓
Public study site + link to canonical PDF
```

Static-first means no login, database, chatbot, analytics, or server runtime. Vietnamese search should be tested with diacritics and without diacritics; retain exact topic tags as a fallback. Risks include broken internal links, inconsistent aliases, rights ambiguity in exam material, and search tokenization of Vietnamese text.

## Visual direction

Keep the IT004 identity academic, technical, student-built, fast, and high-density. Avoid generic AI gradients, anime imagery, fake terminal chrome, database-cylinder clip art, and decorative motion.
