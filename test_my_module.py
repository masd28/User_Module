from User_Module.my_module import largest_prime_factor, fast_flip_num
import pytest

def test_factor():
    assert largest_prime_factor(600851475143) == 6857

def test_flip():
    assert fast_flip_num(123) == 321