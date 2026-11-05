# Changelog

Mọi thay đổi đáng chú ý của AIMS-mini được ghi tại đây.
Định dạng theo [Keep a Changelog](https://keepachangelog.com/vi/1.1.0/),
đánh số phiên bản theo [Semantic Versioning](https://semver.org/lang/vi/).

## [Unreleased]

## [1.0.0] - 2026-11-05
Phiên bản ổn định đầu tiên. API công khai được cam kết tương thích theo SemVer:
`DigitalVideoDisc`, `Cart` (`add_dvd`, `remove_dvd`, `total_cost`,
`total_cost_with_discount`, `print_cart`), `aims.search.search_by_title`.
### Added
- `aims.__version__`; `main.py` in `AIMS-mini v<version>`.
- `CHANGELOG.md`.

## [0.3.0] - 2026-11-05
### Added
- `Cart.total_cost_with_discount(percent)`: tổng tiền sau giảm giá, kiểm tra 0 ≤ percent ≤ 100.
- Thông báo tiếng Việt khi thêm đĩa vào giỏ.
- Unit test (`tests/`) cho giỏ hàng, giảm giá và tìm kiếm.
### Fixed
- Giỏ hàng nhận đĩa thứ 21 dù giới hạn là 20 (#10).
- `total_cost_with_discount` trả về số tiền được giảm thay vì tổng tiền sau giảm.

## [0.2.0] - 2026-11-05
### Added
- `Cart.print_cart()` (in "The cart is empty" khi giỏ trống) và dùng trong `main.py`.
- `aims.search.search_by_title()`.
- Tài liệu use case, pull request template.

## [0.1.0] - 2026-11-03
### Added
- `DigitalVideoDisc`, `Cart` (thêm/xóa đĩa, tổng tiền) và chương trình demo.
### Changed
- Tổ chức mã nguồn thành package `aims`.

[Unreleased]: https://github.com/minhpham1512/it3180-202416279-aims/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/minhpham1512/it3180-202416279-aims/compare/v0.3.0...v1.0.0
[0.3.0]: https://github.com/minhpham1512/it3180-202416279-aims/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/minhpham1512/it3180-202416279-aims/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/minhpham1512/it3180-202416279-aims/releases/tag/v0.1.0
