# NGÂN HÀNG ĐỀ THI & LỜI GIẢI GIỮA KỲ IT004 — CƠ SỞ DỮ LIỆU
**Đơn vị:** Trường Đại học Công nghệ Thông tin, ĐHQG-HCM
**Tác giả biên soạn:** VÕ TRỌNG PHÚC
**Phiên bản:** v1.2 GK Master Release

---

## 1. Giới Thiệu Module Giữa Kỳ (GK)
Module này cung cấp giải pháp toàn diện cho sinh viên tự học và luyện thi Giữa kỳ môn **IT004 – Cơ sở dữ liệu** đạt điểm tối đa (9–10 điểm), bao gồm:
1. **Ngân hàng câu hỏi phân dạng (173 bài tập)**:
   - Chuyên đề 1: [Mô hình ERD & Ánh xạ quan hệ](bank/topic_01_erd.md) (33 bài)
   - Chuyên đề 2: [ĐSQH cơ bản, phép tập hợp & kết nối](bank/topic_02_ra_basic_join.md) (62 bài)
   - Chuyên đề 3: [Phép chia, gom nhóm & truy vấn phức hợp](bank/topic_03_ra_division_grouping.md) (52 bài)
   - Chuyên đề 4: [Transact-SQL DDL/DML & chuyển đổi ĐSQH](bank/topic_04_sql_ddl_dml.md) (26 bài)
2. **15 Đề thi mô phỏng 75 phút chuẩn hóa**:
   - Mỗi đề đúng 10.0 điểm, 75 phút tự luận, có đề bài riêng không lộ đáp án và hướng dẫn chấm chi tiết kèm barem điểm từng ý.
3. **Bộ ấn phẩm PDF A4 chất lượng cao**:
   - `IT004_GK_NganHangDe_VoTrongPhuc.pdf`: Ngân hàng đề thi bài tập & 15 Mock exam.
   - `IT004_GK_LoiGiaiChiTiet_VoTrongPhuc.pdf`: Toàn bộ lời giải chi tiết, phân tích tư duy và barem chấm điểm.
   - `IT004_GK_CheatSheet_VoTrongPhuc.pdf`: Tóm tắt công thức, checklist phòng thi, mẹo nhận diện từ khóa.

## 2. Hướng Dẫn Sử Dụng Để Đạt Điểm 9–10
- **Tuần 1–2:** Hoàn thành Chuyên đề 1 và Chuyên đề 2 để vững nền tảng ERD và các phép kết cơ bản.
- **Tuần 3:** Luyện chuyên sâu Chuyên đề 3 (Phép chia và Gom nhóm cực trị - câu phân loại 9–10).
- **Tuần 4:** Bấm giờ làm 15 đề mock trong thư mục `mocks/MOCK-01` đến `mocks/MOCK-15` (mỗi đề đúng 75 phút), sau đó đối chiếu `solution.md` để tự chấm điểm và tra cứu lỗi sai thường gặp.

## 3. Quy Trình Kiểm Thử & Kiểm Định (QA Audit)
Chạy validator tự động để kiểm tra tính toàn vẹn của ngân hàng đề:
```powershell
python exam/gk/scripts/validate_gk.py
```
