---
title: RBTV và Bảng tầm ảnh hưởng
description: Ràng buộc toàn vẹn trong CSDL, phân loại 4 cấp độ, phương pháp lập Bảng tầm ảnh hưởng và chiến lược hiện thực hóa.
type: theory
topics: [integrity, constraints, impact-table, triggers]
related: [practice/multi-row-trigger, practice/lab-04, exam-patterns/rbtv-trigger, errors/scalar-trigger, errors/multi-row-trigger-failure]
provenance: verified-artifact
courseEvidence: [UIT-O06, LOC-LEC-LONG-CH05]
---
# RBTV và Bảng tầm ảnh hưởng (Impact Matrix)

Ràng buộc toàn vẹn (RBTV - Integrity Constraints) là tập hợp các quy tắc ngữ nghĩa áp đặt lên dữ liệu nhằm đảm bảo tính chính xác, nhất quán và phản ánh đúng hiện thực khách quan trong suốt vòng đời của cơ sở dữ liệu.

## 1. Định nghĩa hình thức

Một trạng thái cơ sở dữ liệu $s$ được gọi là **hợp lệ** nếu và chỉ nếu nó thỏa mãn toàn bộ tập các ràng buộc toàn vẹn $\mathcal{IC}$ được định nghĩa trên lược đồ:
$$\forall I \in \mathcal{IC}, s \models I$$

Khi người dùng thực hiện các thao tác thay đổi dữ liệu (`INSERT`, `UPDATE`, `DELETE`), hệ thống phải thẩm định xem trạng thái mới $s'$ có tiếp tục thỏa mãn $\mathcal{IC}$ hay không. Nếu có bất kỳ ràng buộc nào bị vi phạm, thao tác phải bị từ chối hoặc rollback để bảo toàn tính toàn vẹn (ACID).

## 2. Phân loại 4 cấp độ ràng buộc

1. **Ràng buộc miền giá trị (Domain Integrity):** Quy định kiểu dữ liệu, miền giá trị hợp lệ, điều kiện logic trên từng thuộc tính (`NOT NULL`, `CHECK (Tuoi >= 18)`).
2. **Ràng buộc thực thể (Entity Integrity):** Quy định mỗi bộ trong quan hệ phải được phân biệt duy nhất, khóa chính không được phép chứa giá trị NULL (`PRIMARY KEY`, `UNIQUE`).
3. **Ràng buộc tham chiếu (Referential Integrity):** Quy định khóa ngoại phải tham chiếu đến một giá trị khóa chính đang tồn tại hoặc nhận giá trị NULL (`FOREIGN KEY ... REFERENCES ...`).
4. **Ràng buộc ngữ nghĩa phức tạp (Complex Business Constraints):** Các quy tắc liên bộ hoặc liên quan hệ vượt quá khả năng biểu diễn của cơ chế khai báo (declarative DDL).

## 3. Quy trình phân tích Bảng tầm ảnh hưởng (Impact Matrix)

Khi xuất hiện một tân từ ngữ nghĩa liên quan hệ, kỹ sư CSDL bắt buộc phải lập **Bảng tầm ảnh hưởng** để xác định chính xác những thao tác DML nào trên bảng nào có nguy cơ phá vỡ ràng buộc.

### Các ký hiệu chuẩn trong bảng:
- Dấu `+`: Thao tác **chắc chắn có nguy cơ vi phạm** $\implies$ Bắt buộc phải cài đặt kiểm tra.
- Dấu `-`: Thao tác **không thể gây vi phạm** $\implies$ Bỏ qua, không kiểm tra để tối ưu hiệu năng.
- Dấu `*`: Thao tác **chỉ có nguy cơ vi phạm khi sửa đổi một số thuộc tính cụ thể** $\implies$ Kiểm tra có điều kiện với danh sách cột `*(A_1, A_2, ...)`.

### Ví dụ phân tích thực tế:
Tân từ: *"Trưởng bộ phận (`HeadEmployeeId`) của mỗi phòng ban phải là nhân viên thuộc chính phòng ban đó (`DeptId`), và không được xóa nhân viên đang đảm nhiệm chức vụ trưởng bộ phận."*

Lập bảng tầm ảnh hưởng trên hai quan hệ `tr_departments` và `tr_employees`:

| Quan hệ | Thêm (`INSERT`) | Xóa (`DELETE`) | Sửa (`UPDATE`) |
| :--- | :---: | :---: | :---: |
| `tr_departments` | `+` | `-` | `*(HeadEmployeeId, DeptId)` |
| `tr_employees` | `-` | `+` | `*(DeptId)` |

- **Giải thích:**
  - Thêm nhân viên mới (`INSERT tr_employees`): Nhân viên mới vào chưa làm trưởng bộ phận $\implies$ Không vi phạm (`-`).
  - Xóa nhân viên (`DELETE tr_employees`): Nếu xóa trúng người đang làm trưởng bộ phận $\implies$ Vi phạm (`+`).
  - Đổi phòng ban nhân viên (`UPDATE tr_employees`): Nếu trưởng bộ phận bị chuyển sang phòng khác $\implies$ Vi phạm (`*(DeptId)`). Các cập nhật khác (lương, họ tên) không ảnh hưởng.

## 4. Chiến lược hiện thực hóa và phân định trách nhiệm

1. **Ưu tiên khai báo (Declarative First):** Nếu ràng buộc có thể giải quyết bằng các câu lệnh DDL cơ bản (`CHECK`, `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`), luôn ưu tiên dùng DDL vì được tối ưu sâu ở nhân lưu trữ (storage engine).
2. **Cài đặt thủ tục khi cần thiết (Procedural Trigger):** Với các ràng buộc liên quan hệ phức tạp, cài đặt bằng DML Trigger an toàn đa dòng (xem [[practice/multi-row-trigger|Multi-row trigger]]).
3. **Phòng tránh lỗi sập logic:** Tuyệt đối không dùng biến vô hướng trong trigger (xem [[errors/scalar-trigger|Lỗi Trigger vô hướng]]) và đảm bảo trigger xử lý đúng toàn bộ batch dòng (xem [[errors/multi-row-trigger-failure|Sập trigger do batch đa dòng]]).

Thực hành lập trình trigger tại [[practice/lab-04|Lab 04 — RBTV và Trigger]] và tham khảo dạng bài tập thi tại [[exam-patterns/rbtv-trigger|Observed pattern — RBTV and trigger]].
