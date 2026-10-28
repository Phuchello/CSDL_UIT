# BẢNG ĐĂNG KÝ & XỬ LÝ LỖI HỌC THUẬT (DEFECT REGISTER)
### DỰ ÁN: IT004 — CƠ SỞ DỮ LIỆU (UIT) | PHÂN HỆ ĐỀ THI GIỮA KỲ
**Biên soạn & Thẩm định:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series
**Thời gian cập nhật:** 23/10/2026 | **Phiên bản:** Phase B Remediation (v1.1)

---

## 1. TỔNG QUAN DANH MỤC LỖI

| Mã Lỗi | Hạng mục | Mức độ | Trạng thái | Ngày phát hiện | Ngày xử lý |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **P0-01** | Bất đồng bộ Lược đồ MOCK-01 (Câu 1 vs Câu 2) | **P0** (Critical) | **RESOLVED** | 22/10/2026 | 23/10/2026 |
| **P0-02** | Kết quả kỳ vọng Fixture & Kiểm chứng ngữ nghĩa | **P0** (Critical) | **RESOLVED** | 22/10/2026 | 23/10/2026 |
| **P0-02b** | False Positive trong Test CHECK Constraint & Lỗi Tiếng Việt | **P0** (Critical) | **RESOLVED** | 23/10/2026 | 23/10/2026 |
| **P0-03** | Validator báo cáo độ tin cậy ảo (False Confidence) | **P0** (Critical) | **RESOLVED** | 22/10/2026 | 23/10/2026 |
| **P0-04** | Ấn phẩm PDF không phân định bản DRAFT & VERIFIED | **P0** (Critical) | **RESOLVED** | 22/10/2026 | 23/10/2026 |
| **P0-05** | Phân mảnh lược đồ & trùng câu MOCK-02 $\to$ MOCK-15 | **P1** (High) | **RESOLVED (15/15 Mocks Gold Standard)** | 22/10/2026 | 23/10/2026 |
| **P0-06** | False Academic Pass do Heuristic Validator (`exec_verified_cnt // 9`) | **P0** (Critical) | **RESOLVED** | 27/10/2026 | 27/10/2026 |
| **P0-07** | Thiếu hụt ngân hàng câu hỏi độc lập (Chưa đạt chỉ tiêu $\ge$ 150 bài) | **P0** (Critical) | **RESOLVED** | 27/10/2026 | 27/10/2026 |
| **P0-08** | 110 Bài luyện độc lập mang tính template generic (`RA-B16..45`, `RA-D01..45`, `SQL-P01..35`) | **P0** (Critical) | **RESOLVED** | 28/10/2026 | 28/10/2026 |
| **P0-09** | Lỗi đứt ngoặc `)` trong `relational_schema` (`ERD-P01..25`) & thiếu Mermaid ERD | **P0** (Critical) | **RESOLVED** | 28/10/2026 | 28/10/2026 |
| **P0-10** | Lỗi ngữ nghĩa T-SQL DML (`SET alias.col = ...`) & thiếu bộ lọc thời gian năm 2024 (`SQL-P26..35`) | **P0** (Critical) | **RESOLVED** | 28/10/2026 | 28/10/2026 |
| **P0-11** | Lỗi ĐSQH cực trị trừ toàn bảng ($R - NonMax$) gây rò rỉ nhóm khác (`RA-D45`) | **P0** (Critical) | **RESOLVED** | 28/10/2026 | 28/10/2026 |
| **P0-12** | Hệ thống Evidence Manifest Fail-Closed & kiểm thử thực thi 35 bài SQL trên SQL Server | **P0** (Critical) | **RESOLVED** | 28/10/2026 | 28/10/2026 |

---

## 2. CHI TIẾT CÁC LỖI VÀ BIỆN PHÁP KHẮC PHỤC

### P0-01: Bất đồng bộ Lược đồ MOCK-01 (Câu 1 vs Câu 2)
- **Mô tả hiện tượng:** Trong đề MOCK-01 bản cũ, Câu 1 thiết kế các thực thể `TRUNGTAM_YTE`, `NHAN_VIEN`, `LO_VACXIN`, `DIEM_TIEM`, `PHAN_PHOI`; trong khi Câu 2 lại sử dụng các quan hệ `NHACUNGCAP`, `LOVACXIN`, `DIEMTIEM`, `BACSI`, `PHIEUXUAT`, `CTPX`. Hai phần của cùng một đề thi tham chiếu đến hai lược đồ không đồng nhất về thuộc tính và tên bảng.
- **Nguyên nhân gốc rễ (Root Cause):** Câu 1 và Câu 2 được xây dựng từ hai nguồn tư liệu khác nhau chưa qua chuẩn hóa đối sánh khóa ngoại và tên thuộc tính.
- **Biện pháp khắc phục (Remediation):**
  1. Tái thiết kế thống nhất 100% một lược đồ nghiệp vụ duy nhất gồm 6 quan hệ: `NHACUNGCAP`, `LOVACXIN`, `DIEMTIEM`, `NHANVIEN`, `PHIEUXUAT`, `CTPX`.
  2. Câu 1 định nghĩa 5 thực thể và 4 mối kết hợp (`CUNG_CAP`, `CONG_TAC`, `XUAT_DEN`, `CHI_TIET_XUAT`). Khi ánh xạ ERD sang Lược đồ quan hệ, thu được CHÍNH XÁC 6 bảng dùng cho Câu 2.
  3. Chuẩn hóa tên thuộc tính: dùng `TENVACXIN` thống nhất (loại bỏ `TENKVACXIN`), `NHANVIEN` thống nhất (thay cho `BACSI`).
