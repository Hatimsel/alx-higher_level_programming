#!/usr/bin/python3
"""
Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation of the class
        """
        if super().integer_validator('width', width):
            self.__width = width
        if super().integer_validator('height', height):
            self.__height = height
