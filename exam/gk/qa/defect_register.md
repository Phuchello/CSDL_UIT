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
| **P0-03** | Validator báo cáo độ tin cậy ảo (False Confidence) | **P0** (Critical) | **RESOLVED** | 22/10/2026 | 23/10/2026 |
| **P0-04** | Ấn phẩm PDF không phân định bản DRAFT & VERIFIED | **P0** (Critical) | **RESOLVED** | 22/10/2026 | 23/10/2026 |
| **P0-05** | Phân mảnh lược đồ & trùng câu MOCK-02 $\to$ MOCK-15 | **P1** (High) | **REGISTERED / IN_PROGRESS** | 22/10/2026 | Theo kế hoạch Phase B |

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

### P0-03: Validator báo cáo độ tin cậy ảo (False Confidence)
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
- **Kế hoạch xử lý (Phase B Remediation):**
  1. Tạm thời giữ nguyên trạng thái `DRAFT / NOT_RELEASE_READY` cho MOCK-02 đến MOCK-15.
  2. Sau khi MOCK-01 đạt toàn bộ Acceptance Gate, tiến hành xây dựng lần lượt từng đề một theo tiêu chuẩn vàng của MOCK-01 (mỗi đề sở hữu một ngữ cảnh nghiệp vụ duy nhất xuyên suốt).
