#!/usr/bin/python3
"""Module that defines the is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a_class or its subclasses."""
    return isinstance(obj, a_class)
