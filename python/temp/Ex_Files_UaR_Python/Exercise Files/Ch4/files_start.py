#
# Read and write files using the built-in Python file methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
import os 
from os import path

def main():  
	if path.isfile('textfile2.txt'): 
		pass
	else: 
		print "Error: file is not here!"
		print "it should be here:" + str(path.split(path.realpath()))
		exit(1)

	with open("textfile2.txt", 'r') as f:
		#pass
		#for i in range(5):
			#f.write("Adding new lines, this is line %d\n" % (i+1) ) 
		#if f.mode == 'r':
		#	print f.read()
		for line in f:
			print "hi", line.rstrip('\n')
    
if __name__ == "__main__":
  main()
