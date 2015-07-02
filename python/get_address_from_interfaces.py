'''
>>> somestr = 'address 66.7.251.69'
>>> new_match  = re.search(r'(?P<type>\w+) (?P<ip_address>\S+)', somestr)
>>> new_match.group('type')
'address'
>>> new_match.group('ip_address')
'66.7.251.69'

'''
import re

# open the file 
def openFile(fileName):
	lst1 = []
	with open(fileName, 'r') as f: 
		for line in f:
			#print line.rstrip('\n')
			addr_rgx = re.compile(r'address\s(\d{1,}\.\d{1,}\.\d{1,}\.\d{1,})')
			addr = re.findall(addr_rgx,line)
			lst1 += addr
		#print lst1
		lst1 = list(set(lst1))

		for ip in lst1: 
			if ip[:2] == 10:
				print "internal IP: ", ip
			elif ip[:2] == 66 or ip[:2] == 71:
				print "External IP: ", ip
			else: 
				print "Dmz ip:", ip





# file name should be an argument 
filename = ''
openFile('configs/interfaces')
