#!/usr/bin/python3

"""
Define a module for Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a new Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializ a new square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of square"""
        y = str(self.y)
        x = str(self.x)
        w = str(self.width)
        i = str(self.id)
        string = "[Square] (" + i + ") " + x + "/" + y + " - " + w
        return string

    @property
    def size(self):
        """Getter for the width of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter for the size of the square"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updating the square"""
        if args:
            a = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, a[i], e)
            return
        for x, y in kwargs.items():
            if hasattr(self, x):
                setattr(self, x, y)

    def to_dictionary(self):
        """Dictionary representation of square"""
        Dict = {}
        for x, y in vars(self).items():
            if x.startswith("_"):
                if not x.endswith("width") and not x.endswith("height"):
                    idx = x.index("__")
                    Dict[x[idx + 2:]] = y
                else:
                    Dict["size"] = y
            else:
                Dict[x] = y
        return Dict
