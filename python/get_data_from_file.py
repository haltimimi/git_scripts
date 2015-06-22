file_name = './configs/test.txt'


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

# Writing data to file 
def write_data(file_name,text):
	f = open(file_name,'w')
	f.write(text)
	f.close 


#write_data(file_name , ' Just add this line (192.168.1.1)\n then add this line (255.255.255.0)\n')





