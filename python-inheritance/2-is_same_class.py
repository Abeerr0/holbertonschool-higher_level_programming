#!/usr/bin/python3
"""Module for is_same_class."""


def is_same_class(obj, a_class):
    """Checks if exact instance."""
    return type(obj) is a_class
