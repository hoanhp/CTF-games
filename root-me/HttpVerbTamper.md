Bài tập này là về phần method của http request. Đầu tiên ngay khi chung ta Start challenge thì một hộp thoại xác  thực đã hiện ra. Hộp thoại này không phải do người dùng lập trinh ra mà là do họ sử dụng một công cụ xác thực có tên là htaccess. Tìm hiểu thêm và htaccess ( https://www.alertlogic.com/blog/blackhat-review-of-htaccess-tricks/ )
Một file htaccess có dạng:  
AuthName “restrict posting”  
AuthType Basic  
AuthUserFile /usr/local/etc/httpd/users  
< Limit POST >  
require group staff  
< /Limit >  

Tạm thời ta chỉ quan tâm tới phần nắm trong the LIMIT. Nó sẽ quy định những method nào khi gửi lên thì hộp thoại xác thực mới được phép alert. Và lợi dụng điểm yếu này mà một hacker có thể thay đổi method ( quá đơn giản với các tool như bây giờ ) và thế là ta đã có thể vượt qua phần xác thực => get pass
