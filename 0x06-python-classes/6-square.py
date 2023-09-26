#!/usr/bin/python3
"""Define class Square."""


class Square:
    """Represent square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize square
        Attributes:
            size (int): default to 0
            position (int): tuple of two positive int's
        """
        self.size = size
        self.position = position

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
            value: set value to value, if int and >= 0
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

     @property
    def position(self):
        """
        Getter
        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter
        Args:
            value: set position to tuple if value is tuple of 2 positive int's
        """

        if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or type(value[1]) is not int or \
            value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Return area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square with #"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                "#" * self.__size
                for rows in range(self.__size)]))
