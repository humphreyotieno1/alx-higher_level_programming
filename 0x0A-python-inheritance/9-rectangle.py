#!/usr/bin/python3
"""Define a class Rectangle from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define Rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """

        self().integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

        def area(self):
            """Return area of Rectangle"""

            return self.__width * self.__height

        def __str__(self):
        """prints Rectangle"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