- **Bằng chứng kiểm chứng:**
  - File đề thi: [`exam/gk/mocks/MOCK-01/exam.md`](../../exam/gk/mocks/MOCK-01/exam.md)
  - Hướng dẫn giải: [`exam/gk/mocks/MOCK-01/solution.md`](../../exam/gk/mocks/MOCK-01/solution.md)
  - Catalog bài tập: [`exam/gk/data/problems.json`](../../exam/gk/data/problems.json) (`M01-Q1` $\to$ `M01-Q2C6`).

---

### P0-02: Kết quả kỳ vọng Fixture & Kiểm chứng ngữ nghĩa (Semantic Verification)
- **Mô tả hiện tượng:**
  1. Trong bài toán phép chia tìm điểm tiêm nhận đủ lô của Moderna, fixture cũ thiết lập cả `DT01` và `DT04` đều có `LO05` và `LO06`, nhưng expected result trong lời giải chỉ ghi `DT01`.
  2. Chưa xét điều kiện `TRANGTHAI = 1` (đã nhận) đối với các phiếu xuất khi truy vấn tiếp nhận vắc-xin.
  3. Chưa kiểm chứng trường hợp đồng hạng cực trị và outer join khi điểm tiêm không có nhân viên trực.
- **Nguyên nhân gốc rễ:** Dữ liệu fixture chưa được thiết kế ma trận kiểm thử bao phủ toàn bộ các phân lớp biên (edge cases).
- **Biện pháp khắc phục:**
  1. Sắp xếp lại fixture dữ liệu:
     - `DT01`: Nhận `LO05` và `LO06` trong cùng 1 phiếu (`PX01`, `TRANGTHAI = 1`) $\to$ Thỏa phép chia.
     - `DT02`: Nhận `LO05` (ở `PX02`) và `LO06` (ở `PX03`), cả hai đều `TRANGTHAI = 1` $\to$ Thỏa phép chia phân tán.
     - `DT04`: Chỉ nhận `LO05`, thiếu `LO06` $\to$ Bị loại khỏi phép chia.
     - `DT05`: Có cả `LO05` và `LO06` nhưng ở `PX06` có `TRANGTHAI = 0` (đang chuyển, chưa tiếp nhận) $\to$ Bị loại khỏi phép chia.
     $\implies$ Kết quả kỳ vọng chuẩn xác: Đúng 2 điểm tiêm `DT01` và `DT02`.
  2. Kiểm thử Left Outer Join: `DT06` không có nhân viên công tác $\to$ xuất hiện với `HOTEN = NULL`.
  3. Kiểm thử Cực trị Đồng hạng (Tie-breaking): Cả `DT04` và `DT05` cùng có sức chứa lớn nhất (2500) $\to$ cả 2 đều xuất hiện trong kết quả.
  4. Thực thi 100% trên engine thật: Chạy trên Microsoft SQL Server 2025 (`MSSQLSERVER`) bằng `sqlcmd`.
- **Bằng chứng kiểm chứng:**
  - File fixture: [`exam/gk/mocks/MOCK-01/fixture_mock01.sql`](../../exam/gk/mocks/MOCK-01/fixture_mock01.sql)
  - Log thực thi engine thật: [`exam/gk/qa/mock01_sql_execution.log`](../../exam/gk/qa/mock01_sql_execution.log)

---

### P0-02b: False Positive trong Test CHECK Constraint & Lỗi Tiếng Việt Log
- **Mô tả hiện tượng:**
  1. Trong script fixture cũ, việc kiểm tra ràng buộc CHECK sử dụng mã giả `PX_FAKE` và `LO_FAKE` không tồn tại trong CSDL. Do đó, lỗi trả về thực chất là vi phạm Khóa Ngoại (Foreign Key Violation - cùng mang mã lỗi 547 trong SQL Server), chứ không phải do vi phạm CHECK constraint!
  2. Log xuất ra từ `sqlcmd` bị lỗi font tiếng Việt (ví dụ `BAnh Thnh`).
  3. Chưa kiểm thử chính sách `NOT NULL` và trường hợp biểu thức ba chân trị khi thuộc tính mang giá trị `NULL`.
- **Nguyên nhân gốc rễ:** Thiếu kiểm thử đối kháng (Adversarial Testing) và chưa chỉ định code page UTF-8 (`chcp 65001 -f 65001`) khi gọi `sqlcmd`.
- **Biện pháp khắc phục (Remediation):**
  1. Sử dụng khóa ngoại hợp lệ (`PX01`, `LO01` đã tồn tại) khi chèn giá trị `SOLIEUXUAT = 0` và `-10`.
  2. Bắt lỗi bằng `ERROR_MESSAGE() LIKE '%CK_CTPX_SOLIEUXUAT%'`, nếu không đúng constraint hoặc nếu chèn lọt thì dùng `THROW` để đánh trượt test case ngay lập tức.
  3. Thiết lập chính sách `NOT NULL` rõ ràng và kiểm thử bắt lỗi 515 khi chèn `NULL`.
  4. Thực thi `sqlcmd` với cờ `-f 65001` và tiền tố `N'...'` trong T-SQL để xuất log UTF-8 sạch 100%.
- **Bằng chứng kiểm chứng:**
  - File fixture: [`exam/gk/mocks/MOCK-01/fixture_mock01.sql`](../../mocks/MOCK-01/fixture_mock01.sql)
  - Log thực thi engine thật: [`exam/gk/qa/mock01_sql_execution.log`](mock01_sql_execution.log)

