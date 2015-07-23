# use url library to get a web page:
import urllib.request as req
from os import path
import re
import random 

class link():
	def __init__(self, value):
		self.value = value 
		self.next = None
	def next(self):
		next_node = value + 55
		return next_node 


with req.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345') as response:
	html = response.read()
	#html2 = str(html)
	reg = re.compile(r'[1-9]{2,}')
	match = reg.search(str(html))
	print (match.group()) 

def get_next(new_num):
	url = "x="+str(num)
	rand = int(random.uniform(1,10000))
	return rand

new_num = get_next(11)


#print (html)
#print (file)