def median(numbers):
    l = len(numbers) # 4 
    numbers = sorted(numbers)
    print numbers
    if l % 2 == 0:
    	print 'even', numbers[l/2-1:l/2+1]
    	return (numbers[l/2] + numbers[l/2-1]) / 2.0 
    	#print float(median)
    else:
    	return numbers[l/2]

    

median([1,7,19,8,10,3])