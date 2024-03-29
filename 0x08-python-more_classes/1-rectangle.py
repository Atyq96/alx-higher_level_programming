#!/usr/bin/python3
"""
This is module 1-rectangle

It contains 1 class rectangle.
"""


class Rectangle:
    """Defines class Rectangle

    Instance fields:
        width: private and must be a non negative int
        height: private and  must be a non negative int

    Instance methods:
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        __init__(self, width=0, height=0)
        __check_arg(self, value)

    """
    def __init__(self, width=0, height=0):
        """A constructor that inistantiates a Rectangle.

        Args:
            width: facultative, a non-negative int
            height: facultative, a non-negative int
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Getter, retrieves height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for rectangle height.

        Args:
            value: non-negative int

        Raise:
            TypeError: If the height is not an integer
            ValueError: If the height is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Getter, retrieves width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for rectangle width.

        Args:
            value: non-negative int

        Raises:
            TypeError: If the width is not an integer
            ValueError: If the width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
