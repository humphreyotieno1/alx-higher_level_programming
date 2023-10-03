#!/usr/bin/python3
"""Define integer addition function"""


def add_integer(a, b=98):
    """Return integer addition of a and b

    Float args typecasted before addition is done

    Raises:
        TypeError: If either a or b is a non-integer and non-float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
