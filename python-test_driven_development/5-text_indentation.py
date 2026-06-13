#!/usr/bin/python3
"""
This module provides a function to indent text based on specific punctuation.
It contains one function: `text_indentation(text)`.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The string to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # نستخدم المؤشر (skip_space) لتخطي أي مسافة تأتي في بداية السطر الجديد
    skip_space = True

    for char in text:
        if skip_space and char == ' ':
            continue
        
        # إذا انتهى السطر الجديد بمحرف سطر جديد أصلي، يجب أيضاً تفعيل تخطي المسافة التالية
        if char == '\n':
            print(char, end="")
            skip_space = True
            continue

        print(char, end="")
        skip_space = False

        if char in ['.', '?', ':']:
            print("\n")
            skip_space = True