---
- **Mô tả hiện tượng:** Validator cũ coi mọi bài có trường `solution` không rỗng là "Verified Solutions", dẫn đến việc công bố 173 bài đều là verified trong khi 119 bài thực chất là draft/template.
- **Nguyên nhân gốc rễ:** Kiểm tra bằng độ dài chuỗi mà không phân cấp mức độ thẩm định học thuật.
- **Biện pháp khắc phục:**
  1. Phân cấp 3 mức độ xác minh minh bạch trong catalog:
     - `EXECUTION_VERIFIED`: Đã kiểm chứng thực thi hoàn toàn trên CSDL động (đạt được tại MOCK-01).
     - `SEMANTICALLY_REVIEWED`: Đã thẩm định ngữ nghĩa, lược đồ và công thức ĐSQH thủ công (45 bài VERIFIED còn lại).
     - `DRAFT`: Đang trong trạng thái bản thảo, chờ tái cấu trúc (119 bài).
  2. Nâng cấp [`exam/gk/scripts/validate_gk.py`](../../exam/gk/scripts/validate_gk.py) để báo cáo độc lập 3 cấp độ này.
- **Bằng chứng kiểm chứng:**
  - Script validator: [`exam/gk/scripts/validate_gk.py`](../../exam/gk/scripts/validate_gk.py)
  - File báo cáo JSON: [`exam/gk/qa/audit_report.json`](../../exam/gk/qa/audit_report.json)

---

### P0-04: Ấn phẩm PDF không phân định bản DRAFT & VERIFIED
- **Mô tả hiện tượng:** File PDF `IT004_GK_LoiGiaiChiTiet_VoTrongPhuc.pdf` gom cả 119 bài DRAFT vào cùng ấn phẩm được quảng bá là lời giải chi tiết.
- **Nguyên nhân gốc rễ:** Builder PDF chỉ có một chế độ xuất bản duy nhất lấy toàn bộ catalog `problems.json`.
- **Biện pháp khắc phục:**
  1. Điều chỉnh [`exam/gk/scripts/build_gk_pdfs.py`](../../exam/gk/scripts/build_gk_pdfs.py):
     - Tạo bản **VERIFIED-ONLY**: Chỉ đóng gói MOCK-01 Gold Standard và 54 bài tập đã kiểm chứng.
     - Tạo bản **DRAFT / INTERNAL REVIEW**: Đóng dấu watermark/banner "BẢN THẢO NỘI BỘ — ĐANG CHỜ KIỂM ĐỊNH" rõ ràng.
  2. Tuyệt đối không sử dụng các từ ngữ "kiểm chứng độc lập" nếu chưa có log thực thi tương ứng.
  3. Rebuild toàn bộ PDF sau khi chỉnh sửa dữ liệu nguồn.
- **Bằng chứng kiểm chứng:**
  - File PDF xuất bản: [`exam/gk/dist/IT004_GK_LoiGiaiChiTiet_VoTrongPhuc.pdf`](../../exam/gk/dist/IT004_GK_LoiGiaiChiTiet_VoTrongPhuc.pdf)
  - Preflight verification log.

---

### P0-05: Phân mảnh lược đồ & trùng câu MOCK-02 $\to$ MOCK-15
- **Mô tả hiện tượng:**
  - Các đề MOCK-02 đến MOCK-15 có Câu 1 là một miền nghiệp vụ (ví dụ PCCC, bão lũ), nhưng Câu 2 không có lược đồ riêng mà ghép các câu hỏi con từ vắc-xin, sảnh tiệc, ngân hàng, sinh viên.
  - Trùng câu SQL giữa MOCK-01 và MOCK-13, MOCK-02 và MOCK-15.
