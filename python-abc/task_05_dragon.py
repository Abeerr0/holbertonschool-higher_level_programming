#!/usr/bin/env python3
"""Module demonstrating the use of Mixins to compose behaviors."""


class SwimMixin:
    """Mixin providing swimming behavior."""

    def swim(self):
        """Prints swimming ability."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying behavior."""

    def fly(self):
        """Prints flying ability."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class composed of swimming and flying mixins."""

    def roar(self):
        """Prints roaring sound."""
        print("The dragon roars!")
