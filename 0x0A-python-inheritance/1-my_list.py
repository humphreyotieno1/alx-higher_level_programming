#!/usr/bin/python3
"""Define inherited list in class MyList"""


class MyList(List):
    """Implement sorted printing for a built in list class
        Inherit from List
    """
    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
