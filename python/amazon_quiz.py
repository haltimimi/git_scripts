# make sure to open a file and can be done in two ways, one is fast the other is slow

# number of words in a file 
with open('configs/interfaces','r') as f: 
	print (len(f.read().split(' ')))

with open('configs/new_1', 'w+') as w:
	w.write('something new!')

# number of letters in a file 
with open('configs/interfaces', 'r') as x:
	file2 = x.read()
	count = 0 
	for l in file2: 
		count += 1 
	print ('letters count is', count) 

# number of words in a file ( this will include spaces of new lines and tabs)
with open('configs/interfaces','r') as f: 
	total = 0
	for line in f:
		line = line.rstrip('\n')
		l1 = line.split(' ')
		print( l1 )
		
		total += len(l1)
		print (total)
	print(total)


