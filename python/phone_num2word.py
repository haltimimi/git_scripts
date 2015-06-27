# we want to enter a phone number and output a list of possible words.
# if you type 1, possible words are aa, ab, ac, ba, bb, bc, ca, cc ,cd 

import string 
from collections import defaultdict

def phone2(num):
	alfa = list(string.lowercase)
	#print alfa
	d1 = defaultdict(list)
	#print alfa[:3]
	x, count = 0, 1 
	for i in range(3,len(alfa),3):
		count += 1 
		if count == 6 or count == 7: 
			i += 1 
		if count == 8:
			i += 2 
		#print alfa[x:i], x, i, count 

		d1[count].append(alfa[x:i])
		x = i 
	print d1
	print d1[9]
	''' 
	d = defaultdict(list)
	for k,v in enumerate(l1):
		d[k+1].append(v)
	
	print d
	'''



phone2(12)