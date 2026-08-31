# Phase A Theory Handbook Editorial Audit

## Scope inspected

The assembled handbook (`book/index.html`) and chapter map were inspected without changing them. The handbook remains an 88-page publication and the source of truth for its own previously verified academic fixes. This audit proposes a future editorial direction only; it does not redesign or regenerate the PDF.

## Concrete current observations

1. **Front matter is information-heavy.** The cover, author/editorial information, references, table of contents, learning method, roadmap, dataset descriptions, and disclaimers all occur before Chapter 1. A future edition could separate a compact cover/front matter from a clearly labelled “How to use this book” page.
2. **The title uses a promotional register.** “Cẩm nang từ nền tảng đến Exam Mastery”, “Mental Model”, “Fast Patterns”, “Common Traps”, and “Exam Signals” are useful internal labels, but their density can read like marketing copy. Keep pedagogical labels selectively and state the academic purpose plainly.
3. **Visual language is somewhat template-like.** Repeated emoji callouts and many boxed sections create scanability but can make the book feel generic. Preserve the information hierarchy while reducing decorative repetition in a future rewrite.
4. **Administrative and rights material should be separated.** Author attribution, rights, source policy, and the colophon belong in a compact front/back-matter treatment; they should not compete with the learning roadmap.
5. **The current cover lacks one dominant visual metaphor.** A restrained relational/schema graphic can unify the academic identity without adding marketing text.

## Corrected cover brief

### Recommended direction — relational schema / graph editorial cover

- Composition: warm white or light neutral field with a restrained node-edge schema diagram occupying the lower two-thirds.
- Typography: clear Vietnamese-capable display face for the course title and a humanist sans for the author line.
- Database metaphor: relations, attributes, PK/FK lines, and a small ER-to-relation transition; no cylinder icon.
- Density: medium-high, editorial, diagram-led; complexity comes from composition, typography, and relational graphics.
- **Cover text only:**
  - `IT004`
  - `CƠ SỞ DỮ LIỆU`
  - `BIÊN SOẠN: VÕ TRỌNG PHÚC`
- Subtitle: none recommended at this stage; propose one only if a later visual test shows a material gain.

Do not place edition year, academic-use note, version, GitHub, Exam Mastery, Theory • Practice • Exam, copyright, publication status, school-affiliation block, or badges on the cover. Those details belong in front/back matter or repository metadata.

## Alternative visual directions for human review

### Direction B — query pipeline / layered architecture

Three quiet horizontal bands represent model → query → integrity, with one thin flow line. Keep all explanatory text off the cover; use the bands as the visual structure.

### Direction C — annotated relation / FD study sheet

A carefully edited relation fragment and one FD/normalization annotation form a high-density but calm composition. Keep the cover text limited to the three required lines.

These alternatives are briefs only. No implementation, image generation, or PDF change is in scope for Phase A.
