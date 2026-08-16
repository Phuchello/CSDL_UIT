# QA & Validation

Thư mục này chỉ giữ các kiểm tra có thể tái hiện từ repository hiện tại, thay vì các bản tự chấm điểm hoặc biên bản phê duyệt nội bộ.

## Kiểm tra nhanh

```bash
python scripts/build.py
python scripts/validate.py
```

GitHub Actions cũng chạy validation tự động trên `main`.

## Phạm vi kiểm tra

- nguồn HTML có thể build thành `book/index.html`;
- tài nguyên dùng đường dẫn tương đối và không phụ thuộc đường dẫn máy cá nhân;
- PDF chuẩn tồn tại tại `dist/IT004_CSDL_UIT_CamNang_VoTrongPhuc.pdf`;
- README, BUILD, NOTICE, CHANGELOG và source inventory có liên kết hợp lệ;
- repository không chứa secret, `.env`, cache hay thư mục phụ thuộc sinh tự động;
- GitHub Pages có thể deploy bản HTML từ workflow hiện tại.

Các báo cáo audit chi tiết từng được dùng trong quá trình biên soạn vẫn còn trong lịch sử Git, nhưng không được giữ ở cây `main` hiện tại để mặt tiền repository gọn và dễ đọc hơn.
