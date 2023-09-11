#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """not empty anymore"""
    def area(self):
        """
        return the area of a shape when implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        validates the second parameter passed to be an int and greater than 0
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
