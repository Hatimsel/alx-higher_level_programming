#!/usr/bin/python3
"""
lookup function take an obj as a parameter and returns attrs and methods
"""


def lookup(obj):
    """
    returns a list of attrs and methods available
    """
    return dir(obj)
