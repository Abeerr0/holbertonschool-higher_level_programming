#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """Class that inherits from list with sorted printing capability."""

    def print_sorted(self):
        """Prints the list elements in ascending sorted order."""
        print(sorted(self))
