from src.hw.one.basics import *

def test_leap_year():

    assert is_leap_year(1000) == "NO"
    assert is_leap_year(400) == "YES"
    assert is_leap_year(1001) == "NO"
    assert is_leap_year(1004) == "YES"

def test_num_decs():

    assert num_decs(15634780) == 8
    assert num_decs(101) == 0

def test_factorial_sum():

    assert factorial_sum(4) == 33
    assert factorial_sum(10) == 4037913

def test_is_palindrome():

    assert is_palindrome("бащаб")
    assert is_palindrome("А роза упала на лапу Азора")
