import re 

# opening the file 
def opening_file(filename):
	result = []
	with open(filename, 'r') as f:
		for line in f:
			#print line
			# run some 
			match = re.sub('[@%#()!^*$\[\]_&+{}\n]','',line)
			
			result += match

	print result 

opening_file('file.txt')