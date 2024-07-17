"""
It is mandatory that the file name and the testcase names should have 'test' string
either at the begining or end of their names, otherwise they won't be considered 
by pytest as a testcase.
"""

import pytest

@pytest.mark.default
def test_case1():
    a = 1
    b = 2
    assert a+1 == b, "test passed"
    assert a+1 != b, "test failed"

def test_case2():
    str1 = "harry "
    str2 = "potter"
    assert str1+str2 == "harry potter", "string concat is a successful match."

def test_case3():
    assert False

@pytest.mark.default
def test_case4():
    assert 100 == 100
