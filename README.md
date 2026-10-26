# Mediapie_Assignment

Trò Chơi Oẳn Tù Tì (Rock-Paper-Scissors) với MediaPipe

Dự án này là một ứng dụng/game tương tác qua webcam sử dụng ngôn ngữ lập trình Python và thư viện Computer Vision (MediaPipe, OpenCV). Người chơi sẽ thi đấu trực tiếp trò chơi dân gian "Oẳn Tù Tì" với máy tính thông qua việc nhận diện cử chỉ bàn tay.

## **1. Danh sách các thư viện cần thiết (Requirements)**

Để chạy được dự án này, máy tính của bạn cần cài đặt Python 3.x và các thư viện sau:

opencv-python (Dùng để truy cập webcam và xử lý khung hình).

mediapipe (Framework của Google dùng để trích xuất dữ liệu tọa độ các khớp bàn tay - Hand Landmarks).

## **2. Hướng dẫn cài đặt và chạy chương trình**

**Bước 1:** Tải toàn bộ mã nguồn (source code) của dự án này về máy tính và giải nén (hoặc dùng lệnh git clone).

**Bước 2**: Mở Terminal (hoặc Command Prompt / PowerShell) và điều hướng đến thư mục chứa mã nguồn dự án.

**Bước 3**: Cài đặt các thư viện cần thiết bằng lệnh pip:

pip install opencv-python mediapipe


(Lưu ý: Nếu mạng chậm gây lỗi timeout, bạn có thể thêm tham số --default-timeout=1000 vào giữa lệnh install).

**Bước 4**: Chạy chương trình bằng lệnh sau:

python Rock_Paper_Scissors.py


# **3. Hướng dẫn sử dụng (Gameplay)**

Sau khi chạy lệnh ở Bước 4, đèn Webcam sẽ sáng và một cửa sổ ứng dụng sẽ hiện lên.

Bắt đầu: Khi màn hình hiển thị dòng chữ "GIO TAY DE BAT DAU", bạn hãy giơ tay lên khung hình và tạo một trong 3 hình: Búa (nắm tay), Kéo (giơ 2 ngón trỏ và giữa), hoặc Bao (xòe cả 5 ngón).

Đếm ngược: Hệ thống sẽ nhận diện cử chỉ của bạn và bắt đầu đếm ngược 3 giây. Trong khoảng thời gian này, bạn phải giữ nguyên tay hoặc có thể đổi đòn.

Kết quả: Ngay khi hết 3 giây, máy tính sẽ chốt đòn của bạn, đồng thời tung ra một đòn ngẫu nhiên để phản công. Kết quả Thắng/Thua/Hòa sẽ được in lớn lên màn hình.

Ván mới: Màn hình kết quả sẽ dừng lại 3 giây để bạn quan sát, sau đó tự động reset về trạng thái chờ để bạn tiếp tục chơi ván mới.

Thoát game: Để đóng ứng dụng an toàn, bạn hãy bấm phím Q trên bàn phím.

# **4. Video Demo**
