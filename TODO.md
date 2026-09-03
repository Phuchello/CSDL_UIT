# TODO — CSDL_UIT v1.1

## Completed Milestones
- [x] Phase A: Research Snapshot Frozen (`v1.1-editorial-practice` @ `6aef91e`)
- [x] Phase B2: Theory Handbook v1.1 Frozen (`v1.1-theory-redesign` @ `61eb5c8`)
- [x] Phase C1: Practical Handbook Architecture & Proof Frozen (`v1.1-practice-handbook` @ `f7dd840`)
- [x] Phase C2: Full Practical Handbook Frozen (`v1.1-practice-handbook` @ `59c519b`)
- [x] Phase D1: Knowledge Garden Architecture Proof Frozen (`v1.1-knowledge-garden` @ `922afe07bea7f28abf30c49054159a09a31be743`)
- [x] Phase D2: Quartz Knowledge Garden Production Candidate Built & Verified (`v1.1-quartz-garden` @ `be34ef3ef79956d9c1c2541782cabc82e66d0c6e`)
  - [x] remove invented TECH-MS* and UIT-E* IDs; derive strictly from Phase A ledgers
  - [x] validate and resolve all `related` targets uniquely
  - [x] enforce mandatory graph chain links (`division` ↔ `double-not-exists` ↔ `lab-03` ↔ `wrong-universal-candidate`)
  - [x] deepen all 11 core notes to standalone teaching depth
  - [x] restore canonical Trigger event discrimination contract & DeptId NOT NULL distinction
  - [x] remove legacy CamNang from current product navigation; strict single lowercase PDF naming
  - [x] rebuild Quartz (109 files emitted) with zero broken internal links (2,819 checked)
  - [x] regenerate all 10 review captures in `dist/review/v1.1_quartz/`
  - [x] mentor final D2 review and freeze patch completed
- [x] Workflow Migration: Phuchello Agent Workflow v2 Adopted
- [x] Integration Review: Independent Blind Audit Completed (`v1.1-integration-review` @ `reports/v1.1_glm53_blind_integration_review.md`)

## Active Queue (Pre-Merge Remediation)
- [ ] M-01: Update root `README.md` to reflect v1.1 dual handbooks (Theory 64p + Practice 71p) and Quartz Knowledge Garden
- [ ] M-02: Update `.github/workflows/pages.yml` to build Quartz in `garden/` and deploy `garden/public`
- [ ] m-01: Archive historical monolithic `dist/IT004_CSDL_UIT_CamNang_VoTrongPhuc.pdf` in release metadata
- [ ] Rerun integration verification gate

## Final Release Gates (Held until M-01 / M-02 Remediation)
- [ ] fast-forward merge `v1.1-quartz-garden` to `main`
- [ ] tag and release `v1.1.0`
- [ ] publish GitHub Pages
