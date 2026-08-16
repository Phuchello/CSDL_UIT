# Lịch sử dự án

Tài liệu này ghi lại các giai đoạn chính trong quá trình nghiên cứu, biên soạn và hoàn thiện Cẩm nang CSDL IT004 UIT.

---

## 1. Dòng thời gian phát triển

### Giai đoạn 1: Khảo sát & xây dựng cấu trúc sách
- Thu thập và phân loại giáo trình, slide bài giảng và tài liệu tham khảo liên quan đến học phần Cơ sở dữ liệu (IT004).
- Tổng hợp bài tập thực hành SQL Server và đề thi tham khảo.
- Thiết lập ma trận bao phủ kiến thức (`research/coverage_matrix.md`) và bảng đối chiếu khác biệt giữa các nguồn (`research/source_conflicts.md`).

### Giai đoạn 2: Soạn thảo & chế bản
- Xây dựng Print CSS A4 trong `book/css/book.css` để kiểm soát lề, ngắt trang, bảng và khối mã lệnh.
- Soạn các chương về ER, mô hình quan hệ, Đại số quan hệ, SQL Server, ràng buộc toàn vẹn, phụ thuộc hàm, chuẩn hóa và thực hành.
- Bổ sung Exam Playbook, Cheat Sheet và bài tập có lời giải.

### Giai đoạn 3: Rà soát học thuật
- Kiểm tra các điểm dễ nhầm như 3NF/BCNF, phép chia và trường hợp tập chia rỗng, tính khả hợp của phép hợp và trigger đa dòng trên SQL Server.
- Đối chiếu lại tên thuộc tính, lược đồ ví dụ và cách dùng ký hiệu giữa các chương.

### Giai đoạn 4: Tinh chỉnh trước phát hành
- Sửa các lỗi ngắt trang, tiêu đề mồ côi và khối code bị chia cắt.
- Điều chỉnh bảng dài để tránh tràn lề.
- Nhúng metadata Title, Author và Subject vào PDF.
- Hoàn thiện bản PDF 88 trang A4.

### Giai đoạn 5: Tích hợp repository công khai
- Chuẩn hóa cấu trúc repository và loại bỏ tệp tạm, đường dẫn cục bộ cùng dữ liệu không phù hợp để công khai.
- Xây dựng `scripts/build.py`, `scripts/validate.py` và GitHub Actions.
- Triển khai bản HTML đọc trực tuyến bằng GitHub Pages.
- Bổ sung bản đồ kiến thức IT004 làm hình ảnh chính cho README.
