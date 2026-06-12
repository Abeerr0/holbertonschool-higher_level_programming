#!/usr/bin/python3
"""Module for text_indentation"""


def text_indentation(text):
    """Prints a text with 2 new lines after each: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
