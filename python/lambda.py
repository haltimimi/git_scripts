squares = [x**2 for x in range(1,11)] 
print squares
new = filter(lambda i: i > 30 and i < 70, squares)
print new