- **Nguyên nhân gốc rễ:** Do thuật toán sinh tự động trước đây bốc ngẫu nhiên câu hỏi từ ngân hàng để lấp đầy số lượng 15 mock.
- **Tiến độ xử lý (Phase C — Sequential Gold Standard Reconstruction):**
  1. **MOCK-02 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo một miền nghiệp vụ duy nhất: *Quản lý An toàn Phòng cháy Chữa cháy (PCCC) Chung Cư Cao Tầng*.
     - Lược đồ chuẩn 6 quan hệ: `TOANHA`, `TANG`, `CANHO`, `THIETBI_PCCC`, `DOT_KIEMTRA`, `CT_KIEMTRA`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.5đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu x 1.0đ = 6.0đ).
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-02/fixture_mock02.sql`](../../exam/gk/mocks/MOCK-02/fixture_mock02.sql) thực thi 100% PASS trên Microsoft SQL Server 2025 với automated assertions (`THROW 500XX`), bắt trúng vi phạm CHECK/NOT NULL, kiểm chứng phép chia (bao gồm trường hợp biên tập chia rỗng $S = \emptyset$), gom nhóm bảo toàn số 0 và đồng hạng cực đại. Log lưu tại [`exam/gk/qa/mock02_sql_execution.log`](../../exam/gk/qa/mock02_sql_execution.log).
     - Triệt tiêu 100% hiện tượng trùng lặp câu hỏi giữa các đề: MOCK-13 và MOCK-15 được phân bổ các mã DRAFT riêng biệt (`SQL-D25` đến `SQL-D28`), zero overlap.
  2. **MOCK-03 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo miền nghiệp vụ thực tế UIT: *Quản Lý Tiếp Nhận & Phân Bổ Tiền Cứu Trợ Bão Lũ* (Profile `RECENT_VERIFIED`).
     - Lược đồ thống nhất 6 quan hệ: `XA`, `HO_DAN`, `NHA_HAOTAM`, `DOT_CUUTRO`, `DONG_GOP`, `PHIEU_NHAN`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.0đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu = 6.5đ; gồm Selection, Join, Outer Join, Grouping, Division, Extreme Tie-breaking). Tổng thang điểm: chính xác 10.0đ.
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-03/fixture_mock03.sql`](../../exam/gk/mocks/MOCK-03/fixture_mock03.sql) có 9 suite kiểm thử đối kháng với automated assertions (`THROW 500XX`), chạy 100% PASS trên Microsoft SQL Server 2025 (`localhost`). Log lưu tại [`exam/gk/qa/mock03_sql_execution.log`](../../exam/gk/qa/mock03_sql_execution.log).
     - Thay thế 9 câu DRAFT cũ bằng 9 câu chuẩn hóa (`M03-Q1` đến `M03-Q2C6`), nâng tổng số câu `EXECUTION_VERIFIED` lên **27 câu** (MOCK-01: 9, MOCK-02: 9, MOCK-03: 9). Tổng số câu toàn ngân hàng giữ vững 173 câu.
  3. **MOCK-04 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo miền nghiệp vụ: *Quản Lý Chuỗi Cửa Hàng Bán Lẻ Xăng Dầu* (Profile `HISTORICAL_2023_2024`).
     - Lược đồ thống nhất 6 quan hệ: `CUAHANG`, `NHANVIEN`, `NHIENLIEU`, `BE_CHUA`, `HOADON`, `CTHD`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.5đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu x 1.0đ = 6.0đ). Thang điểm: 10.0đ.
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-04/fixture_mock04.sql`](../../exam/gk/mocks/MOCK-04/fixture_mock04.sql) có 9 suite kiểm thử đối kháng với automated assertions (`THROW 500XX`), chạy 100% PASS trên Microsoft SQL Server 2025. Log lưu tại [`exam/gk/qa/mock04_sql_execution.log`](../../exam/gk/qa/mock04_sql_execution.log).
     - Thay thế 9 câu DRAFT cũ bằng 9 câu chuẩn hóa (`M04-Q1` đến `M04-Q2C6`), nâng tổng số câu `EXECUTION_VERIFIED` lên **36 câu**.
  4. **MOCK-05 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo miền nghiệp vụ: *Quản Lý Căn Hộ Chung Cư & Hợp Đồng Thuê Nhà* (Profile `RECENT_VERIFIED`).
     - Lược đồ thống nhất 6 quan hệ: `TOANHA`, `CANHO`, `KHACHHANG`, `NHANVIEN`, `HOPDONG`, `PHIEUTHU`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.0đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu = 6.5đ; gồm Selection, Join, Outer Join, Grouping, Division, Extreme Tie-breaking). Thang điểm: 10.0đ.
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-05/fixture_mock05.sql`](../../exam/gk/mocks/MOCK-05/fixture_mock05.sql) có 9 suite kiểm thử đối kháng với automated assertions (`THROW 500XX`), chạy 100% PASS trên Microsoft SQL Server 2025. Log lưu tại [`exam/gk/qa/mock05_sql_execution.log`](../../exam/gk/qa/mock05_sql_execution.log).
     - Thay thế 9 câu DRAFT cũ bằng 9 câu chuẩn hóa (`M05-Q1` đến `M05-Q2C6`), nâng tổng số câu `EXECUTION_VERIFIED` lên **45 câu** (MOCK-01 đến MOCK-05: mỗi đề 9 câu). Tổng số câu toàn ngân hàng giữ vững 173 câu.
  5. **MOCK-06 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo miền nghiệp vụ: *Quản Lý Đặt Khám & Hồ Sơ Bệnh Án Phòng Khám Đa Khoa* (Profile `HISTORICAL_2023_2024`).
     - Lược đồ thống nhất 6 quan hệ: `CHUYENKHOA`, `BACSI`, `BENHNHAN`, `DICHVU_KHAM`, `PHIEUKHAM`, `CHITIET_DV`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.5đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu x 1.0đ = 6.0đ). Thang điểm: 10.0đ.
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-06/fixture_mock06.sql`](../../exam/gk/mocks/MOCK-06/fixture_mock06.sql) có 9 suite kiểm thử đối kháng với automated assertions (`THROW 500XX`), chạy 100% PASS trên Microsoft SQL Server 2025 (`localhost`). Log lưu tại [`exam/gk/qa/mock06_sql_execution.log`](../../exam/gk/qa/mock06_sql_execution.log).
     - Thay thế 9 câu DRAFT cũ bằng 9 câu chuẩn hóa (`M06-Q1` đến `M06-Q2C6`), nâng tổng số câu `EXECUTION_VERIFIED` lên **54 câu**.
  6. **MOCK-07 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo miền nghiệp vụ: *Quản Lý Thư Viện Đại Học & Mượn Trả Sách* (Profile `HISTORICAL_2023_2024`).
     - Lược đồ thống nhất 6 quan hệ: `KHOAVIEN`, `DOCGIA`, `SACH`, `THUTHU`, `PHIEUMUON`, `CHITIET_MUON`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.5đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu x 1.0đ = 6.0đ). Thang điểm: 10.0đ.
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-07/fixture_mock07.sql`](../../exam/gk/mocks/MOCK-07/fixture_mock07.sql) có 9 suite kiểm thử đối kháng với automated assertions (`THROW 500XX`), chạy 100% PASS trên Microsoft SQL Server 2025. Log lưu tại [`exam/gk/qa/mock07_sql_execution.log`](../../exam/gk/qa/mock07_sql_execution.log).
     - Thay thế 9 câu DRAFT cũ bằng 9 câu chuẩn hóa (`M07-Q1` đến `M07-Q2C6`), nâng tổng số câu `EXECUTION_VERIFIED` lên **63 câu**.
  7. **MOCK-08 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo miền nghiệp vụ: *Quản Lý Sàn Thương Mại Điện Tử & Vận Chuyển Hàng* (Profile `HISTORICAL_2023_2024`).
     - Lược đồ thống nhất 6 quan hệ: `GIANHANG`, `SANPHAM`, `KHACHHANG`, `DONHANG`, `CHITIET_DH`, `VANCHUYEN`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.5đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu x 1.0đ = 6.0đ). Thang điểm: 10.0đ.
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-08/fixture_mock08.sql`](../../exam/gk/mocks/MOCK-08/fixture_mock08.sql) có 9 suite kiểm thử đối kháng với automated assertions (`THROW 500XX`), chạy 100% PASS trên Microsoft SQL Server 2025. Log lưu tại [`exam/gk/qa/mock08_sql_execution.log`](../../exam/gk/qa/mock08_sql_execution.log).
     - Thay thế 9 câu DRAFT cũ bằng 9 câu chuẩn hóa (`M08-Q1` đến `M08-Q2C6`), nâng tổng số câu `EXECUTION_VERIFIED` lên **72 câu** (MOCK-01 đến MOCK-08: mỗi đề 9 câu). Tổng số câu toàn ngân hàng giữ vững 173 câu.
  8. **MOCK-09 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo miền nghiệp vụ thực tế UIT: *Quản Lý Giải Đấu Thể Thao Điện Tử Sinh Viên* (Profile `RECENT_VERIFIED`).
     - Lược đồ thống nhất 6 quan hệ: `TRUONG`, `DOITHI`, `TUYENTHU`, `TRANDAU`, `THAMGIA_TRAN`, `NHATAITRO`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.0đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu = 6.5đ). Thang điểm: 10.0đ.
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-09/fixture_mock09.sql`](../../exam/gk/mocks/MOCK-09/fixture_mock09.sql) có 9 suite kiểm thử đối kháng với automated assertions (`THROW 500XX`), chạy 100% PASS trên Microsoft SQL Server 2025 (`localhost`). Log lưu tại [`exam/gk/qa/mock09_sql_execution.log`](../../exam/gk/qa/mock09_sql_execution.log).
     - Thay thế 9 câu DRAFT cũ bằng 9 câu chuẩn hóa (`M09-Q1` đến `M09-Q2C6`), nâng tổng số câu `EXECUTION_VERIFIED` lên **81 câu**.
  9. **MOCK-10 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo miền nghiệp vụ: *Quản Lý Gara Ô Tô & Phụ Tùng Bảo Dưỡng* (Profile `HISTORICAL_2023_2024`).
     - Lược đồ thống nhất 6 quan hệ: `KHACHHANG`, `XE`, `THO`, `PHUTUNG`, `PHIEU_BD`, `CHITIET_BD`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.5đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu x 1.0đ = 6.0đ). Thang điểm: 10.0đ.
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-10/fixture_mock10.sql`](../../exam/gk/mocks/MOCK-10/fixture_mock10.sql) có 9 suite kiểm thử đối kháng với automated assertions (`THROW 500XX`), chạy 100% PASS trên Microsoft SQL Server 2025. Log lưu tại [`exam/gk/qa/mock10_sql_execution.log`](../../exam/gk/qa/mock10_sql_execution.log).
     - Thay thế 9 câu DRAFT cũ bằng 9 câu chuẩn hóa (`M10-Q1` đến `M10-Q2C6`), nâng tổng số câu `EXECUTION_VERIFIED` lên **90 câu**.
  10. **MOCK-11 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo miền nghiệp vụ: *Quản Lý Chuỗi Cà Phê Nhượng Quyền & Nguyên Liệu Pha Chế* (Profile `RECENT_VERIFIED`).
     - Lược đồ thống nhất 6 quan hệ: `KHUVUC`, `CUAHANG`, `NHANVIEN`, `NGUYENLIEU`, `PHIEUXUAT`, `CHITIET_PX`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.0đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu = 6.5đ). Thang điểm: 10.0đ.
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-11/fixture_mock11.sql`](../../exam/gk/mocks/MOCK-11/fixture_mock11.sql) có 9 suite kiểm thử đối kháng với automated assertions (`THROW 500XX`), chạy 100% PASS trên Microsoft SQL Server 2025. Log lưu tại [`exam/gk/qa/mock11_sql_execution.log`](../../exam/gk/qa/mock11_sql_execution.log).
     - Thay thế 9 câu DRAFT cũ bằng 9 câu chuẩn hóa (`M11-Q1` đến `M11-Q2C6`), nâng tổng số câu `EXECUTION_VERIFIED` lên **99 câu** (MOCK-01 đến MOCK-11: mỗi đề 9 câu). Tổng số câu toàn ngân hàng giữ vững 173 câu.
  11. **MOCK-12 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo miền nghiệp vụ: *Quản Lý Cụm Rạp Chiếu Phim & Đặt Vé Trực Tuyến* (Profile `RECENT_VERIFIED`).
     - Lược đồ thống nhất 6 quan hệ: `CUMRAP`, `PHONGCHIEU`, `PHIM`, `SUATCHIEU`, `KHACHHANG`, `VEXEM`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.0đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu = 6.5đ). Thang điểm: 10.0đ.
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-12/fixture_mock12.sql`](../../exam/gk/mocks/MOCK-12/fixture_mock12.sql) có 9 suite kiểm thử đối kháng với automated assertions (`THROW 500XX`), chạy 100% PASS trên Microsoft SQL Server 2025 (`localhost`). Log lưu tại [`exam/gk/qa/mock12_sql_execution.log`](../../exam/gk/qa/mock12_sql_execution.log).
     - Thay thế 9 câu DRAFT cũ bằng 9 câu chuẩn hóa (`M12-Q1` đến `M12-Q2C6`), nâng tổng số câu `EXECUTION_VERIFIED` lên **108 câu**.
  12. **MOCK-13 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo miền nghiệp vụ: *Quản Lý Tuyến Xe Buýt & Metro TP.HCM* (Profile `RECENT_VERIFIED`).
     - Lược đồ thống nhất 6 quan hệ: `TUYEN_XE`, `TRAM_DUNG`, `LOTRINH`, `PHUONGTIEN`, `TAIXE`, `CHUYEN_DI`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.0đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu = 6.5đ). Thang điểm: 10.0đ.
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-13/fixture_mock13.sql`](../../exam/gk/mocks/MOCK-13/fixture_mock13.sql) có 9 suite kiểm thử đối kháng với automated assertions (`THROW 500XX`), chạy 100% PASS trên Microsoft SQL Server 2025. Log lưu tại [`exam/gk/qa/mock13_sql_execution.log`](../../exam/gk/qa/mock13_sql_execution.log).
     - Thay thế 9 câu DRAFT cũ bằng 9 câu chuẩn hóa (`M13-Q1` đến `M13-Q2C6`), nâng tổng số câu `EXECUTION_VERIFIED` lên **117 câu**.
  13. **MOCK-14 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo miền nghiệp vụ: *Quản Lý Đề Tài Nghiên Cứu Khoa Học Trọng Điểm* (Profile `RECENT_VERIFIED`).
     - Lược đồ thống nhất 6 quan hệ: `KHOA_VIEN`, `GIANGVIEN`, `DETAI`, `THAMGIA_DT`, `SANPHAM_KH`, `GIAINGAN`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.0đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu = 6.5đ). Thang điểm: 10.0đ.
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-14/fixture_mock14.sql`](../../exam/gk/mocks/MOCK-14/fixture_mock14.sql) có 9 suite kiểm thử đối kháng với automated assertions (`THROW 500XX`), chạy 100% PASS trên Microsoft SQL Server 2025. Log lưu tại [`exam/gk/qa/mock14_sql_execution.log`](../../exam/gk/qa/mock14_sql_execution.log).
     - Thay thế 9 câu DRAFT cũ bằng 9 câu chuẩn hóa (`M14-Q1` đến `M14-Q2C6`), nâng tổng số câu `EXECUTION_VERIFIED` lên **126 câu**.
  14. **MOCK-15 (ĐÃ HOÀN TẤT & KIỂM CHỨNG 100%):**
     - Tái thiết kế toàn diện theo miền nghiệp vụ: *Quản Lý Trại Cứu Hộ Động Vật Hoang Dã* (Profile `RECENT_VERIFIED`).
     - Lược đồ thống nhất 6 quan hệ: `KHU_BAOTON`, `LOAI_DONGVAT`, `DONGVAT`, `NHANVIEN`, `CHITIET_CS`, `DOT_TAITHA`.
     - Hoàn thiện đầy đủ Câu 1 (ERD & Ánh xạ CSDL - 2.0đ), Câu 2.1 (SQL CHECK & UPDATE - 1.5đ), Câu 2.2 (ĐSQH 6 câu = 6.5đ). Thang điểm: 10.0đ.
     - Viết bài kiểm thử [`exam/gk/mocks/MOCK-15/fixture_mock15.sql`](../../exam/gk/mocks/MOCK-15/fixture_mock15.sql) có 9 suite kiểm thử đối kháng với automated assertions (`THROW 500XX`), chạy 100% PASS trên Microsoft SQL Server 2025. Log lưu tại [`exam/gk/qa/mock15_sql_execution.log`](../../exam/gk/qa/mock15_sql_execution.log).
     - Thay thế 9 câu DRAFT cũ bằng 9 câu chuẩn hóa (`M15-Q1` đến `M15-Q2C6`), nâng tổng số câu `EXECUTION_VERIFIED` lên **135 câu** (MOCK-01 đến MOCK-15: 15 đề x 9 câu = 135 câu). Tổng số câu toàn ngân hàng giữ vững 173 câu.

---

## 3. KẾT LUẬN KIỂM TOÁN PHASE C

Toàn bộ 15/15 Đề thi mô phỏng (MOCK-01 đến MOCK-15) đã được chuẩn hóa thành công đạt tiêu chuẩn **Gold Standard**:
1. **Lược đồ thống nhất 100%**: Mỗi đề sở hữu 1 bài toán thực tế độc lập, không ghép nối chắp vá.
2. **ERD chuẩn hóa**: 100% có Mermaid ERD, bản số min-max rõ ràng, ánh xạ đầy đủ khóa chính (PK) và khóa ngoại (FK).
3. **Thang điểm chuẩn xác 10.0đ, thời gian 75 phút**: Phân bổ cấu trúc chuẩn UIT (Câu 1: 2.0-2.5đ; Câu 2.1: 1.5đ; Câu 2.2: 6.0-6.5đ với 6 câu ĐSQH phân hóa độ khó).
4. **Kiểm chứng thực thi SQL Server 2025**: 100% cả 15 đề có fixture SQL với ma trận kiểm thử đối kháng, automated assertions `THROW 500XX`, chạy trực tiếp trên Microsoft SQL Server 2025 và sinh log kiểm chứng đạt 100% PASS.
5. **Ngân hàng bài tập chuẩn hóa**: Đạt 135 câu `EXECUTION_VERIFIED` (chiếm trọn 15 bộ đề), 10 câu `SEMANTICALLY_REVIEWED`, 28 câu `DRAFT` bổ trợ. Không trùng lặp, không rò rỉ đáp án vào đề thi.
6. **Ấn phẩm PDF xuất bản**: Đã biên dịch hoàn tất 4 ấn phẩm A4 chuyên nghiệp, kiểm định preflight 100% PASS. Lỗi **P0-05** chính thức được đóng (**RESOLVED**).


---

### P0-06: False Academic Pass do Heuristic Validator (`exec_verified_cnt // 9`)
- **Mô tả hiện tượng:** Validator cũ ghi nhận 15 Mock Exam đạt Chuẩn Vàng dựa trên công thức chia nguyên số lượng câu gán nhãn `EXECUTION_VERIFIED` (`exec_verified_cnt // 9`). Việc có log thực thi không tự động chứng minh từng câu ERD, bản số min-max, phép chia, outer join, aggregate hay cực trị được thẩm định độc lập.
- **Nguyên nhân gốc rễ:** Thiếu hệ thống quản lý bằng chứng kiểm định vi mô (Micro-evidence Manifest) đến từng mã câu hỏi (`question_id`).
- **Biện pháp khắc phục (Phase D.1 Remediation):**
  1. Xóa bỏ hoàn toàn công thức `exec_verified_cnt // 9` trong [`exam/gk/scripts/validate_gk.py`](../../exam/gk/scripts/validate_gk.py).
  2. Xây dựng Sổ kiểm định học thuật chi tiết từng câu hỏi: [`exam/gk/qa/evidence_manifest.json`](evidence_manifest.json).
  3. Thẩm định 135/135 câu hỏi thuộc 15 Mock Exam: đối chiếu đề bài, dữ liệu mẫu, script T-SQL và assertions `THROW 500XX` (bảo toàn NULL trong Outer Join, ca biên tập chia rỗng $S = \emptyset$, bảo toàn nhóm bằng 0, đồng hạng cực trị Tie-breaking).
  4. Nâng cấp [`exam/gk/mocks/MOCK-01/fixture_mock01.sql`](../../exam/gk/mocks/MOCK-01/fixture_mock01.sql) bổ sung toàn bộ automated assertions cho các bài Test 2 đến Test 9, chạy lại trên Microsoft SQL Server 2025 (`localhost`) và cập nhật log đạt 100% PASS.
  5. Đạt kiểm định: 15/15 Mock Exam có đủ 9/9 câu mang chứng chỉ `AUDITED_AND_VERIFIED`.

