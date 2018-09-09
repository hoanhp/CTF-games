Ứng dụng điều khiển truy cập vào nội bộ bị hạn chế trang bằng cách chuyển hướng người sử dụng không được chứng thực đi đến một số page nào đó , thường là trang đăng nhập.
Điều này thường được thực hiện bằng cách sử dụng status line:  '302 Found'- Phản ứng chuyển hướng HTTP.
Trong PHP, mã  '302 Redirection' không ám chỉ dừng việc thực hiện các
mã được viết dưới nó. Kết quả là, http response vẫn chứa
đáp ứng đầy đủ HTML của trang như bình thường. Dùng burpsuit để bắt response và view source để lấy flag