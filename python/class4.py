class Team(object):
	def __init__(self,name):
		self.name = name 
	def __str__(self):
		return "my team is " + self.name 
	def __call__(self):
		print("I am just a team class!")
	class Player(object):
		def __init__(self,name):
			print ('I am a player',name)


t1 = Team('Droiders')
print (t1) 

# t1 is an instance of the class Team
print (type(t1))

# however type of Team should be class but it shows type 
w = type(Team) 
print (w) 

a = 1 
print (type(a))

# is t1 an instance of Team class? every object should be an instance of something else. 
print (isinstance(t1, Team))
# is class Team an instance of type? yes because every object is an instance of something. 
print (isinstance(Team, type))

man = t1.Player('haider')
print (type(man))
