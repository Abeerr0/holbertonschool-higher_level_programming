#!/usr/bin/env python3
"""Module demonstrating multiple inheritance with Fish, Bird, and FlyingFish."""


class Fish:
    """Class representing a Fish."""

    def swim(self):
        """Prints swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Prints fish habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a Bird."""

    def fly(self):
        """Prints flying message."""
        print("The bird is flying")

    def habitat(self):
        """Prints bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a FlyingFish inheriting from Fish and Bird."""

    def swim(self):
        """Overrides swim method."""
        print("The flying fish is swimming!")

    def fly(self):
        """Overrides fly method."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Overrides habitat method."""
        print("The flying fish lives both in water and the sky!")
