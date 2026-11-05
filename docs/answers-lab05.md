# Lab 05 - Câu hỏi thảo luận

## 1. Ưu, nhược điểm của *upstream first* so với *release first*

- **Release first** (học phần): tạo `hotfix/*` từ `release/lab04` (bản đang lỗi),
  sửa, phát hành `v1.0.1`, **sau đó** cherry-pick sang `master` và `release/lab05`.
- **Upstream first** (Release Flow của Microsoft): sửa trên `master` trước (qua PR
  vào `master`), rồi cherry-pick xuống các `release/*` cần vá.

| | Release first | Upstream first |
|---|---|---|
| Ưu | Sửa và kiểm thử **đúng trên mã đang chạy** của bản lỗi → vá nhanh, ít rủi ro cho người dùng bản đó. Commit sửa không lẫn tính năng mới của `master`. | Không bao giờ "quên" sửa dòng chính: bản sửa vào `master` trước nên mọi bản phát hành **tương lai** chắc chắn có. Một nguồn sự thật duy nhất; review/CI chạy trên `master`. |
| Nhược | Dễ **quên lan truyền** về `master`/release mới hơn → lỗi tái xuất ở bản sau (regression). Phải cherry-pick ngược lên mã mới hơn, có thể xung đột. | Bản vá cho người dùng **chậm hơn** (phải qua `master` trước). Mã `master` đã khác xa bản cũ → cherry-pick xuống release cũ dễ xung đột, có khi phải viết lại; bản sửa được kiểm thử trên `master` chứ không phải trên bản đang lỗi. |
| Hợp với | Ít dòng phát hành, cần vá khẩn bản đang dùng | Sản phẩm lớn, phát hành theo sprint, nhiều release song song |

Dù chọn cách nào, cần **kiểm toán** sau khi lan truyền (Phần F) và dùng
`cherry-pick -x` để truy vết nguồn gốc.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F phát hiện?

- `git cherry -v origin/release/lab05 origin/release/lab04` – `git cherry` so
  **nội dung thay đổi** (patch-id) chứ không so SHA. Nếu `release/lab05` chưa có
  bản tương đương, commit `fix: make search_by_title case-insensitive` sẽ hiện
  dấu **`+`** (chưa có) thay vì `-` (đã có bản tương đương).
- `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"` – chỉ
  ra **1** bản cherry-pick (cho `master`) thay vì 2.
- Vòng lặp kiểm tra hành vi trên `v1.0.1`, `v1.1.0`, `master` – dòng `v1.1.0` in
  **0** thay vì 1 (tìm `'lion'` không ra *The Lion King*). Đây là bằng chứng mạnh
  nhất vì kiểm tra **hành vi**, không chỉ lịch sử.
- Lưu ý: `git tag --contains <FIX_SHA>` **không** phát hiện được, vì cherry-pick
  tạo commit mới (SHA khác); lệnh này luôn chỉ ra `v1.0.1` dù đã lan truyền hay chưa.

## 3. Vì sao ở Phần A chưa gắn tag `v1.1.0`?

- Tag là baseline **bất biến**, đã chia sẻ thì không xóa/không di chuyển. Lúc cắt
  `release/lab05`, lỗi `search_by_title` (có từ Lab 02) đã được báo; nếu gắn
  `v1.1.0` ngay thì `v1.1.0` sẽ chứa lỗi đã biết và bản sửa buộc phải phát hành
  thành `v1.1.1`.
- Nhánh release được tạo trước để **ổn định hóa** (nhận hotfix qua PR), tag chỉ
  gắn khi baseline đã hoàn chỉnh và được kiểm thử (sau khi cherry-pick bản sửa).

## 4. Vì sao không merge cả nhánh hotfix vào `master`?

Nhánh hotfix có 2 commit: (1) sửa lỗi + test, (2) `chore: bump version to 1.0.1`.
Commit (2) chỉ đúng cho dòng 1.0.x; `master` đang ở 1.1.0 → merge sẽ xung đột ở
`aims/__init__.py`/`CHANGELOG.md`, và nếu giải sai sẽ **kéo lùi phiên bản** của
`master`. Vì vậy chỉ `cherry-pick -x` đúng commit (1). Đó cũng là lý do commit sửa
lỗi phải **tách riêng** khỏi commit nâng phiên bản.

## 5. Vì sao dùng `cherry-pick -x`?

`-x` thêm dòng `(cherry picked from commit <FIX_SHA>)` vào thông điệp commit mới,
tạo liên kết truy vết giữa các bản sao của cùng một bản sửa trên nhiều dòng phiên
bản; Phần F dùng chính dòng này để kiểm toán (`git log --grep`).
