# Nhật Ký Tìm Kiếm Web & Thẩm Định Độ Bão Hòa (Web Search Log) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31
**Mục đích:** Ghi lại chi tiết các đợt tìm kiếm web công khai, đối chiếu đa nguồn và chứng minh đạt ngưỡng bão hòa tìm kiếm (Search Saturation).

---

## 1. Nhật Ký Các Đợt Tìm Kiếm (Search Batches)

| Batch ID | Truy vấn chính (Search Queries) | Nền tảng / Miền mục tiêu | Nguồn tài liệu mới phát hiện | Canonical Artifacts mới | Năm học ghi nhận | Chủ đề & Mẫu đề thi mới | Ghi chú & Đánh giá |
| :---: | :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| **BATCH-01** | `site:uit.edu.vn OR site:httt.uit.edu.vn "IT004" "Cơ sở dữ liệu" OR "Database"` | `uit.edu.vn`, `httt.uit.edu.vn`, `student.uit.edu.vn` | Thông báo học vụ, lịch thi thực hành tập trung, mã lớp môn học (`IT004.Q11`, `IT004.L111`) | - | 2022–2026 | Quy định thi thực hành máy tập trung, tuyển trợ giảng môn CSDL | Xác thực tên môn học, mã môn chính thức và cơ chế đánh giá thực hành. |
| **BATCH-02** | `site:httt.uit.edu.vn "IT004" OR "Cơ sở dữ liệu" "đề cương" OR "giáo trình" OR "tín chỉ"` | `httt.uit.edu.vn` | Danh mục giáo trình Khoa HTTT: *Giáo trình CSDL quan hệ* (Huỳnh Thị Hà et al.), *SQL Server* (Đỗ Thị Minh Phụng) | - | 2022–2025 | Cấu trúc chương trình đào tạo chuẩn 132 tín chỉ, đề cương môn học | Xác lập danh mục tài liệu đối chiếu học thuật cấp Khoa. |
| **BATCH-03** | `"IT004" "Đề thi" OR "giữa kỳ" OR "cuối kỳ" site:github.com OR site:studocu.com` | `github.com`, `studocu.com` | Kho đề thi thực hành & cuối kỳ trên Studocu (`course/131131`), repo `UIT-DS/IT004.L19-Database` | `EXAM-2023-2024-HK1-FINAL-01`, `EXAM-2020-2021-HK2-MID-01` | 2020–2024 | ERD, ĐSQH, SQL Server, RBTV Trigger, Phụ thuộc hàm & Chuẩn hóa | Xác định nguồn đề thi tham khảo phổ biến của sinh viên UIT. |
| **BATCH-04** | `site:github.com "IT004" "CSDL" OR "Database" "QuanLyBanHang" OR "QuanLyGiaoVu"` | `github.com` | Repositories: `SeaW1nd/IT004-CSDL`, `HiImKing1509/IT004_Database`, `phanxuanquang/UIT_SoftwareEngineering_Subjects` | `LAB-CORPUS-QLBH-QLGV` | 2018–2024 | DDL/DML QLBH & QLGV, bài giải Lab01–Lab04, Trigger thực hành | Đối chiếu mã nguồn thực hành của cộng đồng với tệp lab cục bộ. |
| **BATCH-05** | `"IT004" "đề thi" "2021" OR "2022" OR "2023" OR "2024" OR "2025" "Cơ sở dữ liệu"` | `studocu.com`, `scribd.com`, `youtube.com` | Bộ đề thi lý thuyết và thực hành 2021–2025 trên Studocu & Scribd | `EXAM-2022-2023-HK1-FINAL-01`, `EXAM-2021-2022-HK1-FINAL-01` | 2021–2025 | Dạng chuẩn 1NF–BCNF, Phân rã Lossless, Trigger đa dòng | Xác nhận độ tương đồng rất cao giữa đề các năm. |
| **BATCH-06** | `site:learn.microsoft.com "CREATE TRIGGER" "Transact-SQL" "inserted" "deleted"` | `learn.microsoft.com` | Tài liệu chính thức Microsoft T-SQL: DML Trigger, bảng ảo `inserted`/`deleted`, Multi-row trigger guidance | - | Technical Reference | Cú pháp chuẩn `CREATE TRIGGER`, `ROLLBACK TRANSACTION`, `THROW`, an toàn đa dòng | Chuẩn hóa kỹ thuật cho Chương 5 & Chương 7. |
| **BATCH-07** | `"IT004" "phụ thuộc hàm" OR "dạng chuẩn" "đề thi" OR "đáp án" site:uit.edu.vn OR site:studocu.com` | `uit.edu.vn`, `studocu.com`, `github.com` | Chuyên đề ôn tập PTH & Chuẩn hóa: thuật toán bao đóng, thuật toán tìm khóa (tập nguồn/trung gian/treo), phân rã 3NF/BCNF | `EXAM-2019-2020-HK1-FINAL-01` | 2019–2024 | Bài toán thành viên $X \rightarrow Y \in F^+$, Phủ tối thiểu $F_c$, Khóa ứng viên | Khớp với thuật toán giảng dạy trong slide của ThS. Dương Phi Long. |
| **BATCH-08** | `"IT004" ("2015-2016" OR "2016-2017" OR "2017-2018" OR "2018-2019") "giữa kỳ" OR "cuối kỳ"` | `studocu.com`, `scribd.com` | Đề thi lịch sử các năm 2015–2019 trên Studocu và Scribd | `EXAM-2018-2019-HK1-MID-01`, `EXAM-2017-2018-HK1-MID-01`, `EXAM-2016-2017-HK1-MID-01` | 2015–2019 | ERD Vé xe, Quản lý tài khoản ngân hàng, Quản lý nhà cung cấp | Xác nhận tính liên tục của dạng đề thi qua hơn 10 năm. |

