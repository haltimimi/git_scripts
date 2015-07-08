def remove_duplicates(lst):
    result = []
    for x in lst:
    	if x not in result:
    		result.append(x)
    print result
        
remove_duplicates([2,3,4,5,4,5])