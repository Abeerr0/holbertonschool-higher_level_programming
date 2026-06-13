#!/usr/bin/python3
"""
Module that contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    # استبدال الرموز بسطرين جديدين، ثم تقسيم النص لتنظيف المسافات الذكية
    s = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')
    lines = s.split('\n')

    for i in range(len(lines)):
        if i == len(lines) - 1:
            print(lines[i].strip(' '), end="")
        else:
            print(lines[i].strip(' '))
