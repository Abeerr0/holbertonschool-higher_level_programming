#!/usr/bin/python3
"""Module for MyList."""


class MyList(list):
    """Custom list class."""

    def print_sorted(self):
        """Prints sorted list."""
        print(sorted(self))
