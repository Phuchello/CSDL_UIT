# TODO — CSDL_UIT v1.1

## Phase A: Research Snapshot Frozen / Approved for Implementation on `v1.1-editorial-practice`

- [x] Ingest and audit all 6 local transport attachments with verified page counts (`local_corpus_audit.md`).
- [x] Bóc tách 17 original documents from consolidated PDFs/TXT/DOCX/XLSX.
- [x] Ingest all mentor-provided direct URLs and correct the 2023–2024 Midterm Đề 1 document URL.
- [x] Inspect and deduplicate the additional practical variants; promote 4 with visible header/content evidence and retain 4 blocked leads as non-canonical.
- [x] Rebuild `artifact_registry.md` with 31 canonical artifacts (17 exam, 10 practical-exam, 3 review, 1 lab-corpus), exact URLs for web-sourced entries, and actual local paths for reconstructions.
- [x] Maintain the 17-batch research log and freeze a high-coverage implementation snapshot without claiming exhaustive Internet coverage.
- [x] Mathematically synchronize `artifact_count` in `exam_pattern_map.md` and `essay_bank_plan.md` with listed unique exam/practical-exam IDs.
- [x] Assign dedicated Microsoft Learn source IDs (`TECH-A01` to `TECH-A11`).
- [x] Reclassify Trigger scope as `CORE THEORY & EXAM REQUIREMENT; ADVANCED PRACTICAL`.
- [x] Replace false precision with qualitative confidence scales (`HIGH`, `MEDIUM-HIGH`, `MEDIUM`, `LOW`).
- [x] Create `validation_report.md` with Research Snapshot, Direct URL, Source-ID, Artifact-ID, Artifact Count, Copyright Safety, Repository Safety and Ready-for-Implementation checks.
- [x] Keep `artifact_registry.md` extensible for future evidence; further discovery is non-blocking for Phase B.

## Human Review Gate (Pending Mentor Decision)

- [ ] Mentor review and approval of source register (`source_inventory.md`).
- [ ] Mentor approval of 31 canonical artifacts and four unpromoted leads (`artifact_registry.md`).
- [ ] Mentor approval of practical skill scope (`CORE` vs `OPTIONAL`).
- [ ] Mentor approval of theory cover brief (Minimal Relational Schema Graph).
- [ ] Mentor approval of Quartz Knowledge Garden static architecture.

## Phase B2: Theory Handbook Redesign & Final Polish — Complete on `v1.1-theory-redesign`

- [x] Apply the approved B1 design system to the theory source HTML without changing the public v1.0 artifact.
- [x] Produce and normalize `dist/IT004_CSDL_UIT_LyThuyet_VoTrongPhuc.pdf` with deterministic build and metadata validation (Title: `IT004 – Cơ sở dữ liệu`, Subject: `IT004 – Cơ sở dữ liệu — Sổ tay lý thuyết`).
- [x] Redesign legacy multicolor visuals (Part 0 Bản đồ toàn môn and Ch1 ANSI/SPARC architecture) into restrained B1 vector SVGs.
- [x] Remove legacy warning/bẫy icon language from printed theory sources.
- [x] Integrate automated legacy artifact linter (palette + label) in build/QA pipeline.
- [x] Run chapter/content checks, rendered-page review, overflow checks, and record evidence in `reports/v1.1_theory_qa.md`.
- [x] Keep practical handbook authoring and Quartz implementation out of this branch.

## Phase B3/C — Strictly Blocked Until Mentor Approval

- [ ] Build or scaffold Quartz site.
- [ ] Rewrite theory handbook chapters.
- [ ] Author practical SQL Server handbook.
- [ ] Generate new PDFs or publish releases.
