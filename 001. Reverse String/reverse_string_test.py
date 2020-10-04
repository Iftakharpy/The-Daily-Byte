import pytest
from reverse_string import reverse_string


def test_case_1() -> None:
    assert reverse_string("Cat") == "taC"

def test_case_2() -> None:
    assert reverse_string("The Daily Byte") == "etyB yliaD ehT"

def test_case_3() -> None:
    assert reverse_string("civic") == "civic"