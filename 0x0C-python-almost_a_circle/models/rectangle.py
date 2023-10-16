#!/usr/bin/python3

"""
Defines a module for Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """Represent a new rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Getter for the height of the rectangle"""
        return self.__height

    @property
    def x(self):
        """Getter for the x coordinate of the rectangle"""
        return self.__x

    @property
    def y(self):
        """Getter for the y coordinate of the rectangle"""
        return self.__y

    @width.setter
    def width(self, width):
        """Setter for the width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Setter for the height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """Setter for the x coordinate"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Setter for the y coordinate"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return the area of the new rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the new rectangle using the # character"""
        y = self.__y
        height = self.__height
        x = self.__x
        width = self.__width
        for i in range(y):
            print()
        for i in range(height):
            print(" " * x, end="")
            print("#" * width)

    def __str__(self):
        """return the string representation"""
        y = str(self.__y)
        h = str(self.__height)
        x = str(self.__x)
        w = str(self.__width)
        i = str(self.id)
        string = "[Rectangle] (" + i + ") " + x + "/" + y + " - " + w + "/" + h
        return string

    def update(self, *args, **kwargs):
        """Update the rectangle"""
        if args:
            a = ["id", "width", "height", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, a[i], e)
            return
        for x, y in kwargs.items():
            if hasattr(self, x):
                setattr(self, x, y)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle"""
        Dictionary = {}
        for x, y in vars(self).items():
            Dictionary[x.split("__")[-1]] = y
        return Dictionary
