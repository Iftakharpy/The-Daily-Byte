class Node:
	def __init__(self,val=0, nxt=None):
		self.val = val
		self.next = nxt

	def __repr__(self):
		return f"Node(val={self.val}, next={self.next})"
	
	def __eq__(self, other):
		return repr(self) == repr(other)

# O(n+m) time
# O(1) space 
# avoiding usage of extraspace by removing the references when the object is merged
def merge_linked_lists(first_ll: Node , second_ll: Node) -> Node:
	if first_ll==None:
		return second_ll
	elif second_ll==None:
		return first_ll
	else:
		f_val = first_ll.val
		s_val = second_ll.val
		
		if f_val<s_val:
			ans = Node(f_val)
			first_ll = first_ll.next
		else:
			ans = Node(s_val)
			second_ll = second_ll.next
		ref = ans
		
		#trying to merge both lists if any of lists get's exausted exiting the loop
		while second_ll!=None and first_ll!=None:
			f_val = first_ll.val
			s_val = second_ll.val
			if f_val<s_val:
				first_ll = first_ll.next
				temp = Node(f_val)
				ref.next = temp
				ref = temp
			elif f_val == s_val:
				first_ll = first_ll.next
				second_ll = second_ll.next
				temp = Node(f_val)
				temp_nxt = Node(s_val)
				temp.next = temp_nxt
				ref.next = temp
				ref = temp_nxt
			else:
				second_ll = second_ll.next
				temp = Node(s_val)
				ref.next = temp
				ref = temp
		
		# #trying to merge any of the linked list that's not exausted
		ref.next = first_ll or second_ll

		#returning the reference
		return ans
