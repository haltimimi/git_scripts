#!/usr/bin/python

import re
phone = raw_input("Enter your phone number, i.e 123-456-7890: ")

# check if the phone number is correct
if re.match(r'^\d{3}-?\d{3}-?\d{4}', phone):
	print "Phone number is correct", phone 
else:
	print "Phone is not correct"

def get_city(area_code):
	if area_code == '408':
		city = 'San Jose' 
		return city
	elif area_code == '647':
		city = 'Sauga'
		return city
	elif area_code == '416':
		city = 'Toronto'
		return city
	else:
		city = 'Un-known'
		return city 

print "City is: ",  get_city(phone[:3])
#print "City: ", x 

# Change the phone number to letters:
dic1 = { 
	'2' : 'a',
	'3' : 'e',
	'4' : 'h',
	'5' : 'k',
	'6' : 'n',
	'7' : 'q',
	'8' : 't',
	'9' : 'x', 	
} 
for digit in phone: 
	print digit














