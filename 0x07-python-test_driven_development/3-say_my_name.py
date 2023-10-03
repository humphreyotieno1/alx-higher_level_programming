#!/usr/bin/python3
"""Define a function that prints name"""


def say_my_name(first_name, last_name=""):
    """Prints name

    Args:
        first_name: first name to print
        last_name: last name printed

    Raises:
        TypeError: if the name arguments are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
