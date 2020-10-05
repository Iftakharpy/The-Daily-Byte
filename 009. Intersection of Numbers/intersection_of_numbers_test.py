import pytest
from intersection_of_numbers import intersection_of_numbers

"""
> nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]<br>
> nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]<br>
> nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
"""

def test_case_1() -> None:
    assert intersection_of_numbers([2, 4, 6, 8], [1, 3, 5, 7]) == []

def test_case_2() -> None:
    assert intersection_of_numbers([1, 2, 3, 3], [3,3]) == [3]

def test_case_3() -> None:
    assert intersection_of_numbers([2, 4, 4, 2], [2, 4]) == [2,4]