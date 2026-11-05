# Báo cáo thực hành Git & GitHub (IT3180) – Lab 01 → Lab 05

Repo: https://github.com/minhpham1512/it3180-202416279-aims · Làm một mình
(`Require approvals = 0`, mọi thay đổi vẫn bắt buộc qua Pull Request).

Câu trả lời thảo luận từng bài:
[Lab 01](answers-lab01.md) · [Lab 02](answers-lab02.md) · [Lab 03](answers-lab03.md) ·
[Lab 04](answers-lab04.md) · [Lab 05](answers-lab05.md)

## Bài nộp (baseline)

| Bài | Nhánh nộp | Tag | Ghi chú |
|---|---|---|---|
| Lab 01 | `release/lab01` | `v0.1.0` | Hotfix câu trả lời qua PR #6 (→ release) + PR #7 (cherry-pick → master) |
| Lab 02 | `release/lab02` | `v0.2.0` | |
| Lab 03 | `release/lab03` | `v0.3.0` | |
| Lab 04 | `release/lab04` | `v1.0.0`, `v1.0.1` | GitHub Release cho cả hai |
| Lab 05 | `release/lab05` | `v1.1.0` | GitHub Release |

## Checklist

| Bài | Mục | Trạng thái |
|---|---|---|
| 01 | Repo có `aims/`, `main.py`, không có `__pycache__/`; PR #1 merged; release trùng master lúc nộp | ✅ |
| 02 | Push thẳng `master` bị chặn (`protected branch hook declined`) | ✅ |
| 02 | ≥ 5 PR merged; đủ 3 kiểu merge: merge commit (#4), squash (#9), rebase (#8) | ✅ |
| 02 | PR cart-print có *Changes requested → Approved* | ❌ Không làm được khi làm một mình: tác giả PR không thể tự review/approve PR của mình |
| 03 | Issue #10 Closed qua PR #11 (`Fixes #10`); commit `test:` đứng trước `fix:` | ✅ |
| 03 | PR #14 bugfix có base `feature/discount` | ✅ |
| 03 | Xung đột PR #17 được giải, không còn dấu xung đột; PR revert #18; `master` 4 tests OK | ✅ |
| 04 | `git tag -n`: `v0.1.0`…`v1.0.0` annotated; `v1.0.0` trùng đầu `release/lab04` lúc phát hành | ✅ |
| 04 | Push thẳng `release/*` bị chặn (GH013); có GitHub Release | ✅ |
| 04 | `sort_by_cost` có trên `master`, không có trên `release/lab04` | ✅ |
| 05 | `v1.0.1` trên `release/lab04`, `v1.1.0` trên `release/lab05`; `diff --stat v1.0.0 v1.0.1` chỉ 4 tệp | ✅ |
| 05 | 2 commit có `(cherry picked from ...)`; Issue #28 Closed; vòng lặp in 1 cho cả 3 phiên bản | ✅ |
| 05 | Mở rộng: CI GitHub Actions bắt buộc pass, PR demo #24 bị chặn merge | ✅ |

## Sự cố gặp phải và cách xử lý

1. **`release/lab01` bị merge ngược vào `master` (PR #12).** Vi phạm quy tắc
   "release/* không bao giờ merge ngược". Nội dung không đổi (diff rỗng do bản
   sửa đã được cherry-pick sang `master` ở PR #7) nên không cần revert; lịch sử
   `master` đã được bảo vệ nên không viết lại được.
2. **`release/lab01` bị GitHub tự xóa** do tùy chọn *Automatically delete head
   branches* khi merge PR #12 (nhánh release là *head* của PR đó). Đã tạo lại nhánh
   từ commit đã nộp `da3850c`, và bật ruleset `release/*` (cấm xóa, cấm force-push,
   bắt buộc PR) để không lặp lại.
3. **PR #5 merge bằng merge commit** thay vì squash như hướng dẫn → kiểu squash
   được minh họa bằng PR #9.
4. **Cherry-pick hotfix xung đột** ở Lab 05 do thay đổi newline cuối tệp
   `aims/search.py` – xem phụ lục [Lab 05](answers-lab05.md).
5. **Chạy chương trình trên Windows khi chuyển hướng output** (`python main.py | head`)
   có thể lỗi `UnicodeEncodeError` vì thông báo tiếng Việt; đặt `PYTHONUTF8=1`.
