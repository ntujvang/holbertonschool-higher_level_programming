#!/usr/bin/python3
"""
This is the "Add Integer" module.

The Addition module supplies a simple function, add_integer().
It adds 2 variable of either int or float type and returns an int.
"""


def add_integer(a, b):
    """ Return the sum of 2 arguments after casting both into int.
    Or raise TypeError for either argument type.
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (a + b)
