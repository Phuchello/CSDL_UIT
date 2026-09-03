---
title: "Phân rã bảo toàn thông tin nối (Lossless-Join Decomposition)"
description: Phân rã không mất thông tin, phòng ngừa bộ giả, định lý giao siêu khóa và tính bảo toàn phụ thuộc hàm.
type: theory
topics: [normalization, decomposition, lossless-join, dependency-preservation]
related: [theory/3nf, theory/bcnf, theory/functional-dependencies, theory/candidate-keys, exercises/normalization-exercise]
provenance: verified-artifact
courseEvidence: [UIT-O02, LOC-LEC-LONG-CH06]
---
# Phân rã bảo toàn thông tin nối (Lossless-Join Decomposition)

Khi thực hiện chuẩn hóa cơ sở dữ liệu lên các dạng chuẩn cao hơn ([[theory/3nf|3NF]], [[theory/bcnf|BCNF]]), ta phải phân rã (decompose) một lược đồ quan hệ lớn thành nhiều lược đồ quan hệ nhỏ hơn. Phép phân rã chỉ có giá trị thực tiễn nếu nó thỏa mãn tính chất **kết nối không mất thông tin (Lossless-join)** và lý tưởng nhất là **bảo toàn phụ thuộc hàm (Dependency Preservation)**.

## 1. Định nghĩa toán học hình thức

Cho lược đồ quan hệ $R(U)$ và tập phụ thuộc hàm $F$.
Một phép phân rã $\rho = \{R_1, R_2, \dots, R_k\}$ (với $R_1 \cup R_2 \cup \dots \cup R_k = U$) được gọi là **kết nối không mất thông tin (Lossless Join)** đối với $F$ nếu với mọi thể hiện hợp lệ $r$ của $R$ thỏa mãn $F$:

$$\pi_{R_1}(r) \bowtie \pi_{R_2}(r) \bowtie \dots \bowtie \pi_{R_k}(r) = r$$

- **Cảnh báo:** Phép nối tự nhiên của các bảng con luôn chứa $r$ ($\pi_{R_1}(r) \bowtie \dots \bowtie \pi_{R_k}(r) \supseteq r$). Hiện tượng "mất thông tin" (lossy) không phải là mất dữ liệu, mà là **sinh ra các bộ giả mạo sai lệch (spurious tuples)** khiến ta không thể khôi phục lại chính xác trạng thái dữ liệu ban đầu.

## 2. Nguy cơ sinh ra bộ giả (Spurious Tuples)

Xét quan hệ: $R(\text{NhanVien}, \text{ChiNhanh}, \text{DuAn})$
- Giả sử một nhân viên làm việc ở nhiều chi nhánh và tham gia nhiều dự án độc lập.
- Nếu ta tách sai thành $R_1(\text{NhanVien}, \text{ChiNhanh})$ và $R_2(\text{ChiNhanh}, \text{DuAn})$:
  - Khi thực hiện phép kết tự nhiên $R_1 \bowtie R_2$ trên thuộc tính chung $\text{ChiNhanh}$, hệ thống sẽ ghép mọi nhân viên của chi nhánh với mọi dự án thuộc chi nhánh đó.
  - Kết quả sinh ra các bộ dữ liệu ghi nhận nhân viên tham gia các dự án mà trên thực tế họ không hề làm $\implies$ **Bộ giả mạo (Spurious Tuples)**.

## 3. Định lý giao siêu khóa cho phép phân rã 2 quan hệ

Trường hợp phân rã lược đồ $R$ thành hai lược đồ con $\rho = \{R_1, R_2\}$, có một định lý toán học đơn giản để kiểm tra tính không mất thông tin:

Phép phân rã $\rho = \{R_1, R_2\}$ là **kết nối không mất thông tin** đối với $F$ nếu và chỉ nếu phần giao của hai lược đồ chứa một [[theory/candidate-keys|siêu khóa]] của ít nhất một trong hai lược đồ:

$$(R_1 \cap R_2) \rightarrow R_1 \in F^+ \quad \text{HOẶC} \quad (R_1 \cap R_2) \rightarrow R_2 \in F^+$$

- **Nói cách khác:** Thuộc tính chung giữa hai bảng con phải là một khóa (khóa chính hoặc khóa ứng viên) của bảng $R_1$ hoặc bảng $R_2$. Điều này tương đương với mô hình Khóa ngoại tham chiếu Khóa chính trong thiết kế CSDL thực tế.

## 4. Tính bảo toàn phụ thuộc hàm (Dependency Preservation)

Bên cạnh tính không mất thông tin, một phép phân rã $\rho = \{R_1, \dots, R_k\}$ được gọi là **bảo toàn phụ thuộc hàm** nếu:

$$\Big( \bigcup_{i=1}^k \pi_{R_i}(F) \Big)^+ = F^+$$

- **Ý nghĩa thực tiễn:** Mọi ràng buộc phụ thuộc hàm ban đầu đều có thể được kiểm tra độc lập trên từng bảng con mà không cần phải thực hiện phép nối (JOIN) nhiều bảng lại với nhau.
- **Quy tắc thiết kế:**
  - Chuẩn hóa lên [[theory/3nf|3NF]] luôn luôn đạt được đồng thời: vừa **Lossless-join**, vừa **Bảo toàn phụ thuộc hàm 100%**.
  - Chuẩn hóa lên [[theory/bcnf|BCNF]] luôn đạt được **Lossless-join**, nhưng có thể làm **mất phụ thuộc hàm**.

Xem chi tiết điều kiện kiểm tra tại [[theory/3nf|Dạng chuẩn 3 (3NF)]], thuật toán phân rã tại [[theory/bcnf|BCNF]], cách tìm siêu khóa tại [[theory/candidate-keys|Khóa ứng viên]], và bài tập worked example tại [[exercises/normalization-exercise|Bài tập chuẩn hóa]].
