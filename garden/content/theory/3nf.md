---
title: "Dạng chuẩn 3 (Third Normal Form - 3NF)"
description: Định nghĩa hình thức 3NF, điều kiện cứu vãn thuộc tính khóa, phụ thuộc bắc cầu và tính bảo toàn phụ thuộc hàm.
type: theory
topics: [3nf, normalization, functional-dependency, candidate-keys]
related: [theory/bcnf, theory/candidate-keys, theory/closure, theory/lossless-decomposition, exercises/normalization-exercise]
provenance: verified-artifact
courseEvidence: [UIT-O02, LOC-LEC-LONG-CH06]
---
# Dạng chuẩn 3 (Third Normal Form - 3NF)

Dạng chuẩn 3 (3NF) do E.F. Codd đề xuất (1971) và được hoàn thiện bởi Zaniolo (1982) là chuẩn thiết kế cân bằng hoàn hảo trong thực tế: loại bỏ hầu hết các bất thường cập nhật (anomalies) trong khi luôn đảm bảo tồn tại phép tách đồng thời vừa bảo toàn phụ thuộc hàm vừa bảo toàn thông tin (lossless join).

## 1. Định nghĩa toán học hình thức

Cho lược đồ quan hệ $R(U)$ và tập phụ thuộc hàm $F$.
Lược đồ $R$ đạt **Dạng chuẩn 3 (3NF)** nếu và chỉ nếu với mọi phụ thuộc hàm không tầm thường $X \rightarrow A \in F^+$ (với $A \notin X$), ít nhất một trong hai điều kiện sau được thỏa mãn:

1. **$X$ là một siêu khóa (superkey) của $R$** ($X^+ = U$), HOẶC
2. **$A$ là một thuộc tính khóa (prime attribute)** của $R$.

- **Thuộc tính khóa (Prime Attribute):** Là thuộc tính xuất hiện trong **ít nhất một** [[theory/candidate-keys|khóa ứng viên (candidate key)]] của $R$.
- **Thuộc tính không khóa (Non-prime Attribute):** Là thuộc tính không thuộc bất kỳ khóa ứng viên nào của $R$.

## 2. Điều kiện cứu vãn (Prime Attribute Saving Clause)

Điểm khác biệt cốt tử giữa 3NF và [[theory/bcnf|BCNF]] chính là điều kiện thứ hai: *"HOẶC $A$ là thuộc tính khóa"*.
- Nếu $X$ không phải là siêu khóa, nhưng $A$ may mắn là thuộc tính nằm trong một khóa ứng viên nào đó của quan hệ, thì phụ thuộc hàm $X \rightarrow A$ **được phép tồn tại** mà không làm vi phạm dạng chuẩn 3.
- Điều kiện cứu vãn này cho phép giữ lại các ràng buộc toàn vẹn quan trọng mà không buộc phải phân rã bảng làm mất liên kết kiểm tra phụ thuộc hàm.

## 3. Phụ thuộc bắc cầu (Transitive Dependency) và Bất thường dữ liệu

Nếu một lược đồ vi phạm 3NF, điều đó có nghĩa là tồn tại một thuộc tính không khóa phụ thuộc bắc cầu vào khóa chính thông qua một thuộc tính không khóa khác:
$$\text{Khóa} \rightarrow Y \quad \text{và} \quad Y \rightarrow A \quad (Y \text{ không là siêu khóa, } A \text{ không là thuộc tính khóa})$$

### Ví dụ bất thường dữ liệu:
Xét quan hệ sinh viên: $R(\text{MSSV}, \text{HoTen}, \text{MaKhoa}, \text{TenKhoa})$ với khóa chính duy nhất là $\text{MSSV}$:
- Ta có các phụ thuộc hàm: $\text{MSSV} \rightarrow \text{MaKhoa}$ và $\text{MaKhoa} \rightarrow \text{TenKhoa}$.
- Xét FD: $\text{MaKhoa} \rightarrow \text{TenKhoa}$:
  - $\text{MaKhoa}$ không phải là siêu khóa ($\text{MaKhoa}^+ = \{\text{MaKhoa}, \text{TenKhoa}\} \neq U$).
  - $\text{TenKhoa}$ không phải là thuộc tính khóa (khóa duy nhất là $\text{MSSV}$).
  - $\implies$ Vi phạm 3NF nghiêm trọng do phụ thuộc bắc cầu.
- **Hậu quả bất thường:**
  - Dư thừa dữ liệu: Tên khoa bị lặp lại cho mỗi sinh viên cùng khoa.
  - Bất thường cập nhật: Muốn đổi tên khoa phải sửa hàng ngàn dòng sinh viên.
  - Bất thường xóa: Xóa sinh viên cuối cùng của một khoa sẽ làm mất luôn thông tin tên khoa đó.

## 4. Thuật toán kiểm tra Dạng chuẩn 3 từng bước

1. **Bước 1:** Tìm tất cả các [[theory/candidate-keys|khóa ứng viên]] của lược đồ $R$.
2. **Bước 2:** Xác định tập tất cả các thuộc tính khóa $\mathcal{P} = \bigcup \{K_i \mid K_i \text{ là khóa ứng viên}\}$.
3. **Bước 3:** Xét từng phụ thuộc hàm $X \rightarrow A$ trong tập phụ thuộc hàm (hoặc sau khi tách vế phải thành thuộc tính đơn lẻ):
   - Kiểm tra xem $X$ có phải là siêu khóa không (tính $X^+$ qua [[theory/closure|thuật toán bao đóng]]). Nếu có $\implies$ Thỏa mãn.
   - Nếu $X$ không là siêu khóa, kiểm tra xem $A \in \mathcal{P}$ hay không. Nếu có $\implies$ Thỏa mãn.
   - Nếu cả hai điều kiện đều thất bại $\implies$ Kết luận quan hệ **không đạt 3NF**.

## 5. Đánh đổi lý thuyết: 3NF vs BCNF

| Tiêu chí | Dạng chuẩn 3 (3NF) | Dạng chuẩn Boyce-Codd (BCNF) |
| :--- | :---: | :---: |
| **Độ nghiêm ngặt** | Vừa phải (cho phép cứu vãn) | Rất cao ($X$ bắt buộc phải là siêu khóa) |
| **Bảo toàn thông tin (Lossless Join)** | Luôn đạt được | Luôn đạt được |
| **Bảo toàn phụ thuộc hàm** | **Luôn luôn bảo toàn được 100%** | **Có thể bị mất một số phụ thuộc hàm** |
| **Mức độ khử dư thừa** | Khử hầu hết dư thừa | Khử triệt để mọi dư thừa do FD |

Xem tiếp dạng chuẩn khắt khe hơn tại [[theory/bcnf|Dạng chuẩn Boyce-Codd (BCNF)]], lý thuyết phân rã không mất thông tin tại [[theory/lossless-decomposition|Phân rã bảo toàn]], và bài tập thực hành chi tiết tại [[exercises/normalization-exercise|Bài tập chuẩn hóa]].
