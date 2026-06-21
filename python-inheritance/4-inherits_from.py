#!/usr/bin/python3
"""Module that defines the inherits_from function."""


def inherits_from(obj, a_class):
    """Checks if an object inherits from a_class (only subclass)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
