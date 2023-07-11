#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """ a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    count = 0
    with open(filename, "a", encoding='utf-8') as f:
        for i in text:
            f.write(i)
            count += 1

    return count
