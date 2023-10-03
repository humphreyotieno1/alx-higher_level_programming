#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """Prevents the user from creating new instance attribute
    for LockedClass unless attribute is 'first_name'
    """

    __slots__ = "first_name"
