#!/usr/bin/python3
"""
This module provides a function to indent text based on punctuation.
It contains one function: `text_indentation(text)`.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of '.', '?' and ':'.

    Args:
        text (str): The text to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] in [".", "?", ":"] or text[i] == "\n":
            if text[i] in [".", "?", ":"]:
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