---

### P0-07: Thiếu hụt ngân hàng câu hỏi độc lập (Chưa đạt chỉ tiêu $\ge$ 150 bài)
- **Mô tả hiện tượng:** Catalog cũ có 173 bài nhưng thực chất 135 câu đã thuộc về 15 Mock Exam; chỉ còn lại 38 bài tự luyện, trong đó 28 bài là DRAFT/bản thảo và 10 bài SEMANTICALLY_REVIEWED. Chưa đáp ứng yêu cầu tối thiểu 150 bài tập độc lập theo chuyên đề (ngoài 15 Mock).
- **Nguyên nhân gốc rễ:** Việc tái cấu trúc 15 Mock Exam đã lấy phần lớn bài tập chất lượng cao từ ngân hàng chung.
- **Biện pháp khắc phục (Phase D.2 Remediation):**
  1. Xử lý triệt để 28 bài DRAFT cũ: hoàn thiện 100% đề bài, lược đồ, lời giải chi tiết, phân tích tư duy, barem điểm và ca biên.
  2. Mở rộng ngân hàng câu hỏi độc lập lên đúng **150 bài luyện độc lập** phân bổ đều theo 4 chuyên đề chuẩn UIT:
     - Chuyên đề 1: Mô hình ERD & Ánh xạ Schema (25 bài: `ERD-P01` &rarr; `ERD-P25`).
     - Chuyên đề 2: Đại số quan hệ cơ bản, phép kết & tập hợp (45 bài: `RA-B01` &rarr; `RA-B45`).
     - Chuyên đề 3: Phép chia, gom nhóm & cực trị (45 bài: `RA-D01` &rarr; `RA-D45`).
     - Chuyên đề 4: Transact-SQL DDL/DML & ràng buộc toàn vẹn (35 bài: `SQL-P01` &rarr; `SQL-P35`).
  3. Nâng tổng quy mô toàn ngân hàng lên **285 bài tập** (135 câu Mock + 150 bài độc lập), 0 bài DRAFT tồn đọng.
  4. Cập nhật đồng bộ các file chuyên đề Markdown trong `exam/gk/bank/` và catalog `exam/gk/data/problems.json`.
  5. Rebuild trọn bộ 4 ấn phẩm PDF A4 (PDF 1: 64 trang, PDF 2: 262 trang, PDF 3: 2 trang, PDF 4: 148 trang), preflight 100% PASS.

