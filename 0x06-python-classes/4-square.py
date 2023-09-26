#!/usr/bin/python3
"""Define class Square."""


class Square:
    """Represent square."""

    def __init__(self, size=0):
        """Initialize new square.

        Args:
            size (int): size of new square.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
            value: set size to value, if int and >= 0
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return area of square."""
        return (self.__size * self.__size)
