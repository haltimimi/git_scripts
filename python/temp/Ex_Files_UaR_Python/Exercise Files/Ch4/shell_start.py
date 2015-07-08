#
# Example file for working with filesystem shell methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

import os 
import shutil 
from os import path
from shutil import make_archive 
from zipfile import ZipFile

def main():
	fileName = 'textfile2.txt'
	# if path.exists(fileName):
	src = path.realpath(fileName)
	# 	head, tail = path.split(src)
	# 	print 'Path:', head
	# 	print 'FileName:', tail 

	# dst = src + '.bak'
	# shutil.copy(src,dst)

	# os.rename(dst, 'yep.txt')
	root_dir, tail = path.split(src)
	shutil.make_archive("archive", "zip", root_dir)
	


if __name__ == "__main__":
  main()
