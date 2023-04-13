# sample_code.py

def multiply(a, b):
    return a * b

# test_sample_code.py
import pytest

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 4) == 0
    assert multiply(-2, 5) == -10
