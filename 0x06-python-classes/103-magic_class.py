#!/usr/bin/python3
"""Define MagicClass"""
import math


class MagicClass:
    """Initialize and def methods area and circumference"""
    def __init__(self, radius):
        """Initialize MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Find area"""
        return self._radius * self._radius * math.pi

    def circumference(self):
        """FInd circumference"""
        return 2 * math.pi * self._radius
