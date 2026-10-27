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
| **P0-05** | Phân mảnh lược đồ & trùng câu MOCK-02 $\to$ MOCK-15 | **P1** (High) | **IN_PROGRESS (MOCK-01 &rarr; MOCK-05 RESOLVED)** | 22/10/2026 | Đang xử lý Phase C |

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
  5. **MOCK-06 đến MOCK-15:** Giữ nguyên trạng thái `DRAFT / NOT_RELEASE_READY`, tiếp tục tái cấu trúc tuần tự trong Phase C (Batch C.4: MOCK-06, MOCK-07, MOCK-08).
