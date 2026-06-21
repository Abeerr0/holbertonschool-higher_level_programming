#!/usr/bin/python3
"""Module that defines a full Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a complete square, inherits from Rectangle."""

    def __init__(self, size):
        """Initializes Square with a validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
