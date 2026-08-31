# PROJECT STATE — CSDL_UIT

## Checkpoint

v1.1 Phase B2 — Theory Handbook Final Microcopy Freeze Complete

## Date

2026-08-31

## Active branch

`v1.1-theory-redesign`

## Status

PHASE A remains frozen. PHASE B2 final microcopy freeze is 100% COMPLETE on `v1.1-theory-redesign`: all study-guide/decorative emojis removed, promotional/hype phrasing replaced with restrained academic prose, unsupported lecturer-preference claims neutralized to evidence-safe statements, heading 5.3 reframed, and expanded automated QA linter integrated. All QA, visual, and safety checks PASS. Theory v1.1 is ready to freeze. Sách v1.0.0, PDF chính thức, nhánh `main`, `v1.1-editorial-practice` và kho `phuchello/phuchello` hoàn toàn không bị ảnh hưởng.

## Scope completed in this checkpoint

- Bóc tách toàn diện 6 tệp đính kèm cục bộ thành 17 tài liệu gốc với số trang chuẩn xác (`local_corpus_audit.md`);
- Sổ đăng ký nguồn đầy đủ 60 nguồn (`source_inventory.md`);
- Danh bộ 31 hiện vật chuẩn hóa với URL trực tiếp cho nguồn web hoặc đường dẫn cục bộ thực tế cho bản tái dựng, bằng chứng khử trùng lặp mirror và quyết định promote/unpromote (`artifact_registry.md`);
- Nhật ký 17 đợt tìm kiếm/cross-check với trạng thái snapshot đóng băng cho triển khai (`web_search_log.md`);
- Bản đồ mẫu đề thi thực chứng với `artifact_count` khớp 100% về mặt cơ học (`exam_pattern_map.md`);
- Bản đồ kỹ năng T-SQL với mã nguồn Microsoft `TECH-A01`–`TECH-A11` chuẩn xác và phân loại Trigger (`practical_coverage_map.md`);
- Kế hoạch ngân hàng câu hỏi tự luận theo chuyên đề với 3 lớp xuất xứ minh bạch (`essay_bank_plan.md`);
- Báo cáo kiểm thử snapshot, URL, source/artifact IDs, counts, copyright và repository safety (`validation_report.md`).
- Bộ nguồn lý thuyết đã áp dụng design system B1, cùng PDF lý thuyết 64 trang và các contact sheet QA (`dist/IT004_CSDL_UIT_LyThuyet_VoTrongPhuc.pdf`, `dist/review/v1.1_theory/`).
- Báo cáo QA B2 và các trình dựng/chuẩn hóa PDF xác định (`reports/v1.1_theory_qa.md`, `scripts/build_theory_pdf.js`, `scripts/normalize_theory_pdf.py`).

## Explicit hold

Further source discovery is non-blocking for the theory-redesign review. This branch does not build Quartz, author the practical book, merge to `main`, tag, or release.

## Deliverables

`research/v1.1_phase_a/`
