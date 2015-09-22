import re, operator
from collections import Counter
# from os import path 

# read file 
log_file = 'apache.log'
ip_address = '10.10.13.1'

def read_file(file_name):
	try:
		return open(file_name, 'r')
		close(filename)
	except FileNotFoundError: 
		print("Error: File \"%s\" doesn't exist" % filename)

def get_var_list(location):
	var_list = []
	for line in read_file(log_file):
		var_list.append(line.split(' ')[location])
	return var_list

def write_data(var_list):
	pass 

ips, codes = get_var_list(0), get_var_list(8)

def values_counts(listname):
	c = Counter(listname)
	return sorted(c.values())	

count_list(ips)
count_list(codes)

# for x in ips:
	# print(x, ips.count(x))
# print([l,m for l,m in get_var_list(0), get_var_list(8)])


