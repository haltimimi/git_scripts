'''
>>> somestr = 'address 66.7.251.69'
>>> new_match  = re.search(r'(?P<type>\w+) (?P<ip_address>\S+)', somestr)
>>> new_match.group('type')
'address'
>>> new_match.group('ip_address')
'66.7.251.69'

'''



