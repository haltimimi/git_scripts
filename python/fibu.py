# give a number,
# print out the fibonacci sequence 

# x = list(range(7))
# print x 
0,1,1,2,3
#for i,v in enumerate(x):
x = [0,1]
r = 55

for w in range(2,r):
	m = x[w-1] + x[w-2]
	if m >= r+1:
		break
	else:
		x.append(m)
print x 

def fib(n):
	x = [0,1]
	# while w >= n: 

d1 = {'ali':[1,2,3],
	2: [4,5,5],
	'nope': 'hello'
}
d1[3]="New value"
print d1.items()
d1['haider']= "string"
d1['ali'] = [1,2,3,4]
d1[3]=None
d1
print "d1 after modification", d1.items()

for k,v in d1.items():
	#print "type of key %s is %s" % (k, type(k))

	if type(k) is str:
		print "%s Key is string" % k
	else:
		print "%s key is NOT string" % k

d1['ali']=None


