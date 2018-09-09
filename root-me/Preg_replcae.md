Lỗi của bài này được mô tả khá rõ ràng ở đây:
https://bitquark.co.uk/blog/2013/07/23/the_unexpected_dangers_of_preg_replace
Vắn tắt:

	* Hàm preg_replace(pattern, replacement, string) của php cho phép người dùng sử dụng regex để thay thế nội dung trong string và return string mới, nguy hiểm nằm ở tùy chọn /e ở regex nó khiến cho đoạn replacement sẽ được đáp vào hàm eval(), nghĩa là replacement sẽ được thực thi như code php

Payload:
search=/.*/e&replace=file_get_contents('flag.php')&content=test

Lưu ý: trong khi sử dụng e modifier thì " Single quotes, double quotes, backslashes (\) and NULL chars will be escaped by backslashes in substituted backreferences" => cần phải tránh sử dụng hoặc bypass qua phần này
