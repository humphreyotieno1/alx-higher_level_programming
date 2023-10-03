#!/usr/bin/python3
"""Define a function for printing a square"""


def print_square(size):
    """Print a square with the # character

    Args:
        size (int): length of the square

    Raises:
        TypeError: if size is not an int
        ValueError: if size < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
