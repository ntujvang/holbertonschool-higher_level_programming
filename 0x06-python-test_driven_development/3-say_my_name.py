#!/usr/bin/python3
"""
This is the "Say My Name" module.

This module takes one required and one optional argument.
It prints "My name is (first) (last)"
"""


def say_my_name(first_name, last_name=""):
    """Print "My name is (first)" or "(first) (last)"
    Otherwise print error.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
