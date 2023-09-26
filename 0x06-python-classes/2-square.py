#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Rep class Square"""
    def __init__(self, size=0):
        """
        Initialize new square

        Args:
            size(int): size of new square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
