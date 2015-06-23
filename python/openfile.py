def open_file(file_name):
	with open(file_name,'r') as f:
		for line in f:
			print 'this is a new line: ', line


#open_file('file.txt')
