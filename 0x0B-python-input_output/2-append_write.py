#!/usr/bin/python3
"""
append_write function
"""


def append_write(filename="", text=""):
    """
    returns the number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        add_chrs = f.write(text)
    return add_chrs
