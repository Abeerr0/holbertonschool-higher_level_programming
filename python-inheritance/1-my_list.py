#!/usr/bin/python3
"""Module that defines the MyList class.

This module provides a MyList class that inherits from list
and adds a method to print the list in sorted order.
"""


class MyList(list):
    """Class that inherits from list with sorted printing capability."""

    def print_sorted(self):
        """Prints the list elements in ascending sorted order."""
        print(sorted(self))
