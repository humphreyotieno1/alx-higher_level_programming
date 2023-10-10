#!/usr/bin/python3
"""Define a function that reads text in a file"""


def read_file(filename=""):
    """Print file content to standard output"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
