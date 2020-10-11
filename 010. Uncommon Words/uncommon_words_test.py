import pytest
from uncommon_words import uncommon_words

"""
> sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]<br>
> sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]<br>
> sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]
"""

def test_case_1() -> None:
    assert uncommon_words("the quick", "brown fox").sort() == ["the", "quick", "brown", "fox"].sort()

def test_case_2() -> None:
    assert uncommon_words("the tortoise beat the haire", "the tortoise lost to the haire").sort() == ["beat", "to", "lost"].sort()

def test_case_3() -> None:
    assert uncommon_words("copper coffee pot", "hot coffee pot").sort() == ["copper", "hot"].sort()

def test_case_4() -> None:
    assert uncommon_words("", "").sort() == [].sort()
