#!/usr/bin/python3
"""Define Rectangle subclass is Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define Square"""

    def __init__(self, size):
        """Initialize Square
        Args:
            size (int): size of square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
