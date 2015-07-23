# create a class that will get the 
import urllib.request as req 
import re 

def getNum(num):
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(num)
	with req.urlopen(url) as response:
		result = response.read()
		# Filter the result to return only number 
		regex = re.compile(r'[0-9]{2,}')
		match = regex.search(str(result))
		if match:
			return match.group()	

x = getNum(1234)
print (type(x))
print (x+2)

list = []
while isinstance(x,int):
	x = getNum(x)
	print('this is', x)
	
print (list)  




