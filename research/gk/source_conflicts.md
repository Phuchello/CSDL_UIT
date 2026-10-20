# BIÊN BẢN ĐIỀU TRA MÂU THUẪN & SAI LỆCH NGUỒN (SOURCE CONFLICTS & ERRATA)

**Dự án:** `Phuchello/CSDL_UIT` — Module Giữa Kỳ (GK) IT004  
**Bản ghi nhận:** Snapshot nghiên cứu học thuật thực chứng  
**Nguyên tắc:** Minh bạch hóa mọi sai lệch, mâu thuẫn giữa các bản sao mirror, giới hạn truy cập và cảnh báo học thuật; không che giấu lỗi hay giả định tính toàn vẹn khi chưa có bằng chứng hiển thị độc lập.

---

## 1. Mâu Thuẫn Về Số Lượng Hiện Vật & Trạng Thái "Đề Giữa Kỳ"

### Vấn đề:
Trong `research/v1.1_phase_a/artifact_registry.md` trước đây có tổng cộng **31 hiện vật chuẩn hóa**. Một số tài liệu tóm tắt hoặc người học có thể ngộ nhận rằng repo có "31 đề thi giữa kỳ".

### Điều tra thực tế:
Kiểm toán độc lập từng mã ID cho thấy:
- Chỉ có đúng **10 hiện vật** là đề thi Giữa kỳ Lý thuyết chính thức (`EXAM-...-MID-...`).
- **7 hiện vật** là đề thi Cuối kỳ Lý thuyết (`EXAM-...-FINAL-...`), tập trung vào Phụ thuộc hàm, Chuẩn hóa BCNF/3NF, Bảng tầm ảnh hưởng.
- **10 hiện vật** là đề thi Thực hành trên máy (`PRAC-...`), tập trung vào cài đặt Trigger và DDL trên phòng máy.
- **3 hiện vật** là tài liệu ôn tập và barem điểm chấm thi (`REV-...`).
- **1 hiện vật** là hệ thống lab 4 buổi (`LAB-...`).

### Quyết định xử lý:
Module GK chỉ sử dụng 10 đề GK thật + 3 tài liệu ôn tập GK làm căn cứ xây dựng ngân hàng đề và chuẩn hóa ma trận. Tuyệt đối không quảng bá con số 31 đề GK.

---

## 2. Mâu Thuẫn Về Phân Bổ Điểm Số ERD: 2.5 Điểm vs 2.0 Điểm

### Vấn đề:
- Các đề thi HK1 2023–2024 (Đề 1 và Đề 2) ghi rõ: `Câu 1: (2.5 điểm) [G1, G2] - Xây dựng mô hình ERD và chuyển sang mô hình quan hệ`. Câu 2 chiếm 7.5 điểm (DDL/UPDATE 1.5đ + 6 câu ĐSQH 6.0đ).
- Đề thi HK1 2024–2025 (Bản xem trước cộng đồng) ghi: `Câu 1: 2.0 điểm` và `Câu 2: 8.0 điểm`.
- Các đề thi cũ hơn (2017–2020) đôi khi tách câu hỏi ĐSQH thành thang điểm 1.0đ hoặc 1.5đ cho câu phân loại.

### Quyết định xử lý:
Xây dựng 2 profile mô phỏng chuẩn trong ngân hàng đề:
- **Profile A (Mẫu lịch sử 2023–2024):** ERD 2.5đ + SQL DDL/UPDATE 1.5đ + ĐSQH 6.0đ = 10.0đ.
- **Profile B (Mẫu cải cách 2024–2025):** ERD 2.0đ + SQL DDL/UPDATE 1.5đ + ĐSQH 6.5đ = 10.0đ.
Cả hai profile đều đảm bảo chính xác 10.0 điểm / 75 phút và phản ánh đúng thực tế khảo thí của UIT.

---

