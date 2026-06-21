#!/usr/bin/python3
"""Module that defines the is_same_class function."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a_class."""
    return type(obj) is a_class
