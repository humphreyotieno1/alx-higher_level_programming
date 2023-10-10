#!/usr/bin/python3
"""Define function that writes to the text file"""


def write_file(filename="", text=""):
    """Write string to the text file
    Args:
        filename (str): name of text file
        text (str): text to add to the file
    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
