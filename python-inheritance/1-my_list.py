#!/usr/bin/python3
"""Module for MyList."""


class MyList(list):
    """Custom list class that inherits from list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
