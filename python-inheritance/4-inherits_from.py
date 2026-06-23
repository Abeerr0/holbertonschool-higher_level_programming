#!/usr/bin/python3
"""Module for inherits_from."""


def inherits_from(obj, a_class):
    """Checks if subclass only."""
    return isinstance(obj, a_class) and type(obj) is not a_class
