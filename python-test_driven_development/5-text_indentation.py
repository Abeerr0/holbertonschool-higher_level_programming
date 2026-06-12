#!/usr/bin/python3
"""Module for text_indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after each: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
        
    lines = []
    current_line = ""
    for char in text:
        current_line += char
        if char in ['.', '?', ':']:
            lines.append(current_line)
            current_line = ""
    if current_line:
        lines.append(current_line)
        
    for line in lines:
        line = line.strip()
        if line:
            if line[-1] in ['.', '?', ':']:
                print(line)
                print("")
            else:
                print(line, end="")
