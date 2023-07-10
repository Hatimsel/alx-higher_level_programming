#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """an empty class"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""
        self.name = name
        if not isinstance(value, int):
            raise TypeError(f'{self.name} must be an integer')
        if value <= 0:
            raise ValueError(f'{self.name} must be greater than 0')
        else:
            self.value = value
