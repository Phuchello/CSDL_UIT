# Hướng Dẫn Đánh Giá Bản Mẫu Thực Hành (Practice Proof Review Guide) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31  
**Tác giả biên soạn:** Võ Trọng Phúc  
**Tài liệu đánh giá:** `dist/proofs/IT004_CSDL_UIT_v1.1_Practice_DesignProof.pdf` (21 trang A4)  
**Ảnh xem trước:** `dist/review/v1.1_practice/cover.png`, `contact-sheet-01.png`, `contact-sheet-02.png`

---

## 1. Mục Đích Bản Mẫu Phase C1

Bản mẫu Phase C1 (21 trang A4) được xây dựng nhằm chứng minh đầy đủ kiến trúc, ngôn ngữ thiết kế, phương pháp sư phạm, cơ chế phân tích dòng thực thi (Execution Trace) và chất lượng mã nguồn T-SQL trước khi tiến hành viết toàn văn toàn bộ Cẩm nang Thực hành ở Phase C2.

---

## 2. Bảng 10 Tiêu Chí Đánh Giá Dành Cho Người Thẩm Định (Mentor Review Rubric)

Kính đề nghị Người thẩm định / Mentor đánh giá bản mẫu dựa trên 10 tiêu chí học thuật và kỹ thuật sau:

| STT | Tiêu chí đánh giá | Câu hỏi định hướng | Kết quả mong đợi |
| :---: | :--- | :--- | :--- |
| **1** | **Quan hệ gia đình với Bìa Lý thuyết** | Bìa thực hành có giữ đúng ngôn ngữ tối giản của Cover A, đồng thời thể hiện rõ đặc trưng xử lý dữ liệu thực hành không? | Nhất quán về kiểu chữ, màu sắc; sơ đồ vector mô tả luồng: *Bảng nguồn $\rightarrow$ Engine $\rightarrow$ Kết quả*. |
| **2** | **Độ rõ nét & Khả năng đọc mã nguồn (A4)** | Các khối mã SQL trên nền nhạt có dễ đọc, ngắt dòng hợp lý và không bị tràn lề ngang trên trang in A4 không? | Kích thước font 8.5pt–9pt, syntax highlight trang nhã, không dùng khung terminal đen nặng nề. |
| **3** | **Độ trực quan của Bảng kết quả** | Các bảng kết quả HTML có đủ nhỏ gọn để minh chứng cho truy vấn mà không chiếm quá nhiều diện tích trang không? | Thể hiện rõ các dòng kết quả then chốt, làm nổi bật giá trị thay đổi, nhóm gom và giá trị `NULL`. |
| **4** | **Tính sáng tỏ của Dòng thực thi (Execution Trace)** | Phần phân tích từng bước xử lý truy vấn có giúp người học hiểu rõ *tại sao* câu lệnh lại ra kết quả đó không? | Thể hiện rõ các chặng `FROM/JOIN` $\rightarrow$ `WHERE` $\rightarrow$ `GROUP BY/HAVING` $\rightarrow$ `SELECT/ORDER BY`. |
| **5** | **Cấu trúc bài giảng Lab chuẩn mực** | Tiến trình từ *Mục tiêu $\rightarrow$ Dữ liệu $\rightarrow$ Viết code $\rightarrow$ Kiểm chứng $\rightarrow$ Gỡ lỗi* có mạch lạc và sư phạm không? | Học viên có thể tự thực hành theo từng bước mà không bị bỡ ngỡ. |
| **6** | **Tính thực chiến của Hệ thống gỡ lỗi** | 6 nhóm mã lỗi SQL Server (Msg 208, 547, 8152, 8120, 512, 245) có đúng với các vấn đề thực tế sinh viên hay gặp không? | Khung chẩn đoán 5 bước giải quyết nhanh chóng trong 60 giây. |
| **7** | **Chuẩn mực Trigger & An toàn đa dòng** | Phần giải thích bảng ảo `inserted`/`deleted` và việc bác bỏ biến vô hướng có chặt chẽ về mặt kỹ thuật không? | Tuyệt đối tuân thủ tư duy tập hợp của SQL Server, an toàn 100% khi thao tác DML hàng loạt. |
| **8** | **Mật độ thông tin & Trình bày trang** | Tỷ lệ giữa lý thuyết bổ trợ, mã nguồn, bảng dữ liệu và sơ đồ có cân đối, không có trang trắng thừa không? | 21 trang A4 được bố cục trọn vẹn, ngắt trang chính xác theo từng chuyên đề. |
| **9** | **Khả năng tự học không cần bài giảng** | Một sinh viên mới bắt đầu có thể tự cài đặt môi trường, chạy script và hiểu bản chất thông qua tài liệu này không? | Có checklist 60 giây và hướng dẫn chi tiết từng bước. |
| **10** | **Sự sẵn sàng cho Phase C2** | Toàn bộ hệ thống thiết kế và khung bài học này đã đủ độ chín để triển khai viết trọn vẹn toàn bộ cuốn sách chưa? | Đạt tiêu chuẩn phê duyệt để bước vào giai đoạn biên soạn toàn văn. |

---

## 3. Quy Trình Phê Duyệt & Bước Kế Tiếp

- **Nếu ĐẠT (Approved):** Mentor phê duyệt kiến trúc và khung thiết kế Phase C1 $\rightarrow$ Mở khóa Phase C2 để biên soạn toàn văn 8 phần chuyên đề.
- **Nếu cần điều chỉnh (Changes Requested):** Bổ sung hoặc tinh chỉnh các phần theo phản hồi cụ thể của Mentor trước khi bắt đầu Phase C2.
