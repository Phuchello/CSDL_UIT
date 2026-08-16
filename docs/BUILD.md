# Hướng Dẫn Biên Dịch & Xây Dựng (Build Guide)

Tài liệu này hướng dẫn cách tái tạo (reproduce), biên dịch bản HTML từ các tệp chương nguồn và thực hiện kiểm thử tự động.

---

## 1. Yêu cầu Môi trường (Prerequisites)

- **Python**: Phiên bản 3.10 trở lên.
- **Thư viện Python phụ trợ** (phục vụ chạy test suite):
  ```bash
  pip install pypdf pypdfium2 pillow lxml
  ```
- **Trình duyệt (tùy chọn để in ấn PDF)**: Google Chrome hoặc Microsoft Edge.

---

## 2. Quy trình Biên Dịch (Compilation Workflow)

### Bước 1: Biên dịch HTML từ các chương nguồn
Khi bạn chỉnh sửa nội dung trong thư mục `book/chapters/`, hãy chạy lệnh biên dịch để cập nhật `book/index.html`:

```bash
# Bằng Python
python scripts/build.py

# Hoặc bằng PowerShell
./scripts/build.ps1
```

Script sẽ tự động:
1. Đọc 11 tệp HTML theo đúng thứ tự sư phạm.
2. Thêm thuộc tính `open` cho tất cả các thẻ `<details>` để bảo đảm toàn bộ lời giải và ví dụ được hiển thị đầy đủ khi xem hoặc in ấn.
3. Gộp thành một tệp duy nhất `book/index.html`.

---

### Bước 2: Kiểm thử tính toàn vẹn (Validation Suite)
Chạy bộ kiểm thử tự động 6 bước để xác nhận không có liên kết hỏng, cấu trúc HTML hợp lệ, tệp PDF chuẩn hóa và an toàn mã nguồn:

```bash
# Bằng Python
python scripts/validate.py

# Hoặc bằng PowerShell
./scripts/validate.ps1
```

---

## 3. Quy trình Xuất Bản PDF Chuẩn In ấn A4

Nếu cần xuất bản lại tệp PDF chuẩn in ấn A4 từ `book/index.html`:

1. Mở tệp `book/index.html` bằng Google Chrome hoặc Microsoft Edge.
2. Nhấn `Ctrl + P` (hoặc chọn Menu $\rightarrow$ Print).
3. Thiết lập thông số in:
   - **Destination**: *Save as PDF*
   - **Paper size**: *A4*
   - **Layout**: *Portrait*
   - **Margins**: *None* (hoặc *Custom: 0*) vì file CSS `book/css/book.css` đã quản lý lề `@page` tiêu chuẩn.
   - **Options**: Tích chọn *Background graphics* (Đồ họa nền).
4. Lưu tệp vào thư mục `dist/`.

---

## 4. Kích hoạt GitHub Pages (Online Reading Activation)

Để kích hoạt tính năng đọc trực tuyến tự động qua GitHub Pages:
1. Truy cập vào trang quản trị Repository trên GitHub: **Settings $\rightarrow$ Pages**.
2. Tại mục **Build and deployment $\rightarrow$ Source**, chọn: **GitHub Actions**.
3. Sau khi kích hoạt, workflow `.github/workflows/pages.yml` sẽ tự động triển khai bản HTML tại địa chỉ `https://phuchello.github.io/CSDL_UIT/` mỗi khi có commit mới trên nhánh `main`.
