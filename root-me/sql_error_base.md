This challenge took quite much time from me. At first, I thought it's just a basic sql error base and the database will be still mysqli as almost other time.
In first step, we need to find out the injectale point(s). By adding some characters like ', ", ), -- - . I quickly detect that we can inject into the argument named "order" (full path: http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=ASC)
So i tried some popular ways to exploit SQli as using UNION SELECT, ORDER BY but almost not work. Until then, I still beleive that They use Mysql Database (It's the biggest mistake)
After few hours for searching and trying many different ways, finally I realize DB totally can be something else. So lucky for me, i found some hints about PostgreSQL, after using some tricks, I completely confirm It's extractly what I am looking for.
i got a nice tutorial in exploiting SQLi for PostgreSQL here (https://forum.sqliwiki.com/printthread.php?tid=30)
And the rest was so easy, I step by step got the table_name, column_name, username, password. In the last step, by logging in as admin, You could capture the flag
My final payload below:
http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=,(select cast((select concat(us3rn4m3_c0l,CHR(58),p455w0rd_c0l) from m3mbr35t4bl3 limit 1 offset 0 ) as int))-- 
