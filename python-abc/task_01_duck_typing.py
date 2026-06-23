#!/usr/bin/env python3
"""Module that defines geometric shapes using Abstract Base Classes (ABCs).

This module demonstrates polymorphic behaviors and duck typing through
Shape, Circle, and Rectangle classes, along with a custom info function.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class acting as an interface blueprint for shapes."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate the area of a shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter of a shape."""
        pass


class Circle(Shape):
    """Concrete implementation of a circle geometric shape."""

    def __init__(self, radius):
        """Initializes a Circle instance with a given radius."""
        self.radius = radius

    def area(self):
        """Computes and returns the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Computes and returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete implementation of a rectangle geometric shape."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height values."""
        self.width = width
        self.height = height

    def area(self):
        """Computes and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Computes and returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a given shape object.

    This function relies directly on duck typing—if the object behaves
    like a shape (has area and perimeter methods), it executes smoothly.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
