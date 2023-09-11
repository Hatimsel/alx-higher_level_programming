#!/usr/bin/python3
"""
empty class
"""


class BaseGeometry:
    """
    not empty anymore
    """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater then 0'.format(name))
