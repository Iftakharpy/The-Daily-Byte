import pytest
from valid_palindrome import valid_palindrome


def test_case_1() -> None:
    assert valid_palindrome("hello") == False

def test_case_2() -> None:
    assert valid_palindrome("algorithm") == False

def test_case_3() -> None:
    assert valid_palindrome("a,B") == False

def test_case_4() -> None:
    assert valid_palindrome("a,A") == True

def test_case_5() -> None:
    assert valid_palindrome("level") == True

def test_case_6() -> None:
    assert valid_palindrome("A man, a plan, a canal: Panama.") == True
