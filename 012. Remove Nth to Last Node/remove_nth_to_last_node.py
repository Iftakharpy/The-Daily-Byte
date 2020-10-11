class Node:
	def __init__(self,val=0, nxt=None):
		self.val = val
		self.next = nxt

	def __repr__(self):
		return f"Node(val={self.val}, next={self.next})"
	
	def __eq__(self, other):
		return repr(self) == repr(other)


# this is the one pass technique
# O(n) time traversing the hole linked list
# O(1) space only storing references
def remove_nth_to_last_node(head: Node, n: int) -> Node:
	# this dummy node is to help solve the corner cases
	dumb = Node(0,head)
	end_checker = dumb
	back = dumb

	# to make the difference between back and end_checker node
	for i in range(n+1):
		end_checker = end_checker.next
	
	# updating both the nodes untile the end_checker node hits the end of the linked list
	while end_checker!=None:
		back = back.next
		end_checker = end_checker.next
	
	#removing the N-th node
	back.next = back.next.next
	#returning the reference
	return dumb.next
# remove_nth_to_last_node(Node(1, Node(2, Node(4))), 3)
# remove_nth_to_last_node(Node(1, Node(2, Node(4, Node(5)))), 3)


# this is the two pass technique
# O(2n) -> O(n) time traversing the linked list twice
# O(1) space storing reference
def remove_nth_to_last_node(head: Node, n: int) -> Node:
	ref = head
	length = 0
	# getting the length
	while ref!=None:
		length+=1
		ref = ref.next
	
	# dummy node helps with the corner cases like removing the first node
	dumb = Node(0,head)
	ref = dumb
	# traversing to the node before the target node
	for i in range(length-n):
		ref = ref.next
	# removing the target node
	ref.next = ref.next.next
	
	return dumb.next

# remove_nth_to_last_node(Node(1, Node(2, Node(4))), 3)
# remove_nth_to_last_node(Node(1, Node(2, Node(4, Node(5)))), 3)
