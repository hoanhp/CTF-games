At first, you must determine kind of vulnerability of the challenge. For this instance, i khown that it can be exploited by SQL after trying inject ' ' ' follow the password
then , i use length() and count function in SQL to check names of columns, length of password of the admin user
final payload to bruteforce pass :D :
username=blabla&password=1' or ((select substr(password,1,1) from users where username='admin') > 'a') -- -
Note: if you use 'select' after 'where' as a condition, you have to be sure that the return value be always a number ;) 
