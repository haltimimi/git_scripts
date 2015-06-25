from collections import Counter
lst = [7,1,2,3,4,1,3,4,2,55]

print "Original lst: ", lst


non_dup = []
for x in lst:
	if x not in non_dup:
		non_dup.append(x)

result = []
for l1 in non_dup:
	if l1 not in lst:
		result.append(l1)

print lst
print non_dup
print result

# remove duplicates
xx = set(lst)
# To make a list out of anything use the command list
print "Set:",list(xx)
h = list('haider')
print h
print sorted(h)

print h.count(3)


c = Counter(lst)
print "Using counter:", sorted(c)
print "Using set: " , list(set(lst))
print "Dic Items (Counter items): ", c.items()
print "duplicates", [k for k, v in c.items() if v > 1]



mylist= [4,1,2,3,4,3,4]
#[i for i,v in enumerate(lst) if lst.count(v) > 1
print "Indices: ", [i for i, x in enumerate(mylist) if mylist.count(x) > 1]
