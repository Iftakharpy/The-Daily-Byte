import pytest
from correct_capitalization import correct_capitalization


def test_case_1() -> None:
    assert correct_capitalization("USA") == True

def test_case_2() -> None:
    assert correct_capitalization("Calvin") == True

def test_case_3() -> None:
    assert correct_capitalization("computer") == True

def test_case_4() -> None:
    assert correct_capitalization("COding") == False

def test_case_5() -> None:
    assert correct_capitalization("cOOl") == False

def test_case_6() -> None:
    assert correct_capitalization("cOding") == False