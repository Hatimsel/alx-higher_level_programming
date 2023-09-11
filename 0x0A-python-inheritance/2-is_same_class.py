#!/usr/bin/python3
"""
isinstance method
"""


def is_same_class(obj, a_class):
    """
    returns True if obj is an instance of a_class, False otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
