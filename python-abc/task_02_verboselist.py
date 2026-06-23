#!/usr/bin/env python3
"""Module extending the built-in list to add custom notifications."""


class VerboseList(list):
    """A custom list that prints messages when modified."""

    def append(self, item):
        """Appends an item and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extends the list and prints a notification with the count."""
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Removes an item and prints a notification beforehand."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item and prints a notification beforehand."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
