#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """Class that defines a base geometry object with area method."""

    def area(self):
        """Raises an Exception since area is not implemented."""
        raise Exception("area() is not implemented")
