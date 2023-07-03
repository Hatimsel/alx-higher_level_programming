#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 4-rectangle.py)"""


class Rectangle:

    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        __init__(width=0, height=0): Initializes a Rectangle object with
        optional width and height.
        width: Getter method for retrieving the width of the rectangle.
        height: Getter method for retrieving the height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        self.__area = self.__width * self.__height
        return self.__area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        string = ''
        if self.__width == 0 or self.__height == 0:
            return string
        string += ("#" * self.__width + "\n") * self.__height
        return string[:-1]

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
