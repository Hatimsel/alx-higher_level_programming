#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class"""
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """returns the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """returns a square representation"""
        return f'[Square] {self.__size}/{self.__size}'
