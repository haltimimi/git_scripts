import os 
from os import path
import datetime
from datetime import datetime, date, time 

file_name = './configs/test.txt'

# Check if file exist: 
def check_file(file_name):
	if not path.isfile(file_name):
		# split the path of file to filename and path. put them in a tuple called _f
		_f = path.split(path.realpath(file_name))
		print "Error: File %s doesn't exist in %s" % ( _f[1], _f[0] ) 
		print "File Name: %s" % _f[1]
		# if you use the filename it will print part of the path too
		print "Filename is: %s " % file_name #this will print ./configs/test.txt
		print "Path: %s" % _f[0]
		exit(1) 

check_file(file_name)

def mod_time(file_name):
	_mtime = path.getmtime(file_name)
	_mtime_readable = datetime.fromtimestamp(_mtime)
	return _mtime_readable

print "Modificate time is:", mod_time(file_name)
# 1. Open a file to read the lines,

def get_data(file_name):
	f = open(file_name, 'r')
	output = f.read()
	

get_data(file_name)

# 2. parse these lines, use regex to only get the ip address/gateway/
#def 

# antoher way to get lines
def get_data2(file_name):
	with open(file_name, 'r') as f: 
		for line in f: 
			print "LINE is:", line 


get_data2(file_name)

# Writing data to file like a log file
def write_data(file_name,text):
	f = open(file_name,'w')
	f.write(text)
	f.close 


#write_data(file_name , ' Just add this line (192.168.1.1)\n then add this line (255.255.255.0)\n')





