#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """an empty class"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
