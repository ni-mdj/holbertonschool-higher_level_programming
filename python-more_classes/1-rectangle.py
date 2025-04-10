#!/usr/bin/python3
"""Defines a class Rectangle with private attributes width and height."""


class Rectangle:
    """A class that defines a rectangle by its width and height."""

    def __init__(self, width=0, height=0):
        """Initializes Rectangle instance with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the Rectangle."""
        return self.__width

    @property
    def height(self):
        """Retrieves the height of the Rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
