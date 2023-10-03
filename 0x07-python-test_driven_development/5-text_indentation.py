#!/usr/bin/python3
"""Defines a text indentation function"""


def text_indentation(text):
    """Print text with 2 new lines
    Args:
        text (string): text to print.
    Raises:
        TypeError: If text ot a string.
    """
    special = ['.', '?', ':']
    if type(text) != str:
        raise TypeError("text must be string")
    for x in text:
        print(x, end='')
        if x in special:
            print('\n\n', end='')
