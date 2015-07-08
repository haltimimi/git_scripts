def multi_arg(f, s, t, *num):
	print f, s, t 
	print 'rest of arguments: ', list(num)
	args = list(num)
	#print 'each argumet', [w for w in args]
	#x for x in args
	print 'each argumet seperate', ', '.join(str(x) for x in args)

multi_arg(1, 2, 4, 53,54 ,34,'hi')

def main(arg1):
	
