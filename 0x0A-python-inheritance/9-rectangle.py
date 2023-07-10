#!/usr/bin/python3
"""Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry"""
    def __init__(self, width, height):
        """instantiation with width and height"""
        self.integer_validator('width', width)
        self.__width = width

        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns a rectangle description"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
