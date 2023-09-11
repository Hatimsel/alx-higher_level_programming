#!/usr/bin/python3
"""
Only sub class of
"""


def inherits_from(obj, a_class):
    """
    returns True is obj is an instance of a class that inherited from
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
