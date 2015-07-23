'''
>>> somestr = 'address 66.7.251.69'
>>> new_match  = re.search(r'(?P<type>\w+) (?P<ip_address>\S+)', somestr)
>>> new_match.group('type')
'address'
>>> new_match.group('ip_address')
'66.7.251.69'

'''
import re, os 
from os import path

# open the file 
def openFile(fileName):
	# check if file exist: 
	if not path.isfile(fileName): 
		print ("Error: File doesn't exist")
		exit(1) 

	lst1 = []
	with open(fileName, 'r') as f: 
		for line in f:
			#print line.rstrip('\n')
			addr_rgx = re.compile(r'address\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
			addr = re.findall(addr_rgx,line)
			lst1 += addr
		#print lst1
		lst1 = list(set(lst1))

		for ip in lst1: 
			x = ip[:3]
			if x == "10.":
				print ("internal IP: ", ip)
			elif x == "66." or x == "71.":
				print ("External IP: ", ip)
			else: 
				print ("Other Subnet ip:", ip)





# file name should be an argument 
filename = ''
openFile('configs/interfaces')
