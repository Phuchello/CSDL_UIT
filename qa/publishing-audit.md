# Publishing & Visual QA Audit — IT004 Database Handbook

## Tổng quan Đánh giá Chế bản & Xuất bản

Tài liệu này ghi nhận kết quả kiểm toán chế bản in ấn (Print CSS / PDF Rendering Engine), căn lề trang A4, độ co giãn typographic, ngắt trang và hiển thị đa nền tảng.

---

## 1. Tiêu Chuẩn Chế Bản In Ấn (A4 Print Engine)

| Yếu tố Chế bản | Tiêu chuẩn Đặt ra | Kết quả Đạt được | Đánh giá |
| :--- | :--- | :--- | :---: |
| **Kích thước trang (Page Format)** | Chuẩn ISO A4 (210mm × 297mm) | Khớp chính xác 100% | **PASS** |
| **Căn lề (Margins)** | 18mm lề trong, 15mm lề ngoài, đối xứng | Đảm bảo khoảng cách gáy sách khi đóng tập | **PASS** |
| **Tổng số trang (Total Pages)** | Cố định chính xác 88 trang A4 | 88 trang hoàn chỉnh, không trang trắng thừa | **PASS** |
| **Thanh cuộn ngang trong PDF (Horizontal Scrollbar)** | Tuyệt đối không xuất hiện thanh cuộn giả | Tất cả khối code bọc dòng thông minh (`overflow-x: hidden`, `white-space: pre-wrap`) | **PASS** |
| **Bảo toàn Khối Code (Keep-Together)** | Không ngắt đoạn câu lệnh DDL/Trigger giữa chừng | `CREATE TABLE CTHD` (Tr. 49) và `SELF JOIN` (Tr. 53) nằm trọn trong 1 trang | **PASS** |
| **Khối Tóm tắt Ôn tập (Recall Sheet)** | Tiêu đề và nội dung đi liền nhau | Tiêu đề Recall Sheet Chương 3 nằm trọn vẹn đầu Trang 46 | **PASS** |
| **Bảng So sánh Dữ liệu (Data Tables)** | Tự động ngắt dòng cột nội dung dài | Cột "Nhược điểm" (Tr. 56) tự động wrap dòng, không tràn lề phải | **PASS** |
| **Cấu trúc PDF & Metadata** | Tiêu đề, Tác giả, Chủ đề trong XMP/Info | Title, Author, Subject được nhúng trực tiếp chuẩn UTF-16BE | **PASS** |

---

## 2. Thứ Tự Phân Đoạn Cuối Sách (Final Section Sequencing)

Cấu trúc phân bổ 12 trang cuối của cẩm nang được bố cục chặt chẽ:

```
Trang 77–82 : Chương 7 — Thực hành SQL Server & Quản trị CSDL
Trang 83–84 : IT004 Exam Playbook — Chiến thuật phòng thi & Kỹ năng làm bài
Trang 85–86 : IT004 Last-Minute Cheat Sheet — Cứu cánh 15 phút trước giờ thi
Trang 87    : Nguồn tham khảo & Tài liệu đối chiếu (References)
Trang 88    : Colophon & Thông tin xuất bản (Trang kết)
```

---

## 3. Khả Năng Tương Thích Trình Duyệt & GitHub Pages

- **HTML5 Chuẩn hóa**: Tệp `book/index.html` được lắp ráp từ các thành phần mô-đun độc lập, không chứa đường dẫn cục bộ tuyệt đối.
- **Đồ họa & Phông chữ**: Sử dụng phông chữ Inter và JetBrains Mono tối ưu hóa hiển thị trên màn hình Retina cũng như khi in ra bản cứng.
- **Tương thích Mobile / Desktop**: Giao diện co giãn mượt mà theo viewport, các thẻ `<details>` được mở sẵn phục vụ in ấn nhưng vẫn tương tác thu phóng được trên trình duyệt web.
