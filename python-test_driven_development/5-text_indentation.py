#!/usr/bin/python3
"""
This module provides a function to format text based on specific punctuation.
It contains one function: `text_indentation(text)`.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of '.', '?' and ':'.

    Args:
        text (str): The text to be formatted and printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    text_len = len(text)

    while c < text_len and text[c] == ' ':
        c += 1

    while c < text_len:
        print(text[c], end="")
        if text[c] in [".", "?", ":"]:
            print("\n")
            c += 1
            while c < text_len and text[c] == ' ':
                c += 1
            if c < text_len and text[c] == '\n':
                c += 1
                while c < text_len and text[c] == ' ':
                    c += 1
            continue
        c += 1