---

## 2. Kiểm Thử Quy Tắc Bão Hòa Tìm Kiếm (Search Saturation Verification)

Theo quy định, quá trình tìm kiếm đạt ngưỡng bão hòa khi **3 đợt tìm kiếm liên tiếp (Batch 06, Batch 07, Batch 08)** thỏa mãn:
1. Không phát hiện thêm họ nguồn mới ngoài các nhóm đã thiết lập.
2. Không phát hiện thêm chủ đề thực hành hay lý thuyết nào ngoài chương trình IT004 đã nhận diện.
3. Toàn bộ 7 họ nguồn lớn đã được khảo sát đầy đủ:
   - ✅ **Official UIT**: `uit.edu.vn`, `httt.uit.edu.vn`, `student.uit.edu.vn` (Batch 01, 02)
   - ✅ **GitHub**: Các kho lưu trữ chuyên đề UIT CSDL (Batch 03, 04)
   - ✅ **Studocu**: Kho lưu trữ đề thi và bài tập lớn (Batch 03, 05, 07, 08)
   - ✅ **Scribd**: Tài liệu đề thi và bài giảng lưu trữ (Batch 05, 08)
   - ✅ **SVUIT / Public University Indexes**: Các diễn đàn học thuật và video hướng dẫn ôn thi (Batch 03, 05)
   - ✅ **Microsoft Learn**: Tài liệu kỹ thuật chính thức SQL Server / T-SQL (Batch 06)
   - ✅ **Academic Textbooks**: Silberschatz, Elmasri & Navathe, Đồng Thị Bích Thủy et al. (Batch 02, 06)

**KẾT LUẬN: ĐẠT NGƯỠNG BÃO HÒA TÌM KIẾM (SEARCH SATURATION REACHED)**

---

## 3. Các Giới Hạn Của Khảo Sát Web (Documented Limitations)

- **Tài khoản nội bộ / Paywall**: Một số tệp trên Studocu/Scribd yêu cầu tài khoản trả phí hoặc tài khoản sinh viên đăng tải tài liệu để mở khóa toàn bộ trang. Các tài liệu này được nhận diện qua bản xem trước công khai và đối chiếu với bản sao cục bộ.
- **Kho lưu trữ Google Drive cá nhân**: Một số tài liệu lưu trữ trong Drive riêng tư không được lập chỉ mục trên Google Search.
- **Mã nguồn sinh viên**: Các bài giải trên GitHub của sinh viên có giá trị tham khảo về bối cảnh bài tập nhưng không được coi là chân lý học thuật (cần kiểm tra chéo với Microsoft Learn và giáo trình).
