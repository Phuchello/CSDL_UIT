# Nhật Ký Thay Đổi (Changelog)

Tất cả các thay đổi quan trọng và các cột mốc phát hành của dự án Cẩm nang CSDL IT004 UIT được ghi lại tại đây.

---

## [v1.0.0] — 2026-08-16 (Ấn Bản Phát Hành Chính Thức)

### Hoàn thiện & Xuất bản (Publication Ready)
- **Tệp PDF Deliverable**: Phát hành `dist/IT004_CSDL_UIT_CamNang_VoTrongPhuc.pdf` chuẩn 88 trang A4.
- **Kiểm toán Học thuật & Chế bản**: Vượt qua 100% các cổng kiểm tra khắt khe về tính đúng đắn học thuật (3NF/BCNF, empty divisor, RBTV trigger) và chế bản in ấn (không trang mồ côi, không cắt xén code, không thanh cuộn ngang).
- **Bộ Công Cụ Tự Động Hóa**: Xây dựng bộ script `build.py` / `validate.py` và quy trình GitHub Actions CI/CD.
- **Tài Nguyên Trực Quan**: Trích xuất bộ ảnh xem trước chất lượng cao (`cover.png`, `roadmap.png`, `handbook-preview.png`).

---

## [v0.9.0] — 2026-08-13 (Cổng Kiểm Soát Vi Phẫu — Final Surgical Gate)
- Sửa đổi bố cục trang ngắt của tiêu đề Recall Sheet Chương 3 (Tr. 46).
- Cố định phân đoạn code `CREATE TABLE CTHD` và `SELF JOIN` nguyên vẹn trên từng trang (Tr. 49 & Tr. 53).
- Bổ sung quan hệ phụ trợ minh họa `NHANVIEN` và chuẩn hóa thuộc tính chiếu `MA_NGUOI` cho Câu 13 ĐSQH (Tr. 39).
- Bổ sung tệp `references.html` và trang Colophon chuẩn cuối sách.
- Nhúng metadata XMP/Info (Title, Author, Subject) trực tiếp vào PDF.

---

## [v0.5.0] — 2026-08-11 (Bản Thảo Hoàn Chỉnh Toàn Bộ Các Chương)
- Biên soạn hoàn chỉnh 8 chương: Nhập môn, Mô hình ER & Quan hệ, Đại số quan hệ (30 bài tập), SQL Server, Ràng buộc toàn vẹn, Phụ thuộc hàm & Chuẩn hóa, Thực hành SQL Server, Exam Playbook và Cheat Sheet.
- Thiết lập hệ thống Print CSS A4 chuẩn hóa.

---

## [v0.1.0] — 2026-08-06 (Khảo Sát & Khởi Tạo Dự Án)
- Tổng hợp tài liệu tham khảo, slide bài giảng Khoa HTTT – UIT, ngân hàng đề thi 2017–2025.
- Thiết lập kiến trúc sư phạm 11 bước và ma trận bao phủ môn học.