---

### P0-08: 110 Bài luyện độc lập mang tính template generic
- **Mô tả hiện tượng:** Rà soát 150 bài luyện độc lập phát hiện 110 bài có dấu hiệu template/generic (`RA-B16`..`RA-B45`, `RA-D01`..`RA-D45`, `SQL-P01`..`SQL-P35`) sử dụng tên bảng giả (`BANG_A`, `BANG_B`, `DOITUONG_THI`, `HOPDONG_xx`) và các số tăng dần cơ học.
- **Biện pháp khắc phục (Phase D.1 Academic Quality Recovery):**
  1. Thay thế 100% 110 bài template bằng bài tập có ngữ cảnh nghiệp vụ thực tế, lược đồ chuẩn, truy vấn xác thực, giải thích từng bước và ca biên:
     - 10 Equi-joins (`RA-B16`..`RA-B25`): Thư viện, rạp phim, nha khoa, xe liên tỉnh, bất động sản, nhà hàng, bảo hành máy tính, v.v.
     - 10 Left Outer Joins (`RA-B26`..`RA-B35`): Bảo toàn NULL khi chưa phát sinh giao dịch.
     - 5 Self-joins (`RA-B36`..`RA-B40`): Đổi tên quan hệ ($\rho$) so sánh phân cấp và giá cước.
     - 5 Phép tập hợp (`RA-B41`..`RA-B45`): Phép hợp, giao, trừ khả hợp.
     - 15 Phép chia (`RA-D01`..`RA-D15`): Quy trình 4 bước trừ kinh điển và phân tích ca biên tập chia rỗng $S = \emptyset$.
     - 15 Gom nhóm & hàm tổng hợp (`RA-D16`..`RA-D30`): Toán tử $\gamma$, HAVING filter.
     - 15 Cực trị & đồng hạng (`RA-D31`..`RA-D45`): Lọc tập con phân nhóm $R_{sub}$ trước khi trừ NonMax.
     - 35 Transact-SQL (`SQL-P01`..`SQL-P35`): 15 CREATE TABLE, 10 ALTER TABLE, 10 multi-table UPDATE/DELETE.

