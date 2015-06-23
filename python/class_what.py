class inventory(object):
	# Global variable 
	pingable = True
	def __init__(self,name,ip,sn):
		self.name = name 
		self.ip = ip
		self.sn = sn

	def list_all(self):
		print 'name', self.name
		print 'ip ', self.ip
		print 'sn ', self.sn

	# method that do something
	def add_ip(self,ip):
		if not self.ip:
			self.ip = ip
			print "Added ip"
		else:
			#print "Already has ip", self.ip, "Do you want to chage it? y/n"
			text = 'Current ip is: %s, Enter new ip, or hit Enter to continue', self.ip
			answer = raw_input(text)
			if answer:
				self.ip = answer 
				print "new ip: ", self.ip 
			else: 
				print "Next"



machine = inventory('haider','10.10.13.1','AFGEX')
#print  'ip adress: ', machine.ip,",",machine.pingable
#print 'Serianl number: ', machine.sn

machine.list_all()

machine.add_ip('10.10.13.4')