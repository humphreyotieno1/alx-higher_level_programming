#!/usr/bin/python3
"""Define a function that appends string"""


def append_write(filename="", text=""):
    """Append string to the text file
    Args:
        filename (str): name of the file
        text (str): text to append
    Returns:
        number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
