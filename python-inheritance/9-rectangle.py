#!/usr/bin/python3
"""Module that defines a full Rectangle class inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines a complete rectangle, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes Rectangle with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle.

        Returns:
            str: The rectangle description.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
