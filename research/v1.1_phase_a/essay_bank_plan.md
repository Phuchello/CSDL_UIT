# Kế Hoạch Xây Dựng Ngân Hàng Câu Hỏi Tự Luận & Đề Thi (Tự Luận / Essay Bank Plan) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31
**Nguyên tắc:** Ngân hàng câu hỏi được tổ chức theo chuyên đề (Topic-First), phân loại nghiêm ngặt theo 3 lớp xuất xứ (`verified-artifact`, `reconstructed-exam-pattern`, `original-practice`), không sao chép nguyên văn văn bản có bản quyền mà sử dụng văn phong diễn đạt độc lập chuẩn học thuật. Cột `artifact_count` khớp chính xác với số lượng hiện vật đề thi duy nhất quan sát được.

---

## 1. Phân Loại Nguồn Gốc & Thẩm Quyền Câu Hỏi (Provenance Classes)

1. **`verified-artifact`**:
   - Câu hỏi dựa trên các hiện vật đề thi chính thức hoặc bài tập ôn tập có định danh rõ ràng (`EXAM-2024-2025-HK1-MID-01`, `EXAM-2024-2025-HK1-FINAL-01`, `EXAM-2023-2024-HK1-MID-D1`, `EXAM-2023-2024-HK1-MID-D2`, `EXAM-2023-2024-HK1-FINAL-01`, `EXAM-2022-2023-HK1-FINAL-01`, `EXAM-2021-2022-HK1-FINAL-01`, `EXAM-2018-2019-HK1-FINAL-01`, v.v.).
   - Lưu trữ dưới dạng tóm lược cấu trúc, ma trận kiến thức và phân tích hướng giải.

2. **`reconstructed-exam-pattern`**:
   - Câu hỏi được biên soạn lại độc lập (independently written paraphrase) mô phỏng chính xác cấu trúc ngữ cảnh, phong cách ra đề và chuẩn đầu ra của các đề thi UIT thực tế.

3. **`original-practice`**:
   - Câu hỏi được tác giả biên soạn mới hoàn toàn nhằm phủ kín các góc kiến thức lý thuyết hình thức, các trường hợp biên và các bẫy trừ điểm kinh điển.

---

## 2. Kế Hoạch Phân Bổ Câu Hỏi Theo Chuyên Đề (Topic-First Distribution Plan)

