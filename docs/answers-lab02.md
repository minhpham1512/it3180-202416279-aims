# Lab 02 - Câu hỏi thảo luận

## 1. Vì sao phải đồng bộ `master` vào nhánh trước khi gửi PR?

- Nhánh `feature/search-by-title` (Dev 2) được tạo từ `master` **cũ**, khi
  `master` chưa có `print_cart` (PR #4). Nếu không đồng bộ, PR chỉ được kiểm
  tra trên nền cũ: *test pass trên nhánh* không chứng minh được *test pass sau
  khi tích hợp*. Đồng bộ (`git fetch` + `git merge origin/master`) để chạy
  `python main.py`/test trên **đúng tổ hợp mã sẽ có trên master** sau merge.
- Xung đột (nếu có) được giải quyết **trên nhánh của tác giả** – người hiểu
  thay đổi nhất – thay vì để reviewer/người merge xử lý, và không bao giờ phá
  `master`.
- Reviewer xem diff sạch, chỉ gồm thay đổi của PR, không lẫn thay đổi do lệch nền.
- Phù hợp nguyên tắc "nhánh sống ngắn, càng gần master càng tốt" để tránh
  *merge hell*.

## 2. Khi nào **không** được rebase?

Rebase tạo commit mới (SHA mới) thay cho commit cũ, tức là **viết lại lịch sử**.
Không rebase khi:

- Commit **đã được chia sẻ** và người khác có thể đã dựa vào: đã push lên nhánh
  dùng chung (`master`, `release/*`), hoặc nhánh mà đồng đội đang làm tiếp /
  đã tạo nhánh con từ đó (ví dụ `bugfix/*` tạo từ `feature/discount` ở Lab 03).
  Rebase khiến họ có lịch sử "song sinh", phải force-push và dễ mất commit.
- Nhánh đã mở PR và đang được review: SHA thay đổi làm mất ngữ cảnh comment,
  (với *dismiss stale approvals*) mất luôn approval.
- Lịch sử cần giữ đúng như đã xảy ra để kiểm toán (nhánh phát hành, tag).

Được rebase khi nhánh còn là **nhánh riêng, chưa ai dùng**; nếu đã push nhánh
riêng thì dùng `git push --force-with-lease` (không dùng `--force`).

## 3. `feature/*` khác `topic/*` ra sao?

| | `feature/*` | `topic/*` |
|---|---|---|
| Nội dung | Một **tính năng** của sản phẩm, thay đổi hành vi mã nguồn | Một **chủ đề** không phải tính năng: tài liệu, cấu hình, template, chuẩn bị phát hành... |
| Ví dụ trong repo | `feature/cart-print`, `feature/search-by-title` | `topic/pr-template`, `topic/use-case-diagram`, `topic/lab02-answers` |
| Ghi vào CHANGELOG | Thường có (mục *Added*) | Thường không |
| Commit type | `feat:` | `docs:`, `chore:`, `ci:` |

Cả hai đều tạo từ `master`, merge về `master` qua PR; khác nhau ở **mục đích**,
giúp người đọc lịch sử biết ngay nhánh làm gì ("một nhánh, một mục đích").

## 4. So sánh 3 kiểu merge (minh họa trong repo)

| PR | Kiểu merge | Kết quả trên `master` |
|---|---|---|
| #4 `feature/cart-print` | Create a merge commit | `8ea466f Merge pull request #4` + giữ nguyên 3 commit `feat:` của nhánh |
| #9 `topic/lab02-answers` | Squash and merge | 2 commit trên nhánh được gộp thành **1** commit trên `master` |
| #8 `topic/use-case-diagram` | Rebase and merge | Commit được chép lên đầu `master` với **SHA mới** (`0d84636` trên nhánh → `368df82` trên `master`), lịch sử tuyến tính |

- **Merge commit**: giữ đủ lịch sử chi tiết, thấy rõ ranh giới từng PR; revert
  cả tính năng bằng 1 lệnh `git revert -m 1 <merge>`; nhưng lịch sử không tuyến tính.
- **Squash**: lịch sử gọn, 1 PR = 1 commit, revert 1 lệnh; mất commit chi tiết,
  và Git không nhận ra nhánh "đã merge" (phải `git branch -D`).
- **Rebase**: tuyến tính, giữ từng commit; nhưng SHA mới, revert cả tính năng
  phải revert nhiều commit.

Ghi chú: PR #5 (`feature/search-by-title`) đã lỡ được merge bằng merge commit
thay vì squash như hướng dẫn; kiểu squash được minh họa bằng PR #9.
