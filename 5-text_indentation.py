#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    idx = 0
    while idx < len(text):
        print(text[idx], end="")
        if text[idx] in chars:
            print("\n")
            idx += 1
            while idx < len(text) and text[idx] == ' ':
                idx += 1
            continue
        idx += 1
