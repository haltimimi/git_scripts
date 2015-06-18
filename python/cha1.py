import string
all_letters = string.lowercase
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print all_letters
lst1 = [x for x in text]
#print lst1
letters = []
for l in all_letters:
	letters.append(l)

letters_shifted = all_letters[2:] + all_letters[:2]

print letters_shifted
#print text.split(' '),

result = []
for letter in lst1:
	for i, v in enumerate(letters):
		if letter == v:
			result.append( letters_shifted[i] )
		elif letter == ' ':
			result.append(' ')
			break
		elif letter == '.':
			result.append('.')
			break

print ''.join(result)




#def subs(text):
	
	#for i in text:
	#	if i == 'k':


