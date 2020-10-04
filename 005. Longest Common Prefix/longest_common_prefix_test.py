import pytest
from longest_common_prefix import longest_common_prefix


def test_case_1() -> None:
    assert longest_common_prefix(["colorado", "color", "cold"]) == "col"

def test_case_2() -> None:
    assert longest_common_prefix(["ac", "bc", "acw"]) == ""

def test_case_3() -> None:
    assert longest_common_prefix(["spot", "spotty", "spotted"]) == "spot"