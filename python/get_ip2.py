import re
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


ips = get_var_list(0)
codes = get_var_list(8)

print(set(ips))
print(set(codes))