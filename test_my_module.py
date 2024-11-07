from my_module import largest_prime_factor
import pytest

def test_factor():
    assert largest_prime_factor(600851475143) == 6857
