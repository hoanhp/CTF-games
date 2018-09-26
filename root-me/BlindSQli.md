- At first, you must determine the kind of vulnerability of the challenge. 
- For this instance, we khown that it can be exploited by SQL after trying inject ' follow the password
- Then , use length() and count function in SQL to check names of columns, length of password of the admin user
- Finally, modify your payload to get the pass
Note: if you use 'select' after 'where' as a condition, you have to be sure that the return value be always a number ;) 
