text ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

import string 

alfa = string.lowercase 
alfa_lst = [x for x in alfa]
new_list = alfa_lst[2:] + alfa_lst[:2]
print ''.join(new_list)

text_in=[]
for letter in text:
	for i, v in enumerate(alfa_lst):
		if v == letter:
			text_in.append(i)
		if v == ' ':
			text_in.append(i)

#print text_in
result=[]
for m in text_in:
	result.append(new_list[m]),

print ''.join(result)

