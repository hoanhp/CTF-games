Nhìn vào URL thì ta có thể nhận ra web này có dính lỗi LFI => nó sẽ hiển thị filename được nhập vào URL => cho phép ta có thể truy cập đến các file tùy ý.
Để lấy được source php của file ta cần encode nội dung file trước để server trả về source code=> http://challenge01.root-me.org/web-serveur/ch12/?inc=php://filter/read=convert.base64-encode/resource=login.php

