#!/usr/bin/python3
"""Define inherited function to check class"""


def inherits_from(obj, a_class):
    """Check if objext is inherited instance of a class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
