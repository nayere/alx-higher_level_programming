#!/usr/bin/python3
"""
Define a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Get the addition of a and b,
    and raise an error if a and b are not integers or floats
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
