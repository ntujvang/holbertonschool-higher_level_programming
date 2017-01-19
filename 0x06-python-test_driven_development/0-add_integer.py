#!/usr/bin/python3
"""
This function accepts only integers or floats AND
only 2 variables! It returns the sum of both variables as
an INT.
"""
def add_integer(a, b):
    if (isinstance(a, int) is False) and (isinstance(a, float) is False):
        raise TypeError("a must be an integer")
    if (isinstance(b, int) is False) and (isinstance(b, float) is False):
        raise TypeError("b must be an integer")
    return int(a + b)
