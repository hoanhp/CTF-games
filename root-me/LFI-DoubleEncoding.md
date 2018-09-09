![GitHub Logo](/web_security/root-me/asset/LFI-encode.png)

Ở bài này, fuzz chút là có thể thấy được LFI, tuy nhiên khó hơn chút là các kí tự 
".", "/" đã bị filter. Ta sẽ bypass bằng cách encode các kí tự này 2 lần để cheat các filters. 
Cách lấy source code vẫn là sử dụng phpfilter bas64
