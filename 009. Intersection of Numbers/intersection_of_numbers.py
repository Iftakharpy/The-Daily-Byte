from typing import List

# accroding to https://wiki.python.org/moin/TimeComplexity#set
# time complexity of lookup in set() is O(1)
# time complexity of intersection in set() is O(min(len(n),len(m)))
# in python set() is implement like hash table so it's as fast as hash table

def intersection_of_numbers(lst1: List[int], lst2: List[int]) -> List[int]:
	# converting both lists to set and then returning the intersection of the sets
	return list(set(lst1).intersection(set(lst2)))