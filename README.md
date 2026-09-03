# IT004 · CƠ SỞ DỮ LIỆU (v1.1)
### Bộ đôi Cẩm nang Lý thuyết, Thực hành & Knowledge Garden

**Mô hình hóa ER • Đại số quan hệ • SQL Server T-SQL • Ràng buộc toàn vẹn & Trigger • Chuẩn hóa dữ liệu**

Biên soạn: **Võ Trọng Phúc**
*Tài liệu học thuật phi thương mại hỗ trợ sinh viên học phần Cơ sở dữ liệu (IT004) – Trường Đại học Công nghệ Thông tin, ĐHQG-HCM.*

---

<div align="center">

[![Tải Sổ tay Lý thuyết PDF](https://img.shields.io/badge/S%E1%BB%95_tay_L%C3%BD_thuy%E1%BA%BFt-64_Trang_A4-0284c7?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](dist/IT004_CSDL_UIT_LyThuyet_VoTrongPhuc.pdf)
[![Tải Sổ tay Thực hành PDF](https://img.shields.io/badge/S%E1%BB%95_tay_Th%E1%BB%B1c_h%C3%A0nh-71_Trang_A4-0f766e?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](dist/IT004_CSDL_UIT_ThucHanh_VoTrongPhuc.pdf)
[![Đọc Knowledge Garden](https://img.shields.io/badge/Knowledge_Garden-Tr%E1%BB%B1c_Tuy%E1%BA%BFn-059669?style=for-the-badge&logo=obsidian&logoColor=white)](https://phuchello.github.io/CSDL_UIT/)
[![Hướng dẫn Biên dịch](https://img.shields.io/badge/H%C6%B0%E1%BB%9Bng_d%E1%BA%ABn-Bi%C3%AAn_d%E1%BB%8Bch_ngu%E1%BB%93n-475569?style=for-the-badge&logo=markdown&logoColor=white)](docs/BUILD.md)

<br>

[![CI Validation](https://github.com/Phuchello/CSDL_UIT/actions/workflows/validate.yml/badge.svg)](https://github.com/Phuchello/CSDL_UIT/actions/workflows/validate.yml)
[![GitHub Pages](https://github.com/Phuchello/CSDL_UIT/actions/workflows/pages.yml/badge.svg)](https://phuchello.github.io/CSDL_UIT/)

</div>

---

## Ba Trụ Cột Ấn Bản v1.1

Phiên bản v1.1 hoàn thiện cấu trúc sản phẩm thành ba thành phần học thuật độc lập nhưng liên kết chặt chẽ:

```
                               CSDL_UIT (v1.1)
                 ┌────────────────────┼────────────────────┐
                 ▼                    ▼                    ▼
        Sổ tay Lý thuyết     Sổ tay Thực hành      Knowledge Garden
         (64 trang A4)        (71 trang A4)         (Quartz Web v5)
        ────────────────     ────────────────      ─────────────────
        • Mô hình ER         • SQL Server / SSMS   • 57 ghi chú số hóa
        • ĐSQH & Phép chia   • DDL, DML, Labs 01-04 • Đồ thị tri thức (Graph)
        • RBTV 7 nhóm IT004  • Correlated & All    • Tra cứu lỗi & mẹo thi
        • PTH & Dạng chuẩn   • Trigger đa dòng     • Liên kết hai chiều
        • In ấn định dạng A4 • Chẩn đoán 12 lỗi    • Tối ưu đa thiết bị
```

### 1. Sổ tay Lý thuyết (Theory Handbook — 64 trang A4)
- **Thiết kế ấn bản**: Phong cách editorial chuẩn mực, kiểu chữ Georgia, bảng màu nhã nhặn (Navy/Teal/Ochre), loại bỏ hoàn toàn các biểu tượng cảm xúc và ngôn từ phóng đại.
- **Nền tảng & ĐSQH**: Mô hình quan hệ, các phép toán thuần $(\sigma, \pi, \rho, \times, \cup, \cap, -, \div)$ và mở rộng; định lý phép chia tập rỗng $R \div \emptyset = \pi_X(R)$.
- **Ràng buộc toàn vẹn (RBTV)**: Hệ thống hóa 7 nhóm phân loại chuẩn IT004 (`LOC-LEC-LONG-CH05`), kỹ thuật lập Bảng tầm ảnh hưởng với ký hiệu chuẩn xác `+`, `-`, `+(Thuộc tính)`.
- **Chuẩn hóa dữ liệu**: Hệ tiên đề Armstrong, thuật toán bao đóng $X^+$, tìm khóa ứng viên, phủ tối thiểu $F_c$, kiểm tra 1NF $\rightarrow$ 2NF $\rightarrow$ 3NF $\rightarrow$ BCNF và thuật toán phân rã bảo toàn.

### 2. Sổ tay Thực hành (Practical Handbook — 71 trang A4)
- **Hệ thống bài Lab chuẩn tắc**: Labs 01–04 bám sát tiến trình đào tạo thực hành SQL Server tại UIT.
- **Bộ Fixture huấn luyện (`practice/sql/`)**: 9 bảng `tr_*` chuẩn hóa với dữ liệu mẫu xác định, hỗ trợ chu trình reset tự động và kiểm thử độc lập.
- **Truy vấn nâng cao & Bài toán "Tất cả"**: Phân tích 3 bước chuyển dịch từ ngôn ngữ tự nhiên sang Double `NOT EXISTS` và giải pháp thay thế `COUNT(DISTINCT)`.
- **Ràng buộc toàn vẹn & Trigger T-SQL**: Phân biệt tường minh giữa tầng khai báo DDL (`NOT NULL` báo lỗi 515, Foreign Key `Msg 547` chặn trước `AFTER` trigger) và Trigger nghiệp vụ (`THROW 51001`, `51003`) an toàn trên tập dữ liệu đa dòng (statement-level).
- **Cẩm nang Debugging hệ thống**: Quy trình 5 bước chẩn đoán và khắc phục 12 mã lỗi thực hành T-SQL phổ biến (`Msg 208, 207, 547, 2627, 8115, 8152, 8120, 512, 245, 241/242...`).

### 3. Quartz Knowledge Garden (Vườn Tri thức Kỹ thuật số)
- **Địa chỉ trực tuyến**: [https://phuchello.github.io/CSDL_UIT/](https://phuchello.github.io/CSDL_UIT/)
- **Cấu trúc mạng lưới**: 57 ghi chú nguyên tử kết nối qua hàng nghìn liên kết hai chiều (`[[wikilinks]]`), đồ thị tương tác toàn bộ môn học.
- **Trải nghiệm học tập**: Hỗ trợ tìm kiếm toàn văn tức thì, hiển thị công thức toán học KaTeX, khối mã lệnh T-SQL nổi bật, giao diện đáp ứng (responsive) mượt mà từ màn hình điện thoại (390px) đến máy tính bàn (1440px).

---

## Cấu trúc Kho lưu trữ (Project Structure)

```
CSDL_UIT/
├── book/                  # Mã nguồn HTML & CSS Sổ tay Lý thuyết (64 trang A4)
│   ├── chapters/          # Các chương nguồn (ch00 -> ch06, playbook, cheat sheet)
│   └── css/               # Động cơ dàn trang in ấn A4 (book.css, layout, components)
├── practice/              # Mã nguồn HTML & T-SQL Sổ tay Thực hành (71 trang A4)
│   ├── chapters/          # Các chương nguồn thực hành (00 -> 14, Labs 01-04, Debugging)
│   ├── sql/               # Bộ Fixture T-SQL chuẩn tắc (01_schema -> 06_test_cases, reset.sql)
│   └── EXAMPLE_REGISTRY.md# Khế ước đối chiếu giữa mã bài tập và script SQL
├── garden/                # Mã nguồn Quartz v5 Knowledge Garden
│   ├── content/           # 57 ghi chú Markdown nguyên tử (theory, practice, errors, sources)
│   └── quartz.config.yaml # Cấu hình giao diện, plugin và đồ thị tri thức
├── dist/                  # Tệp PDF ấn bản chính thức v1.1
│   ├── IT004_CSDL_UIT_LyThuyet_VoTrongPhuc.pdf  # Ấn bản Lý thuyết (64 trang A4)
│   ├── IT004_CSDL_UIT_ThucHanh_VoTrongPhuc.pdf  # Ấn bản Thực hành (71 trang A4)
│   └── IT004_CSDL_UIT_CamNang_VoTrongPhuc.pdf   # [Lịch sử v1.0] Bản cẩm nang đơn tập 88 trang
├── research/              # Hồ sơ kiểm chứng thực tế Phase A
│   └── v1.1_phase_a/      # 31 hiện vật đề thi, ledger nguồn học thuật & ma trận chuyên đề
├── scripts/               # Bộ công cụ build, kiểm thử tự động, linter & renderer
└── docs/                  # Tài liệu hướng dẫn biên dịch, phương pháp & bản đồ JIT
```

---

## Khởi động & Biên dịch nhanh (Quick Start)

### 1. Kiểm thử toàn vẹn kho lưu trữ (Validation Suite)
```bash
# Kiểm tra tĩnh 6 bước (HTML, schema, seed, trigger, provenance)
python scripts/validate.py

# Kiểm tra hợp đồng nội dung Knowledge Garden D2
python scripts/validate_garden_d2.py
```

### 2. Biên dịch & Vận hành Knowledge Garden (Quartz v5)
```bash
# Cài đặt thư viện phụ trợ (yêu cầu Node >= 22)
cd garden
npm ci

# Biên dịch trang tĩnh vào thư mục garden/public
node ./quartz/bootstrap-cli.mjs build -d content -o public

# Kiểm tra toàn bộ 2,800+ liên kết nội bộ
cd ..
python scripts/agent/check_links.py
```

### 3. Tái tạo các ấn bản HTML & PDF Handbooks
```bash
# Biên dịch Sổ tay Lý thuyết sang book/index.html
python scripts/build.py

# Biên dịch Sổ tay Thực hành sang practice/index.html
python scripts/build_practice.py
```
*Xem chi tiết quy trình xuất bản PDF và cấu hình CI tại [docs/BUILD.md](docs/BUILD.md).*

---

## Nguồn Tham chiếu & Tuyên bố Học thuật (Provenance)

Tài liệu được hệ thống hóa độc lập dựa trên các tài liệu học thuật và bằng chứng thực tế được khảo sát trong Phase A:

1. **Ngữ nghĩa T-SQL Kỹ thuật**: Tài liệu chuẩn Microsoft Learn T-SQL Documentation (`TECH-A01` đến `TECH-A11`).
2. **Phân loại RBTV & Cấu trúc môn học**: Giáo trình Cơ sở dữ liệu (Đồng Thị Bích Thủy, Phạm Thị Bạch Huệ, Nguyễn Trần Minh Thư - NXB KH&KT), bài giảng chính thức `LOC-LEC-LONG-CH05` (Khoa HTTT, Trường ĐH CNTT – ĐHQG-HCM).
3. **Cơ sở Lý thuyết Quốc tế**: Database System Concepts (7th Edition, Silberschatz, Korth, Sudarshan) và Fundamentals of Database Systems (7th Edition, Elmasri, Navathe).
4. **Hiện vật thực chứng đề thi**: 31 đề thi và bài tập thực hành lịch sử được chuẩn hóa trong [`research/v1.1_phase_a/artifact_registry.md`](research/v1.1_phase_a/artifact_registry.md). Các tài liệu chia sẻ từ cộng đồng sinh viên được gắn nhãn community mirror phục vụ kiểm chứng và không đại diện cho ấn bản chính thức của nhà trường.

> **Ghi chú về ấn bản lịch sử**: Tệp `dist/IT004_CSDL_UIT_CamNang_VoTrongPhuc.pdf` (88 trang) là ấn bản đơn tập ban đầu (v1.0.0), hiện được lưu trữ trong kho dữ liệu phục vụ mục đích đối chiếu lịch sử. Ấn bản phát hành chính thức từ v1.1.0 là bộ đôi Sổ tay Lý thuyết và Sổ tay Thực hành kèm Knowledge Garden.

---

## Tác giả & Bản quyền

- **Biên soạn & Hệ thống hóa:** Võ Trọng Phúc
- **Bản quyền nội dung:** © 2026 Võ Trọng Phúc. Toàn bộ quyền được bảo lưu theo quy định tại [NOTICE.md](NOTICE.md).
- **Mã nguồn Quartz:** Phát hành theo giấy phép MIT (jackyzha0 / Quartz Community).
- **Nhật ký cập nhật:** [CHANGELOG.md](CHANGELOG.md) | [CHANGELOG_AGENT.md](CHANGELOG_AGENT.md)
