# D1 Knowledge Garden — Design System

## Intent

The proof is a serious student-built technical study site, not a marketing landing page or a generic Quartz starter. It uses the visual language already established by the two books: navy structure, teal actions/links, ochre attention cues, paper surfaces, and restrained rust for failure states.

## Tokens

| Role | Token / value | Use |
|---|---|---|
| Structure | `--navy-950: #102a43` | wordmark, headings, code surface |
| Link / success | `--teal-700: #0f766e` | links, active navigation, concept edges |
| Study cue | `--ochre-600: #b7791f` | callouts and exam signals |
| Error cue | `--rust-700: #9c3d2d` | common-error labels only |
| Surface | `--paper: #fbfaf6` | page background |
| Ink | `--ink: #243447` | body text |

Typography pairs a readable system sans for UI/body copy with Georgia for editorial headings. Cards and borders stay quiet so the graph and concept relationships carry the hierarchy.

## Components

- **Explorer:** compact left rail with grouped links; no duplicate chapter trees.
- **Context rail:** optional right rail for local TOC and classification.
- **Concept note:** kicker, H1, metadata, selected sections, one or two meaningful related links.
- **Learning map:** Concept → Reasoning → Practice → Error diagnosis → Exam transfer.
- **Provenance tag:** `verified-artifact`, `reconstructed-exam-pattern`, or `original-practice`; never “official” without evidence.
- **Search result:** category tag + title + one-line summary.

## Interaction rules

- Every focusable control has a visible `:focus-visible` outline.
- Skip link appears on keyboard focus.
- On small screens the explorer collapses behind a native button; no hover-only actions.
- Search is local and static; Vietnamese labels remain readable with or without diacritics in content summaries.
- Avoid animation, badges, gradients, and decorative database clip-art.
