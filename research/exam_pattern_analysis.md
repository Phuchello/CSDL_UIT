# Exam Pattern Analysis – IT004 CSDL UIT

> Pattern quan sát từ tập đề hiện có và thông tin thu thập được.
> Số lượng đề mẫu hạn chế — các pattern dưới đây mang tính tham khảo.

## Cấu trúc đánh giá

| Thành phần | Tỷ lệ | Hình thức |
|---|---|---|
| Quá trình | 10% | Điểm danh, bài tập |
| Thực hành | 20-30% | Lab SQL Server |
| Giữa kỳ | 20-30% | Tự luận 60-90 phút |
| Cuối kỳ | 40-50% | Tự luận LT + Thi máy TH |

## Thi Giữa kỳ

| Dạng | Chủ đề | Tần suất | Độ khó | Bẫy | Kỹ năng |
|---|---|---|---|---|---|
| Vẽ ER Diagram | Ch.2 - ER | Rất cao | TB-Khó | Cardinality sai, nhầm entity/attribute | Phân tích đề, gạch danh từ/động từ |
| Ánh xạ ER → Schema | Ch.2 - Mapping | Rất cao | TB | M:N thiếu bảng trung gian, FK sai | Quy tắc ánh xạ 1:1, 1:N, M:N |
| Biểu thức ĐSQH | Ch.3 - RA | Rất cao | TB-Khó | Division sai divisor, projection sớm | Dịch tiếng Việt → phép toán |
| SQL DDL/DML | Ch.4 - SQL | Cao | Dễ-TB | Syntax errors, thiếu constraint | CREATE TABLE, INSERT |
| SQL SELECT | Ch.4 - SQL | Cao | TB | JOIN sai, GROUP BY thiếu | SELECT, JOIN, GROUP BY |

## Thi Cuối kỳ (Lý thuyết)

| Dạng | Chủ đề | Tần suất | Độ khó | Bẫy | Kỹ năng |
|---|---|---|---|---|---|
| Bao đóng X⁺ | Ch.6 - FD | Rất cao | TB | Dừng closure quá sớm | Thuật toán closure |
| Tìm candidate key | Ch.6 - Key | Rất cao | TB-Khó | Bỏ sót key, nhầm superkey | Phân tích LHS/RHS |
| Phủ tối thiểu | Ch.6 - FD | Rất cao | Khó | Loại sai FD, loại sai attr | 3 bước: tách, loại attr, loại FD |
| Xác định dạng chuẩn | Ch.6 - NF | Rất cao | TB-Khó | Nhầm 3NF/BCNF, nhầm partial dep | Decision tree |
| Bảng tầm ảnh hưởng | Ch.5 - RBTV | Rất cao | TB | Thiếu thao tác, sai ký hiệu | Phân tích +/-/+(A) |
| ĐSQH nâng cao | Ch.3 - RA | Cao | Khó | Division, aggregation | Tất cả phép toán |
| SQL nâng cao | Ch.4 - SQL | Cao | TB-Khó | NOT EXISTS, HAVING | Subquery, GROUP BY |

## Thi Cuối kỳ (Thực hành)

| Dạng | Chủ đề | Tần suất | Độ khó | Bẫy | Kỹ năng |
|---|---|---|---|---|---|
| Tạo bảng + FK | DDL | Cao | Dễ | Syntax FK, data type | CREATE TABLE, ALTER TABLE |
| Truy vấn phức tạp | DQL | Rất cao | TB-Khó | JOIN duplicate, NULL trap | SELECT, JOIN, GROUP BY |
| Stored Procedure | SP | Cao | TB | Tham số, logic | CREATE PROCEDURE |
| Trigger | Trigger | Cao | Khó | Inserted/Deleted tables, logic | CREATE TRIGGER |

## Dạng bài phổ biến trong đề UIT

### ER (Giữa kỳ)
- **Quản lý chung cư:** Hộ dân, Căn hộ, Block, Dịch vụ
- **Quản lý trường học:** Sinh viên, Lớp, Môn học, Giảng viên
- **Quản lý bán hàng:** Khách hàng, Sản phẩm, Đơn hàng
- **Đăng ký:** Đăng ký sự kiện, Đăng ký môn
- **Thiết bị:** Quản lý mượn/trả thiết bị
- **Vận động viên:** Cuộc thi, Đội, Thành tích

### ĐSQH & SQL (Giữa kỳ + Cuối kỳ)
- Liệt kê thông tin (selection + projection)
- Tìm ai đã làm gì (join)
- Tìm ai CHƯA TỪNG (difference / NOT EXISTS)
- Tìm ai đã làm TẤT CẢ (division / double NOT EXISTS)
- Đếm, tính trung bình, tìm max/min (aggregation)
- So sánh (having, >= ALL)

### PTH/Chuẩn hóa (Cuối kỳ)
- Cho R(A,B,C,D,E) và tập F, tìm:
  1. Bao đóng {A,B}⁺
  2. Candidate key
  3. Phủ tối thiểu
  4. Dạng chuẩn cao nhất
