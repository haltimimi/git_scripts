
import urllib2 
import re 
def take_input():
	# url = raw_input('What site?')
	url = r'site.com'
	r = re.compile(r'^www')
	m = r.match(url)
	print m
	return url 

url = take_input()

def url_syntax(url):
	r = re.compile(r'^www')
	m = r.match(url)
	if not m:
		print "Please use the following format: http://www.sample.com"
		# take_input()

# url_syntax(url)

_url_open = urllib2.urlopen(url)

def chk_url(url):
	# _url_open = urllib2.urlopen(url)
	_code = _url_open.getcode()

	if _code == 200 :
		print 'Site is okay'
	else: 
		print 'Site might be down!'
		exit(1)
	
def getCont(url):
	pass 
	# print _code 



chk_url('http://yahoo.com')