| Chuyên đề / Chương | Nội dung trọng tâm | Artifact Count thực chứng | Năm học quan sát | Source IDs liên kết | Số câu hỏi đề xuất | Độ ưu tiên |
| :--- | :--- | :---: | :---: | :--- | :---: | :---: |
| **Ch1: Tổng quan CSDL** | • File System vs DBMS<br>• Kiến trúc 3 mức ANSI/SPARC<br>• Độc lập dữ liệu logic & vật lý | **3** | 2020–2021, 2023–2024, 2024–2025 | `LOC-LEC-AN-CH01`, `LOC-LEC-LONG-CH01`, `UIT-O01` | **6 câu**<br>(2 reconstructed + 4 original) | **Cao** |
| **Ch2: Mô hình ER & Quan hệ** | • Thiết kế ERD (Entity, Relationship, Min-Max)<br>• Ánh xạ ER $\rightarrow$ Lược đồ quan hệ (1:1, 1:N, M:N, Is-a)<br>• Xác định Superkey, Candidate Key, PK, FK | **5** | 2017–2018, 2023–2024, 2024–2025 | `LOC-EXAM-2023-2024-MID-D1`, `LOC-EXAM-2023-2024-MID-D2`, `LOC-HW-23520266-5`, `LOC-REV-2024-10-01` | **10 câu**<br>(6 reconstructed + 4 original) | **Rất cao** |
| **Ch3: Đại số quan hệ** | • Phép toán cơ bản ($\sigma, \pi, \rho, \bowtie, \times$)<br>• Phép tập hợp ($\cup, \cap, -$)<br>• Phép kết ngoài (Outer Join)<br>• Phép chia $\div$ (Bài toán "Tất cả")<br>• Gom nhóm $\Im$ & hàm kết hợp | **10** | 2017–2018, 2018–2019, 2019–2020, 2022–2023, 2023–2024, 2024–2025 | `LOC-EXAM-2023-2024-MID-D1`, `LOC-EXAM-2023-2024-MID-D2`, `LOC-HW-23520266-5`, `LOC-LEC-LONG-CH03` | **16 câu**<br>(10 reconstructed + 6 original) | **Rất cao** |
| **Ch4: SQL Server / T-SQL** | • Lệnh DDL, DML, `UPDATE` có tính toán<br>• Kỹ thuật `JOIN`, `SELF JOIN`, Subquery<br>• Xử lý giá trị `NULL`<br>• Phép chia Double `NOT EXISTS` vs `GROUP BY / HAVING` | **27** | 2013–2014, 2017–2018, 2018–2019, 2019–2020, 2020–2021, 2021–2022, 2022–2023, 2023–2024, 2024–2025 | `LOC-EXAM-2023-2024-MID-D1`, `LOC-HW-23520266-5`, `LOC-SQL-LAB01` đến `LAB04`, `TECH-A01`, `TECH-A02`, `TECH-A07`, `TECH-A08`, `COM-C11`, `COM-C12`, `COM-C17`, `COM-C18` | **14 câu**<br>(8 reconstructed + 6 original) | **Rất cao** |
| **Ch5: Ràng buộc toàn vẹn** | • Phát biểu tân từ hình thức<br>• Lập Bảng tầm ảnh hưởng 3 thao tác<br>• Phân loại 7 dạng RBTV (Miền giá trị, Liên thuộc tính, Liên bộ, Tham chiếu, Tổng hợp, Chu trình)<br>• Cài đặt Trigger T-SQL an toàn đa dòng | **17** | 2013–2014, 2018–2019, 2019–2020, 2020–2021, 2021–2022, 2022–2023, 2023–2024, 2024–2025 | `LOC-LEC-LONG-CH05`, `LOC-HW-23520266-5`, `TECH-A03`, `TECH-A04`, `TECH-A05`, `TECH-A06`, `COM-C11`, `COM-C12`, `COM-C17`, `COM-C18` | **10 câu**<br>(6 reconstructed + 4 original) | **Rất cao** |
| **Ch6: PTH & Chuẩn hóa** | • Chứng minh PTH bằng Tiên đề Armstrong<br>• Thuật toán tính bao đóng $X^+$, bài toán thành viên<br>• Tìm tất cả khóa ứng viên (tập nguồn $Ng$, trung gian $Tg$, treo $Tr$)<br>• Tìm phủ tối thiểu $F_c$<br>• Kiểm tra dạng chuẩn cao nhất (1NF $\rightarrow$ BCNF)<br>• Phân rã bảo toàn PTH & Lossless Join | **7** | 2018–2019, 2019–2020, 2020–2021, 2021–2022, 2022–2023, 2023–2024, 2024–2025 | `LOC-LEC-LONG-CH06`, `COM-C02`, `LOC-NOTE-NHAP` | **14 câu**<br>(8 reconstructed + 6 original) | **Rất cao** |
| **Đề thi Tổng hợp (Full Exams)** | Đề thi hoàn chỉnh 75–90 phút kết hợp ERD $\rightarrow$ ĐSQH $\rightarrow$ SQL $\rightarrow$ RBTV $\rightarrow$ Chuẩn hóa | **17** | 2017–2025 | Các Canonical Exam Artifacts (`EXAM-*`) | **6 bộ đề**<br>(4 reconstructed + 2 original) | **Rất cao** |

Các `artifact_count` trên được tính lại từ canonical registry sau khi bổ sung 4 practical artifacts mới; bốn direct leads chưa đủ header để promote không làm tăng count.

---

## 3. Cấu Trúc Siêu Dữ Liệu Chuẩn Cho Mỗi Trang Câu Hỏi (Question Page Metadata)

```yaml
title: "Phân tích Ràng buộc Toàn vẹn và Bảng tầm ảnh hưởng Quản lý Bán hàng"
artifact_id: "EXAM-2023-2024-HK1-MID-D1"
provenance: "reconstructed-exam-pattern" # verified-artifact | reconstructed-exam-pattern | original-practice
academic_year: "2023-2024"
semester: "HK1"
exam_type: "midterm" # midterm | final | practical | review
source_ids: ["LOC-EXAM-2023-2024-MID-D1", "LOC-LEC-LONG-CH05", "TECH-A04"]
topics: ["integrity-constraints", "impact-table", "triggers"]
difficulty: "medium-high" # easy | medium | medium-high | hard
schema: "CuaHangHoa"
```
