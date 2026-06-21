#!/usr/bin/python3
"""Module that defines the is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a_class or its subclasses.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass.
    """
    return isinstance(obj, a_class)
