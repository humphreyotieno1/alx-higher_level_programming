#!/usr/bin/python3
"""Define an inherited list class MyList."""


class MyList(list):
    """Implement sorted printing for built-in list class."""

    def print_sorted(self):
        """Print list in sorted ascending order."""
        print(sorted(self))
