---
title: Dạng chuẩn Boyce-Codd (BCNF)
description: Định nghĩa hình thức BCNF, so sánh với 3NF, thuật toán phân rã BCNF và hiện tượng mất phụ thuộc hàm.
type: theory
topics: [bcnf, 3nf, normalization, decomposition]
related: [theory/3nf, theory/candidate-keys, theory/closure, theory/lossless-decomposition, exercises/normalization-exercise]
provenance: verified-artifact
courseEvidence: [UIT-O02, LOC-LEC-LONG-CH06]
---
# Dạng chuẩn Boyce-Codd (Boyce-Codd Normal Form - BCNF)

Dạng chuẩn Boyce-Codd (BCNF) do Raymond F. Boyce và Edgar F. Codd đề xuất năm 1974 là một phiên bản nghiêm ngặt hơn của Dạng chuẩn 3 ([[theory/3nf|3NF]]). Mục tiêu của BCNF là loại bỏ triệt để mọi dư thừa dữ liệu bắt nguồn từ các phụ thuộc hàm.

## 1. Định nghĩa toán học hình thức

Cho lược đồ quan hệ $R(U)$ và tập phụ thuộc hàm $F$.
Lược đồ $R$ đạt **Dạng chuẩn Boyce-Codd (BCNF)** nếu và chỉ nếu với mọi phụ thuộc hàm không tầm thường $X \rightarrow A \in F^+$ (với $A \notin X$):

$$X \text{ bắt buộc phải là một siêu khóa (superkey) của } R$$

- **Nói cách khác:** Trong BCNF, bất cứ tập thuộc tính nào làm vế trái của một phụ thuộc hàm không tầm thường đều phải xác định được toàn bộ lược đồ quan hệ.
- BCNF **không chấp nhận** điều kiện cứu vãn *"hoặc $A$ là thuộc tính khóa"* của 3NF. Do đó, một quan hệ đạt BCNF thì chắc chắn đạt 3NF, nhưng một quan hệ đạt 3NF chưa chắc đã đạt BCNF.

## 2. BCNF vs 3NF: Ví dụ kinh điển vi phạm BCNF nhưng đạt 3NF

Xét lược đồ phân công giảng dạy: $R(\text{SinhVien}, \text{MonHoc}, \text{GiangVien})$ với tập phụ thuộc hàm $F$:
1. $\{\text{SinhVien}, \text{MonHoc}\} \rightarrow \text{GiangVien}$ (Mỗi sinh viên học một môn chỉ do một giảng viên dạy).
2. $\text{GiangVien} \rightarrow \text{MonHoc}$ (Mỗi giảng viên chỉ chuyên trách dạy duy nhất một môn).

### Phân tích dạng chuẩn:
- **Tìm khóa ứng viên:**
  - $K_1 = \{\text{SinhVien}, \text{MonHoc}\}$ (do $\{\text{SinhVien}, \text{MonHoc}\}^+ = \text{SinhVien, MonHoc, GiangVien}$).
  - $K_2 = \{\text{SinhVien}, \text{GiangVien}\}$ (do $\{\text{SinhVien}, \text{GiangVien}\}^+ = \text{SinhVien, GiangVien, MonHoc}$).
  - Tập các thuộc tính khóa là: $\mathcal{P} = \{\text{SinhVien}, \text{MonHoc}, \text{GiangVien}\}$. Tất cả thuộc tính đều là thuộc tính khóa!
- **Đánh giá 3NF:**
  - Xét $\text{GiangVien} \rightarrow \text{MonHoc}$: Vế trái $\text{GiangVien}$ không là siêu khóa, nhưng vế phải $\text{MonHoc}$ là thuộc tính khóa (nằm trong $K_1$).
  - $\implies$ Quan hệ đạt **Dạng chuẩn 3 (3NF)** nhờ điều kiện cứu vãn.
- **Đánh giá BCNF:**
  - Xét $\text{GiangVien} \rightarrow \text{MonHoc}$: $\text{GiangVien}$ không phải là siêu khóa ($\text{GiangVien}^+ \neq U$).
  - BCNF không cho phép cứu vãn $\implies$ Quan hệ **vi phạm BCNF**.

## 3. Thuật toán phân rã BCNF (BCNF Decomposition Algorithm)

Nếu lược đồ $R$ vi phạm BCNF do phụ thuộc hàm $X \rightarrow Y$ ($X$ không là siêu khóa):
1. **Bước 1:** Tách $R$ thành hai lược đồ con:
   $$R_1 = X \cup Y \quad \text{và} \quad R_2 = R - (Y - X)$$
2. **Bước 2:** Xác định tập phụ thuộc hàm chiếu trên từng lược đồ con ($F_1$ và $F_2$).
3. **Bước 3:** Tiếp tục kiểm tra BCNF trên $R_1$ và $R_2$. Nếu còn quan hệ con nào vi phạm thì đệ quy lặp lại thuật toán cho đến khi mọi quan hệ con đều đạt BCNF.
4. **Đặc tính:** Phép phân rã BCNF luôn đảm bảo tính kết nối không mất thông tin ([[theory/lossless-decomposition|Lossless Join Decomposition]]).

## 4. Cái giá phải trả: Mất tính bảo toàn phụ thuộc hàm

Khi phân rã lược đồ ví dụ trên để đạt BCNF:
- Tách thành: $R_1(\text{GiangVien}, \text{MonHoc})$ với $FD_1 = \{\text{GiangVien} \rightarrow \text{MonHoc}\}$ và $R_2(\text{SinhVien}, \text{GiangVien})$.
- Cả $R_1$ và $R_2$ đều đạt BCNF.
- **Tuy nhiên:** Phụ thuộc hàm $\{\text{SinhVien}, \text{MonHoc}\} \rightarrow \text{GiangVien}$ đã bị phân tán trên hai bảng khác nhau. Để kiểm tra ràng buộc này, hệ quản trị bắt buộc phải thực hiện phép nối (JOIN) tốn kém giữa $R_1$ và $R_2$.
- $\implies$ **Phép phân rã BCNF không đảm bảo bảo toàn phụ thuộc hàm (Dependency Preservation).** Trong thực tế công nghiệp, các kiến trúc sư CSDL thường chấp nhận dừng lại ở 3NF để bảo toàn toàn vẹn dữ liệu khai báo.

Xem lý thuyết chuẩn hóa nền tảng tại [[theory/3nf|Dạng chuẩn 3 (3NF)]], nguyên lý bảo toàn tại [[theory/lossless-decomposition|Phân rã kết nối không mất thông tin]], và bài tập worked example tại [[exercises/normalization-exercise|Bài tập chuẩn hóa]].
