#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        If attrs is a list of strings, only attribute names contained
        in this list are retrieved. Otherwise, all attributes are
        retrieved.
        """
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with the
        key/value pairs contained in the json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
