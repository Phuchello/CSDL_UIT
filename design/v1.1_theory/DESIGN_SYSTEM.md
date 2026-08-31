# IT004 v1.1 — Theory Design System (B1 proof)

This is a controlled visual/editorial proof, not a replacement for the v1.0 handbook. It establishes the page language to review before a full theory conversion.

## Identity

- Book identity: IT004 — CƠ SỞ DỮ LIỆU
- Attribution: BIÊN SOẠN: VÕ TRỌNG PHÚC
- Tone: university technical handbook; calm, precise, authored, diagram-led where a figure clarifies a mechanism.
- Cover content is limited to the three approved lines. Diagram labels are semantic schema notation, not promotional metadata.

## Three cover proofs

- Cover A — Editorial Schema: warm paper field, navy/teal relation boxes, a measured R1 → R2 → R3 → R4 key path, and generous negative space. It is a strong discussion candidate only; the reviewer chooses.
- Cover B — Formal Relational: one prominent π/σ expression above a compact relation structure, denser than A without becoming a formula sheet.
- Cover C — Minimal Structural: large type, a single vertical relation/key spine, sparse marks, and the strongest negative space without extra prose.

## Type system

The proof uses fonts already present on common Windows/macOS/Linux systems and does not bundle font files:

| Role | Stack | Size / leading | Treatment |
|---|---|---:|---|
| Cover title | "Segoe UI", Arial, "Liberation Sans", sans-serif | 30–35 pt | uppercase, 700–800, generous tracking |
| Part/chapter title | "Segoe UI", Arial, "Liberation Sans", sans-serif | 22–25 pt / 1.12 | 700, navy |
| H2 | "Segoe UI", Arial, "Liberation Sans", sans-serif | 15 pt / 1.2 | 700, teal rule |
| H3 | "Segoe UI", Arial, "Liberation Sans", sans-serif | 11.5 pt / 1.25 | 700, ink |
| Body | Georgia, Cambria, "Times New Roman", "Liberation Serif", serif | 10.5 pt / 1.48 | regular, 62–72 character measure |
| Caption/table | "Segoe UI", Arial, "Liberation Sans", sans-serif | 8.5–9 pt / 1.3 | muted ink |
| Code/formula | Consolas, Cascadia Mono, monospace | 8.8–9.3 pt / 1.4 | pale field, no terminal chrome |

## Color system

The palette is deliberately small and printable:

- #203047 ink/navy for titles and primary lines.
- #1E7881 teal for section rules and relationship emphasis.
- #B57B36 ochre for a second semantic relationship or caution.
- #A94A32 rust only for a diagnostic/error state.
- #FBFAF7 paper, #EEF2F2 soft panel, #CAD4D4 rules.

Color encodes hierarchy or relation type; it is never the only carrier of meaning.

## Page grid

- A4 portrait, 210 × 297 mm.
- Content padding: 18 mm left/right, 18 mm top, 17 mm bottom; cover pages use 23 mm.
- Quiet footer: chapter label at left and page number at right; no repeated author slogan.
- Every proof page is an explicit .page with break-after: page so the design can be reviewed one page at a time.
- Figures, tables, code blocks, and callouts use break-inside: avoid; no element is allowed to create a horizontal scrollbar.

## Editorial components

- section-kicker, page-title, lead, and caption form the heading hierarchy.
- .note is a restrained side rule for Ý chính, Nhận xét, Ghi nhớ, or Khi làm bài.
- .trace is a numbered state/logic sequence used for RA, ER mapping, and closure.
- .schema-card and inline SVG figures carry semantic labels and captions.
- Small labels are editorial notation: compact sans text with a thin rule, not filled UI badges.
- Tables use a navy header, light row rules, and modest wrapping; no tiny text or badge wall.
- Code is shown as a clean pale block with a caption and readable line height.

## Proof scope

The 17-page proof contains three covers, a compact publication note, a TOC sample, representative pages for Chapters 1, 2, 3, 5, and 6, one exercise, one worked solution, and one diagnostic page. It does not alter the existing book/ source or the canonical v1.0 PDF.
