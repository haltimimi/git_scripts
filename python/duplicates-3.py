from collections import defaultdict

def find_duplicates(file1):
	uid_lst = []
	users_lst = []
	a = defaultdict(list)
	with open(file1, 'r') as f:
		for line in f:
			uid = line.split(':')[2]
			user = line.split(':')[0]
			a[user].append(uid)
			uid_lst.append(uid)
			users_lst.append(user) 
	# print out only the users with multiple uids
	# set() will make sure there are no duplicates in the list.
	for k in a:
		if len(set(a[k])) > 1:
			print "user (", k , ") has the following uids:", ", ".join(x for x in a[k])

find_duplicates('configs/passwd')
