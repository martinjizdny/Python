from importlib.resources import path
import sys

def add(x, y):
    return x + y

def test_add_A():
    print("Addition assert testing ... by MJ")
    assert add(2, 3) == 5

def test_add_B():
    assert add(2, 3) == 55  # error !!!! 2+3=5 not 55 ...

def test_Calculation():
    print("Calculation assert testing ... by MJ")
    assert 2+2 == 4