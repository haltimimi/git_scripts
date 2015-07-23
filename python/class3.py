
class Node(object):
	test = "testing"
	def __init__(self,value):
		self.value = value
		self.x = "this is x in init"

	def new(self,man=3):
		y = 'hi there new one, your first value is '+ self.value # if you only user value it will break, bc it's not define in that function 
		self.test = ' Inside New def testing '
		f = 'hi, am new instance with global variable '+self.value + self.test 
		print (man*2) 
		print (y, f)

h = Node('VALUE')
# To get the return value of a function you will need to use the ()
h.new(man = 5)
# To get the value of a variable then you can just use the instance with variable. no peranthases 
print (h.x)
h.x = "Changed the value"
w = h.x 
print (w)
# now we call a global variable named y from the class 
print (h.test)


