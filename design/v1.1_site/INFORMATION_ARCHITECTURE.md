# D1 Information Architecture

## Route proof

| Route | Role | Canonical relationship |
|---|---|---|
| `#/` | Home / orientation | learning map and two PDF entry points |
| `#/theory` | Theory landing | four concept notes |
| `#/practice` | Practice landing | labs, trigger, debugging |
| `#/theory/division` | relational algebra concept | Double NOT EXISTS, Lab 03, wrong-domain error |
| `#/theory/double-not-exists` | SQL reasoning concept | division and Lab 03 |
| `#/theory/rbtv-impact` | integrity concept | impact table and trigger |
| `#/practice/multi-row-trigger` | runnable practice note | RBTV and trigger errors |
| `#/theory/closure` | FD / normalization concept | candidate keys, 3NF/BCNF |
| `#/practice/lab-03` | advanced lab | universal query and result checking |
| `#/errors` | diagnosis index | symptom → concept/practice |
| `#/exam-patterns` | assessment index | provenance classes and signals |
| `#/sources` | provenance view | exact URLs/local paths |

The app uses a small hash router so the proof can be opened from a static file or GitHub Pages without a backend. A future Quartz migration can retain these slugs as canonical note IDs.

## Knowledge graph edges

Only pedagogical edges are represented:

- `division ↔ double-not-exists`: same universal-query semantics in procedural/declarative forms.
- `division ↔ lab-03`: practice checkpoint for the concept.
- `division ↔ errors`: wrong candidate domain is the characteristic failure mode.
- `rbtv-impact ↔ multi-row-trigger`: impact table determines the trigger's set-based guard.
- `multi-row-trigger ↔ errors`: scalar trigger variables fail under multi-row DML.
- `closure ↔ exam-patterns`: closure is the reasoning primitive behind candidate-key and normalization questions.

The graph is intentionally small. Year/semester/type views, when added, should query frontmatter and link to one canonical exam note rather than duplicate note bodies.

## Content boundaries

The site summarizes and connects `book/`, `practice/`, and `research/v1.1_phase_a/`; it does not mutate or copy those sources wholesale. The two canonical PDFs remain repository-local entry points and are not published by D1.
