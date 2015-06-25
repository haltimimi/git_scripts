import re

def  report_duplicates(passwd):
   # print passwd
    result = []
    for i in passwd:
        regex = re.compile(r'(\d+):\d+')
        match = re.findall(regex,i)
        result += match
    #for i in match:
    #    regex = 
    #print result 
    # x in result:
    #    if 
    
    
    lst1 = []
    for x in result:
        if x not in lst1:
            lst1.append(x)
   # print lst1, result
    
    lst2 = []
    #for w in result:
    #   if w is not in lst1:
    #            lst2.append(w)
    #print lst2
        
        
    
    

_passwd_cnt = int(raw_input())
_passwd_i=0
_passwd = []
while _passwd_i < _passwd_cnt:
    _passwd_item = raw_input()
    _passwd.append(_passwd_item)
    _passwd_i+=1

    

report_duplicates(_passwd);


