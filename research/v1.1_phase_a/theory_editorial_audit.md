# Kiểm Toán Biên Tập & Đối Chiếu Học Thuật (Theory Handbook Editorial Audit) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31
**Phạm vi:** Đối chiếu bản thảo lý thuyết hiện tại (`book/index.html`) với tập Slide bài giảng chính thức của Giảng viên UIT (`LOC-LEC-AN-*`, `LOC-LEC-LONG-*`) và giáo trình chuẩn mực để định hướng hoàn thiện ấn bản v1.1.

---

## 1. Kết Quả Đối Chiếu Thuật Ngữ & Ký Hiệu Học Thuật (Terminology & Notation Alignment)

| Khái niệm học thuật | Thuật ngữ trong Slide UIT (`LOC-LEC-LONG-*`) | Thuật ngữ trong Sách hiện tại | Đánh giá & Khuyến nghị điều chỉnh v1.1 |
| :--- | :--- | :--- | :--- |
| **Mô hình Dữ liệu** | Mô hình quan hệ (Relational Model), E.F. Codd 1970 | Mô hình dữ liệu quan hệ | **Khớp hoàn hảo**. Giữ vững cấu trúc hình thức. |
| **Tân từ** | Tân từ của quan hệ $\|\|R\|\|$: Quy tắc ngữ nghĩa xác định quan hệ | Tân từ $\|\|R\|\|$ / Predicate | **Khớp hoàn hảo**. Nêu bật ký hiệu $\|\|R\|\|$ chuẩn UIT. |
| **Thể hiện của quan hệ** | Thể hiện của quan hệ $T_R$ tại một thời điểm | Instance / Thể hiện quan hệ $r$ | **Bổ sung ký hiệu $T_R$** bên cạnh ký hiệu $r$ quốc tế. |
| **Phép chiếu ĐSQH** | Phép chiếu lên tập thuộc tính $X$: $R[X]$ hoặc $\pi_X(R)$ | $\pi_{A_1, A_2}(R)$ | **Bổ sung ký hiệu $R[X]$** vì các slide và bài thi viết tay UIT dùng phổ biến $R[X]$. |
| **Phép gom nhóm ĐSQH** | $_{G_1,..,G_n}\Im_{F_1(A_1),..,F_m(A_m)}(E)$ | $\Im$ (Group by) | **Chuẩn hóa cú pháp $\Im$** với chỉ số trước (thuộc tính gom nhóm) và chỉ số sau (hàm tính toán). |
| **Thuật toán tìm khóa** | Tập nguồn $Ng$, Tập trung gian $Tg$, Tập treo $Tr$, Tập bắt buộc $N = Ng \cup Tr$ | Phân tích tập $L, R, N, LR$ | **Khuyến nghị sử dụng song song**: Giải thích cách gọi $Ng/Tg/Tr$ của Slide UIT và $L/R/N/LR$ của sách để sinh viên đối chiếu dễ dàng. |
| **Phân loại RBTV** | 7 loại: Miền giá trị, Liên thuộc tính 1 QH, Liên bộ 1 QH, Tham chiếu, Liên thuộc tính nhiều QH, Thuộc tính tổng hợp, Chu trình | RBTV 1 bảng, RBTV liên bảng, RBTV ngữ nghĩa | **Khuyến nghị cấu trúc lại Chương 5** theo đúng 7 phân loại chuẩn mực của Khoa HTTT – UIT. |

---

## 2. Nhận Xét Biên Tập & Giọng Văn Học Thuật (Tone & Register Review)

1. **Giảm bớt từ ngữ mang sắc thái tiếp thị / quảng bá (De-marketization)**:
   - Thay thế các cụm từ như *"Exam Mastery"*, *"Tuyệt kỹ phòng thi"*, *"Bí kíp 100%"* bằng các thuật ngữ học thuật trung tính và chuyên nghiệp: *"Chiến thuật phòng thi"*, *"Mô hình phân tích"*, *"Quy trình giải toán"*.
   - Giữ lại các khung sư phạm hữu ích (`Mental Model`, `Fast Pattern`, `Common Trap`, `Dry Run`) nhưng trình bày tinh gọn, giảm mật độ icon/emoji trang trí lặp lại.

2. **Tách biệt phần Hành chính / Bản quyền khỏi Mạch học tập**:
   - Chuyển thông tin bản quyền, giấy phép, công cụ biên dịch và lịch sử phiên bản về phần Bìa lót / Lời mở đầu hoặc phụ lục Colophon cuối sách; không để cạnh tranh không gian với Bản đồ tư duy và Lộ trình học tập.

---

## 3. Định Hướng Mỹ Thuật Bìa Sách v1.1 (Cover Design Direction)

### Định Hướng Được Khuyến Nghị: Bìa Đồ Họa Lược Đồ Quan Hệ (Relational Schema / Graph Editorial Cover)

- **Nguyên tắc cốt lõi**: Bìa sách chỉ chứa đúng **3 dòng văn bản học thuật**, hoàn toàn không có phụ đề tiếp thị, không có huy hiệu, không có hình ảnh AI hay nhân vật minh họa:
  1. `IT004`
  2. `CƠ SỞ DỮ LIỆU`
  3. `BIÊN SOẠN: VÕ TRỌNG PHÚC`
- **Ngôn ngữ thị giác**:
  - Nền màu sáng nhã nhặn (warm white / neutral gray / light blueprint).
  - Điểm nhấn thị giác là một sơ đồ mạng lưới quan hệ (Schema Graph) tinh xảo: các thực thể hình chữ nhật, các thuộc tính hình oval, đường liên kết khóa chính/khóa ngoại $PK \rightarrow FK$, và sự chuyển dịch từ ERD sang Lược đồ quan hệ chuẩn.
  - Vẻ đẹp và tính trang trọng của bìa sách đến từ nghệ thuật sắp đặt chữ (Typography), tỷ lệ hình học và tính thẩm mỹ của cấu trúc dữ liệu quan hệ.

---

## 4. Các Phương Án Mỹ Thuật Thay Thế Để Hội Đồng Thẩm Định (Mentor) Cân Nhắc

- **Phương án B (Query Pipeline Architecture)**:
  - Bố cục 3 dải màu ngang tượng trưng cho 3 tầng: Tầng Mô hình (ER/Schema) $\rightarrow$ Tầng Truy vấn (ĐSQH/SQL) $\rightarrow$ Tầng Toàn vẹn & Tối ưu (RBTV/Chuẩn hóa).
- **Phương án C (Annotated Relation Fragment)**:
  - Bố cục trang nhã lấy cảm hứng từ trang viết tay học thuật: bảng dữ liệu quan hệ thu nhỏ kèm các ký hiệu bao đóng $X^+$, mũi tên phụ thuộc hàm $X \rightarrow Y$ và dạng chuẩn BCNF.
