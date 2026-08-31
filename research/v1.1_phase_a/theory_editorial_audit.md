# Phase A Theory Handbook Editorial Audit

## Scope inspected

The current assembled handbook (`book/index.html`) and its chapter map were inspected without changing them. The handbook is a functioning 88-page publication and remains the source of truth for previously verified academic fixes.

## Concrete current observations

1. **Front matter is information-heavy.** The cover, author/editorial information, reference list, table of contents, learning method, roadmap, dataset descriptions, and disclaimers all occur before Chapter 1. Some of this is useful for the PDF but would be better separated into a compact cover/front matter and a clearly labelled “How to use this book” page.
2. **The title uses a promotional register.** “Cẩm nang từ nền tảng đến Exam Mastery”, “Mental Model”, “Fast Patterns”, “Common Traps”, and “Exam Signals” are useful internal labels, but their density can read like marketing copy. Keep the pedagogical labels selectively and state the academic purpose plainly.
3. **Visual language is somewhat template-like.** Repeated emoji callouts and many boxed sections create scanability but can make the book feel like a generic study template. Preserve the information hierarchy while reducing decorative repetition in a future rewrite.
4. **Administrative and rights material should be separated.** Author attribution, rights, source policy, and the colophon belong in a compact front/back-matter treatment; they should not compete with the learning roadmap.
5. **The current cover has a strong text-first identity but no single visual metaphor.** A future cover can keep the title and author while using one restrained database/graph motif rather than several competing badges.

These are editorial observations, not release blockers for the existing v1.0.0 PDF.

## Cover directions for review

### Direction A — Relational graph / schema map (recommended)

- Composition: white or warm-gray field with a restrained node-edge schema diagram occupying the lower two-thirds.
- Typography: bold condensed sans for `IT004`, humanist sans for Vietnamese title and author.
- Database metaphor: relations, attributes, and foreign-key lines; no cylinder icon.
- Density: medium-high, editorial, diagram-led.
- Show: `IT004 – CƠ SỞ DỮ LIỆU`, subtitle, author, edition year, one-line academic-use note.
- Avoid: gradients, badges, fake code, decorative database clip art.

### Direction B — Query pipeline / layered architecture

- Composition: three horizontal bands representing model → query → integrity, with a single thin flow line.
- Typography: technical grotesk with clear Vietnamese diacritics; small monospaced accent only for SQL keywords.
- Database metaphor: ANSI/SPARC layers and a query pipeline, not a literal server room.
- Density: compact and diagrammatic.
- Show: title, subtitle, author, a small `ER → RA → SQL → RBTV` pathway.
- Avoid: terminal-window framing, excessive code, neon colors.

### Direction C — Exam desk / annotated study sheet

- Composition: modular page-grid resembling a carefully edited study sheet, with one highlighted formula and margin annotations.
- Typography: readable serif or humanist sans body paired with a crisp display face.
- Database metaphor: a relation table fragment and a small FD/normalization annotation.
- Density: high but calm; strong hierarchy over decoration.
- Show: title, author, “Theory • Practice • Exam” triad, edition year.
- Avoid: cartoon stationery, gamified stickers, AI-generated imagery.
