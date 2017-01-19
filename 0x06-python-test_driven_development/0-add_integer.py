#!/usr/bin/python3
"""
Function accepts only integers or floats AND
only 2 variables! It retuns the sum of both variables
after floats have  been casted into INT
"""
def add_integer(a, b):
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (a + b)
