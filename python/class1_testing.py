class Car(object):
	first = 'Mazda'
	second = 'BMW'
	def __init__(self,name):
		self.name = name
		self.second = 'BMW Indeed' 

# Create an instance of Car class 
mycar = Car('I love it')

# Change the class variables (global variable)
Car.first = "Nothing"
print (Car.first)
# Test the instance variable value, it did change
print (mycar.first)

# Change the class variable (global variable), which is also a self variable.
# Watch that the instance value doesn't change 
Car.second = "Ford"
print ("Class second car is", Car.second)
print ("Init function second car is", mycar.second)
print ("Init function name is ", mycar.name)

mycar.second='Convertible'
print (mycar.second)


