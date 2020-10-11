import pytest
from remove_nth_to_last_node import remove_nth_to_last_node, Node

"""
> 1->2->3->null, n = 1, return 1->2->null
> 1->2->3->null, n = 2, return 1->3->null
> 1->2->3->null, n = 3, return 2->3->null
"""

def test_case_1() -> None:
    assert remove_nth_to_last_node(Node(1, Node(2, Node(3))), 1) == Node(1, Node(2))

def test_case_2() -> None:
    assert remove_nth_to_last_node(Node(1), 1) == None

def test_case_3() -> None:
    assert remove_nth_to_last_node(Node(1, Node(2, Node(4))), 3) == Node(2, Node(4))
