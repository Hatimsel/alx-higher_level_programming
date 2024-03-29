#!/usr/bin/python3
"""
Square class inheriting from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A new Square class inheriting from Rectangle
    """
    def __init__(self, size):
        """
        Instatiation of a square class
        """
        self.integer_validator('size', size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """
        returns the area of a square
        """
        return self.__size * self.__size
