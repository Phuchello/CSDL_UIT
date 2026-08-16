# Nhật Ký Thay Đổi (Changelog)

Tất cả các thay đổi quan trọng và các cột mốc phát hành của dự án Cẩm nang CSDL IT004 UIT được ghi lại tại đây.

---

## [v1.0.0] — 2026-08-16 (Ấn Bản Phát Hành Chính Thức)

### Hoàn thiện & Xuất bản
- **Tệp PDF**: Phát hành `dist/IT004_CSDL_UIT_CamNang_VoTrongPhuc.pdf` chuẩn 88 trang A4.
- **Kiểm tra học thuật & chế bản**: Rà soát các điểm dễ sai như 3NF/BCNF, empty divisor, trigger RBTV, ngắt trang, khối code và khả năng hiển thị PDF.
- **Bộ công cụ tự động hóa**: Xây dựng `build.py` / `validate.py` và quy trình GitHub Actions CI/CD.
- **Tài nguyên trực quan**: Bổ sung `assets/it004-knowledge-map.svg` làm bản đồ kiến thức chính của repository.
- **Đọc trực tuyến**: Triển khai bản HTML qua GitHub Pages.

---

## [v0.9.0] — 2026-08-13 (Tinh chỉnh cuối trước phát hành)
- Sửa bố cục trang ngắt của Recall Sheet Chương 3 (Tr. 46).
- Giữ các đoạn code `CREATE TABLE CTHD` và `SELF JOIN` nguyên vẹn trên từng trang (Tr. 49 & Tr. 53).
- Bổ sung quan hệ phụ trợ minh họa `NHANVIEN` và chuẩn hóa thuộc tính chiếu `MA_NGUOI` cho Câu 13 ĐSQH (Tr. 39).
- Bổ sung `references.html` và trang Colophon cuối sách.
- Nhúng metadata PDF: Title, Author, Subject.

---

## [v0.5.0] — 2026-08-11 (Bản thảo hoàn chỉnh các chương)
- Biên soạn hoàn chỉnh 8 phần nội dung: nhập môn, Mô hình ER & Quan hệ, Đại số quan hệ, SQL Server, Ràng buộc toàn vẹn, Phụ thuộc hàm & Chuẩn hóa, Thực hành SQL Server, Exam Playbook và Cheat Sheet.
- Thiết lập hệ thống Print CSS A4.

---

## [v0.1.0] — 2026-08-06 (Khảo sát & Khởi tạo)
- Tổng hợp tài liệu tham khảo, slide bài giảng Khoa HTTT – UIT và đề thi tham khảo.
- Thiết lập kiến trúc nội dung và ma trận bao phủ môn học.
