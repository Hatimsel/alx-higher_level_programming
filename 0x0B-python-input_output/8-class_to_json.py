#!/usr/bin/python3
"""
class to json
"""


def class_to_json(obj):
    """
    returns the dictionary description with a simple data structure
    """
    return obj.__dict__
