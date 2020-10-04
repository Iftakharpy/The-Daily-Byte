import pytest
from spot_the_difference import spot_the_difference


"""
> s = "foobar", t = "barfoot", return 't'<br>
> s = "ide", t = "idea", return 'a'<br>
> s = "coding", t = "ingcod", return ''<br>
> s = "a", t = "aa", return 'a'<br>
> s = "abcd", t = "abcde", return 'e'
"""

def test_case_1():
    assert spot_the_difference("foobar", "barfoot") == "t"

def test_case_2():
    assert spot_the_difference("ide", "idea") == "a"

def test_case_3():
    assert spot_the_difference("coding", "ingcod") == ""

def test_case_4():
    assert spot_the_difference("a", "aa") == "a"

def test_case_5():
    assert spot_the_difference("abcd", "abcde") == "e"
