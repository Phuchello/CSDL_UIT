# PROJECT STATE — CSDL_UIT

## Checkpoint

v1.1 Phase C2 — Production Consistency Patch Complete

## Date

2026-08-31

## Active branch

`v1.1-practice-handbook`

## Status

PHASE A and THEORY v1.1 remain FROZEN and UNTOUCHED. PHASE C2 is complete on `v1.1-practice-handbook`: the production-only chapter manifest, deterministic fixture/scripts, example registry, normalized final PDF, contact sheets and QA report are present. The circular-FK reset succeeds on first and second SQLCMD runs; static consistency validation passes. Theory v1.1 (`61eb5c8`), Phase A (`6aef91e`), `main` (`6ccf5a4`) and `phuchello/phuchello` remain untouched. Ready for Human Mentor full-practice review.

## Scope completed in this checkpoint

- Thiết kế kiến trúc tổng thể 8 phần chuyên đề cho cẩm nang thực hành `IT004 — THỰC HÀNH CƠ SỞ DỮ LIỆU`;
- Xây dựng hệ thống thiết kế `practice/css/practice.css` đồng bộ cùng họ B1 với sách lý thuyết;
- Biên soạn 9 tệp chương mẫu trong `practice/chapters/` bao quát 10 phương diện sư phạm và kỹ thuật cốt lõi;
- Xây dựng bản mẫu đại diện 21 trang A4 không có lỗi tràn lề hay ký tự vỡ (`IT004_CSDL_UIT_v1.1_Practice_DesignProof.pdf`);
- Chuẩn hóa mẫu Trigger dạng tập hợp an toàn đa dòng (`Multi-Row Safety`), cho phép cập nhật thông tin không liên quan và chặn chính xác vi phạm;
- Xây dựng khung chẩn đoán lỗi 5 bước cho 8 mã lỗi T-SQL riêng biệt;
- Tái dựng tiến trình Lab 01 và Lab 03–04 cùng chiến lược phòng thi thực hành từ bằng chứng thực nghiệm Phase A;
- Lập bảng đối chiếu mã nguồn kỹ thuật Microsoft Learn `TECH-A01`–`TECH-A11` tách bạch với dữ liệu khảo sát môn học;
- Xuất bản tài liệu ghi chú thiết kế và hướng dẫn đánh giá 10 tiêu chí (`DESIGN_NOTES.md`, `REVIEW_GUIDE.md`);
- Xuất bản báo cáo QA toàn diện và contact sheets (`reports/v1.1_practice_c1_qa.md`, `dist/review/v1.1_practice/`).

## Explicit hold

Do not build Quartz, merge to `main`, tag, or release from this branch.

## Deliverables

- `practice/`
- `design/v1.1_practice/`
- `dist/proofs/IT004_CSDL_UIT_v1.1_Practice_DesignProof.pdf`
- `dist/review/v1.1_practice/`
- `reports/v1.1_practice_c1_qa.md`
- `practice/sql/` deterministic training fixture and test scripts
- `dist/IT004_CSDL_UIT_ThucHanh_VoTrongPhuc.pdf` (71 pages, normalized metadata)
- `dist/review/v1.1_practice_full/` contact sheets
- `reports/v1.1_practice_full_qa.md`
- `scripts/validate_practice_static.py`

## C2 correction-pass evidence

- Explicit circular-FK drop/null lifecycle and idempotent reset validated twice with SQLCMD.
- B01/B02/A01/A02/A03/A04/A05/A06/A07 printed and runnable expectations aligned to `practice/EXAMPLE_REGISTRY.md`.
- Production compilation excludes superseded C1 proof chapters 06–08; PDF normalized to 71 pages.
- Static validator checks frozen provenance IDs, registry conflicts, stale dates, intentional INSERT NOT NULL fields, set-operator variants and trigger-E schema boundary.
