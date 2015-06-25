# 
import re 

str1 = r"Hi there, % how are you? hope $name is %s good,  are yes aaa bbb ccc, it's 2014 june 14 and will be 12 xxx 1003 "
match1 = re.sub('\?','', str1)
print match1

match2 = re.sub('h','',str1)
print match2

r1 = re.compile('are')
m1 = r1.search(str1)
print m1.group()


regex2 = re.compile(r'\d+')
match_list = regex2.findall(str1)
print ''.join(match_list)
print match_list
print ' Notice that findall will retrun a list'
print ' in order to have all results from findall'
print ' I will need to use join()'
print ' this list will be from the group()'
print '=----------------------------------'
regex3 = re.compile(r'[0-9]{2,}([^0-9]{2,})[0-9]{2,}')
match_r3 = re.findall(regex3,str1)
print ''.join(match_r3)

print '---------'

str2 = "%%$@_$^__#)^)&!_+]!*@&^}@[@%]()%+$&[(_@%+%$*^@$^!+]!&_#)_*}{}}!}_]$[%}@[{_@#_^{*"
match3 = re.sub('[@%#()!^*$\[\]_&+{}]','',str2)

str3 = "JukystpMZrhBgLqRVMpaIPsyAvYIsBDVqKNCMLqLwyhJhuWDdCPBgSzJTLkJvaGPirOFwfuMtkyXeKoZ"
match4 = re.findall('[A-Z]', str3)
print ''.join(match4)

match5 = re.match('[A-Z]{3}', str3)
print match5

match6 = re.search('[A-Z]{3}', str3)
print match6.group()

line = 'JukystpMZrhBgLqRVMpaIPsyAvYIsBDVqKNCMLqLwyhJhuWDdCPBgSzJTLkJvaGPiXXXiXXXrOFwfuMtkyXeKoZ'
r = re.compile(r'([A-Z])\1{2}(?P<middle>[a-z])\1{3}')
m = r.match(line)
if m is not None:
    print m.group('middle')

'''
r = re.compile('([A-Z]\1{2})(?P<middle>[a-z])\1{3}')
m = r.match(line)
if m is not None:
	print m.group('middle')

'''
print match1
print match2
print match3