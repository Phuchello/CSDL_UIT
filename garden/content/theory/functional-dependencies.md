---
title: "Phụ thuộc hàm & Tiên đề Armstrong (Functional Dependencies)"
description: Định nghĩa hình thức của phụ thuộc hàm, hệ tiên đề Armstrong và các quy tắc dẫn xuất, ví dụ chứng minh hình thức.
type: theory
topics: [functional-dependency, armstrong, normalization]
related: [theory/closure, theory/candidate-keys, theory/minimal-cover, theory/3nf, theory/bcnf]
provenance: verified-artifact
courseEvidence: [UIT-O02, LOC-LEC-LONG-CH06]
---
# Phụ thuộc hàm & Tiên đề Armstrong (Functional Dependencies)

Phụ thuộc hàm (Functional Dependency - FD) là khái niệm trung tâm trong lý thuyết thiết kế cơ sở dữ liệu quan hệ, làm nền tảng toán học để xác định khóa, bao đóng và thực hiện chuẩn hóa dữ liệu (1NF đến BCNF).

## 1. Định nghĩa toán học hình thức

Cho lược đồ quan hệ $R(U)$ với tập thuộc tính $U$. Cho hai tập con thuộc tính $X, Y \subseteq U$.
Ta nói **$X$ xác định hàm $Y$** (hoặc **$Y$ phụ thuộc hàm vào $X$**), ký hiệu là:
$$X \rightarrow Y$$
nếu và chỉ nếu với mọi quan hệ $r$ hợp lệ trên lược đồ $R$, bất kỳ hai bộ dữ liệu $t_1, t_2 \in r$ nào có cùng giá trị trên $X$ thì cũng bắt buộc phải có cùng giá trị trên $Y$:

$$\forall t_1, t_2 \in r: t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]$$

- **Ý nghĩa trực quan:** Nếu ta biết trước giá trị của tập thuộc tính $X$, ta có thể suy ra duy nhất một giá trị tương ứng của tập thuộc tính $Y$.
- **Ví dụ kinh điển:** Trong quản lý sinh viên: $\text{MSSV} \rightarrow \text{HoTen}$ (mỗi mã sinh viên chỉ có một họ tên duy nhất). Nhưng $\text{HoTen} \rightarrow \text{MSSV}$ không đúng vì có thể có hai sinh viên trùng họ tên.

## 2. Phân loại phụ thuộc hàm

1. **Phụ thuộc hàm tầm thường (Trivial FD):**
   - Định nghĩa: $X \rightarrow Y$ là tầm thường nếu $Y \subseteq X$.
   - Ví dụ: $AB \rightarrow A$, $ABC \rightarrow BC$.
   - Đặc điểm: Luôn đúng trên mọi quan hệ mà không cần kiểm tra dữ liệu thực tế.
2. **Phụ thuộc hàm không tầm thường (Non-trivial FD):**
   - Định nghĩa: $X \rightarrow Y$ là không tầm thường nếu $Y \nsubseteq X$.
   - Đặc điểm: Mang thông tin ràng buộc nghiệp vụ thực tế.
3. **Phụ thuộc hàm hoàn toàn không tầm thường (Completely Non-trivial FD):**
   - Định nghĩa: $X \rightarrow Y$ nếu $X \cap Y = \emptyset$.
   - Ví dụ: $A \rightarrow BC$.

## 3. Hệ tiên đề Armstrong (Armstrong's Axioms)

W.W. Armstrong (1974) đã công bố 3 tiên đề nền tảng, chứng minh được tính đúng đắn (soundness - không sinh ra FD sai) và tính đầy đủ (completeness - sinh ra được mọi FD đúng):

1. **Luật phản xạ (Reflexivity):**
   $$\text{Nếu } Y \subseteq X \subseteq U \implies X \rightarrow Y$$
2. **Luật tăng trưởng (Augmentation):**
   $$\text{Nếu } X \rightarrow Y \implies XZ \rightarrow YZ \quad (\forall Z \subseteq U)$$
3. **Luật bắc cầu (Transitivity):**
   $$\text{Nếu } X \rightarrow Y \text{ và } Y \rightarrow Z \implies X \rightarrow Z$$

## 4. Ba quy tắc suy dẫn thứ cấp (Derived Rules)

Từ 3 tiên đề Armstrong cơ bản, ta suy dẫn ra 3 quy tắc thuận tiện cho tính toán:

1. **Quy tắc hợp (Union rule):**
   $$\text{Nếu } X \rightarrow Y \text{ và } X \rightarrow Z \implies X \rightarrow YZ$$
2. **Quy tắc phân rã (Decomposition rule):**
   $$\text{Nếu } X \rightarrow YZ \implies X \rightarrow Y \text{ và } X \rightarrow Z$$
3. **Quy tắc giả bắc cầu (Pseudotransitivity rule):**
   $$\text{Nếu } X \rightarrow Y \text{ và } WY \rightarrow Z \implies WX \rightarrow Z$$

## 5. Ví dụ chứng minh hình thức từng bước

Cho lược đồ $R(A, B, C, D)$ và tập phụ thuộc hàm $F = \{A \rightarrow B, B \rightarrow C, CD \rightarrow E\}$.
Chứng minh rằng: $AD \rightarrow E$.

- **Lời giải chuẩn tắc:**
  1. $A \rightarrow B$ (Giả thiết)
  2. $B \rightarrow C$ (Giả thiết)
  3. $A \rightarrow C$ (Bắc cầu từ 1 và 2)
  4. $AD \rightarrow CD$ (Tăng trưởng hai vế của 3 với thuộc tính $D$)
  5. $CD \rightarrow E$ (Giả thiết)
  6. $AD \rightarrow E$ (Bắc cầu từ 4 và 5) $\implies$ Điều phải chứng minh ($\blacksquare$).

Thay vì chứng minh bằng các phép biến đổi đại số dài dòng, ta có thể dùng thuật toán tính [[theory/closure|Bao đóng thuộc tính]] để kiểm tra $AD \rightarrow E$ trong thời gian đa thức.

Xem tiếp kỹ thuật tính bao đóng tại [[theory/closure|Bao đóng thuộc tính]], thuật toán tìm [[theory/candidate-keys|Khóa ứng viên]], phương pháp rút gọn [[theory/minimal-cover|Phủ tối thiểu]], và các dạng chuẩn tại [[theory/3nf|3NF]] và [[theory/bcnf|BCNF]].
