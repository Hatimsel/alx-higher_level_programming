#!/usr/bin/python3
"""
"""


def find_peak(list):
    """
    """
    if len(list) == 0:
        return None
    max = list[0]
    i = 1
    while (i < len(list)):
        if list[i] > max:
            max = list[i]
        i += 1
    return max
