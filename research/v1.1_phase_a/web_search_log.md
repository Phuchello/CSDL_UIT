# Nhật Ký Tìm Kiếm Web & Research Snapshot — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31
**Mục đích:** Ghi nhận minh bạch các đợt tìm kiếm web, tài liệu đối chiếu và quyết định đóng băng snapshot sau khi tiếp nhận, kiểm toán và lập chỉ mục các hiện vật đề thi/thực hành đã đủ bằng chứng.

---

## 1. Nhật Ký 17 Đợt Tìm Kiếm Hệ Thống (Systematic Search Batches)

| Batch ID | Truy vấn chính (Search Queries) | Nền tảng / Miền mục tiêu | Nguồn tài liệu phát hiện | Canonical Artifacts mới | Năm học ghi nhận | Chủ đề & Kỹ thuật mới | Trạng thái phát sinh chứng cứ |
| :---: | :--- | :--- | :--- | :---: | :---: | :--- | :---: |
| **BATCH-01** | `site:uit.edu.vn OR site:httt.uit.edu.vn "IT004" "Cơ sở dữ liệu" OR "Database"` | `uit.edu.vn`, `httt.uit.edu.vn` | Thông báo học vụ, lịch thi thực hành tập trung | - | 2022–2026 | Quy chế thi thực hành máy tập trung | Có chứng cứ mới (Thông tin học vụ) |
| **BATCH-02** | `site:httt.uit.edu.vn "IT004" OR "Cơ sở dữ liệu" "đề cương" OR "giáo trình"` | `httt.uit.edu.vn` | Danh mục giáo trình Khoa HTTT: *CSDL quan hệ*, *SQL Server* | - | 2022–2025 | Đề cương chi tiết, chương trình 132 tín chỉ | Có chứng cứ mới (Giáo trình chuẩn) |
| **BATCH-03** | `"IT004" "Đề thi" OR "giữa kỳ" OR "cuối kỳ" site:github.com OR site:studocu.com` | `github.com`, `studocu.com` | Kho đề thi thực hành & cuối kỳ trên Studocu, repo `UIT-DS` | `EXAM-2023-2024-HK1-FINAL-01` | 2020–2024 | ERD, ĐSQH, SQL Server, RBTV, Chuẩn hóa | Có chứng cứ mới (Hiện vật đề thi) |
| **BATCH-04** | `site:github.com "IT004" "CSDL" "QuanLyBanHang" OR "QuanLyGiaoVu"` | `github.com` | Repositories: `SeaW1nd/IT004-CSDL`, `HiImKing1509/IT004_Database` | `LAB-QLBH-QLGV-CORPUS` | 2018–2024 | DDL/DML QLBH & QLGV, bài giải Lab01–Lab04 | Có chứng cứ mới (Mã nguồn lab) |
| **BATCH-05** | `"IT004" "đề thi" "2021" OR "2022" OR "2023" OR "2024" OR "2025"` | `studocu.com`, `scribd.com` | Bộ đề thi thực hành và lý thuyết 2021–2025 trên Studocu & Scribd | `PRAC-2024-2025-HK1-302`, `PRAC-2023-2024-HK1-O117` | 2021–2025 | Dạng chuẩn BCNF, Phân rã Lossless, Đề thi thực hành | Có chứng cứ mới (Hiện vật đề thi) |
| **BATCH-06** | `site:learn.microsoft.com "CREATE TRIGGER" "Transact-SQL"` | `learn.microsoft.com` | Tài liệu kỹ thuật Microsoft T-SQL: DML Trigger, bảng ảo `inserted`/`deleted` | - | Technical Reference | Cú pháp `CREATE TRIGGER`, an toàn đa dòng | Có chứng cứ mới (Chuẩn kỹ thuật) |
| **BATCH-07** | `"IT004" "phụ thuộc hàm" OR "dạng chuẩn" "đề thi" OR "đáp án"` | `uit.edu.vn`, `studocu.com` | Chuyên đề PTH & Chuẩn hóa: bao đóng, thuật toán tìm khóa | `EXAM-2020-2021-HK1-FINAL-01` | 2019–2024 | Bài toán thành viên, Phủ tối thiểu $F_c$ | Có chứng cứ mới (Hiện vật đề thi) |
| **BATCH-08** | `"IT004" ("2017-2018" OR "2018-2019" OR "2019-2020") "giữa kỳ"` | `studocu.com`, `scribd.com` | Đề thi giữa kỳ lịch sử 2017–2020 trên Studocu | `EXAM-2019-2020-HK1-MID-D1/D2`, `EXAM-2018-2019-HK1-MID-D1/D2`, `EXAM-2017-2018-HK1-MID-D1/D2` | 2017–2020 | ERD Vé xe, Ngân hàng, Nhà cung cấp | Có chứng cứ mới (Hiện vật đề thi) |
| **BATCH-09** | `"IT004" "Đề thi cuối kỳ" "2024-2025" site:uit.edu.vn` | `uit.edu.vn`, `httt.uit.edu.vn` | Cổng thông tin không công khai toàn văn | - | - | Thông báo lịch thi | Không phát sinh hiện vật mới |
| **BATCH-10** | `site:github.com "IT004" "Transact-SQL" "trigger" OR "procedure"` | `github.com` | Rà soát các repo sinh viên (`KevMi-UIT`, `HiImKing1509`) | - | - | Tái xác nhận lab chuẩn | Không phát sinh hiện vật mới |
| **BATCH-11** | `site:studocu.vn "IT004" "Đề thi giữa kỳ" "Khoa Hệ thống Thông tin"` | `studocu.vn` | Đối chiếu URL trực tiếp Midterm 2022–2023 | `EXAM-2022-2023-HK1-MID-D2` | 2022–2023 | Mua xe trả góp | Phát sinh URL trực tiếp |
| **BATCH-12** | `site:thuvien.uit.edu.vn "Cơ sở dữ liệu" "Đồng Thị Bích Thủy"` | `thuvien.uit.edu.vn` | Thư mục giáo trình chuẩn | - | - | Giáo trình chuẩn | Không phát sinh hiện vật mới |
| **BATCH-13** | **Kiểm toán & Tiếp nhận Trực tiếp Các Liên Kết Đề Thi Của Mentor & Leads** | `studocu.vn`, `studocu.com` | **Tiếp nhận 10 hiện vật đề thi chuẩn hóa có URL tài liệu trực tiếp**: Cuối kỳ 2018–2019, Cuối kỳ 2019–2020, Cuối kỳ 2022–2023, Giữa kỳ 2024–2025, Cuối kỳ 2024–2025, Thực hành 2013, Cuối kỳ 2021–2022, Thực hành 2020–2021, Thực hành 2022–2023, Thực hành 2023–2024 Đề 04 | `EXAM-2018-2019-HK1-FINAL-01`<br>`EXAM-2019-2020-HK1-FINAL-01`<br>`EXAM-2022-2023-HK1-FINAL-01`<br>`EXAM-2024-2025-HK1-MID-01`<br>`EXAM-2024-2025-HK1-FINAL-01`<br>`EXAM-2021-2022-HK1-FINAL-01`<br>`PRAC-2013-2014-HK1-E181`<br>`PRAC-2020-2021-HK1-M18`<br>`PRAC-2022-2023-HK1-D04`<br>`PRAC-2023-2024-HK1-D04` | 2013–2014, 2018–2019, 2019–2020, 2020–2021, 2021–2022, 2022–2023, 2023–2024, 2024–2025 | Quyên góp bão lũ, Tiêm chủng vắc-xin, Rạp chiếu phim, Dự án xây dựng, Tác giả/NXB, Khách sạn, HTX chăn nuôi, Cây cảnh, Guitar | **CÓ CHỨNG CỨ MỚI (Tiếp nhận toàn diện)** |
| **BATCH-14** | `site:scribd.com "IT004" "Cơ sở dữ liệu" "Đề thi" "UIT"` | `scribd.com` | Rà soát các bản lưu trữ trên Scribd: xác nhận các bản sao trùng lặp của các đề thi đã lập chỉ mục | - | Không phát sinh năm mới | Không phát sinh chủ đề mới ngoài phạm vi | **KHÔNG PHÁT SINH TRONG BATCH** |
| **BATCH-15** | `site:github.com "IT004" "Đề thi" "2014" OR "2015" OR "2016"` | `github.com` | Rà soát các repo sinh viên giai đoạn 2014–2016: chỉ có đề cương lý thuyết và bài tập thực hành mẫu | - | Không phát sinh năm mới | Không phát sinh chủ đề mới | **KHÔNG PHÁT SINH TRONG BATCH** |
| **BATCH-16** | `site:httt.uit.edu.vn "Cơ sở dữ liệu" "đề thi" OR "thực hành" OR "lịch thi"` | `httt.uit.edu.vn` | Rà soát cổng khoa HTTT: các thông báo học vụ định kỳ, quy chế phòng thi | - | Không phát sinh năm mới | Không phát sinh chủ đề mới | **KHÔNG PHÁT SINH TRONG BATCH** |
| **BATCH-17** | **Cross-check 9 direct leads do mentor cung cấp + sửa URL Midterm 2023–2024** | `studocu.vn` | 4 trang có header/nội dung hiển thị đủ để promote (`PRAC-2024-2025-HK1-01`, `PRAC-2024-2025-HK1-02`, `PRAC-2023-2024-HK1-FINAL-01`, `PRAC-2022-2023-HK1-D03`); 4 lead còn lại bị human-verification/403 nên giữ ở trạng thái unpromoted | 4 canonical mới | 2022–2025; 4 lead chưa xác nhận năm | Practical variants, midterm/final leads | **Đã ingest có điều kiện; không tuyên bố exhaustive** |

---

## 2. Research snapshot status

**RESEARCH SNAPSHOT STATUS:**
**FROZEN FOR IMPLEMENTATION**

**SNAPSHOT DATE:**
**2026-08-31**

Snapshot này xác nhận:

- official UIT sources đã được reviewed;
- local corpus đã được fully ingested;
- Microsoft technical references đã được validated;
- multiple GitHub/community repositories đã được reviewed;
- multi-year direct exam/practical artifacts đã được indexed;
- source provenance và copyright boundaries đã được established;
- evidence base đủ để guide v1.1 implementation;
- `artifact_registry.md` vẫn extensible khi có evidence mới.

> “The registry is a high-coverage research snapshot, not a claim of exhaustive coverage of all materials on the Internet.”

BATCH-17 là bước cross-check cuối của snapshot này, không phải tuyên bố search saturation. Các lead bị chặn quyền đọc vẫn được ghi rõ và không làm tăng canonical counts.
