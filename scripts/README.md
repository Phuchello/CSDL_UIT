# Build & Validation Scripts

Thư mục này chứa các script phục vụ biên dịch tài liệu HTML, trích xuất hình ảnh xem trước (preview assets) và kiểm thử chất lượng (automated validation).

---

## 1. Danh sách Scripts

| Tệp tin | Ngôn ngữ | Chức năng chính |
| :--- | :--- | :--- |
| `build.py` | Python 3 | Đọc tuần tự 11 tệp chương trong `book/chapters/`, xử lý thuộc tính `<details open>` và biên dịch ra `book/index.html`. |
| `build.ps1` | PowerShell | Phiên bản PowerShell tương đương của `build.py`. |
| `validate.py` | Python 3 | Bộ kiểm thử toàn diện 6 bước: cấu trúc HTML, tính toàn vẹn PDF, metadata, ký hiệu toán học, thứ tự chương, và an toàn mã nguồn. |
| `validate.ps1` | PowerShell | Trình thực thi tiện ích cho `validate.py` trên môi trường Windows PowerShell. |
| `generate_previews.py` | Python 3 | Tự động trích xuất các trang tiêu biểu từ `dist/IT004_CSDL_UIT_CamNang_VoTrongPhuc.pdf` để tạo ảnh `cover.png`, `roadmap.png`, `handbook-preview.png`. |

---

## 2. Hướng dẫn sử dụng

### Biên dịch lại sách HTML
```bash
# Sử dụng Python
python scripts/build.py

# Hoặc sử dụng PowerShell
./scripts/build.ps1
```

### Chạy bộ kiểm thử tự động (Validation Suite)
```bash
# Sử dụng Python
python scripts/validate.py

# Hoặc sử dụng PowerShell
./scripts/validate.ps1
```

### Trích xuất lại hình ảnh xem trước
```bash
python scripts/generate_previews.py
```
