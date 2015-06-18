

hm = "what @ in the world!"
def reverse(text):
	lst = []
	for l in text:
		lst.append(l)
	#print "Origianl list is", lst
	#print "last char is", lst[len(lst)-1]

	c = len(lst)
	#print "Lenght is ", c
	new_list = []
	for w in range(c-1,-1,-1): 
		#print w 
		new_list.append(lst[w])
	print ''.join(new_list)
	

reverse("Python!")