def count(sequence, item):
	count = 0
	for i in sequence:
		if i == item:
			count += 1

	print count
	print sequence 

count([1,3,4,1,'s','b','b',[1,3]],[1,3])