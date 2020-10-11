class Node:
	def __init__(self,val=0, nxt=None):
		self.val = val
		self.next = nxt

	def __repr__(self):
		return f"Node(val={self.val}, next={self.next})"
	
	def __eq__(self, other):
		return repr(self) == repr(other)


def remove_nth_to_last_node(head: Node, n: int) -> Node:
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
