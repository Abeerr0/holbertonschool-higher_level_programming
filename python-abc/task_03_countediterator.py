#!/usr/bin/env python3
"""Module defining an iterator wrapper that counts iterations."""


class CountedIterator:
    """Iterator wrapper that keeps track of how many items were fetched."""

    def __init__(self, iterable):
        """Initializes the iterator object and the counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Returns the current number of successfully iterated items."""
        return self.counter

    def __next__(self):
        """Fetches the next item and increments the counter if successful."""
        item = next(self.iterator)
        self.counter += 1
        return item
