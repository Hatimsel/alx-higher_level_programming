#!/usr/bin/python3
"""
isinstance function
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if obj is an instance otherwise false
    """
    if isinstance(obj, a_class):
        return True
    return False
