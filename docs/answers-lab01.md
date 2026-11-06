# Câu hỏi thảo luận Lab 01

## 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
- **`--global`**: Được lưu ở thư mục người dùng (`~/.gitconfig` hoặc `~/.config/git/config`), áp dụng cho mọi repository của người dùng đó trên máy.
- **`--local`**: Được lưu trong tệp `.git/config` của riêng repository hiện tại, chỉ có hiệu lực trong repo đó và có độ ưu tiên cao hơn `--global`.

## 2. Vì sao dùng `git mv` thay vì xóa tệp cũ và tạo tệp mới?
- `git mv` thực hiện đồng thời việc di chuyển tệp trên đĩa và ghi nhận ngay vào vùng Staging (Index), giúp Git nhận diện rõ đây là thao tác đổi tên/di chuyển (`renamed`) và giữ nguyên lịch sử thay đổi của tệp qua các lần đổi tên (`git log --follow`).

## 3. `release/lab01` có phải là một baseline không?
- **Có.** `release/lab01` đại diện cho một phiên bản cấu hình đã hoàn chỉnh, thống nhất tại thời điểm kết thúc Lab 01 để bàn giao/chấm điểm và không sửa đổi trực tiếp trên đó.

## 4. Vì sao không commit thẳng lên `master` dù làm một mình?
- Để tuân thủ quy trình kiểm soát thay đổi (Change Control): mọi thay đổi được cô lập trên nhánh riêng giúp `master` luôn ở trạng thái ổn định, đồng thời việc tạo Pull Request giúp tự rà soát lại diff (`Files changed`), kiểm tra trước khi tích hợp và lưu vết lịch sử rõ ràng theo từng mục đích.
