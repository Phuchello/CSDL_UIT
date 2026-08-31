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

## Phase B2: Theory Handbook Redesign & Final Microcopy Freeze — Complete on `v1.1-theory-redesign`

- [x] Apply the approved B1 design system to the theory source HTML without changing the public v1.0 artifact.
- [x] Produce and normalize `dist/IT004_CSDL_UIT_LyThuyet_VoTrongPhuc.pdf` with deterministic build and metadata validation (Title: `IT004 – Cơ sở dữ liệu`, Subject: `IT004 – Cơ sở dữ liệu — Sổ tay lý thuyết`).
- [x] Redesign legacy multicolor visuals (Part 0 Bản đồ toàn môn and Ch1 ANSI/SPARC architecture) into restrained B1 vector SVGs.
- [x] Remove study-guide decorative emojis (`🤔`, `🎯`, `🏃`, `✅`, `🔥`, `⭐`, `💡`, `🚨`, `☢`, `⚠`) from instructional/editorial prose.
- [x] Neutralize promotional/hype wording ("Tuyệt kỹ", "Kỹ năng sống còn", "Thần chú", "TRỌNG ĐIỂM THI", "nhóm phép toán sống còn nhất", "Bậc thầy truy vấn") into restrained academic phrasing.
- [x] Replace unsupported lecturer-preference claims with evidence-safe phrasing for Double NOT EXISTS.
- [x] Reframe heading 5.3 to "5.3 Bảng tầm ảnh hưởng" with restrained evidence-backed introduction.
- [x] Integrate expanded automated QA linter in `scripts/build_theory_pdf.js`.
- [x] Run chapter/content checks, rendered-page review, overflow checks, and record evidence in `reports/v1.1_theory_qa.md`.
- [x] Keep practical handbook authoring and Quartz implementation out of this branch.

## Phase C1: Practical Handbook Architecture & Proof — Complete on `v1.1-practice-handbook`

- [x] Design full 8-part practical architecture and Table of Contents (`practice/chapters/00_cover_toc.html`).
- [x] Create companion design system `practice/css/practice.css` (B1 color family, code blocks, trace boxes, debug cards).
- [x] Author 9 representative proof chapter files covering 10 core pedagogical and technical areas.
- [x] Compile and generate 21-page proof PDF `dist/proofs/IT004_CSDL_UIT_v1.1_Practice_DesignProof.pdf`.
- [x] Enforce strict multi-row safety on triggers (`IF EXISTS (SELECT 1 FROM inserted i JOIN ...)`), rejecting scalar variables.
- [x] Author systematic 5-step debugging guide for 6 common T-SQL error codes.
- [x] Reconstruct Lab 01 and Lab 03–04 progression from Phase A empirical evidence.
- [x] Map all T-SQL topics to Microsoft Learn `TECH-A01`–`TECH-A11` citations.
- [x] Publish `DESIGN_NOTES.md` and 10-point `REVIEW_GUIDE.md` in `design/v1.1_practice/`.
- [x] Generate cover and contact sheet review images in `dist/review/v1.1_practice/`.
- [x] Complete QA validation report `reports/v1.1_practice_c1_qa.md`.

## Human Mentor Review Gate (Phase C1 $\rightarrow$ Phase C2)

- [ ] Mentor review of 21-page design proof PDF (`IT004_CSDL_UIT_v1.1_Practice_DesignProof.pdf`).
- [ ] Mentor review of 10-point rubric in `design/v1.1_practice/REVIEW_GUIDE.md`.
- [ ] Mentor approval to begin full Phase C2 authoring of the practical handbook.

## Phase C2 — Full Practical Handbook Complete on v1.1-practice-handbook

- [x] Author Parts 0–12 plus appendices and Labs 01–04 against the deterministic tr_* fixture.
- [x] Add practice/sql scripts, static semantic validator, final PDF build and normalization.
- [x] Render all pages and publish contact sheets and reports/v1.1_practice_full_qa.md.
- [x] Repair circular-FK reset lifecycle, align printed/runnable examples and add practice/EXAMPLE_REGISTRY.md.
- [x] Exclude superseded C1 proof chapters 06–08 from production compilation and normalize the 71-page PDF.
- [x] Run first and second SQLCMD reset successfully; static consistency validation passes.

## Phase C2 & Beyond — Held by scope

- [ ] Build or scaffold Quartz site.
- [ ] Merge to `main`.
- [ ] Tag and release v1.1.
