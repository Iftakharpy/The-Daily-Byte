import pytest
from add_binary import add_binary


def test_case_1() -> None:
    assert add_binary("100","1") == "101"

def test_case_2() -> None:
    assert add_binary("11","1") == "100"

def test_case_3() -> None:
    assert add_binary("1","0") == "1"

def test_case_4() -> None:
    assert add_binary("0","0") == "0"

def test_case_5() -> None:
    assert add_binary("10110","111")
