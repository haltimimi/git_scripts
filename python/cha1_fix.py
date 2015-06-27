import string
from string import maketrans

# "string" all the alphabets in lowercase 
intab = string.lowercase
# "outtab", will shift the items in the string by a factor of 2 
outtab = intab[2:] + intab[:2]

trantab = maketrans(intab,outtab)

#text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text = "map"
print text.translate(trantab)