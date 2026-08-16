# Lịch Sử Dự Án & Quá Trình Phát Triển (Project History)

Tài liệu này ghi nhận quá trình nghiên cứu, biên soạn, kiểm toán học thuật và hoàn thiện xuất bản của dự án Cẩm nang CSDL IT004 UIT.

---

## 1. Dòng Thời Gian Phát Triển

### Giai đoạn 1: Khảo sát & Xây dựng Cấu trúc Sách (Research & Architecture)
- Thu thập và phân loại toàn bộ giáo trình chính khóa, slide bài giảng môn Cơ sở dữ liệu (IT004) của Khoa Hệ thống Thông tin – UIT.
- Tổng hợp ngân hàng câu hỏi ôn tập, bài tập thực hành Lab SQL Server và đề thi chính thức từ năm 2017 đến 2025.
- Thiết lập ma trận bao phủ kiến thức (`coverage_matrix.md`) và bảng đối chiếu mâu thuẫn ký hiệu giữa các nguồn tài liệu (`source_conflicts.md`).

### Giai đoạn 2: Thiết kế Hệ thống Chế bản & Soạn thảo (Authoring & Print CSS)
- Xây dựng động cơ in ấn CSS A4 chuẩn hóa (`book/css/book.css`) hỗ trợ ngắt trang thông minh, kiểm soát lề gáy sách và hiển thị khối mã lệnh.
- Soạn thảo tuần tự 8 chương chuyên đề, bao gồm 30 bài tập Đại số quan hệ mẫu, các bài thực chiến T-SQL Server, ràng buộc toàn vẹn và lý thuyết chuẩn hóa.

### Giai đoạn 3: Kiểm toán Học thuật Độc lập (Academic Audits)
- Thẩm định chuyên sâu về tính đúng đắn học thuật của các khái niệm then chốt:
  - Phân định rõ 3NF và BCNF theo định nghĩa hình thức.
  - Xử lý ngữ nghĩa phép chia và tập chia rỗng giữa Đại số quan hệ và SQL.
  - Chuẩn hóa lược đồ quan hệ trong các ví dụ nâng cao (phép hợp tổng quát với quan hệ mở rộng `NHANVIEN`).
  - Kiểm tra tính đúng đắn của trigger đa dòng trên SQL Server.

### Giai đoạn 4: Tinh chỉnh Chế bản & Xuất bản Canonical (Final Surgical Gate)
- Loại bỏ triệt để các lỗi ngắt trang (tiêu đề mồ côi, bảng chia cắt vụn).
- Tối ưu hóa các bảng so sánh dài chống tràn lề trang.
- Nhúng siêu dữ liệu chuẩn hóa vào tệp PDF (Title, Author, Subject).
- Hoàn thiện tệp PDF chính thức: **88 trang A4 hoàn hảo**.

### Giai đoạn 5: Tích hợp & Đóng gói Kho lưu trữ Mở (Repository Integration)
- Tái cấu trúc kho lưu trữ sạch sẽ, bảo mật, độc lập nền tảng.
- Xây dựng bộ công cụ kiểm thử tự động (Validation Suite) và hệ thống CI/CD với GitHub Actions.
- Chuẩn bị trang xem trước trực tuyến qua GitHub Pages.
