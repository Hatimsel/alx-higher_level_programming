#!/usr/bin/python3
"""
empty class
"""


class BaseGeometry:
    """
    not empty anymore
    """
    def area(self):
        """
        returns the area of a shape if implemented
        """
        raise Exception('area() is not implemented')
