import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

#print(re.match(r'Love', data))
#print(re.search(r'Kenneth', data))
print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data)) 
# print(re.findall(r'\w+, \w+', data))
# reg = r'\w+, \w+'
# c = re.compile(reg)
# m = c.findall(reg,data)
print(re.findall(r'''
	[\w\d\.\+]+@[\w\d\.]+', data))