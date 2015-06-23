# Get ip addresses from interfaces file
import re

class host_info(object):
	def __init__(self, hostname):
		self.hostname = hostname 

	def file_regex(self,file_name,regex):
		result = ()
		with open(file_name, 'r') as f:
			for line in f:
				output = re.search(regex,line,re.M|re.I)
				if output:
					result += output.group(),
				else:
					print 'no out',
					break 
		print result 

	def get_ip(self):
		pass

something = host_info('b2b-int01')
something.file_regex('configs/file2.txt','([a-z])')