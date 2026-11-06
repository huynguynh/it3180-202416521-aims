# Trả lời câu hỏi thảo luận – Lab 03

## 1. Merge base là gì?
- **Merge base** (tổ tiên chung gần nhất – *best common ancestor*) là commit gần nhất nằm trên lịch sử của cả hai nhánh trước khi chúng tách ra phát triển độc lập (có thể xem bằng lệnh `git merge-base <nhánh-A> <nhánh-B>`).
- Khi thực hiện `git merge` (3-way merge), Git dùng **merge base** làm mốc tham chiếu thứ ba để so sánh với đỉnh của nhánh hiện tại (`HEAD`) và đỉnh của nhánh cần gộp:
  - Nếu một dòng chỉ thay đổi ở một bên so với merge base, Git tự động lấy thay đổi đó.
  - Nếu cả hai bên cùng sửa một vùng mã theo hai cách khác nhau so với merge base, Git báo **xung đột (merge conflict)** để lập trình viên quyết định.

## 2. Vì sao trên nhánh `master` và `release/*` phải dùng `git revert` thay vì `git reset`?
- **`master` và `release/*` là các nhánh lịch sử chung (shared branches)** đại diện cho dòng tích hợp chính và các baseline đã phát hành/nộp bài, được nhiều thành viên cùng kéo về và được bảo vệ bằng Branch Protection (chặn force push).
- **`git reset` viết lại lịch sử** bằng cách dời con trỏ nhánh lùi về commit cũ, làm biến mất các commit đã công bố. Nếu dùng trên nhánh chung sẽ làm lệch lịch sử với các máy khác và phá vỡ tính toàn vẹn của baseline.
- **`git revert` tạo một commit mới đảo ngược nội dung thay đổi** của commit cần hủy mà **không xóa hay sửa lịch sử cũ**. Cách này vừa khôi phục lại trạng thái mã nguồn an toàn qua Pull Request, vừa giữ nguyên dấu vết kiểm toán (audit trail) về việc lỗi được đưa vào khi nào và được hoàn tác khi nào.
