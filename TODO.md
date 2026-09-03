# TODO — CSDL_UIT v1.1

## Completed Milestones
- [x] Phase A: Research Snapshot Frozen (`v1.1-editorial-practice` @ `6aef91e`)
- [x] Phase B2: Theory Handbook v1.1 Frozen (`v1.1-theory-redesign` @ `61eb5c8`)
- [x] Phase C1: Practical Handbook Architecture & Proof Frozen (`v1.1-practice-handbook` @ `f7dd840`)
- [x] Phase C2: Full Practical Handbook Frozen (`v1.1-practice-handbook` @ `59c519b`)
- [x] Phase D1: Knowledge Garden Architecture Proof Frozen (`v1.1-knowledge-garden` @ `922afe07bea7f28abf30c49054159a09a31be743`)
- [x] Phase D2: Quartz Knowledge Garden Production Candidate Built & Verified (`v1.1-quartz-garden` @ `be34ef3ef79956d9c1c2541782cabc82e66d0c6e`)
- [x] Workflow Migration: Phuchello Agent Workflow v2 Adopted
- [x] Integration Review: Independent Blind Audit Completed (`v1.1-integration-review` @ `reports/v1.1_glm53_blind_integration_review.md`)
- [x] Pre-merge Defect Remediation (`v1.1-release-candidate`):
  - [x] M-01: Rewrote root `README.md` for v1.1 dual handbooks (Theory 64p + Practice 71p) and Quartz Knowledge Garden; retained historical note on v1.0 `CamNang`
  - [x] M-02: Replaced `.github/workflows/pages.yml` with Node 22 Quartz deployment; updated `.github/workflows/validate.yml` to test handbooks and Quartz site; updated `docs/BUILD.md`
  - [x] M-03: Factual correction for FK precedence over AFTER DELETE trigger (`FK_tr_departments_head` Msg 547); removed unreachable DELETE logic from `05_triggers.sql`, updated `06_test_cases.sql`, `multi-row-trigger.md`, `13_debugging_expanded.html`, `EXAMPLE_REGISTRY.md`, and validators; regenerated and normalized Practice PDF (71p)
  - [x] Full verification suite, link crawl (2,819 links, 0 broken), and live SQL Server execution verified
- [x] Release-gate Hardening:
  - [x] Configured `pages.yml` as `workflow_dispatch` only (human-controlled gate; no auto-deploy on push to `main`)
  - [x] Documented 4-gate release sequence in `docs/BUILD.md` (validate -> merge -> tag/release -> Pages dispatch)
  - [x] CI Validation Gate: Ran `validate.yml` on `ubuntu-latest` via PR #2 (run `33743104644`, ALL PASS in 28s)

## Active Queue
- [ ] Mentor review of `v1.1-release-candidate` (PR #2 and CI status)

## Final Release Gates (Held until Mentor Review Approval)
- [ ] Cổng 2: fast-forward merge to `main`
- [ ] Cổng 3: tag and release `v1.1.0`
- [ ] Cổng 4: explicit human-authorized Pages dispatch
