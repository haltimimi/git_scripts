def purify(lst):
	x = len(lst)
	while x > 0:
		x -=1
		if lst[x] % 2 != 0:
			lst.remove(lst[x])
	return lst

'''
	for i, v in enumerate(lst):
		#print v 
		print i 
		if v % 2 != 0:
			print 'odd number is ', v 
			del lst[i]
			#print lst 
			#i = i - 1
	print lst
'''
purify([1,2,3,4,5,6,7,8,9])

l1 = [1,2,3,4]
l1.remove(l1[0])