---

### P0-09: Lỗi đứt ngoặc `)` trong `relational_schema` & thiếu Mermaid ERD (`ERD-P01`..`ERD-P25`)
- **Mô tả hiện tượng:** Thuật toán cũ `schema.split("), ")` làm mất dấu ngoặc đóng `)` trên mọi quan hệ trừ bảng cuối cùng; thiếu sơ đồ Mermaid ERD và bản số min-max chi tiết.
- **Biện pháp khắc phục:**
  1. Chuẩn hóa hàm phân tách schema, bảo đảm 100% các bảng kết thúc bằng `)`.
  2. Bổ sung mã nguồn Mermaid `erDiagram` cho toàn bộ 25 bài tập ERD độc lập, đầy đủ thực thể, thuộc tính khóa chính PK, khóa ngoại FK và các bản số hai phía (`||--o{`, `||--||`, v.v.).

---

### P0-10: Lỗi cú pháp T-SQL DML (`SET alias.col = ...`) & thiếu bộ lọc thời gian (`SQL-P26`..`SQL-P35`)
- **Mô tả hiện tượng:** Lời giải UPDATE sử dụng cú pháp không hợp lệ `SET HD.TONGTIEN = ...` thay vì `SET TONGTIEN = ...`; đề bài yêu cầu năm 2024 nhưng bảng thiếu cột ngày và mệnh đề WHERE thiếu điều kiện năm.
- **Biện pháp khắc phục:**
  1. Chuẩn hóa toàn bộ 10 câu UPDATE/DELETE theo cú pháp chuẩn T-SQL của Microsoft SQL Server: `UPDATE target_alias SET col = expr FROM table target_alias JOIN ...`.
  2. Đồng bộ cột ngày (`NGAYDK`, `NGAYNHAP`, `NGAYBAY`, `NGAYKT`, `NGAYLAP`, `THANG`/`NAM`, `NGAYDEN`, `THOIGIAN_BD`, `NGAYTRA`, `NGAYTRUC`) trên tất cả các bảng và bổ sung bộ lọc thời gian năm 2024 chính xác.

