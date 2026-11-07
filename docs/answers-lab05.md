# Trả lời câu hỏi thảo luận – Lab 05

## 1. Vì sao ở Phần A khi mới tạo `release/lab05` lại chưa gắn tag `v1.1.0` ngay?
- Tag trong Git (`v1.1.0`) dùng để định danh **bất biến** một commit phát hành chính thức và **không bao giờ được di chuyển hay xóa sau khi đã chia sẻ**.
- Ở Phần A, nhánh `release/lab05` mới ở trạng thái đóng băng ứng viên phát hành (*release candidate*). Trong quá trình kiểm thử/duyệt trước khi phát hành chính thức, lỗi tìm kiếm phân biệt hoa thường (#21) được phát hiện và cần cherry-pick bản vá sang `release/lab05`.
- Nhờ chưa gắn tag `v1.1.0` ở Phần A, ta có thể đưa bản vá vào `release/lab05` rồi mới gắn tag `v1.1.0`. Nếu đã trót gắn tag `v1.1.0` từ Phần A thì sau khi vá lỗi bắt buộc phải nâng phiên bản và phát hành tag mới là `v1.1.1`.

## 2. So sánh ưu, nhược điểm của *Upstream First* (Microsoft Release Flow) so với *Release First* (Release Flow của học phần)?
- **Release First (tạo `hotfix/*` từ `release/*` bị lỗi, sau đó `cherry-pick -x` về `master` và các nhánh `release/*` khác):**
  - *Ưu điểm:* Bản vá được phát triển và kiểm thử trực tiếp trên đúng môi trường mã nguồn của phiên bản đang chạy thực tế (`v1.0.0`), đảm bảo không kéo theo các tính năng mới chưa ổn định từ `master` vào bản vá `v1.0.1`. Phù hợp với bài tập nộp theo tuần hoặc khi cần vá gấp một baseline cũ đã cách xa `master`.
  - *Nhược điểm:* Nếu quên `cherry-pick` ngược về `master`, lỗi sẽ tái xuất hiện ở các bản phát hành tương lai (*regression*).
- **Upstream First (sửa trên `master` trước, sau đó `cherry-pick -x` lùi về `release/*`):**
  - *Ưu điểm:* Đảm bảo `master` luôn có bản sửa lỗi đầu tiên, không bao giờ xảy ra tình trạng lỗi đã sửa ở bản cũ nhưng bị quên trên `master`.
  - *Nhược điểm:* Nếu `master` đã thay đổi cấu trúc mã nguồn quá nhiều so với nhánh `release/*` cũ, việc `cherry-pick` lùi về `release/*` dễ gặp xung đột hoặc phụ thuộc vào mã mới chưa có ở bản cũ.

## 3. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?
- Có 3 lệnh ở Phần F sẽ lập tức phát hiện việc thiếu bản sửa trên `release/lab05`:
  1. `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`: Sẽ chỉ hiện **1** commit (trên `master`) thay vì **2** commit (trên cả `master` và `release/lab05`).
  2. `git cherry -v origin/release/lab05 origin/release/lab04`: Commit sửa lỗi `fix: make search_by_title case-insensitive` sẽ mang dấu **`+`** (chưa có commit tương đương trên `release/lab05`) thay vì dấu **`-`**.
  3. Vòng lặp kiểm tra hành vi thực tế (`for ref in v1.0.1 v1.1.0 master; do ...`): Tại mốc `v1.1.0` (`release/lab05`), kết quả `len(search_by_title(..., 'lion'))` sẽ in ra **`0`** thay vì **`1`**.
