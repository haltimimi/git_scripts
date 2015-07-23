# args 
def fun(*args):
	for arg in args:
		print arg 

l = [1,2,3,4, 'sam']

fun(*l)
print '--what'
fun(l[1])

print "fun2"
def fun2(x=3,y=3):
	print x*y

fun2()
fun2(x=4,y=23)

''' 
keyword argumets 
'''
def fun3(*args, **kwargs):
	for i in args:
		return i 
	for w in kwargs.items():
		return w 

print fun3('sam', x=3, ww=33)
