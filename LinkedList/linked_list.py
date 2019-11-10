class Node:
	def __init__(self, data, next: Node):
		self.data = data
		self.next = next

"""
A linked list is another type of a container to hold data
Each item within a linked list is a node and within the node are two attributes:
a data element and a pointer (next)

The data of the node contains the stored value
The pointer of the node is an address to the next node in the linked list
"""
class LinkedList:
	def __init__(self):
		self.__head = None

	def append(self, element):
		new_node = Node(element, None)
		if (self.__head == None):
			self.__head = node
			return node
		next_node = self.__head.next
		while next_node.next != None:
			next_node = next_node.next
		next_node.next = new_node
		return new_node
