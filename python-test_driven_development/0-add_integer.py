#!/usr/bin/python3
"""
This module provides a simple integer addition function.
It contains one function: `add_integer(a, b=98)`.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: The first number. Must be an integer or float.
        b: The second number. Must be an integer or float. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
