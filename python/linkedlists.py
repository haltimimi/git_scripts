# Testing linked lists
class Node:
	def __init__(self,cargo=None, next=None):
		self.cargo = cargo
		self.next = next 
	''' 
	The __str__ function retruns a string representation of the instance. 
	print function will retrun whatever is in the __str__ method.
	''' 
	def __str__(self):
		return str(self.cargo)

def print_list(node):
	while node:
		print (node),
		node = node.next
	print 





# Dry runs of the Class, 
nodex = Node('test')
print (nodex)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

#print (node2.next )
#print (node1)

# make nodes linked
node1.next = node2 
node2.next = node3 

print_list(node2)