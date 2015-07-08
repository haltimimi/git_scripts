counter = 1 
def someFun():
	global counter
	for x in range(3):
		counter += 1


someFun()

print counter 