import pytest
from merge_linked_lists import merge_linked_lists, Node

"""
> list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null<br>
> list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null<br>
> list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null
"""

def test_case_1() -> None:
    assert merge_linked_lists(None, None) == None


def test_case_2() -> None:
    assert merge_linked_lists(Node(1), None) == Node(1)


def test_case_3() -> None:
    assert merge_linked_lists(None, Node(2)) == Node(2)


def test_case_4() -> None:
    first_ll = Node(1,Node(2,Node(3)))
    second_ll = Node(1,Node(4,Node(5)))
    res = Node(1,Node(1,Node(2,Node(3,Node(4,Node(5))))))
    assert merge_linked_lists(first_ll, second_ll) == res


def test_case_5() -> None:
    first_ll = Node(1,Node(5,Node(6)))
    second_ll = Node(2,Node(3,Node(4,Node(4.5))))
    res = Node(1,Node(2,Node(3,Node(4,Node(4.5,Node(5,Node(6)))))))

    assert merge_linked_lists(first_ll, second_ll) == res


def test_case_6() -> None:
    first_ll = Node(1,Node(2,Node(4)))
    second_ll = Node(1,Node(3,Node(4)))
    res = Node(1,Node(1,Node(2,Node(3,Node(4,Node(4))))))

    assert merge_linked_lists(first_ll,second_ll) == res


def test_case_7() -> None:
    first_ll = Node(2)
    second_ll = Node(1)
    res = Node(1,Node(2))

    assert merge_linked_lists(first_ll,second_ll) == res


def test_case_8() -> None:
    first_ll = Node(2,Node(4,Node(10)))
    second_ll = Node(3,Node(11,Node(12)))
    res = Node(2,Node(3,Node(4,Node(10,Node(11,Node(12))))))

    assert merge_linked_lists(first_ll,second_ll) == res
