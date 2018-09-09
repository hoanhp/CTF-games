http://challenge01.root-me.org/web-serveur/ch16/?files=/../admin
Lỗi LFI này giúp ta có thể dễ dàng truy cập vào các file khác của thư mục web
( LTV sử dụng những kĩ thuật như include(), require()...để chèn file vào code tuy nhiện lại dùng một biến khác để chứa tên file mà không chèn trực tiếp =>attacker sử dụng điểm yếu này đề modify URL nhằm đọc được các file nhạy cảm khác)
