---
title: RBTV và Bảng tầm ảnh hưởng
description: 7 phân loại RBTV chuẩn tắc IT004, phương pháp lập Bảng tầm ảnh hưởng với ký hiệu +, -, +(Thuộc tính) và chiến lược hiện thực hóa.
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

## 2. Hệ thống 7 phân loại RBTV chuẩn tắc trong giáo trình IT004

Trong học phần IT004, các ràng buộc toàn vẹn được phân loại một cách chặt chẽ dựa trên tầm vực và bản chất ngữ nghĩa thành 7 nhóm:

1. **Ràng buộc miền giá trị (Domain Constraint):** Quy định kiểu dữ liệu, miền giá trị hợp lệ hoặc điều kiện logic trên từng thuộc tính đơn lẻ (`CHECK`, `NOT NULL`).
2. **Ràng buộc khóa (Key Constraint):** Đảm bảo tính duy nhất của các bộ dữ liệu trong quan hệ, không thể có hai dòng trùng nhau trên tập khóa (`PRIMARY KEY`, `UNIQUE`).
3. **Ràng buộc toàn vẹn thực thể (Entity Integrity):** Quy tắc bất di bất dịch yêu cầu các thuộc tính thuộc khóa chính không bao giờ được phép mang giá trị rỗng (`NULL`).
4. **Ràng buộc toàn vẹn tham chiếu (Referential Integrity):** Quy định khóa ngoại trong bảng con phải tồn tại trong khóa chính bảng cha tương ứng hoặc nhận giá trị `NULL` (`FOREIGN KEY ... REFERENCES ...`).
5. **Ràng buộc liên thuộc tính (Inter-attribute Constraint):** Ràng buộc giữa các thuộc tính khác nhau trong **cùng một dòng (bộ)** của một bảng (ví dụ: ngày sinh phải nhỏ hơn ngày vào làm: `NGSINH < NGVL`).
6. **Ràng buộc liên bộ (Inter-tuple Constraint):** Ràng buộc giữa các **dòng (bộ) khác nhau** trong cùng một bảng (ví dụ: trong cùng một khoa, không thể có hai giảng viên có cùng học vị và học hàm).
7. **Ràng buộc liên quan hệ (Multi-relation Constraint):** Các ràng buộc nghiệp vụ phức tạp trải dài trên **nhiều bảng khác nhau** (ví dụ: trưởng bộ phận của một phòng ban phải là nhân viên thuộc chính phòng ban đó).

## 3. Phương pháp phân tích Bảng tầm ảnh hưởng trong IT004

Trong phương pháp luận thiết kế và phân tích CSDL của học phần IT004, **Bảng tầm ảnh hưởng** là công cụ phân tích chuẩn mực giúp sinh viên và kỹ sư CSDL xác định một cách khoa học những thao tác DML nào trên bảng nào có nguy cơ làm vi phạm ràng buộc toàn vẹn, từ đó xác định chính xác thời điểm và phạm vi cần lập trình kiểm tra.

### Ký hiệu chuẩn mực trong Bảng tầm ảnh hưởng IT004:
- **`+`** : Thao tác **có khả năng làm vi phạm** RBTV $\implies$ Bắt buộc phải kiểm tra (hoặc viết trigger).
- **`-`** : Thao tác **không thể làm trạng thái đang hợp lệ trở thành vi phạm** $\implies$ Không cần kiểm tra.
- **`+(Thuộc tính)`** : Thao tác Sửa (`UPDATE`) **chỉ có khả năng gây vi phạm khi sửa đổi trên các thuộc tính chỉ định** $\implies$ Kiểm tra có điều kiện với danh sách cột (ví dụ: `+(HeadEmployeeId, DeptId)`).

### Ví dụ phân tích thực tế:
Tân từ: *"Trưởng bộ phận (`HeadEmployeeId`) của mỗi phòng ban phải là nhân viên thuộc chính phòng ban đó (`DeptId`), và không được xóa nhân viên đang đảm nhiệm chức vụ trưởng bộ phận."*

Lập bảng tầm ảnh hưởng chuẩn tắc IT004 trên hai quan hệ `tr_departments` và `tr_employees`:

| Quan hệ | Thêm (`INSERT`) | Xóa (`DELETE`) | Sửa (`UPDATE`) |
| :--- | :---: | :---: | :---: |
| `tr_departments` | `+` | `-` | `+(HeadEmployeeId, DeptId)` |
| `tr_employees` | `-` | `+` | `+(DeptId)` |

- **Giải thích từng ô:**
  - `INSERT tr_departments (+)`: Thêm một phòng ban mới có thể gán mã trưởng phòng là một nhân viên thuộc phòng ban khác $\implies$ Có nguy cơ vi phạm.
  - `DELETE tr_departments (-)`: Xóa một phòng ban không làm cho trưởng phòng của các phòng ban còn lại bị sai lệch $\implies$ Không thể vi phạm.
  - `UPDATE tr_departments (+(HeadEmployeeId, DeptId))`: Sửa mã trưởng phòng hoặc mã phòng ban có thể làm mất tính nhất quán $\implies$ Cần kiểm tra.
  - `INSERT tr_employees (-)`: Thêm nhân viên mới không làm thay đổi thông tin của các trưởng phòng hiện hữu $\implies$ Không thể vi phạm.
  - `DELETE tr_employees (+)`: Nếu xóa trúng người đang đảm nhiệm chức vụ trưởng bộ phận $\implies$ Vi phạm ràng buộc không được xóa trưởng phòng.
  - `UPDATE tr_employees (+(DeptId))`: Chỉ khi chuyển phòng ban (`DeptId`) của nhân viên, nếu nhân viên đó đang là trưởng bộ phận mà bị chuyển sang phòng ban khác thì mới gây vi phạm $\implies$ Ký hiệu `+(DeptId)`. Các thao tác sửa lương (`Salary`) hay họ tên (`FullName`) hoàn toàn không ảnh hưởng.

## 4. Chiến lược hiện thực hóa và phân định trách nhiệm

1. **Ưu tiên khai báo (Declarative First):** Nếu ràng buộc thuộc 4 nhóm đầu (miền giá trị, khóa, thực thể, tham chiếu), luôn ưu tiên dùng DDL (`CHECK`, `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`) vì được tối ưu sâu ở nhân lưu trữ (storage engine).
2. **Cài đặt thủ tục khi cần thiết (Procedural Trigger):** Với các ràng buộc liên quan hệ hoặc liên bộ phức tạp, cài đặt bằng DML Trigger an toàn đa dòng (xem [[practice/multi-row-trigger|Multi-row trigger]]).
3. **Phòng tránh lỗi sập logic:** Tuyệt đối không dùng biến vô hướng trong trigger (xem [[errors/scalar-trigger|Lỗi Trigger vô hướng]]) và đảm bảo trigger xử lý đúng toàn bộ batch dòng (xem [[errors/multi-row-trigger-failure|Sập trigger do batch đa dòng]]).

Thực hành lập trình trigger tại [[practice/lab-04|Lab 04 — RBTV và Trigger]] và tham khảo dạng bài tập thi tại [[exam-patterns/rbtv-trigger|Observed pattern — RBTV and trigger]].
