#!/usr/bin/python3
"""
This module provides a function to print a formatted full name.
It contains one function: `say_my_name(first_name, last_name="")`.
"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first name> <last name>'.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print. Defaults to "".

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
