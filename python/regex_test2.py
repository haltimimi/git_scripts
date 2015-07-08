import re

url = r'www.site.com'
r = re.compile(r'^www')
m = r.match(url)
if not m:
	print "site it wrong"
url = 'www' + url 


