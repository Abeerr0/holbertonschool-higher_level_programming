#!/usr/bin/env python3
"""Module that defines geometric shapes using Abstract Base Classes (ABCs).

This module demonstrates interfaces and duck typing through Shape,
Circle, and Rectangle classes, alongside a standalone info function.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a geometric shape interface."""

    @abstractmethod
    def area(self):
        """Abstract method to compute the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to compute the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle geometry."""

    def __init__(self, radius):
        """Initializes a Circle instance with a given radius."""
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates and returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle geometry."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of any object implementing the interface.

    This function relies purely on duck typing and does not perform
    any explicit type checking before invoking the methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
