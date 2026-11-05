# Lab 01 - Câu hỏi thảo luận

## 0. (Câu hỏi nhanh) Cấu hình `--global` được lưu ở đâu? Khác gì `--local`?

- `--global` lưu trong tệp `~/.gitconfig` của người dùng hiện tại
  (Windows: `C:\Users\<tên>\.gitconfig`). Mọi repo của người dùng đó đều dùng chung.
- `--local` (mặc định khi đứng trong một repo) lưu trong `.git/config` của
  **chỉ repo đó**, và ghi đè giá trị `--global` (thứ tự ưu tiên:
  `--system` < `--global` < `--local`).
- Kiểm tra nguồn gốc từng giá trị bằng `git config --list --show-origin`.
- Ví dụ: đặt `user.email` email trường ở `--global`, nhưng trong repo dự án
  công ty có thể đặt `--local` một email khác.

## 1. Vì sao dùng `git mv`?

- `git mv a b` = đổi tên tệp trong working directory **và** ghi nhận ngay
  việc đổi tên vào staging (tương đương `mv a b && git rm a && git add b`).
  Nếu chỉ dùng `mv` của hệ điều hành, Git thấy "một tệp bị xóa" và "một tệp
  lạ chưa theo dõi"; dễ quên `git add` tệp mới hoặc commit thiếu.
- Git không lưu thông tin "rename" mà phát hiện dựa trên độ giống nhau của nội
  dung. Khi đổi tên bằng `git mv` và **không sửa nội dung trong cùng commit**
  (commit `refactor: move sources into aims package` chỉ di chuyển, việc sửa
  import nằm ở commit sau), độ giống nhau là 100% nên:
  - Tab *Files changed* của PR #1 hiển thị **renamed** thay vì xóa + thêm.
  - `git log --follow -- aims/cart.py` vẫn truy được lịch sử về `cart.py` ở
    thư mục gốc, `git blame` vẫn chỉ đúng tác giả của từng dòng.
- Về SCM: Configuration Item vẫn giữ **định danh và lịch sử** dù đổi vị trí,
  đảm bảo khả năng truy vết.

## 2. `release/lab01` có phải baseline không?

**Có**, theo nghĩa nó là một phiên bản đã được thống nhất (bài nộp Lab 01),
được tạo từ `master` sau khi PR #1 đã được duyệt và merge, và từ nay chỉ được
thay đổi qua quy trình (hotfix + PR, như chính thay đổi này).

Tuy nhiên nhánh là con trỏ **di chuyển được**: khi có hotfix, đầu nhánh
`release/lab01` đổi. Vì vậy để định danh **chính xác, bất biến** một baseline
còn cần gắn **annotated tag** (Lab 04 gắn `v0.1.0` vào `release/lab01`).
Có thể hiểu: nhánh `release/lab01` là *dòng baseline/dòng bảo trì* của bài
Lab 01, còn tag là *mốc baseline cụ thể* trên dòng đó.

## 3. Vì sao không commit thẳng `master` dù làm một mình?

- **Kiểm soát thay đổi**: mọi thay đổi vào baseline phải đi qua Change Request
  (PR) có mô tả *Mục đích – Thay đổi – Kiểm thử*. Đây là bản ghi kiểm toán
  (ai, khi nào, vì sao) mà commit thẳng không có.
- **`master` luôn ở trạng thái tích hợp được**: làm trên nhánh riêng thì việc
  dang dở/hỏng không ảnh hưởng `master`; có thể bỏ cả nhánh nếu hướng đi sai.
- **Điểm kiểm tra tự động**: PR là nơi CI chạy test (Lab 05) và nơi branch
  protection được áp dụng; commit thẳng bỏ qua tất cả.
- **Luyện thói quen** cho làm việc nhóm: khi có thêm người, quy trình đã sẵn.
- Ngay cả khi `Require approvals = 0`, PR vẫn cho phép **tự review diff**
  trước khi merge (bắt được tệp rác như `__pycache__/`, lỗi import...).
