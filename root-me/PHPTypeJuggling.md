Bài này nhiệm vụ chủ yếu là bypass qua phần xác thực này:
```
    if($auth['data']['login'] == $USER && !strcmp($auth['data']['password'], $PASSWORD_SHA256)){
        $return['status'] = "Access granted! The validation password is: $FLAG";
    }
```
Cả 2 điều kiện trong vế if đều tồn tại điểm yếu về so sánh
1. Ở vế đầu với phép so sánh "==" ta có thể dễ dành bypass nhờ so sánh biến USER với 0 => kết quả luôn True
2. Ở vế thứ 2 với phép so sánh bằng hàm strcmp(), nếu tham số truyền vào là string vs array => kết quả trả về sẽ là Null (+ warning), tuy nhiên NULL == 0 nên => 2 vế bằng nhau đúng với định nghĩa của hàm strcmp()

Payload:
```
auth={"data":{"login":0,"password":["test"]}}
```
Reference:
http://repository.root-me.org/Exploitation%20-%20Web/EN%20-%20PHP%20loose%20comparison%20-%20Type%20Juggling%20-%20OWASP.pdf

Ps:Mọi giá trị trong các biến GET, POST mà Client gửi lên đều được PHP xem như String (bao gồm cả các giá trị nằm trong array hay json) => Cần có các xử lý trên server để convert về kiểu dữ liệu ban đầu (int, string ...)
