# IT004 Knowledge Garden

This is the production-candidate, Markdown-first web companion for **IT004 / CƠ SỞ DỮ LIỆU / Knowledge Garden**. It is intentionally a focused set of linked theory, practice, exercise, exam-pattern, error, cheat-sheet, and source notes; the frozen handbook and D1 proof site remain the canonical print references.

## Build

Prerequisites: Node `>=22` and npm `>=10.9.2`.

```powershell
cd garden
npm ci
cd ..
node scripts/copy_garden_assets.mjs
cd garden
npm run quartz -- build -d content -o public
cd ..
python scripts/validate_garden_d2.py
```

For a local preview, use `npm run quartz -- build -d content -o public --serve --baseDir /CSDL_UIT/ --port 4180`. The base path is `/CSDL_UIT/`; do not assume the site is hosted at `/`.

`garden/public/`, `garden/node_modules/`, and generated PDF copies are ignored. `scripts/copy_garden_assets.mjs` reproducibly copies the three frozen root PDFs into the build's static PDF directory and checks SHA-256 equality before a build. No analytics, remote fonts, or backend search are used; Quartz's local static index powers search.

## Content contract

Every note has a title, description, type, topics, and related links. Provenance is explicit: `verified-artifact`, `reconstructed-exam-pattern`, or `original-practice`. Wikilinks express the semantic graph; the validator checks their targets, fixture identifiers, source IDs, and public-copy safety.
