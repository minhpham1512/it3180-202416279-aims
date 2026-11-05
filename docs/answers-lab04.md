# Lab 04 - Câu hỏi thảo luận

## 0. Vì sao chuẩn bị phát hành trên `master` trước, không sửa trên nhánh release?

- Nhánh `release/*` là **baseline đóng băng**: lý tưởng là nó được cắt ra từ
  `master` ở trạng thái *đã sẵn sàng* (số phiên bản, CHANGELOG đã đúng), để
  `release/lab04` lúc tạo ra **trùng khít** với một commit trên `master` và tag
  `v1.0.0` gắn đúng vào đó.
- Nếu sửa số phiên bản/CHANGELOG trên nhánh release, thay đổi đó **không có trên
  `master`** (release không bao giờ merge ngược) → phải chép tay lại, dễ quên;
  bản 1.1.0 sau này có thể thiếu mục 1.0.0 trong CHANGELOG.
- Việc chuẩn bị cũng là một thay đổi cần **review qua PR** (PR #20) như mọi thay
  đổi khác; làm trên `master` thì quy trình giống hệt mọi PR thường ngày.
- Nhánh release chỉ nhận **hotfix**, càng ít thay đổi càng dễ kiểm toán.

## 1. Vì sao `release/*` không merge vào `master`?

- Trong Release Flow, `master` là **dòng chính duy nhất** – mọi thay đổi vào
  `master` *trước* (qua PR), còn `release/*` chỉ là **ảnh chụp** của `master`
  tại một thời điểm, rồi rẽ nhánh để bảo trì. Luồng thay đổi đi **một chiều**:
  `master → release/*` (cắt nhánh) và bản sửa đi bằng cherry-pick.
- Nhánh release chứa những thứ **chỉ đúng cho dòng phiên bản đó**, ví dụ commit
  `chore: bump version to 1.0.1` trên `release/lab04`. Merge vào `master` (đang
  ở 1.1.0) sẽ gây xung đột hoặc tệ hơn, kéo lùi số phiên bản/hành vi của `master`.
- Merge ngược làm lịch sử rối (mỗi release thành một nhánh "hội tụ" lại), khó
  trả lời câu hỏi status accounting "bản sửa X đã có ở đâu?" vì nhánh nào cũng
  lẫn vào nhau.
- Bài học thật trong repo: PR #12 đã lỡ merge `release/lab01` vào `master`. Nội
  dung không đổi (diff rỗng vì bản sửa đã được cherry-pick sang `master` ở PR #7),
  nhưng lịch sử có thêm một nhánh hội tụ và – do *Automatically delete head
  branches* – GitHub đã **tự xóa `release/lab01`** (đã khôi phục lại về `da3850c`).
  Từ Lab 04, rule `release/*` cấm xóa/force-push nên sự cố này không lặp lại.

## 2. So sánh với GitFlow

| | Release Flow (học phần) | GitFlow |
|---|---|---|
| Nhánh dài hạn | Chỉ `master` (+ các `release/*` để bảo trì) | `main` (bản đã phát hành) + `develop` (tích hợp) |
| Tính năng merge vào | `master` | `develop` |
| Nhánh release | Cắt từ `master`, **không merge lại**, sống tiếp làm dòng bảo trì | Cắt từ `develop`, ổn định xong thì **merge vào `main` và `develop`** rồi xóa |
| Hotfix | Từ `release/*`, đưa về `release/*` + `master` (cherry-pick) | Từ `main`, merge vào `main` + `develop` |
| Tag | Trên nhánh release | Trên `main` |
| Bảo trì nhiều phiên bản song song | Tự nhiên (mỗi phiên bản một nhánh `release/*`) | Khó: `main` chỉ có một dòng phiên bản mới nhất |
| Độ phức tạp | Ít nhánh, ít merge | Nhiều nhánh, merge hai chiều |

GitFlow hợp với phát hành định kỳ, một phiên bản đang dùng; Release Flow hợp
với việc cần giữ **nhiều bản phát hành sống song song** (mỗi tuần một
`release/labXX`, có thể hotfix bản cũ).

## 3. Vì sao lên `1.0.0` mà không phải `0.4.0`?

- Theo SemVer, `0.y.z` là giai đoạn phát triển ban đầu, "bất cứ thứ gì cũng có
  thể thay đổi", API công khai chưa ổn định. `1.0.0` là lời **cam kết công khai**:
  API (`Cart`, `DigitalVideoDisc`, `search_by_title`, …) từ nay ổn định; thay đổi
  phá vỡ tương thích phải tăng MAJOR.
- Lab 04 là lần đầu sản phẩm được **phát hành chính thức**: có baseline được
  bảo vệ, tag annotated, CHANGELOG, GitHub Release và quy trình hotfix/bảo trì.
  Đó chính là điều kiện để gọi là 1.0.0.
- Nếu tiếp tục `0.4.0`, người dùng không có tín hiệu nào cho biết bản này đã đáng
  tin cậy hay chưa; và việc đánh số PATCH (`1.0.1`) cho hotfix ở Lab 05 sẽ thiếu ý
  nghĩa "bản vá tương thích của một bản ổn định".
- Các bản cũ được gắn `v0.1.0`, `v0.2.0`, `v0.3.0` (Lab 01–03) để thể hiện đúng
  giai đoạn chưa ổn định.

## 4. Tag và nhánh release khác nhau thế nào?

- Tag `v1.0.0` (annotated: có người tạo, ngày, thông điệp) **không bao giờ di
  chuyển** → định danh chính xác, bất biến một baseline; tái tạo được bất cứ lúc
  nào (`git switch --detach v1.0.0`, `git worktree add`, `git archive`).
- Nhánh `release/lab04` **di chuyển** khi có hotfix → là *dòng bảo trì* của bản
  phát hành; đầu nhánh luôn là bản mới nhất của dòng 1.0.x (1.0.0 → 1.0.1).
- Tag không tự đi theo `git push`, phải `git push origin <tag>`; tag đã chia sẻ
  thì không xóa/không di chuyển (sai thì phát hành số mới).
