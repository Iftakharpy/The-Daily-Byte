import pytest
from jewels_and_stones import jewels_and_stones

"""
> jewels = "abc", stones = "ac", return 2<br>
> jewels = "Af", stones = "AaaddfFf", return 3<br>
> jewels = "AYOPD", stones = "ayopd", return 0
"""

def test_case_1() -> None:
    assert jewels_and_stones("abc", "ac") == 2

def test_case_2() -> None:
    assert jewels_and_stones("Af", "AaaddfFf") == 3

def test_case_3() -> None:
    assert jewels_and_stones("AYOPD", "ayopd") == 0