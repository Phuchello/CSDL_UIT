# PROJECT STATE — CSDL_UIT

## Checkpoint

v1.1 Phase C1 — Practical Handbook Architecture & Representative Proof (Technical Correction Complete)

## Date

2026-08-31

## Active branch

`v1.1-practice-handbook`

## Status

PHASE A and THEORY v1.1 remain FROZEN and UNTOUCHED. PHASE C1 is 100% COMPLETE on `v1.1-practice-handbook`: created the separate practical handbook architecture, authored and technically corrected the 21-page representative proof PDF (`dist/proofs/IT004_CSDL_UIT_v1.1_Practice_DesignProof.pdf`), audited SQL semantics (TOP WITH TIES, explicit Self-Join mini-schema, half-open date range, granular GIAOVIEN trigger logic with test cases, logical query processing trace, DML sandbox vs persist mode, 8-error debugging dictionary, restrained exam provenance, and Microsoft Learn source-role separation). Theory v1.1 (`61eb5c8`), Phase A (`6aef91e`), `main` (`6ccf5a4`) and `phuchello/phuchello` remain completely untouched. Ready for Human Mentor C1 Approval.

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

Do not author the full Phase C2 practical book, build Quartz, merge to `main`, tag, or release until the mentor approves the Phase C1 design proof.

## Deliverables

- `practice/`
- `design/v1.1_practice/`
- `dist/proofs/IT004_CSDL_UIT_v1.1_Practice_DesignProof.pdf`
- `dist/review/v1.1_practice/`
- `reports/v1.1_practice_c1_qa.md`