## 3. Giới Hạn Truy Cập Đối Với Các Lead 2025–2026 (Access Limits & Anti-Bot Blockers)

### Vấn đề:
Một số liên kết trên Studocu được chia sẻ gần đây với tiêu đề "Đề thi giữa kỳ CSDL 2025–2026 HK1" (Mã tài liệu: `149604841` - `COM-C13`):
- Hệ thống trả về trang kiểm tra bảo mật bot / Cloudflare Challenge / HTTP 403.
- Không thể đọc được toàn văn ảnh đề, header chính thức của trường hoặc nội dung chi tiết.

### Quyết định xử lý:
- Gắn nhãn chuẩn `ACCESS_LIMITED / UNVERIFIED` cho `COM-C13`.
- Giữ nguyên URL trong bảng kê nguồn để đối chiếu tương lai.
- **Tuyệt đối KHÔNG giả định hay bịa đặt** nội dung đề thi năm 2025–2026.
- Sử dụng căn cứ thực chứng vững chắc nhất từ các đề đã xác minh đầy đủ (2017 đến 2024–2025) để tổng hợp xu hướng.

---

## 4. Mâu Thuẫn Về Ký Pháp Gom Nhóm Trong Đại Số Quan Hệ ($\gamma$ vs $\Im$)

### Vấn đề:
- Trong một số slide bài giảng UIT (ThS. Đỗ Phúc Long), phép gom nhóm được ký hiệu bằng chữ $\Im$ (Fractur I).
- Trong tài liệu quốc tế (Silberschatz - Database System Concepts), bài giảng chuẩn và barem chấm điểm viết tay Khóa 18 (`REV-2024-K18-SOL`), ký pháp chuẩn là $\gamma$ (Gamma) hoặc biểu thức dạng:
  $$\text{ThuộcTínhGomNhóm} \ \gamma \ _{\text{HàmTổngHợp}(\text{ThuộcTính})}(\text{QuanHệ})$$

### Quyết định xử lý:
- Trong toàn bộ lời giải và đề mô phỏng của ngân hàng đề, sử dụng ký pháp chuẩn mực toán học $\gamma$ (hoặc $\Im$ được chú thích tương đương) kèm giải thích tường minh: danh sách thuộc tính gom nhóm, hàm kết hợp, và tên cột đầu ra.
- Đảm bảo người học viết theo bất kỳ ký pháp nào cũng được hội đồng chấm điểm công nhận đúng bản chất.

---

## 5. Mâu Thuẫn Trong Ngữ Nghĩa Phép Chia Khi Tập Mục Tiêu Rỗng (Vacuous Truth)

### Vấn đề:
Khi giải bài toán phép chia (ví dụ: "Tìm đơn hàng đặt *tất cả* các mặt hàng của nhà cung cấp X"):
- Nếu nhà cung cấp X không có mặt hàng nào trong CSDL (tập chia rỗng $\emptyset$):
  - Theo logic toán học ($\forall y \in \emptyset, P(x, y)$), mọi đơn hàng $x$ đều thỏa mãn một cách rỗng (vacuous truth).
  - Tuy nhiên, trong thực tế chấm thi tại UIT, tân từ bài toán luôn ngầm định: Nhà cung cấp X phải có ít nhất 1 mặt hàng, và đơn hàng $x$ phải thực sự có đặt hàng.

### Quyết định xử lý:
Mọi lời giải mẫu của bài toán phép chia đều phân tích rõ ràng 2 phương pháp:
1. **Phương pháp Phép chia ĐSQH ($\div$):**
   $$R_1 \div R_2 = \pi_X(R_1) - \pi_X((\pi_X(R_1) \times R_2) - R_1)$$
2. **Phương pháp Double `NOT EXISTS` & Gom nhóm `COUNT(DISTINCT)` trong SQL:**
   Chỉ rõ cách bắt điều kiện để tránh việc tập con rỗng gây ra kết quả sai lệch trong phòng thi.
