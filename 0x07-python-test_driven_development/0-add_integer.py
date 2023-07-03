#!/usr/bin/python3
""" adds two integers
    a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be
    an integer
    returns an integer the addition of a and b"""


def add_integer(a, b=98):
    """ adds two integers
    they should be casted to int before performing the addition
    returns the result of their addition"""
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    result = int(a) + int(b)
    return result
