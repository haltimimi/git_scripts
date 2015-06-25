# Get ip addresses from interfaces file
import re

class host_info(object):
	def __init__(self, hostname):
		self.hostname = hostname 

	def file_regex(self,file_name,regex):
		result = ()
		with open(file_name, 'r') as f:
			for line in f:
				output = re.search(regex,line)
				if output:
					#result += output.group(0)
					print output.group(0)
		#print result 

	def print_all(self, file_name):
		count = 0
		with open(file_name) as f:
			for line in f:
				count += 1
				# using rstrip to remove all white spaces in a string before printing including \n (newlines)
				print "line#%s => %s" % (count, line.rstrip('\n'))

		

something = host_info('b2b-int01')
something.file_regex('configs/file2.txt',r'[0-2]?[0-2]?[0-5]?.[0-2]?[0-2]?[0-5]?.[0-2]?[0-2]?[0-5]?.[0-2]?[0-2]?[0-5]?')
something.file_regex('configs/file2.txt',r'\d{1,3}\.\d{1,3}')
print '-------'
something.file_regex('configs/file3.txt', '[0-2]?[0-2]?')
something.file_regex('configs/file3.txt', r'([0-9])\1+' )


print '----------'
something.print_all('configs/file3.txt')
something.print_all('configs/file2.txt')