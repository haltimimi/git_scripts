import re

result = ''
# open file 
with open('file2.txt', 'r') as f:
	for line in f:
		#print line  
		#match = re.sub('[a-z]','',line)
		#print match
		#match = re.search('([A-Z]{3})([a-z])([A-Z]{3})', line)
		
		#r = re.compile(r'([A-Z])\1{2})(?P<middle>[a-z])\1{3}')
		r = re.compile(r'(?<=[A-Z]{3})[a-z](?=[A-Z]{3})')
		m = r.finall(line)
		if m is not None:
			print m
		#print m

		#print match.group(3)
		#result += match2 

#print result 