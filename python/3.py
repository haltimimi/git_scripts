# this is a comment
def anti_vowel(text):
	lst = ['a','e','i','o', 'u']
	result =[]
	for i in text:
		flag=True
		for b in lst:
			#print i, b
			if i.lower() == b:
				flag=False
		if flag: 
			result.append(i)
	print ''.join(result)

anti_vowel("Hi There How can I help you")

