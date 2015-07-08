from collections import Counter

lst1, lst2 = [], []

def ip_count(file1):
	with open(file1, 'r') as f:
		for line in f:
			lst1 = line.split(",")
			lst2.append(lst1[2])

		c = Counter(lst2)
		counter = 0
		for k, v in c.items():
			print k 
			if v == 1 : 
				counter += 1 
		print "number of unique ips is:", counter

			#print lst1
			#print line.rstrip('\n')
			#print line.strip(',')[4]
			#print line[5:].rstrip('\n')

	# print lst1, lst2



		

ip_count('temp/amazon.txt')