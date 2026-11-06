# Trả lời câu hỏi thảo luận – Lab 02

## 1. Vì sao phải đồng bộ `master` trước khi gửi Pull Request?
- Trong quá trình phát triển song song, nhánh `master` có thể đã tiến thêm với các thay đổi từ thành viên khác (ví dụ: PR `feature/cart-print` đã được merge trước).
- Việc kéo (`git fetch` + `git merge origin/master`) vào nhánh tính năng trước khi gửi PR giúp phát hiện và giải quyết xung đột (nếu có) ngay trên nhánh riêng, đồng thời kiểm tra tích hợp (`python3 main.py` / chạy test) để đảm bảo tính năng mới hoạt động đúng cùng mã nguồn mới nhất của `master` trước khi đưa ra hội đồng duyệt (reviewer).

## 2. Khi nào không được dùng `rebase`?
- **Không được rebase các nhánh công khai / các commit đã chia sẻ cho người khác cùng làm việc** (như `master`, `release/*`, hoặc nhánh chung nhiều người cùng push).
- Lý do: `git rebase` viết lại lịch sử bằng cách tạo các commit mới với mã băm (SHA) mới. Nếu rebase commit đã được người khác kéo về, lịch sử giữa các máy sẽ bị phân nhánh lệch nhau, buộc người khác phải xử lý lại lịch sử hoặc vô tình tạo các commit trùng lặp khi merge lại.

## 3. Nhánh `feature/*` khác nhánh `topic/*` ra sao?
- **`feature/*`**: Dùng để phát triển các **tính năng phần mềm thuộc nghiệp vụ sản phẩm** trực tiếp phục vụ người dùng cuối (ví dụ: `feature/cart-print`, `feature/search-by-title`).
- **`topic/*`**: Dùng cho các **chủ đề kỹ thuật, tài liệu, cấu hình, hoặc quy trình hỗ trợ dự án** không phải là tính năng nghiệp vụ của ứng dụng (ví dụ: `topic/pr-template`, `topic/use-case-diagram`, `topic/ci-unit-tests`).
