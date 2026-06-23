#!/usr/bin/python3
"""Module for MyInt."""


class MyInt(int):
    """Rebel integer class with inverted == and != operators."""

    def __eq__(self, other):
        """Invert the == operator to act like !=."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Invert the != operator to act like ==."""
        return int.__eq__(self, other)
