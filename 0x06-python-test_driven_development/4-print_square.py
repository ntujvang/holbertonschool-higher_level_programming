#!/usr/bin/python3
"""
This is the "Print Square" module.

This module prints a square using '#'.
The size variable given determines the square parameters.
"""


def print_square(size):
    """Print a perfect square given a valid int or float
    """
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, (int, float)) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    for i in range(int(size)):
        print("#" * int(size))
