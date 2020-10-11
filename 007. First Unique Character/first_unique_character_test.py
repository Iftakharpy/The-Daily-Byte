import pytest
from first_unique_character import first_unique_character

"""
> "abcabd", return 2<br>
> "thedailybyte", return 1<br>
> "developer", return 0
"""

def test_case_1() -> None:
    assert first_unique_character("abcabd") == 2

def test_case_2() -> None:
    assert first_unique_character("thedailybyte") == 1

def test_case_3() -> None:
    assert first_unique_character("developer") == 0

def test_case_4() -> None:
    assert first_unique_character("lalala") == -1

def test_case_5() -> None:
    assert first_unique_character("loveleetcode") == 2
