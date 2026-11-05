# Lab 03 - Câu hỏi thảo luận

## Tóm tắt những gì đã làm

| Phần | Kết quả trong repo |
|---|---|
| A. Bugfix từ `master` | Issue #10 → `bugfix/cart-limit-off-by-one` → commit `test: reproduce cart limit bug (#10)` (FAIL) **trước** commit `fix: reject DVDs beyond MAX_NUMBERS_ORDERED` (`Fixes #10`) → PR #11 → Issue #10 tự đóng |
| B. Bugfix từ `feature/*` | `bugfix/discount-calculation` tạo từ `origin/feature/discount` → PR #14 **base `feature/discount`** → PR #15 đưa tính năng vào `master` |
| C. Xung đột | PR #16 (`feature/vietnamese-messages`) merge trước → PR #17 (`feature/show-added-title`) báo *This branch has conflicts* → `git merge origin/master`, kết hợp thành `print(f"Đã thêm đĩa '{dvd.title}' vào giỏ hàng")`, chạy test, commit, push → merge |
| D. Hoàn tác | `reset --soft/--mixed/--hard` + `reflog` trên nhánh nháp local; `git revert -m 1 6fd30a8` qua `bugfix/revert-show-added-title` → PR #18 |

Ngoài ra PR #13 bổ sung `tests/test_search.py`. `master` hiện có **4 tests OK**.

Kết quả thực tế khi luyện `reset` (nhánh `topic/undo-practice`, không push):

```
== reset --soft HEAD~1      →  M  notes.txt   (thay đổi về STAGING)
== reset --mixed HEAD~1     →   M notes.txt   (thay đổi về WORKING DIR)
== reset --hard HEAD~1      →  d6b1a5b chore: practice commit 2 (thay đổi bị xóa)
== git reflog
d6b1a5b HEAD@{0}: reset: moving to HEAD~1
f49dc5f HEAD@{1}: commit: chore: practice commit 3 (again 2)
== git reset --hard f49dc5f →  khôi phục được commit "đã mất"
```

Xung đột ở Phần C cũng được thử giải bằng **rebase** trên một nhánh local
(`git rebase` → sửa → `git add` → `git rebase --continue`): kết quả `cart.py`
giống hệt cách merge, nhưng lịch sử tuyến tính và commit có SHA mới. Vì nhánh
đã push và đang có PR nên bài chọn cách merge (không phải force-push).

## 1. Merge base là gì?

**Merge base** là *tổ tiên chung gần nhất* (best common ancestor) của hai
commit/nhánh, tính bằng `git merge-base A B`. Đây là điểm mà hai nhánh rẽ ra.

Khi merge, Git thực hiện **3-way merge** giữa ba phiên bản: merge base, đầu
nhánh hiện tại (`HEAD`/"ours") và đầu nhánh được merge ("theirs"):

- Một dòng chỉ đổi ở một phía so với merge base → Git tự lấy phía đã đổi.
- Cùng một vùng bị đổi **khác nhau ở cả hai phía** so với merge base → **xung đột**,
  cần con người quyết định.

Ví dụ trong repo: `feature/vietnamese-messages` (4900841) và
`feature/show-added-title` (5f7b123) đều tạo từ `f949738` (merge PR #15), nên
`git merge-base 5f7b123 4900841` = `f949738`. Ở merge base dòng đó là
`print("The disc has been added")`; mỗi nhánh sửa nó theo một cách → xung đột.

Merge base cũng quyết định PR hiển thị gì: tab *Files changed* là diff từ merge
base tới đầu nhánh (vì vậy PR bugfix chọn sai base sẽ hiện "nhiều commit lạ").

## 2. Vì sao `master`/`release/*` phải dùng `revert` thay vì `reset`?

- `reset` **dời con trỏ nhánh về quá khứ**, tức là xóa commit khỏi lịch sử. Với
  nhánh đã chia sẻ, mọi người đã có các commit đó: muốn đẩy lên phải
  force-push (bị branch protection chặn), người khác pull về sẽ có lịch sử lệch,
  commit dễ bị "hồi sinh" khi họ merge lại, hoặc mất hẳn công việc của người khác.
- `revert` **tạo một commit mới đảo ngược** thay đổi: lịch sử chỉ tiến về phía
  trước, ai cũng `pull` bình thường, không cần force-push.
- Về SCM: baseline và lịch sử phải **bất biến và truy vết được**. Revert để lại
  bản ghi "đã thêm X (PR #17) → đã gỡ X (PR #18), vì sao" và được review qua PR
  như mọi thay đổi khác. Một tag đã phát hành vẫn trỏ đúng nội dung đã giao.
- `reset`/`amend`/`rebase` chỉ dùng cho commit **chưa push** (như nhánh nháp
  `topic/undo-practice`).

Lưu ý khi revert một merge commit phải chỉ định mainline `-m 1` (phía `master`);
nếu sau này muốn đưa lại tính năng thì phải *revert commit revert*, vì Git coi
các commit của nhánh cũ là "đã merge".
