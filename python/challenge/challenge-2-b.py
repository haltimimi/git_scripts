import re
m = []
with open('cha2-b','r') as f:
	data = f.read()
	regex = re.compile(r'[A-Z]\1{2}([a-z])')
	#regex = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
	#c = re.compile(r'[A-Z]{3}')
	#print ''.join(regex.findall(data))
	m += regex.findall(data)
	print m 
	