#!/usr/bin/python3
"""function that returns the addition of two integers"""


def add_integer(a, b=98):
    """adds two integer"""
    if type(a) is not int and type(a) is not float or a != a:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float or b != b:
        raise TypeError("b must be an integer")
    return int(a + b)
