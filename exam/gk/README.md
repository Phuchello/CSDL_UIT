# NGÂN HÀNG ĐỀ THI & LỜI GIẢI GIỮA KỲ IT004 — CƠ SỞ DỮ LIỆU
**Đơn vị:** Trường Đại học Công nghệ Thông tin, ĐHQG-HCM
**Tác giả biên soạn:** VÕ TRỌNG PHÚC
**Phiên bản:** v1.3 GK Master Release (Phase D Academic Audit & Bank Expansion)

---

## 1. Giới Thiệu Module Giữa Kỳ (GK)
Module này cung cấp học liệu ôn tập toàn diện cho sinh viên ôn thi Giữa kỳ môn **IT004 – Cơ sở dữ liệu** đạt điểm tối đa (9–10 điểm), bao gồm:

1. **Bộ 150 bài tập độc lập phân dạng chuyên sâu (100% Đã kiểm chứng học thuật)**:
   - Chuyên đề 1: [Mô hình ERD & Ánh xạ quan hệ](bank/topic_01_erd.md) (25 bài độc lập: `ERD-P01` &rarr; `ERD-P25`)
   - Chuyên đề 2: [ĐSQH cơ bản, phép tập hợp & kết nối](bank/topic_02_ra_basic_join.md) (45 bài độc lập: `RA-B01` &rarr; `RA-B45`)
   - Chuyên đề 3: [Phép chia, gom nhóm & truy vấn phức hợp](bank/topic_03_ra_division_grouping.md) (45 bài độc lập: `RA-D01` &rarr; `RA-D45`)
   - Chuyên đề 4: [Transact-SQL DDL/DML & ràng buộc toàn vẹn](bank/topic_04_sql_ddl_dml.md) (35 bài độc lập: `SQL-P01` &rarr; `SQL-P35`)

2. **Bộ 15 Đề thi mô phỏng 75 phút chuẩn hóa UIT (135 câu hỏi Chuẩn Vàng)**:
   - Mỗi đề đúng 10.0 điểm, 75 phút tự luận, sở hữu 1 miền nghiệp vụ thực tế độc lập (15/15 đề đạt tiêu chuẩn **Gold Standard**).
   - Đã kiểm chứng thực thi 100% trên engine Microsoft SQL Server 2025 với kịch bản kiểm thử đối kháng bắt trúng các ca biên (tập chia rỗng, NULL outer join, đồng hạng cực trị).
   - Minh chứng kiểm định từng câu hỏi lưu tại [evidence_manifest.json](qa/evidence_manifest.json).

3. **Tiêu chuẩn kiểm chứng học thuật (Academic Verification Status)**:
   - **Tổng quy mô toàn ngân hàng:** **285 bài tập** (135 câu thuộc 15 Mock Exam + 150 bài luyện độc lập).
   - **Phân cấp xác minh thực tế:**
     * `EXECUTION_VERIFIED`: **155 bài** (120 câu Mock DDL/DML & RA + 35 bài luyện T-SQL độc lập thực thi trên SQL Server 2025).
     * `SEMANTICALLY_REVIEWED`: **130 bài** (15 câu Mock ERD + 25 bài luyện ERD + 90 bài luyện ĐSQH).
     * `DRAFT / PENDING REMEDIATION`: **0 bài (100% hoàn thiện)**.
   - **Thống kê phân loại kiểm định chuyên sâu (Verification Categories)**:
     * `ERD_REVIEWED`: **40 bài** (15 Mock Q1 + 25 Independent ERD).
     * `SQL_EXECUTED`: **65 bài** (30 Mock Q2A/Q2B + 35 Independent SQL).
     * `SQL_EXECUTED_AND_RA_VERIFIED`: **90 bài** (90 Mock RA Q2C1..Q2C6).
     * `RA_SEMANTICALLY_VERIFIED`: **90 bài** (45 Independent RA Basic + 45 Independent Division & Grouping, kèm bộ kiểm thử phản ví dụ 15 bài phép chia).
   - **Minh chứng minh bạch:** Toàn bộ 285/285 câu hỏi được lưu trữ bằng chứng chi tiết tại [evidence_manifest.json](qa/evidence_manifest.json) và [audit_report.json](qa/audit_report.json).

4. **Bộ 4 ấn phẩm PDF A4 chất lượng cao**:
   - `IT004_GK_NganHangDe_VoTrongPhuc.pdf` (65 trang A4): Đề bài 150 bài tập độc lập & 15 Mock Exam sạch (tuyệt đối không lộ đáp án).
   - `IT004_GK_LoiGiaiChiTiet_VoTrongPhuc.pdf` (257 trang A4): Toàn bộ hướng dẫn giải chi tiết 285 bài, phân tích tư duy toán học, barem điểm từng ý và bảng kiểm chứng thực thi.
   - `IT004_GK_CheatSheet_VoTrongPhuc.pdf` (2 trang A4): Tóm tắt công thức, checklist phòng thi, mẹo nhận diện từ khóa.
   - `IT004_GK_VerifiedOnly_VoTrongPhuc.pdf` (148 trang A4): Ấn bản tuyển tập chọn lọc nghiêm ngặt CHỈ chứa các nội dung đã kiểm chứng học thuật.

## 2. Hướng Dẫn Sử Dụng Để Đạt Điểm 9–10
- **Tuần 1–2:** Hoàn thành Chuyên đề 1 và Chuyên đề 2 để vững nền tảng ERD và các phép kết cơ bản.
- **Tuần 3:** Luyện chuyên sâu Chuyên đề 3 (Phép chia và Gom nhóm cực trị - câu phân loại 9–10) và Chuyên đề 4 (T-SQL DDL/DML).
- **Tuần 4:** Bấm giờ làm 15 đề Chuẩn Vàng trong thư mục `mocks/` (mỗi đề đúng 75 phút), sau đó đối chiếu `solution.md` để tự chấm điểm và tra cứu lỗi sai thường gặp.

## 3. Quy Trình Kiểm Thử & Kiểm Định (QA Audit)
Chạy validator tự động để kiểm tra tính toàn vẹn của ngân hàng đề:
```powershell
python exam/gk/scripts/validate_gk.py
```
Kiểm tra chất lượng render ấn phẩm PDF A4:
```powershell
python exam/gk/scripts/verify_pdf_preflight.py
```