---

### P0-11: Lỗi ĐSQH cực trị trừ toàn bảng ($R - NonMax$) gây rò rỉ nhóm khác (`RA-D45`)
- **Mô tả hiện tượng:** Tại `RA-D45`, biểu thức lấy toàn bảng $R$ trừ đi NonMax (chỉ tính trong nhóm 45), dẫn đến các bộ thuộc các nhóm khác không có trong NonMax bị sót lại trong kết quả sai lệch.
- **Biện pháp khắc phục:**
  1. Áp dụng công thức chuẩn: Lọc tập con $R_{sub} = \sigma_{cond}(R)$ trước khi tích Descartes và chỉ thực hiện phép trừ trên chính $R_{sub}$:
     $$R_{sub} = \sigma_{MAPK = 'PK\_CNC'}(DOANHNGHIEP\_KCN)$$
     $$NonMax = \pi_{attrs}(\sigma_{val1 < val2}(\rho_{D1}(R_{sub}) \times \rho_{D2}(R_{sub})))$$
     $$KQ = R_{sub} - NonMax$$
  2. Áp dụng thống nhất cho toàn bộ 15 bài toán cực trị từ `RA-D31` đến `RA-D45`.

---

### P0-12: Hệ thống Evidence Manifest Fail-Closed & kiểm thử thực thi 35 bài SQL
- **Mô tả hiện tượng:** Validator chấp nhận pass mà không đối chiếu log thực thi chi tiết của từng câu hỏi độc lập.
- **Biện pháp khắc phục:**
  1. Nâng cấp generator manifest theo nguyên lý Fail-Closed: bất kỳ cờ kiểm tra nào sai đều gán `FAIL`.
  2. Tạo fixture `exam/gk/qa/test_sql_practice.sql` thực thi toàn bộ 35 câu T-SQL trên SQL Server 2025 (`localhost`), sinh log `exam/gk/qa/sql_practice_execution.log` với 35/35 `[PASS]`.
  3. Cập nhật `evidence_manifest.json` đạt 170/170 câu hỏi (135 câu Mock + 35 câu SQL độc lập) được thẩm định và kiểm chứng thực thi với 0 FAIL.

---

## 4. KẾT LUẬN TOÀN DIỆN (ACADEMIC QUALITY RECOVERY COMPLETED)

1. **Khắc phục toàn bộ danh mục lỗi:** 100% lỗi từ P0-01 đến P0-12 đã chuyển sang trạng thái **RESOLVED**.
2. **Quy mô học thuật đạt chuẩn vượt mức:**
   - 15/15 Mock Exam đạt Chuẩn Vàng (Gold Standard), 100% kiểm chứng thực thi SQL Server 2025.
   - 150 bài tập độc lập chuẩn hóa UIT phân loại độ khó (25 ERD, 45 RA Basic, 45 RA Division & Grouping, 35 SQL DDL/DML), 0 template, 0 placeholder.
   - Tổng cộng 285 bài tập (135 câu Mock + 150 bài luyện riêng), toàn bộ có lời giải chi tiết, phân tích tư duy, ca biên và barem chấm điểm.
3. **Ấn phẩm xuất bản A4:** Hoàn tất 4 PDF A4 đồng bộ tại workspace và thư mục OneDrive, preflight kiểm định 100% PASS.
