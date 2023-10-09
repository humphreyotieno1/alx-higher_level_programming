#!/usr/bin/python3
"""Define class MyInt that inherits from Int"""


class MyInt(int):
    """Invert int operators"""

    def __init__(self, num):
        """Initialize number"""
        self.num = num

    def __eq__(self, other):
        """Return:
            True if both not equal
        """
        return self.num != other

    def __ne__(self, other):
        """Return:
            True if both are equal
        """
        return self.num == other
