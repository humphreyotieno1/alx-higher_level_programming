#!/usr/bin/python3
"""Define function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """Add new attribute to object
    Args:
        obj (any): object to add attribute
        att (str): attribute to add
        value (any): value of the attribute
    Raises:
        TypeError: If attribute can't be added
    """

    if ('__dict__' in dir(obj)):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
