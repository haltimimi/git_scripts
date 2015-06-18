to_21 = range(1,22)
odds = to_21[::2]

print to_21
print odds
third = len(to_21) / 3 
middle_third = to_21[third:third*2]
print middle_third
print to_21[0:3]
# this means list[start:length:interval] and not [start:end:interval]
print range(10)