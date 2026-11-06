# Trả lời câu hỏi thảo luận – Lab 04

## 1. Vì sao chuẩn bị phát hành (`__version__`, `CHANGELOG.md`) trên `master` trước, không sửa trực tiếp trên nhánh `release/*`?
- Trong mô hình **Release Flow**, nhánh `release/*` chỉ đóng vai trò **đóng băng baseline** từ `master` và không bao giờ merge ngược lại vào `master`.
- Nếu sửa `__version__` và `CHANGELOG.md` trực tiếp trên `release/lab04`, nhánh `master` sẽ thiếu thông tin phiên bản `1.0.0` và lịch sử `CHANGELOG.md` của bản phát hành đó (hoặc buộc phải cherry-pick ngược lại). Chuẩn bị trên `master` (qua nhánh `topic/prepare-release-1.0.0` + PR) giúp cả `master` lẫn `release/lab04` cùng chia sẻ chính xác một commit baseline trước khi tách nhánh.

## 2. Vì sao `release/*` không merge ngược vào `master`? So sánh với GitFlow.
- **Vì sao `release/*` không merge vào `master` trong Release Flow:**
  - Nhánh `release/*` là dòng bảo trì riêng của một phiên bản đã phát hành (chứa số hiệu phiên bản riêng của dòng đó, ví dụ `1.0.1`), trong khi `master` đã tiến lên phiên bản tiếp theo (`1.1.0` hoặc `2.0.0`). Nếu merge cả nhánh `release/*` vào `master` sẽ gây xung đột số phiên bản và kéo theo các cấu hình chỉ dành riêng cho bản cũ. Thay vào đó, các bản vá lỗi (hotfix) chỉ được trích chọn phần mã sửa lỗi sang `master` bằng `git cherry-pick -x`.
- **So sánh với GitFlow:**
  - **GitFlow:** Có 2 nhánh dài hạn (`main`/`master` và `develop`). Nhánh `release/*` tách ra từ `develop`, hoàn thiện trên `release/*`, sau đó **phải merge vào cả `main` lẫn `develop`** rồi xóa nhánh `release/*`. Phù hợp với sản phẩm đóng gói có chu kỳ phát hành dài.
  - **Release Flow:** Chỉ có 1 nhánh tích hợp chính (`master`). Nhánh `release/*` tách ra từ `master` để đóng băng và duy trì song song nhiều phiên bản phát hành/nộp bài, **không merge ngược vào `master`**. Quy trình gọn nhẹ hơn, giữ đồ thị lịch sử đơn giản và hỗ trợ bảo trì đa phiên bản trực quan.

## 3. Vì sao nâng phiên bản lên `1.0.0` mà không phải `0.4.0`?
- Theo quy ước **Semantic Versioning (`MAJOR.MINOR.PATCH`)**:
  - Dải phiên bản `0.y.z` (`v0.1.0`, `v0.2.0`, `v0.3.0` ở Lab 01–03) dùng cho giai đoạn phát triển ban đầu (*initial development*), khi cấu trúc gói và API còn thay đổi liên tục.
  - Ở Lab 04, sản phẩm AIMS-mini đã hoàn thiện các chức năng cốt lõi (quản lý giỏ hàng, tìm kiếm, tính tiền chiết khấu, kiểm thử tự động `unittest`, tài liệu hóa và `CHANGELOG.md`) và lần đầu tiên được đóng băng baseline chính thức để xuất bản **GitHub Release** cho người dùng, do đó cần chuyển sang phiên bản ổn định đầu tiên là **`1.0.0`**.
