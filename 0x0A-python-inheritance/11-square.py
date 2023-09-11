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
        self.integer_validator('size', size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
