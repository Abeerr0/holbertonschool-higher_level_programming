#!/usr/bin/python3
"""Module that defines the inherits_from function."""


def inherits_from(obj, a_class):
    """Checks if an object inherits from a_class, but is not exactly it.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj's class inherited from a_class.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
