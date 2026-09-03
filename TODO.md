# TODO — CSDL_UIT

## Completed Milestones
- [x] Phase A: Research Snapshot Frozen (`v1.1-editorial-practice` @ `6aef91e`)
- [x] Phase B2: Theory Handbook v1.1 Frozen (`v1.1-theory-redesign` @ `61eb5c8`)
- [x] Phase C1: Practical Handbook Architecture & Proof Frozen (`v1.1-practice-handbook` @ `f7dd840`)
- [x] Phase C2: Full Practical Handbook Frozen (`v1.1-practice-handbook` @ `59c519b`)
- [x] Phase D1: Knowledge Garden Architecture Proof Frozen (`v1.1-knowledge-garden` @ `922afe07bea7f28abf30c49054159a09a31be743`)
- [x] Phase D2: Quartz Knowledge Garden Production Candidate Built & Verified (`v1.1-quartz-garden` @ `be34ef3ef79956d9c1c2541782cabc82e66d0c6e`)
- [x] Workflow Migration: Phuchello Agent Workflow v2 Adopted
- [x] Integration Review: Independent Blind Audit Completed (`v1.1-integration-review` @ `reports/v1.1_glm53_blind_integration_review.md`)
- [x] Pre-merge Defect Remediation (`v1.1-release-candidate`)
- [x] Release-gate Hardening and GitHub CI validation
- [x] Gate 2: fast-forward release candidate to `main` @ `ad0ef293d0b85ba59de8ffad8966bd0d40720580`
- [x] Gate 3: tag and publish immutable `v1.1.0` at the same commit
- [x] Gate 4: manual Pages deployment (`workflow_dispatch` run `33761760360`, SUCCESS)

## Active Queue — v1.1.1 Maintenance
- [x] Reproduce live math-rendering defect from deployed v1.1.0 artifact
- [x] Identify root cause: `@quartz-community/latex` disabled in `garden/quartz.config.yaml`
- [x] Enable KaTeX rendering on `v1.1.1-maintenance`
- [x] Add post-build `scripts/validate_garden_render.py` regression smoke gate
- [x] Wire render smoke into `.github/workflows/validate.yml`
- [x] Open maintenance PR #3 to `main`
- [x] GitHub-hosted CI passes with render smoke enabled (runs `33763735969` and `33764039396`)
- [x] Apply duplicate H1 / redundant TOC cleanup without changing Garden prose
- [x] Replace nested desktop TOC/backlinks scrollbars with one context-rail scrollbar
- [x] Shorten visible left-rail site title while keeping `Knowledge Garden` as title suffix
- [ ] Merge PR #3 to `main`
- [ ] Human-authorized Pages deployment for the maintenance fix
- [ ] Desktop + mobile live visual smoke
- [ ] Decide whether to tag `v1.1.1`

## Deferred Maintenance
- [ ] Triage Garden npm audit findings separately from the visual-render fix (1 low, 2 high observed during v1.1.0 Pages build)
