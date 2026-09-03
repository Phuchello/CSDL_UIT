# Hướng Dẫn Biên Dịch & Xây Dựng (Build Guide)

Tài liệu này hướng dẫn cách tái tạo (reproduce), biên dịch các ấn bản Sổ tay (Lý thuyết & Thực hành) và xây dựng phiên bản trực tuyến **Quartz Knowledge Garden** triển khai trên GitHub Pages.

---

## 1. Yêu cầu Môi trường (Prerequisites)

- **Python**: Phiên bản 3.10 trở lên (khuyến nghị Python 3.12).
- **Node.js**: Phiên bản **22.0.0 trở lên** (kèm npm >= 10.9.2, yêu cầu bắt buộc cho Quartz v5).
- **Thư viện Python phụ trợ** (cho bộ kiểm thử và chuẩn hóa PDF):
  ```bash
  pip install pypdf pypdfium2 pillow lxml pyyaml
  ```
- **Hệ quản trị CSDL (tùy chọn)**: Microsoft SQL Server (2019/2022/2025) để chạy trực tiếp bộ fixture `practice/sql/`.

---

## 2. Biên dịch Sổ tay Học thuật (Handbooks)

Sản phẩm sách bao gồm 2 sổ tay độc lập được ghép từ các chương nguồn HTML:

### 2.1 Sổ tay Lý thuyết (Theory Handbook)
Khi cập nhật nội dung tại `book/chapters/`:
```bash
python scripts/build.py
```
- Kết quả: Tổng hợp các chương thành `book/index.html`.
- Xuất bản PDF chuẩn in ấn A4: Mở `book/index.html` trên trình duyệt Chrome/Edge, chọn `Ctrl + P` $\rightarrow$ *Save as PDF*, khổ giấy *A4*, lề *None*, tích chọn *Background graphics*, lưu tại `dist/IT004_CSDL_UIT_LyThuyet_VoTrongPhuc.pdf`.

### 2.2 Sổ tay Thực hành (Practical Handbook)
Khi cập nhật nội dung tại `practice/chapters/`:
```bash
python scripts/build_practice.py
```
- Kết quả: Biên dịch 12 chương thực hành thành `practice/index.html`.
- Kiểm thử tính nhất quán khế ước fixture:
  ```bash
  python scripts/validate_practice_static.py
  ```
- Xuất bản PDF thực hành: Lưu tại `dist/IT004_CSDL_UIT_ThucHanh_VoTrongPhuc.pdf` (chuẩn hóa metadata bằng `python scripts/normalize_practice_pdf.py`).

---

## 3. Biên dịch Canonical Quartz Knowledge Garden (GitHub Pages Build)

Knowledge Garden tại thư mục `garden/` là ấn bản web tương tác chính thức của CSDL_UIT v1.1.

### Quy trình biên dịch cục bộ (Local Build):
```bash
# 1. Đồng bộ hóa tệp PDF và assets từ dist/ vào garden
node scripts/copy_garden_assets.mjs

# 2. Cài đặt các gói phụ thuộc của Quartz
cd garden
npm ci

# 3. Biên dịch mã nguồn Markdown thành trang web tĩnh (static HTML)
node ./quartz/bootstrap-cli.mjs build -d content -o public

# 4. Kiểm thử toàn bộ liên kết nội bộ
cd ..
python scripts/agent/check_links.py
```

### Kiểm thử Hợp đồng D2 (Content Contract):
```bash
python scripts/validate_garden_d2.py
```
Script kiểm tra tính toàn vẹn của:
- 57 ghi chú Markdown và các trường frontmatter ngữ nghĩa.
- Đồ thị liên kết bắt buộc (`division` $\leftrightarrow$ `double-not-exists` $\leftrightarrow$ `lab-03` $\leftrightarrow$ `wrong-universal-candidate`).
- Độ sâu sư phạm của các ghi chú cốt lõi (thuật toán, bảng dry-run).
- Khế ước bảng và cột chuẩn tắc khớp 100% với `practice/sql/01_schema.sql`.
- Thứ tự ưu tiên giữa khóa ngoại khai báo (`Msg 547`) và trigger `AFTER UPDATE`.
- Tính hợp lệ của cặp tệp PDF xuất bản.

---

## 4. Tự động hóa CI/CD & GitHub Pages Deployment

Quy trình phát hành tự động được cấu hình qua hai GitHub Actions workflows:

1. **Kiểm thử tự động (`.github/workflows/validate.yml`)**:
   - Chạy trên mọi push và pull request vào nhánh `main`.
   - Kiểm tra biên dịch HTML cho cả hai sổ tay, chạy `scripts/validate.py`, `scripts/validate_practice_static.py`, `scripts/validate_garden_d2.py`, build thử Quartz và quét toàn bộ liên kết nội bộ.

2. **Triển khai GitHub Pages (`.github/workflows/pages.yml`)**:
   - Tự động kích hoạt khi có commit mới trên nhánh `main`.
   - Khởi tạo môi trường Node 22, đồng bộ assets, cài đặt dependencies, biên dịch Quartz từ `garden/` sang `garden/public`, và phát hành trực tiếp lên GitHub Pages tại địa chỉ:
     **[https://phuchello.github.io/CSDL_UIT/](https://phuchello.github.io/CSDL_UIT/)**.
